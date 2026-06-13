# Supported Tools

This repo works with any LLM that can read files. Agent-specific bootstrap files are included:

| Tool | Bootstrap File | Setup |
|------|---------------|-------|
| **Claude Code** | `.claude/CLAUDE.md`, `.claude/agents/` | Automatic; includes native wiki-maintainer subagents |
| **Cursor** | `.cursor/rules/` | Automatic |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Automatic in VS Code |
| **Windsurf** | `.windsurfrules` | Automatic |
| **Codex CLI / Gemini CLI / others** | `AGENTS.md` | Automatic via the [AGENTS.md standard](https://agents.md/) |
| **Claude Chat (claude.ai)** | — | GitHub sync via Projects (see below) |
| **ChatGPT** | — | GitHub connector or Vector Store Sync (see below) |

## How It Works

All real instructions live in `_config/config.md` and `_meta/instructions/general.md`. The tool-specific bootstrap files are thin shims that point there.

Claude Code also supports native project subagents in `.claude/agents/`. This repo uses that newer agent framework for role-specific wiki maintenance agents — librarian, researcher, critic, gardener, and editor — instead of relying only on broad prompt instructions.

This is intentional. When you customize the system's core behavior, you change it in one place and every tool picks it up. When a tool has a first-class agent framework, this repo can add focused role definitions that still point back to the same LLM Wiki principles.

## The State of Agent Instruction Files

The ecosystem is still converging. [AGENTS.md](https://agents.md/) (now under the Linux Foundation) is the closest thing to a cross-tool standard, but most tools still read their own proprietary file too. This repo ships shims for the most common ones. If your tool isn't listed, creating a shim takes 30 seconds.

---

## Agentic Tools vs. Chat LLMs

There are two classes of tools, and they work differently with this system.

**Agentic tools** (Claude Code, Cursor, Copilot, Windsurf) have file system access. They read your wiki at session start, write files, and commit to git. They get the full experience — session start protocol, routing table, lint, everything.

**Chat LLMs** (Claude Chat, ChatGPT) have no file system access by default. They can't write to your repo. They're thinking partners and research tools — useful alongside agentic tools, not as replacements for them.

The practical split:
- Use an agentic tool to capture, file, and maintain the wiki
- Use a chat LLM to research, brainstorm, and think — then bring the output back to the agentic tool to file

---

## Using Claude Chat (claude.ai) with Your Wiki

### GitHub Sync via Claude Projects

Claude Projects has an official GitHub connector. Setup:

1. Create a Project at [claude.ai](https://claude.ai)
2. In the project settings, connect your GitHub repo
3. Select the branch and files to sync — recommended: `_config/config.md`, `_config/context.md`, and whatever you're currently working on
4. Every chat in the project loads those files as background context

When you push changes, click "Sync now" inside the project to pull the latest. One click, not a re-upload.

**What gets synced:** File contents only. Not git history or PR metadata.

**For private repos:** Claude reads through GitHub's OAuth — your data stays inside GitHub's trust boundary. Nothing is exposed publicly.

---

## Using ChatGPT with Your Wiki

Two options, in increasing order of automation.

### Option A: GitHub Connector (On-Demand)

ChatGPT can connect to your GitHub repo and read it in real time via the GitHub connector in ChatGPT settings. Good for one-off questions about your wiki content without any setup beyond OAuth.

### Option B: Vector Store Sync (Automatic)

The [ChatGPT Assistants Vector Store Sync](https://github.com/marketplace/actions/chatgpt-assistants-vector-store-sync) GitHub Action automatically updates a ChatGPT assistant's knowledge base every time you push to the repo. After setup, every `git push` triggers a sync — no manual action needed.

This is the most automated option available without building a custom server.

---

## MCP Servers and Privacy

An MCP server wrapping the wiki can expose it to any MCP-compatible client. Before setting one up, consider:

**Local MCP server (safe):** Run it on `localhost` only. Claude Code connects to it locally. Nothing touches the internet. Works when your computer is on; doesn't help with mobile or remote access.

**Internet-facing MCP server (use carefully):** Exposes your wiki over the internet. If your wiki contains private notes, journal entries, or sensitive decisions, this is a real risk. If you need it, protect it with a secret token and run it on a managed platform (Cloudflare Workers, Fly.io) rather than your own machine.

**The safer alternative for most needs:** The GitHub-based sync options above (Claude Projects, ChatGPT connector) keep everything within GitHub's security perimeter. You're already trusting GitHub with the data — these integrations don't expand that trust boundary.

**GitHub Actions as private compute:** For automation that needs to read the full wiki and do AI-powered work (summaries, analysis, scheduled reports), GitHub Actions is a good option. It runs within GitHub's infrastructure, reads your private repo with your credentials, and writes results back — no server required, no data exposed.
