# 🤖 Sovereign AI Skills & Agents

This repository contains custom skill definitions and integration scripts used to extend the capabilities of **Gemini CLI** and other AI agents within my sovereign infrastructure.

## 🚀 Key Components

### 🧠 Custom Skills (`*.skill`)
- **`security-ops.skill`**: Expert guidance for security monitoring, log analysis, and incident response.
- **`predict-maint.skill`**: Specialized logic for predictive maintenance and infrastructure health monitoring.

### 🛠️ Integration Tools
- **`ollama_suite.py`**: A comprehensive bridge for interacting with local LLMs via the Ollama API, including custom generation and management functions.
- **`native_security_tools_function.py`**: Python-based function definitions that allow AI agents to interface natively with system security tools.

## 🏗️ Usage
These skills are designed to be activated within a Gemini CLI session to provide context-aware expertise and tool-calling capabilities.

```bash
# Example of activating a skill
gemini --activate-skill security-ops.skill
```

---
*Developed by Dina - Building autonomous, sovereign intelligence.*
