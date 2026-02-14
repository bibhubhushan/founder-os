#!/usr/bin/env python3
"""FounderOS localhost server.

Pure-Python web app server for chat-style interaction with FounderOS workflows.
No third-party dependencies required.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import re
import textwrap
from dataclasses import dataclass
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
APP_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = APP_DIR / "public"
MEMORY_DIR = ROOT / "memory"

MEMORY_FILES = {
    "ACTIVE_PROJECT": MEMORY_DIR / "ACTIVE_PROJECT.md",
    "DECISIONS": MEMORY_DIR / "DECISIONS.md",
    "JOURNAL": MEMORY_DIR / "JOURNAL.md",
    "LESSONS": MEMORY_DIR / "LESSONS.md",
    "EVALS": MEMORY_DIR / "EVALS.md",
}

COMMANDS = {
    "/coo": {
        "agent": "SATOSHI",
        "type": "ops",
        "title": "Operations and Execution",
        "focus": "turn goals into clear tasks, owners, and deadlines",
    },
    "/ceo": {
        "agent": "ELON",
        "type": "strategy",
        "title": "Strategy and Direction",
        "focus": "validate direction, leverage, and moat",
    },
    "/cto": {
        "agent": "DANIEL",
        "type": "build",
        "title": "Engineering",
        "focus": "spec, architecture, implementation path",
    },
    "/cdo": {
        "agent": "BRIAN",
        "type": "design",
        "title": "Design",
        "focus": "interaction quality, visual hierarchy, user clarity",
    },
    "/cro": {
        "agent": "ANDREJ",
        "type": "learning",
        "title": "Learning and Research",
        "focus": "teach clearly and expose knowledge gaps",
    },
    "/team_mvp": {
        "agent": "ELON + DANIEL + BRIAN",
        "type": "team",
        "title": "MVP Build Squad",
        "focus": "align strategy, build, and UX into one sprint",
    },
    "/cofounder": {
        "agent": "ELON + SATOSHI",
        "type": "team",
        "title": "Leadership Duo",
        "focus": "balance ambition with execution",
    },
    "/core_team": {
        "agent": "SATOSHI + DANIEL + BRIAN + ANDREJ",
        "type": "team",
        "title": "Core Team",
        "focus": "cross-functional standup",
    },
    "/my_team": {
        "agent": "SATOSHI + ANDREJ",
        "type": "team",
        "title": "Personal Advisory Team",
        "focus": "combine execution discipline and learning depth",
    },
    "/board_meeting": {
        "agent": "LEADERSHIP BOARD",
        "type": "team",
        "title": "Board Meeting",
        "focus": "resolve key directional decisions with explicit approval",
    },
    "/all_hands": {
        "agent": "ALL AGENTS",
        "type": "team",
        "title": "Grand Council",
        "focus": "high-stakes multi-agent decision",
    },
    "/route": {
        "agent": "AUTO",
        "type": "router",
        "title": "Auto Router",
        "focus": "select the best command",
    },
}

ROUTE_RULES = [
    ("/cto", ("build", "code", "implement", "debug", "fix", "api", "database", "frontend", "backend")),
    ("/cdo", ("design", "ui", "ux", "layout", "brand", "typography", "color", "landing")),
    ("/coo", ("plan", "schedule", "task", "priority", "sprint", "roadmap", "launch", "ship")),
    ("/ceo", ("strategy", "vision", "position", "moat", "market", "pricing", "pivot")),
    ("/cro", ("teach", "learn", "explain", "research", "understand", "concept")),
]

QUICK_PROMPTS = [
    {
        "label": "Plan My Week",
        "command": "/coo",
        "message": "Turn this week into a focused sprint. We need one metric, top 3 goals, and daily tasks.",
    },
    {
        "label": "Launch MVP",
        "command": "/team_mvp",
        "message": "Design and build an MVP in 72 hours with explicit scope and acceptance criteria.",
    },
    {
        "label": "Fix Direction",
        "command": "/ceo",
        "message": "Audit our current idea and challenge the strategy from first principles.",
    },
    {
        "label": "Postmortem",
        "command": "/all_hands",
        "message": "We missed the weekly target. Find root causes and define a corrective 7-day plan.",
    },
]

WRITE_LOCK = Lock()


@dataclass
class RouteResult:
    requested_command: str
    selected_command: str
    reason: str


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def infer_command(message: str, requested: str | None) -> RouteResult:
    normalized = message.lower().strip()
    requested_command = requested or ""

    explicit = re.match(r"^\s*(/[a-z_]+)", message)
    if explicit and explicit.group(1) in COMMANDS:
        cmd = explicit.group(1)
        if cmd == "/route":
            routed = route_from_keywords(normalized)
            return RouteResult(cmd, routed, f"Auto-router matched keywords for {routed}.")
        return RouteResult(cmd, cmd, "Explicit command in message.")

    if requested_command in COMMANDS and requested_command != "/route":
        return RouteResult(requested_command, requested_command, "Command selected in UI.")

    routed = route_from_keywords(normalized)
    if requested_command == "/route":
        return RouteResult("/route", routed, f"Auto-router matched keywords for {routed}.")

    return RouteResult(requested_command or "", routed, f"No explicit command found. Routed to {routed}.")


def route_from_keywords(normalized: str) -> str:
    for command, keywords in ROUTE_RULES:
        if any(word in normalized for word in keywords):
            return command
    return "/coo"


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def append_text(path: Path, content: str) -> None:
    existing = read_text(path)
    if existing and not existing.endswith("\n"):
        existing += "\n"
    write_text(path, existing + content)


def memory_snapshot() -> dict[str, str]:
    return {key: read_text(path) for key, path in MEMORY_FILES.items()}


def active_project_brief(active_project: str) -> str:
    lines = [line.strip() for line in active_project.splitlines() if line.strip().startswith("-")]
    if not lines:
        return "No active project fields filled yet."
    return " ".join(lines[:3])


def strip_command_prefix(message: str) -> str:
    return re.sub(r"^\s*/[a-z_]+\s*", "", message, count=1, flags=re.IGNORECASE).strip()


def make_plan(command: str, objective: str) -> list[str]:
    templates = {
        "/coo": [
            "Define one weekly metric with a numeric target.",
            "Break the objective into 3 executable tasks and assign a day to each.",
            "Set a Friday review with a ship/no-ship checkpoint.",
        ],
        "/ceo": [
            "State the contrarian angle and why this can win.",
            "Name the moat and how it strengthens in 30 days.",
            "Choose one strategic bet and one thing to stop doing.",
        ],
        "/cto": [
            "Write acceptance criteria for the smallest shippable slice.",
            "Build a vertical slice from input to visible output.",
            "Run a regression pass and document deployment steps.",
        ],
        "/cdo": [
            "Define the main user flow and primary CTA.",
            "Produce one visual direction and one simplified variant.",
            "Finalize spacing, typography, and interaction states.",
        ],
        "/cro": [
            "Explain the concept in plain language.",
            "Identify 3 knowledge gaps and fill them with examples.",
            "Create a teach-back test to validate understanding.",
        ],
        "/team_mvp": [
            "Lock positioning, UX scope, and build scope in one page.",
            "Implement core user flow end-to-end in MVP quality.",
            "Run launch checklist and capture post-launch feedback.",
        ],
        "/cofounder": [
            "Set a 7-day objective aligned with long-term strategy.",
            "Agree on top 3 execution priorities.",
            "Define one kill metric and one success metric.",
        ],
        "/core_team": [
            "Collect each specialist recommendation in one sentence.",
            "Resolve conflicts and decide one operating plan.",
            "Assign owners and checkpoints.",
        ],
        "/my_team": [
            "Define your top execution bottleneck and top learning bottleneck.",
            "Create one plan for immediate action and one for skill growth.",
            "Set checkpoints for progress and reflection.",
        ],
        "/board_meeting": [
            "State the decision clearly with options and constraints.",
            "Collect domain input and identify the highest-risk assumption.",
            "Approve one path with a review date.",
        ],
        "/all_hands": [
            "Run quick diagnosis by domain (strategy, ops, build, design, learning).",
            "Pick the highest-leverage correction.",
            "Commit to a 7-day recovery plan with daily checkpoints.",
        ],
    }
    base = templates.get(command, templates["/coo"])
    return [f"{idx + 1}. {item}" for idx, item in enumerate(base)]


def derive_metric_hint(command: str) -> str:
    metrics = {
        "/coo": "tasks completed without re-prompt",
        "/ceo": "strategic bets validated this week",
        "/cto": "time-to-first-working-build",
        "/cdo": "onboarding completion rate",
        "/cro": "teach-back accuracy",
        "/team_mvp": "features shipped in 72 hours",
        "/cofounder": "objective completion rate",
        "/core_team": "cross-team blocker resolution time",
        "/my_team": "daily output consistency",
        "/board_meeting": "decision-to-execution lead time",
        "/all_hands": "recovery velocity after decision",
    }
    return metrics.get(command, "weekly throughput")


def compose_response(message: str, route: RouteResult, memory: dict[str, str]) -> dict[str, Any]:
    command_meta = COMMANDS.get(route.selected_command, COMMANDS["/coo"])
    objective = clean_text(strip_command_prefix(message)) or "Improve execution quality this week."
    active_project = active_project_brief(memory.get("ACTIVE_PROJECT", ""))
    plan = make_plan(route.selected_command, objective)
    metric = derive_metric_hint(route.selected_command)

    response = textwrap.dedent(
        f"""
        {command_meta['agent']} MODE ({route.selected_command})

        Objective:
        {objective}

        Context from memory:
        {active_project}

        Focus:
        {command_meta['focus']}

        48-hour execution plan:
        {plan[0]}
        {plan[1]}
        {plan[2]}

        Metric to track now:
        {metric}

        Next command:
        Use /route if scope changes mid-sprint, otherwise stay in {route.selected_command} until a concrete output ships.
        """
    ).strip()

    suggestions = [
        f"{route.selected_command} Convert this into a day-by-day checklist.",
        "/team_mvp Build and ship the smallest usable version.",
        "/all_hands Stress test this plan before launch.",
    ]

    return {
        "text": response,
        "suggestions": suggestions,
        "agent": command_meta["agent"],
        "title": command_meta["title"],
    }


def append_journal_entry(route: RouteResult, message: str, result: dict[str, Any]) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    compact_input = clean_text(message)[:240]
    compact_output = clean_text(result["text"])[:280]
    entry = (
        f"\nDate: {ts}\n"
        f"What was attempted: {compact_input}\n"
        f"What shipped: Plan generated via {route.selected_command}\n"
        f"What failed: pending execution\n"
        f"Next session focus: {compact_output}\n"
    )
    with WRITE_LOCK:
        append_text(MEMORY_FILES["JOURNAL"], entry)


def read_json_body(handler: BaseHTTPRequestHandler) -> dict[str, Any]:
    try:
        length = int(handler.headers.get("Content-Length", "0"))
    except ValueError:
        return {}

    raw = handler.rfile.read(length) if length > 0 else b"{}"
    if not raw:
        return {}
    try:
        return json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError:
        return {}


class FounderHandler(BaseHTTPRequestHandler):
    server_version = "FounderOSLocal/1.0"

    def _send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path) -> None:
        if not path.exists() or not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return

        mime_type, _ = mimetypes.guess_type(str(path))
        data = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", mime_type or "application/octet-stream")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _serve_static(self, request_path: str) -> None:
        relative = request_path.lstrip("/") or "index.html"
        target = (PUBLIC_DIR / relative).resolve()
        public_root = PUBLIC_DIR.resolve()
        if public_root not in target.parents and target != public_root:
            self.send_error(HTTPStatus.FORBIDDEN, "Invalid path")
            return

        if target.exists() and target.is_file():
            self._send_file(target)
            return

        # SPA fallback
        self._send_file(PUBLIC_DIR / "index.html")

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)

        if parsed.path == "/api/health":
            self._send_json(HTTPStatus.OK, {"ok": True, "time": utc_now_iso()})
            return

        if parsed.path == "/api/bootstrap":
            memory = memory_snapshot()
            payload = {
                "ok": True,
                "commands": COMMANDS,
                "quick_prompts": QUICK_PROMPTS,
                "memory_status": {
                    key: {
                        "chars": len(content),
                        "updated": MEMORY_FILES[key].stat().st_mtime if MEMORY_FILES[key].exists() else None,
                    }
                    for key, content in memory.items()
                },
            }
            self._send_json(HTTPStatus.OK, payload)
            return

        if parsed.path == "/api/memory":
            self._send_json(HTTPStatus.OK, {"ok": True, "memory": memory_snapshot()})
            return

        self._serve_static(parsed.path)

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)

        if parsed.path == "/api/chat":
            payload = read_json_body(self)
            message = str(payload.get("message", "")).strip()
            command = str(payload.get("command", "")).strip()
            auto_persist = bool(payload.get("autoPersist", True))

            if not message:
                self._send_json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "Message is required."})
                return

            route = infer_command(message, command)
            memory = memory_snapshot()
            result = compose_response(message, route, memory)

            if auto_persist:
                append_journal_entry(route, message, result)

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "route": {
                        "requested": route.requested_command,
                        "selected": route.selected_command,
                        "reason": route.reason,
                    },
                    "message": {
                        "id": utc_now_iso(),
                        "role": "assistant",
                        "agent": result["agent"],
                        "title": result["title"],
                        "content": result["text"],
                    },
                    "suggestions": result["suggestions"],
                },
            )
            return

        if parsed.path == "/api/memory/append":
            payload = read_json_body(self)
            file_key = str(payload.get("file", "")).strip().upper()
            entry = str(payload.get("entry", "")).strip()

            if file_key not in MEMORY_FILES:
                self._send_json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "Invalid memory file key."})
                return
            if not entry:
                self._send_json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "Entry is required."})
                return

            with WRITE_LOCK:
                append_text(MEMORY_FILES[file_key], f"\n{entry}\n")
            self._send_json(HTTPStatus.OK, {"ok": True})
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "Unknown endpoint."})

    def do_PUT(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        match = re.match(r"^/api/memory/([A-Z_]+)$", parsed.path)
        if not match:
            self._send_json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "Unknown endpoint."})
            return

        file_key = match.group(1)
        if file_key not in MEMORY_FILES:
            self._send_json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "Invalid memory file key."})
            return

        payload = read_json_body(self)
        content = str(payload.get("content", ""))
        with WRITE_LOCK:
            write_text(MEMORY_FILES[file_key], content)

        self._send_json(HTTPStatus.OK, {"ok": True, "file": file_key, "chars": len(content)})


def run_server(host: str, port: int) -> None:
    server = ThreadingHTTPServer((host, port), FounderHandler)
    print(f"FounderOS local app running on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run FounderOS local web app.")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind.")
    parser.add_argument("--port", type=int, default=8787, help="Port to bind.")
    args = parser.parse_args()
    run_server(host=args.host, port=args.port)
