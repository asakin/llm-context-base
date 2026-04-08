# Using with Obsidian

The recommended way to use this system: **Obsidian on one side, your AI agent on the other.** You talk to the AI. It reads, writes, and organizes your wiki. You watch the results appear in Obsidian in real time — follow links, check the graph view, browse what's changed.

Obsidian is where you browse your wiki. You can talk to your AI directly inside Obsidian using a plugin, from a terminal alongside it, or from any AI tool you already use — Claude Code, Cursor, the Claude app, whatever you prefer.

---

## Getting Started

**1. Open the vault.** This repo ships as a ready-to-use Obsidian vault. Open the cloned directory as a vault in Obsidian — graph colors, core plugins, and display settings are pre-configured.

**2. Pick your AI agent.** You have two options:

- **Inside Obsidian** — install an LLM plugin like [Claudian](https://github.com/YishenTu/claudian) or [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) to chat with your AI directly in the editor
- **Side by side** — open a terminal or AI tool (Claude Code, Cursor, ChatGPT, etc.) next to Obsidian

Either way works. The key is having both open at once — you talk on one side, the wiki updates on the other.

**3. Start talking.** See the [Quick Start](../README.md#quick-start) for what to say first.

---

## What's Pre-configured

Already set in the shipped vault, no action needed:

| Setting | Value | Why |
|---------|-------|-----|
| New files default location | `_inbox/` | Ctrl+N always creates in the inbox. Inbox-first without thinking. |
| Templates folder | `_meta/templates/` | Ctrl+T inserts from the included set. |
| Daily notes location | `3-Journal/` | Daily note button creates a journal entry with the right template. |
| Attachments location | `assets/` | Images stored in a fixed directory, not scattered. |
| Graph view | Color-coded by directory | Projects (blue), Knowledge (green), Journal (purple), Private (red), Inbox (orange), System files (gray) |
| Workspace files | Gitignored | Your local layout stays private. |

---

## Recommended Plugins

### LLM Integration

These give you an AI console inside Obsidian, so you don't need a separate terminal:

| Plugin | What it does |
|--------|-------------|
| **[Claudian](https://github.com/YishenTu/claudian)** | Claude Code inside Obsidian — read/write wiki entries directly in the editor |
| **[claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)** | Claude Code plugin with hot cache for minimal context usage |
| **[Copilot](https://www.obsidiancopilot.com/)** | AI chat over your vault — conversational Q&A across your entire knowledge base |

### Enhanced Browsing

These make the viewing and navigation side better:

| Plugin | What it does |
|--------|-------------|
| **[Obsidian Web Clipper](https://obsidian.md/clipper)** | Save web pages as markdown directly into `_inbox/` |
| **[Dataview](https://blacksmithgu.github.io/obsidian-dataview/)** | Query engine for markdown metadata — build dashboards and filtered views* |
| **[Templater](https://github.com/SilentVoid13/Templater)** | Dynamic templates with variables — auto-populate metadata blocks |
| **[Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes)** | Daily/weekly/monthly notes mapped to `3-Journal/` |
| **[Kanban](https://github.com/mgmeyers/obsidian-kanban)** | Markdown-backed kanban boards for visual project management |

*\*Dataview note: Dataview inline fields require double-colon syntax (`**Type**:: knowledge`) while this system uses single-colon (`**Type:** knowledge`). If you want Dataview queries, either use double-colons in your files or use YAML frontmatter. The single-colon format is optimized for LLM readability.*

---

## Web Clipper Setup

If you install [Obsidian Web Clipper](https://obsidian.md/clipper), configure it to drop clips straight into your inbox:

1. Open the Web Clipper extension, click the **gear icon**, then **Templates**
2. Edit the **Default** template:
   - **Note name:** `{{date|date:"YYYY-MM-DD"}}-{{title}}`
   - **Note location:** `_inbox`
   - **Note content:** (add the metadata block at the top)
     ```
     **Type:** knowledge
     **Summary:** {{meta:name:description}}
     **Tags:** #clipped
     **Status:** draft
     **Updated:** {{date|date:"YYYY-MM-DD"}}
     **Source:** {{url}}

     ---

     {{content}}
     ```

One-click web capture that lands in your inbox with the metadata standard applied. Your AI picks it up at the next session and offers to file it.

---

## Tips

**Store images locally.** Bind "Download attachments for current file" to a hotkey (e.g., `Ctrl+Shift+D`). The vault saves attachments to `assets/`. This downloads remote images to that local folder, preventing broken URLs. *(Tip from [Karpathy's original post](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))*

**Use the graph view.** As your wiki grows, the graph view becomes a map of your thinking. Color-coded directories make it easy to spot clusters and gaps.

**Let the AI handle organization.** Resist the urge to manually file things. Capture into `_inbox/`, then let your AI suggest where it goes. That's the whole point.
