# 🤖 Sovereign AI Skills & Agents

> *Custom skill definitions and integration tools extending local AI agents within the sovereign lab — enabling autonomous security operations, infrastructure monitoring, and predictive maintenance.*

---

## 🎯 Overview

This repository defines custom skills and integration bridges used by local AI agents (Gemini CLI, Ollama-backed agents) to interact with the lab's infrastructure. Skills encode domain-specific expertise so AI agents can reason about security events, infrastructure health, and maintenance workflows without relying on external services.

---

## 🧠 Custom Skill Definitions

| Skill | Description |
|-------|-------------|
| `security-ops.skill` | Expert guidance for security monitoring, log analysis, and incident response workflows |
| `predict-maint.skill` | Predictive maintenance logic for infrastructure health monitoring and failure anticipation |

---

## 🛠️ Integration Tools

### `ollama_suite.py`
A comprehensive bridge for interacting with local LLMs via the Ollama API. Provides structured prompt management, context injection, and response parsing for agent workflows.

---

## 🔗 Ecosystem Integration

```
[Local AI Agent (Gemini CLI / Ollama)]
              │
     [sovereign-ai-skills]
      ├── security-ops.skill  ──→ [cybersecurity-lab-automation]
      ├── predict-maint.skill ──→ [sovereign-ai-infrastructure]
      └── ollama_suite.py     ──→ [local-ai-sovereign-stack]
```

---

## 🔗 Related Repositories

| Repository | Role |
|------------|------|
| [`local-ai-sovereign-stack`](https://github.com/Dinaverse/local-ai-sovereign-stack) | Ollama runtime |
| [`cybersecurity-lab-automation`](https://github.com/Dinaverse/cybersecurity-lab-automation) | Security automation target |
| [`sovereign-ai-infrastructure`](https://github.com/Dinaverse/sovereign-ai-infrastructure) | Infrastructure context |

---

*Skills that run locally — AI sovereignty in practice.*
