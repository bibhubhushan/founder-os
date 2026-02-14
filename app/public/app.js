const state = {
  commands: {},
  selectedCommand: "/coo",
  memory: {},
  selectedMemoryKey: "ACTIVE_PROJECT",
  suggestions: [],
};

const els = {
  healthDot: document.getElementById("healthDot"),
  healthText: document.getElementById("healthText"),
  commandList: document.getElementById("commandList"),
  quickPrompts: document.getElementById("quickPrompts"),
  commandSelect: document.getElementById("commandSelect"),
  routeBadge: document.getElementById("routeBadge"),
  messages: document.getElementById("messages"),
  suggestions: document.getElementById("suggestions"),
  input: document.getElementById("input"),
  composer: document.getElementById("composer"),
  persistToggle: document.getElementById("persistToggle"),
  clearChatBtn: document.getElementById("clearChatBtn"),
  memoryTabs: document.getElementById("memoryTabs"),
  memoryEditor: document.getElementById("memoryEditor"),
  saveMemoryBtn: document.getElementById("saveMemoryBtn"),
  reloadMemoryBtn: document.getElementById("reloadMemoryBtn"),
  messageTemplate: document.getElementById("messageTemplate"),
};

async function jsonFetch(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const payload = await response.json().catch(() => ({}));
  if (!response.ok || payload.ok === false) {
    const error = payload.error || `Request failed: ${response.status}`;
    throw new Error(error);
  }
  return payload;
}

function nowTime() {
  return new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

function addMessage(role, content, meta = "") {
  const node = els.messageTemplate.content.firstElementChild.cloneNode(true);
  node.classList.add(role);

  const roleNode = node.querySelector(".msg-role");
  const metaNode = node.querySelector(".msg-meta");
  const contentNode = node.querySelector(".msg-content");

  roleNode.textContent = role === "assistant" ? "FounderOS" : "You";
  metaNode.textContent = meta || nowTime();
  contentNode.textContent = content;

  els.messages.appendChild(node);
  els.messages.scrollTop = els.messages.scrollHeight;
}

function setSuggestions(items) {
  state.suggestions = items || [];
  els.suggestions.innerHTML = "";

  state.suggestions.forEach((item) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "suggestion-chip";
    button.textContent = item;
    button.addEventListener("click", () => {
      els.input.value = item;
      els.input.focus();
    });
    els.suggestions.appendChild(button);
  });
}

function setSelectedCommand(command) {
  if (!state.commands[command]) {
    return;
  }
  state.selectedCommand = command;
  els.routeBadge.textContent = command;
  els.commandSelect.value = command;

  document.querySelectorAll(".command-btn").forEach((node) => {
    node.classList.toggle("active", node.dataset.command === command);
  });
}

function renderCommands() {
  els.commandList.innerHTML = "";
  els.commandSelect.innerHTML = "";

  const ordered = Object.entries(state.commands).sort(([a], [b]) => a.localeCompare(b));

  ordered.forEach(([command, details]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "command-btn";
    button.dataset.command = command;
    button.innerHTML = `<strong>${command}</strong><small>${details.title}</small>`;
    button.addEventListener("click", () => setSelectedCommand(command));
    els.commandList.appendChild(button);

    const option = document.createElement("option");
    option.value = command;
    option.textContent = `${command} - ${details.agent}`;
    els.commandSelect.appendChild(option);
  });

  els.commandSelect.addEventListener("change", (event) => {
    setSelectedCommand(event.target.value);
  });

  setSelectedCommand(state.selectedCommand);
}

function renderQuickPrompts(prompts) {
  els.quickPrompts.innerHTML = "";

  prompts.forEach((prompt) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "prompt-btn";
    button.innerHTML = `<strong>${prompt.label}</strong><small>${prompt.command}</small>`;
    button.addEventListener("click", () => {
      setSelectedCommand(prompt.command);
      els.input.value = prompt.message;
      els.input.focus();
    });
    els.quickPrompts.appendChild(button);
  });
}

