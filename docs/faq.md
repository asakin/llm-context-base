# FAQ

**How do I get upstream updates?**

Two paths:

**Quick Start (template)** — what the README recommends. Clean start, no shared history. Fine if you set it up once and don't care about updates.

**Framework Track** — for users who want to pull improvements as the system evolves. Three extra steps upfront:

```bash
# 1. Clone directly (instead of "Use this template")
git clone https://github.com/asakin/llm-context-base.git my-wiki
cd my-wiki

# 2. Create an empty private repo on GitHub, then rewire remotes:
git remote rename origin upstream
git remote add origin https://github.com/YOU/my-wiki.git
git push -u origin main

# 3. Pull future updates:
git fetch upstream
git rebase upstream/main
git push --force-with-lease origin main
```

Your repo is fully independent (not a GitHub fork, not publicly linked). You just share git history with upstream, which is what makes rebase work cleanly.

---

**On my first Claude Code session I saw something about a missing MEMORY.md. Is that an error?**

No. Claude Code has a built-in memory system that stores notes about your project in a file outside the repo (`~/.claude/projects/.../memory/MEMORY.md`). On the very first session it tries to read that file, finds it doesn't exist yet, and creates it. You'll only see this once.

---

**Does this work with local/smaller models (Ollama, etc.)?**

Yes. All instructions are plain markdown, no special API calls or tool use required. Smaller models may need you to manually update the `Current Phase` field in `_config/config.md` rather than calculating it automatically, and may not follow the training behavior as precisely. The core value (metadata standard, directory structure, templates) works regardless of model capability.

---

**Will my company's proxy or firewall block this? Can I use it at work?**

There is nothing for a proxy to block. llm-context-base has zero runtime and generates no network activity of its own. It is a git clone of markdown files. After clone, the repo never touches the network: no telemetry, no phone-home, no CDN dependencies, no background processes, no analytics.

The only network-related question is whether your company allows the AI tool you use to read and write files (Claude Code, Cursor, Copilot, Windsurf, ChatGPT, etc.) — and that's the same question you'd face with or without this repo. If your AI tool works at work, llm-context-base works at work. The framework adds no additional surface a proxy could block.

This is a direct consequence of the substrate principle: the repo stays dumb, intelligence lives above it. See [PHILOSOPHY.md → The Substrate Principle](../PHILOSOPHY.md#the-substrate-principle) for the design rationale.

---

**Why not just use [existing wiki tool]?**

Most LLM wiki implementations focus on ingestion and retrieval. This system adds a training period that adapts the structure to your specific needs, templates battle-tested over months of daily use, an Obsidian-ready vault with graph visualization, and a lint system that keeps things healthy over time. It also works with any LLM, not locked to one provider.

---

**Should I use one vault for everything or split by domain?**

Start with one. The cross-domain connections are where the most value emerges. A decision about tooling might reference a knowledge article about deployment which links to a project initiative. Splitting loses these connections. If it gets unwieldy, the training period will help you find the right boundaries.

---

**Which Claude model should I use with this?**

Claude Sonnet 4.6 or Opus 4.6. Both support 1M token context windows natively. Avoid using the deprecated `context-1m-2025-08-07` beta header with older Sonnet models — it stops working April 30, 2026, and requests exceeding 200k tokens will error. If you're on an older model, upgrade to Sonnet 4.6.

---

**Can I load more context at session start with MCP?**

Yes. Claude Code's MCP integration now supports tool results up to 500,000 characters (set via `_meta["anthropic/maxResultSizeChars"]`). If you're building an MCP server to feed wiki content to Claude Code, you can advertise this limit to inject significantly more context at session start than was previously possible.

<!-- rebase smoke test -->
