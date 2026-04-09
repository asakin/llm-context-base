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

If you install [Obsidian Web Clipper](https://obsidian.md/clipper), import the pre-built template to drop clips straight into your inbox with the right metadata:

1. Open the Web Clipper extension → click the **gear icon** → **Templates**
2. Click **Import** and select `assets/clipper-template.json` from this repo
3. Set it as your default template

That's it. Every clip lands in `_inbox/` with the metadata standard applied.

**The template adds one important field:**

```
> Why I saved this: [fill in one sentence before closing the clipper]
```

Fill this in before you close the clipper — one sentence is enough. Your AI uses it at triage to decide what to do:

| What you write | What the AI does |
|----------------|-----------------|
| "read later" | Leaves it in inbox, surfaces it at next session |
| "save the key points on X" | Extracts the relevant knowledge, files it, discards the raw clip |
| "relates to [project name]" | Links it to or files it under that project |
| "source for [draft name]" | Pulls relevant quotes into the draft |
| *(left blank)* | Asks you what you want before doing anything |

If you skip the line, your AI will ask before filing — it won't guess.

---

## Tips

**Store images locally.** Bind "Download attachments for current file" to a hotkey (e.g., `Ctrl+Shift+D`). The vault saves attachments to `assets/`. This downloads remote images to that local folder, preventing broken URLs. *(Tip from [Karpathy's original post](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))*

**Use the graph view.** As your wiki grows, the graph view becomes a map of your thinking. Color-coded directories make it easy to spot clusters and gaps.

**Let the AI handle organization.** Resist the urge to manually file things. Capture into `_inbox/`, then let your AI suggest where it goes. That's the whole point.

---

## Making It Look Good

The vault ships with a CSS snippet (`llm-wiki.css`) and graph view settings pre-configured. But you need to install a theme to get the full effect.

### Step 1: Install the Minimal theme (recommended)

1. Open Obsidian → Settings → Appearance → Themes → Browse
2. Search for **Minimal** and install it
3. The vault's `appearance.json` already points to it — it activates automatically

Minimal is the most popular Obsidian theme. It has clean typography, good dark/light mode support, and a companion plugin (Minimal Theme Settings) for further customization without touching CSS.

**Adapt to system theme:** In Settings → Appearance → Base color scheme, set it to **Adapt to system**. Obsidian will follow your OS's light/dark schedule automatically.

### Step 2: CSS snippet (already active)

The vault ships with `llm-wiki.css` in `.obsidian/snippets/`. It's already enabled. It does:

- **Metadata card** — the `**Type:**`, `**Summary:**`, etc. block at the top of every file renders as a subtle card with an accent border, not raw bold text
- **Typography** — readable line length (760px max), better heading hierarchy, 1.75 line height
- **Tables** — cleaner borders, hover highlight
- **Blockquotes** — styled as pull quotes with an accent bar

If you want to customize it: Settings → Appearance → CSS snippets → pencil icon next to `llm-wiki`.

### Step 3: Graph view

The graph is pre-configured with colors per directory:

| Color | Directory |
|-------|-----------|
| Blue | 1-Projects |
| Green | 2-Knowledge |
| Purple | 3-Journal |
| Red | 4-Private |
| Orange | _inbox |
| Gray | _meta, _config |
| Teal | _output, _sources |

If Obsidian resets your graph settings (it sometimes does when the vault reopens), you can restore them by running `git checkout .obsidian/graph.json` and restarting Obsidian.