function renderMemoryTabs() {
  els.memoryTabs.innerHTML = "";

  Object.keys(state.memory).forEach((key) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "memory-tab";
    button.dataset.key = key;
    button.textContent = key;
    button.addEventListener("click", () => {
      state.selectedMemoryKey = key;
      updateMemoryEditor();
      renderMemoryTabs();
    });

    if (state.selectedMemoryKey === key) {
      button.classList.add("active");
    }

    els.memoryTabs.appendChild(button);
  });
}

function updateMemoryEditor() {
  els.memoryEditor.value = state.memory[state.selectedMemoryKey] ?? "";
}

async function loadHealth() {
  try {
    await jsonFetch("/api/health", { method: "GET" });
    els.healthDot.classList.add("ok");
    els.healthText.textContent = "Server online";
  } catch (error) {
    els.healthDot.classList.remove("ok");
    els.healthText.textContent = "Server offline";
    addMessage("assistant", `Server check failed: ${error.message}`, "system");
  }
}

async function loadBootstrap() {
  const payload = await jsonFetch("/api/bootstrap", { method: "GET" });
  state.commands = payload.commands;
  renderCommands();
  renderQuickPrompts(payload.quick_prompts || []);
}

async function loadMemory() {
  const payload = await jsonFetch("/api/memory", { method: "GET" });
  state.memory = payload.memory || {};

  if (!state.memory[state.selectedMemoryKey]) {
    state.selectedMemoryKey = Object.keys(state.memory)[0] || "ACTIVE_PROJECT";
  }

  renderMemoryTabs();
  updateMemoryEditor();
}

async function sendChat(message) {
  addMessage("user", message, state.selectedCommand);

  try {
    const payload = await jsonFetch("/api/chat", {
      method: "POST",
      body: JSON.stringify({
        message,
        command: state.selectedCommand,
        autoPersist: els.persistToggle.checked,
      }),
    });

    const route = payload.route || {};
    const responseMessage = payload.message || {};

    setSelectedCommand(route.selected || state.selectedCommand);
    addMessage(
      "assistant",
      responseMessage.content || "No response",
      `${responseMessage.agent || "AGENT"} - ${route.reason || "routed"}`
    );

    setSuggestions(payload.suggestions || []);
  } catch (error) {
    addMessage("assistant", `Error: ${error.message}`, "system");
  }
}

async function saveMemory() {
  const key = state.selectedMemoryKey;
  const content = els.memoryEditor.value;

  try {
    await jsonFetch(`/api/memory/${key}`, {
      method: "PUT",
      body: JSON.stringify({ content }),
    });

    state.memory[key] = content;
    addMessage("assistant", `${key} saved successfully.`, "memory");
  } catch (error) {
    addMessage("assistant", `Failed to save ${key}: ${error.message}`, "memory");
  }
}

function bindEvents() {
  els.composer.addEventListener("submit", async (event) => {
    event.preventDefault();
    const message = els.input.value.trim();
    if (!message) return;

    els.input.value = "";
    await sendChat(message);
  });

  els.clearChatBtn.addEventListener("click", () => {
    els.messages.innerHTML = "";
    addMessage(
      "assistant",
      "Chat reset. Share your next objective and I will route it to the right command.",
      "system"
    );
    setSuggestions([]);
  });

  els.saveMemoryBtn.addEventListener("click", saveMemory);

  els.reloadMemoryBtn.addEventListener("click", async () => {
    await loadMemory();
    addMessage("assistant", "Memory reloaded from disk.", "memory");
  });

  els.input.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key === "Enter") {
      event.preventDefault();
      els.composer.requestSubmit();
    }
  });
}

async function init() {
  bindEvents();

  await loadHealth();
  await loadBootstrap();
  await loadMemory();

  addMessage(
    "assistant",
    "FounderOS local console is ready. Pick a command or type your objective. Use Cmd/Ctrl+Enter to send.",
    "system"
  );

  setSuggestions([
    "/coo Break this idea into a one-week sprint.",
    "/team_mvp Scope and ship an MVP in 72 hours.",
    "/ceo Challenge this strategy before building.",
  ]);
}

init();
