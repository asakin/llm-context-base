# Supported Tools

This repo works with any LLM that can read files. Agent-specific bootstrap files are included:

| Tool | Bootstrap File | Setup |
|------|---------------|-------|
| **Claude Code** | `.claude/CLAUDE.md` | Automatic |
| **Cursor** | `.cursor/rules/` | Automatic |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Automatic in VS Code |
| **Windsurf** | `.windsurfrules` | Automatic |
| **Codex CLI / Gemini CLI / others** | `AGENTS.md` | Automatic via the [AGENTS.md standard](https://agents.md/) |
| **ChatGPT / Others** | `_config/config.md` | Paste contents as system prompt or reference at session start |

## How It Works

All real instructions live in `_config/config.md` and `_meta/instructions/general.md`. The tool-specific files are thin shims that point there.

This is intentional. When you customize the system's behavior, you change it in one place and every tool picks it up. Adding support for a new tool is trivial: create a shim file that says "read config.md first."

## The State of Agent Instruction Files

The ecosystem is still converging. [AGENTS.md](https://agents.md/) (now under the Linux Foundation) is the closest thing to a cross-tool standard, but most tools still read their own proprietary file too. This repo ships shims for the most common ones. If your tool isn't listed, creating a shim takes 30 seconds.
