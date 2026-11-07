# Using with Obsidian

The recommended setup is Obsidian on one side and your AI agent on the other. You talk to the agent; it reads, writes and organizes the notes; you watch them appear in Obsidian, follow links and browse the graph. The two don't need to be connected: they read and write the same folder.

---

## Setup

1. Run setup in your vault folder (see the [README](../README.md#quick-start)). It never touches `.obsidian/`, so your theme, plugins and hotkeys stay as they are. Setup's files live in hidden folders (`.agents/`, `.claude/`), so Obsidian doesn't show them; `AGENTS.md`, `CLAUDE.md` and the inbox are visible.
2. Open your agent in a terminal next to Obsidian, or inside Obsidian with one of the plugins below.
3. Optional: point Obsidian's **Default location for new notes** (Settings → Files and links) at the inbox so new notes land there.

If you want to edit `.agents/wiki/config.md` in Obsidian, open it from your editor or ask the agent to change it; Obsidian hides dot-folders.

## Agent skills for Obsidian syntax

[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) teaches agents Obsidian-flavored markdown, Bases, JSON Canvas and the Obsidian CLI. It complements llm-context-base, which handles what goes where and when; install both.

## Web Clipper

[Obsidian Web Clipper](https://obsidian.md/clipper) can drop pages straight into the inbox with frontmatter filled in.

1. Download [`assets/clipper-template.json`](../assets/clipper-template.json).
2. In Web Clipper: gear icon → Templates → Import, and select the file.
3. Set its note location to your inbox folder if it isn't `inbox`, and make it the default template.

Each clip starts with:

```text
> Why I saved this: [fill in one sentence before closing the clipper]
```

The agent uses that line when it files the inbox:

| What you write | What the agent does |
|---|---|
| "read later" | Leaves it in the inbox and brings it up at the next triage |
| "save the key points on X" | Extracts what matters into a note and discards the raw clip |
| "relates to [project]" | Files it under or links it from that project |
| "source for [draft]" | Pulls the relevant quotes into the draft |
| (blank) | Asks what you want before doing anything |

## Plugins for working with an agent inside Obsidian

All optional.

| Plugin | What it does |
|---|---|
| [Claudian](https://github.com/YishenTu/claudian) | A Claude Code panel inside Obsidian |
| [Terminal](https://github.com/polyipseity/obsidian-terminal) | A terminal pane, so you can run any agent CLI without leaving Obsidian |
| [Copilot for Obsidian](https://www.obsidiancopilot.com/) | A chat sidebar for several model providers. It doesn't read `AGENTS.md`, so the wiki rules don't apply there |

## Views over the metadata

Because notes carry YAML frontmatter, the core **Bases** plugin can show tables, cards or a kanban of notes filtered by `type`, `status`, `tags` or `updated`: an "active decisions" table, a board of initiatives by status, a list of drafts older than a month. Ask the agent to build one; with kepano/obsidian-skills installed it writes `.base` files directly. Dataview reads the same frontmatter if you prefer it.

## Tips

- **Keep images local.** Bind "Download attachments for current file" to a hotkey so remote images don't break later.
- **Let the agent file.** Capture into the inbox and let the agent propose where things go; that is what it's for.
- **Watch the graph.** Notes the agent links show up as clusters; isolated dots are what lint calls orphans.
