# Supported Tools

llm-context-base works with any AI agent that can read and write files in a folder. The rules live in `AGENTS.md`, which most agents now read on their own; the on-demand parts are [Agent Skills](https://agentskills.io) in `.agents/skills/`.

---

## Agents with file access

| Tool | Reads the rules from | Skills | Warren and Marlowe |
|---|---|---|---|
| **Claude Code** | `CLAUDE.md`, which imports `AGENTS.md` | `.claude/skills/` (setup links it to `.agents/skills/`) | Native subagents |
| **Codex** | `AGENTS.md` | `.agents/skills/` | — |
| **Cursor** | `AGENTS.md` | `.agents/skills/` | — |
| **GitHub Copilot** (VS Code, CLI, cloud agent) | `AGENTS.md` | `.agents/skills/` | — |
| **Antigravity CLI** (successor to Gemini CLI) | `AGENTS.md` | `.agents/skills/` | — |
| **pi** | `AGENTS.md` | `.agents/skills/` | Through the pi agents extension, which setup offers when `pi` is installed |
| **Devin Desktop** (formerly Windsurf) | `AGENTS.md` | Reads a skill's file when `AGENTS.md` points it there | — |
| **Gemini CLI** | `GEMINI.md` by default; add `AGENTS.md` to `context.fileName` in `.gemini/settings.json` | `.agents/skills/` | — |
| **Anything else** | Tell it to read `AGENTS.md` first | `AGENTS.md` lists each skill's path | — |

Claude Code needs the `CLAUDE.md` import because it reads `AGENTS.md` only when no `CLAUDE.md` exists, and versions before 2.1.277 don't read it at all. The one-line `@AGENTS.md` works on every version.

If a tool doesn't load skills by itself, nothing breaks: `AGENTS.md` names each skill and tells the agent to read its `SKILL.md` when a task matches.

## Chat apps

Chat apps without access to your files (the Claude and ChatGPT apps) can read a wiki kept in a GitHub repository through their GitHub connectors. Use them for research and thinking, then bring the result to an agent with file access to capture and file it. They can't follow the write rules, so they shouldn't be the ones editing the wiki.

## Local models

The instructions are plain markdown and need no special tool calls. Smaller local models handle the capture, metadata and query rules; multi-step skills such as setup and lint go better with a stronger model.

## Privacy

llm-context-base makes no network calls of its own. What leaves your machine is whatever your agent sends to its model provider, so the question is the usual one: is that tool allowed to read these files? Folders listed under `private` in config are never quoted in anything that leaves the wiki.

If you expose the wiki through an MCP server, keep it on `localhost` unless you need remote access, and put authentication in front of a remote one. A wiki usually holds things you wouldn't publish.
