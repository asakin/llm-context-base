# FAQ

**On my first Claude Code session I saw something about a missing MEMORY.md. Is that an error?**

No. Claude Code has a built-in memory system that stores notes about your project in a file outside the repo (`~/.claude/projects/.../memory/MEMORY.md`). On the very first session it tries to read that file, finds it doesn't exist yet, and creates it. You'll only see this once.

---

**Does this work with local/smaller models (Ollama, etc.)?**

Yes. All instructions are plain markdown, no special API calls or tool use required. Smaller models may need you to manually update the `Current Phase` field in `_config/config.md` rather than calculating it automatically, and may not follow the training behavior as precisely. The core value (metadata standard, directory structure, templates) works regardless of model capability.

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
