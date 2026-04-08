# Using with Obsidian

This repo ships as a ready-to-use Obsidian vault. Open the cloned directory as a vault. Graph colors, core plugins, and display settings are pre-configured.

---

## What's Included

- **Graph view color-coded by directory** — Projects (blue), Knowledge (green), Journal (purple), Private (red), Inbox (orange), System files (gray)
- **Core plugins enabled** — file explorer, graph, backlinks, tags, daily notes, templates, outline, search
- **Workspace files gitignored** — your local layout stays private

## Pre-configured Settings

Already set in the shipped vault, no action needed:

| Setting | Value | Why |
|---------|-------|-----|
| New files default location | `_inbox/` | Ctrl+N always creates in the inbox. Inbox-first without thinking. |
| Templates folder | `_meta/templates/` | Ctrl+T inserts from the included set. |
| Daily notes location | `3-Journal/` | Daily note button creates a journal entry with the right template. |
| Attachments location | `assets/` | Images stored in a fixed directory, not scattered. |

## Recommended Community Plugins

| Plugin | What it does | Why it fits |
|--------|-------------|-------------|
| **[Claudian](https://github.com/YishenTu/claudian)** | Claude Code inside Obsidian | Read/write wiki entries directly in the editor |
| **[claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)** | Claude Code plugin for Obsidian vaults | Cross-referenced wiki pages with hot cache for minimal context usage |
| **[Obsidian Web Clipper](https://obsidian.md/clipper)** | Save web pages as markdown | Clip articles, docs, and references directly into `_inbox/` |
| **[Dataview](https://blacksmithgu.github.io/obsidian-dataview/)** | Query engine for markdown metadata | Build dashboards and filtered views from your metadata* |
| **[Templater](https://github.com/SilentVoid13/Templater)** | Dynamic templates with variables | Auto-populate metadata blocks when creating new files |
| **[Copilot](https://www.obsidiancopilot.com/)** | AI chat over your vault | Conversational Q&A across your entire knowledge base |
| **[Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes)** | Daily/weekly/monthly notes | Maps to your `3-Journal/` directory with templated entries |
| **[Kanban](https://github.com/mgmeyers/obsidian-kanban)** | Markdown-backed kanban boards | Visual project management for `1-Projects/` |

*\*Dataview note: Dataview inline fields require double-colon syntax (`**Type**:: knowledge`) while this system uses single-colon (`**Type:** knowledge`). If you want Dataview queries, either use double-colons in your files or use YAML frontmatter. The single-colon format is optimized for LLM readability.*

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

## Tips

**Store images locally.** Bind "Download attachments for current file" to a hotkey (e.g., `Ctrl+Shift+D`). The vault saves attachments to `assets/`. This hotkey downloads remote images in existing files to that local folder, preventing broken URLs. *(Tip from [Karpathy's original post](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))*

**Side-by-side workflow.** Keep your AI agent open on one side and Obsidian on the other. Watch edits in real-time, follow links, and check the graph view as your wiki grows. *(Also from Karpathy)*
