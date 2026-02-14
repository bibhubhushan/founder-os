#!/usr/bin/env bash
set -euo pipefail

# Sync only persistent memory files across tools (Claude/Codex/Antigravity).
# Usage:
#   ./sync_memory.sh
#   ./sync_memory.sh "chore(memory): update after session"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not inside a git repository."
  exit 1
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
MESSAGE="${1:-chore(memory): sync $(date '+%Y-%m-%d %H:%M')}"

MEMORY_FILES=(
  "memory/ACTIVE_PROJECT.md"
  "memory/DECISIONS.md"
  "memory/JOURNAL.md"
  "memory/LESSONS.md"
  "memory/EVALS.md"
)

UPSTREAM=""
if UPSTREAM="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null)"; then
  echo "Pulling latest changes from ${UPSTREAM}..."
  git pull --rebase --autostash
else
  if git remote get-url origin >/dev/null 2>&1; then
    echo "No upstream set for branch '${BRANCH}'."
    echo "I will push with: git push -u origin ${BRANCH}"
  else
    echo "No remote configured. Add one first:"
    echo "  git remote add origin <repo-url>"
    exit 1
  fi
fi

echo "Staging memory files..."
git add "${MEMORY_FILES[@]}"

if git diff --cached --quiet; then
  echo "No memory changes to commit."
else
  echo "Committing memory updates..."
  git commit -m "${MESSAGE}"
fi

if [[ -n "${UPSTREAM}" ]]; then
  echo "Pushing to ${UPSTREAM}..."
  git push
else
  echo "Pushing and setting upstream..."
  git push -u origin "${BRANCH}"
fi

echo "Memory sync complete."
