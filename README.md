# llm-context-base

**A bootstrap repo for building your own LLM-powered knowledge base.**

Use the template, point your AI assistant at it, and start talking. Over time, it learns how you work and adapts its structure to your needs without you having to design anything upfront.

---

## What This Is

This is an implementation of [Andrej Karpathy's LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - the idea that an LLM should incrementally build and maintain a persistent, structured knowledge base rather than rediscovering everything from raw documents on every query.

I've been building a more advanced version of this pattern over the past few months, applied to running a business operations organization. This repo extracts the core framework so anyone can use it - whether you're a CIO managing a team, a developer organizing technical knowledge, a researcher cataloguing papers, or someone who just wants a better way to organize recipes.

**Key additions beyond the basic pattern:**
- A **metadata standard** across all document types (not just knowledge pages) - makes every file queryable by any LLM
- An **inbox-first capture protocol** - frictionless capture with automated triage
- A **training period** - the system starts chatty (learning your needs) and becomes quiet as it adapts
- A **lint operation** - keeps your wiki healthy over time
- **Templates** for common document types - decisions, initiatives, meeting notes, knowledge articles
- **Multi-LLM support** - works with Claude Code, Cursor, GitHub Copilot, ChatGPT, Gemini, and any other LLM

---

## Quick Start (5 minutes)

### 1. Create Your Copy

Click **"Use this template"** → **"Create a new repository"** on GitHub. Make it private (this will be *your* knowledge base). Then clone your new repo:

```bash
git clone https://github.com/YOUR-USERNAME/my-wiki.git
cd my-wiki
```

### 2. Configure

Open `_config/config.md` and fill in the **About You** section:

```markdown
**Name:** Jane
**Role:** Software engineer at a startup
**Goals:** I want to organize my technical knowledge, track decisions, and build a personal reference system
**Context:** I work across frontend and backend, and I'm often the one documenting processes for the team
```

Set `Training Start Date` to today's date (format: `YYYY-MM-DD`).

### 3. Start Talking

Open in your AI tool of choice and just... talk:

**For personal knowledge:**
- *"I just read a great article about productivity - capture the key ideas for me"*
- *"We decided to go with the Montessori school over the public option - let me document why"*
- *"What do I know about meal planning?"*

**For teams and organizations:**
- *"Capture this: here's how our onboarding process works..."*
- *"We decided to switch from Slack to Teams - let me document the rationale"*
- *"Lint the wiki - what needs attention?"*

**For developers:**
- *"I just figured out how to configure our CI pipeline - capture this for me"*
- *"We decided to use PostgreSQL over MongoDB - let me document why"*
- *"What do we know about our deployment process?"*

The system will adapt to what you actually need.

---

## Walking the Pattern

When you first create your copy, the system doesn't know you. A recipe collector needs different structure than an engineering lead. So rather than asking you to design your wiki upfront, the system walks the pattern with you - an initial period of active collaboration where the AI learns how you think, what you need, and how to organize your knowledge. By the end, the system is transformed into something uniquely yours.

**How it works:**

| Phase           | Duration                 | Behavior                                                                                                                             |
| --------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Training**    | Days 1–30 (configurable) | Chatty. Asks about your role, suggests directories, learns preferences, logs adaptations.                                            |
| **Cooldown**    | Days 31–44               | Quieter. ~70% fewer suggestions. Uses what it learned.                                                                               |
| **Established** | Day 45+                  | Silent efficiency. Just works. Only speaks up when something is broken or when new content types need structural changes. |

During training, your AI will:
- Ask questions about how you work
- Suggest new directories when content doesn't fit
- Propose naming conventions based on your patterns
- Log everything it learns in `_config/config.md`

The system uses **just-in-time context loading**: your AI doesn't read every instruction file at startup. It loads `_config/config.md` first (always), then pulls in specific instruction modules only when triggered (e.g., the lint module loads only when you say "lint the wiki"). This keeps context windows efficient as your wiki grows.

By the end of training, the system is customized to *your* needs without you having to design anything upfront.

**Configure in `_config/config.md`:**
```markdown
**Training Start Date:** 2026-04-07
**Training Period Days:** 30
```

---

## Directory Structure

```
llm-context-base/
  _config/                    # Your configuration (the brain)
    config.md                 # Profile + training controller + LLM instructions
    standard.md               # Document metadata standard

  _meta/                      # System instructions (the engine)
    instructions/             # How the AI operates
    templates/                # Document templates

  _inbox/                     # Frictionless capture zone
  _output/                    # Generated artifacts (presentations, exports, reports)
  _sources/                   # Preserved originals (opt-in, see config.md)
  1-Projects/                 # Active multi-artifact work
  2-Knowledge/                # What you know
    HowTo/                    # Step-by-step guides
    Decisions/                # Decision records
    References/               # Manuals, specs, architecture docs
  3-Journal/                  # What you think (private reflections)
  4-Private/                  # Sensitive content (gitignored)
  examples/                   # Example files showing the standard in action
```

**Why only 4 directories?** The system starts minimal. During the training period, the AI will suggest new directories based on your actual usage. A recipe collector might end up with `5-Recipes/` and `6-MealPlans/`. A CIO might end up with `5-Strategy/` and `6-Operations/`. The structure adapts to you.

---

## The Metadata Standard

Every file gets a metadata block at the top. This is what makes the system queryable - your AI can scan summaries and tags without reading full files.

```markdown
# How I Organize My Weekly Meal Prep

**Type:** knowledge
**Summary:** Weekly meal prep workflow including grocery list generation and batch cooking schedule.
**Tags:** #cooking #how-to #meal-prep
**Status:** active
**Owner:** Jane
**Updated:** 2026-04-07
**Related:** [favorite-recipes.md](2-Knowledge/References/favorite-recipes.md)
```

A developer's version might look like:

```markdown
# How We Deploy to Production

**Type:** knowledge
**Summary:** Step-by-step deployment process including rollback procedures and monitoring checks.
**Tags:** #engineering #how-to #deployment
**Status:** active
**Owner:** Jane
**Updated:** 2026-04-07
**Related:** [ci-pipeline-setup.md](2-Knowledge/HowTo/ci-pipeline-setup.md)
```

Each field serves a specific purpose in the system:
- **Summary** enables query routing - your AI reads summaries to find relevant files without loading entire documents
- **Status** prevents draft accumulation - the [Definition of Done](_meta/instructions/definition-of-done.md) module uses this to distinguish live knowledge from work-in-progress
- **Related** creates a navigable knowledge graph - your AI follows these links to surface connected context, and Obsidian renders them in the graph view
- **Tags** act as a secondary discovery mechanism - when query routing by summary doesn't surface what you need, tags provide cross-cutting categories
- **Updated** powers the lint system - files with active status that haven't been updated in 90+ days get flagged for review

See `_config/standard.md` for the full specification and the rationale behind bold fields vs. YAML frontmatter.

---

## Supported Tools

This repo works with any LLM that can read files. Agent-specific bootstrap files are included:

| Tool | Bootstrap File | Setup |
|------|---------------|-------|
| **Claude Code** | `.claude/CLAUDE.md` | Automatic - just open the project |
| **Cursor** | `.cursor/rules/` | Automatic - just open the project |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Automatic in VS Code |
| **Windsurf** | `.windsurfrules` | Automatic - just open the project |
| **Codex CLI / Gemini CLI / others** | `AGENTS.md` | Automatic - the [AGENTS.md standard](https://agents.md/) is supported by most tools |
| **ChatGPT / Others** | `_config/config.md` | Paste contents as system prompt or reference at session start |

All real instructions live in `_config/config.md` and `_meta/instructions/general.md` - the tool-specific files are thin shims that point there. This centralization is intentional: when you customize the system's behavior, you change it in one place and every tool picks it up. It also means adding support for a new tool is trivial - just create a shim file that says "read config.md first."

The ecosystem of agent instruction files is still converging. [AGENTS.md](https://agents.md/) (now under the Linux Foundation) is the closest thing to a cross-tool standard, but most tools still read their own proprietary file too. This repo ships shims for the most common ones. If your tool isn't listed, creating a shim takes 30 seconds.

---

## Using with Obsidian

This repo ships as a ready-to-use Obsidian vault. Just open the cloned directory as a vault - graph colors, core plugins, and display settings are pre-configured.

**What's included:**
- **Graph view color-coded by directory** - Projects (blue), Knowledge (green), Journal (purple), Private (red), Inbox (orange), System files (gray)
- **Core plugins enabled** - file explorer, graph, backlinks, tags, daily notes, templates, outline, search
- **Workspace files gitignored** - your local layout stays private

### Recommended Community Plugins

These plugins pair well with the LLM wiki pattern:

| Plugin | What it does | Why it fits |
|--------|-------------|-------------|
| **[Claudian](https://github.com/YishenTu/claudian)** | Claude Code inside Obsidian | Your AI reads/writes wiki entries directly in the editor |
| **[claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)** | Claude Code plugin for Obsidian vaults | Cross-referenced wiki pages with hot cache for minimal context usage |
| **[Obsidian Web Clipper](https://obsidian.md/clipper)** | Save web pages as markdown | Clip articles, docs, and references directly into your wiki or `_inbox/` |
| **[Dataview](https://blacksmithgu.github.io/obsidian-dataview/)** | Query engine for markdown metadata | Build dashboards and filtered views from your metadata* |
| **[Templater](https://github.com/SilentVoid13/Templater)** | Dynamic templates with variables | Auto-populate metadata blocks when creating new files |
| **[Copilot](https://www.obsidiancopilot.com/)** | AI chat over your vault | Conversational Q&A across your entire knowledge base |
| **[Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes)** | Daily/weekly/monthly notes | Maps to your `3-Journal/` directory with templated entries |
| **[Kanban](https://github.com/mgmeyers/obsidian-kanban)** | Markdown-backed kanban boards | Visual project management for `1-Projects/` |

*\*Dataview note: Dataview inline fields require double-colon syntax (`**Type**:: knowledge`) while this system uses single-colon (`**Type:** knowledge`). If you want Dataview queries, either use double-colons in your files or use YAML frontmatter. The single-colon format is optimized for LLM readability.*

### Pre-configured Settings

These are already set in the shipped vault - no action needed:

- **New files default to `_inbox/`** - Ctrl+N always creates in the inbox. Inbox-first without thinking.
- **Templates folder → `_meta/templates/`** - Ctrl+T inserts a template from the included set.
- **Daily notes → `3-Journal/`** - Daily note button creates a journal entry with the right template.
- **Attachments → `assets/`** - Images stored locally in a fixed directory, not scattered.

### Web Clipper Setup

If you install [Obsidian Web Clipper](https://obsidian.md/clipper), configure it to drop clips straight into your inbox:

1. Open the Web Clipper extension → click the **gear icon** → **Templates**
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

This gives you one-click web capture that lands in your inbox with the metadata standard already applied. Your AI will pick it up at the next session and offer to file it.

### Tips for Obsidian Setup

**Store images locally.** Bind "Download attachments for current file" to a hotkey (e.g., `Ctrl+Shift+D`). The vault is already configured to save attachments to `assets/` - this hotkey downloads remote images in existing files to that local folder, preventing broken URLs. *(Tip from [Karpathy's original post](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))*

**Side-by-side workflow.** Keep your AI agent (Claude Code, terminal, etc.) open on one side and Obsidian on the other. Watch edits in real-time, follow links, and check the graph view as your wiki grows. *(Also from Karpathy)*

---

## What You Can Do

These capabilities aren't independent features - they form a cycle. You capture knowledge, which feeds queries, which inform decisions, which get tracked, which get reviewed by lint, which surfaces what needs updating. The system compounds over time because each action strengthens the others.

### Capture Knowledge
*"Capture this: here's how we set up our monitoring stack..."*
→ Creates a file in `_inbox/`, offers to file it to the right location. The inbox is ephemeral (7-day TTL) - it's a landing zone, not a filing cabinet. This separation means you never hesitate to capture because you don't have to decide where it goes yet.

### Track Decisions
*"We decided to homeschool instead of private school - let me document why"* / *"We decided to use Terraform over Pulumi - let me document why"*
→ Creates a decision record with context, options considered, and rationale. Crucially, each decision has an `## Outcome` section designed to be filled in later - so the system learns not just what you decided, but how it turned out.

### Query Your Wiki
*"What do we know about our hiring process?"* / *"What did we decide about the database?"*
→ Routes to the right files using summary scanning (not loading everything), synthesizes an answer with source citations. When you're facing a new decision, the AI also checks past decisions and their outcomes - surfacing relevant precedents before you decide.

### Run Health Checks
*"Lint the wiki"* / *"What's stale?"*
→ Surfaces missing metadata, stale files, orphaned docs, and oversized directories. Without maintenance, any knowledge system decays. The lint system is what keeps the wiki trustworthy over months of use.

### Manage Projects
*"Start a new initiative: plan the kitchen renovation"* / *"Start a new initiative: migrate to Kubernetes"*
→ Creates a project workspace with brief, timeline, artifact tracking. Projects live in `1-Projects/` while active and move to `1-Projects/_SHIPPED/` when complete - keeping your active workspace clean.

### Generate Outputs
*"Create a summary of what we've learned about sourdough starters"* / *"Create a slide deck summarizing our Q1 decisions"*
→ Generates a presentation in `_output/`, dated and organized. Most AI-generated content feeds back into the wiki (that's the point - knowledge compounds). `_output/` is only for throwaway deliverables like slide decks or one-time exports that don't belong in your permanent knowledge base.

---

## Examples

The `examples/` directory contains four files showing the metadata standard in action:

- `example-knowledge-article.md` - A personal how-to guide (meal planning)
- `example-decision-record.md` - A technical decision with full context and outcome tracking
- `example-initiative.md` - A multi-artifact project (documentation overhaul)
- `example-inbox-capture.md` - A quick capture from the inbox (cooking notes)

Read these to understand the patterns, then delete them when you're comfortable.

---

## Philosophy

Read [PHILOSOPHY.md](PHILOSOPHY.md) for the deeper thinking behind this system. The short version:

> This is not a documentation system. This is a thinking machine that helps you think more clearly, learn from patterns, and build institutional knowledge - while an AI handles the structure.

**The key principles:**
1. **Structure follows usage** - don't design upfront, let patterns emerge
2. **Nothing is done until it's live** - drafts are not deliverables
3. **Capture first, organize later** - the inbox prevents lost knowledge
4. **The AI is a first-class citizen** - it reads, writes, queries, and maintains the system
5. **If you stop using something, delete it** - don't force structure that doesn't serve you

---

## Design Decisions

A few deliberate choices worth understanding:

### No index files
Many wiki systems use a central index file that grows with every page. This breaks at scale - the index becomes too large for context windows, and maintaining it becomes a chore. Instead, this system uses **query routing**: your AI scans file names and `**Summary:**` lines to find relevant content without loading everything. This scales to hundreds of files without degradation.

### Write-back is the core mechanism
Most knowledge systems focus on ingestion - getting information in. This system focuses on **write-back** - the AI writes observations, conventions, and structural adaptations back into `_config/config.md` during training. Knowledge compounds through use, not just capture. The training period is fundamentally a write-back loop.

### Related links create a knowledge graph
The `**Related:**` field in the metadata standard isn't just decoration. It creates a navigable graph of connections between documents. Your AI follows these links to surface related context when answering queries. In Obsidian, these render as clickable links and appear in the graph view, color-coded by directory.

### Minimal structure by design
The system ships with only 4 content directories. This is intentional. Your AI will suggest new directories during the training period based on what you actually create. This prevents the empty-folder problem where you set up a beautiful taxonomy and never use half of it.

### WIKI-LOG.md and simpler models
The append-only `WIKI-LOG.md` works well with capable models (Claude, GPT-4, Gemini Pro) but may confuse smaller or local models. If you're using a simpler model, you can safely ignore or delete this file - it's useful for tracking evolution but not required for the system to function.

### Decision learning loop
Decision records include an `## Outcome` section designed to be filled in after the decision plays out. When you face a similar decision later, your AI checks past decisions and their outcomes - including failures. This means the system doesn't just remember what you decided, but learns from how those decisions turned out.

### Bold fields instead of YAML frontmatter
Karpathy's pattern recommends YAML frontmatter, which works natively with Obsidian's Dataview plugin. This system uses `**Type:** value` (bold inline fields) instead, because they render correctly in any markdown viewer without a parser, work with any LLM without special handling, and are human-readable in raw form. The trade-off is that Dataview compatibility requires switching to double-colon syntax (`**Type**:: value`) - documented in the Obsidian section above.

### Ephemeral inbox, optional source preservation
The pattern recommends a `raw/` directory for immutable source documents. This system uses an ephemeral `_inbox/` with a 7-day TTL instead - captures are filed into the wiki and the originals are discarded. For users who want to preserve important sources (for re-ingestion when better models arrive, or as permanent reference), set `Preserve Important Sources: yes` in `_config/config.md`. The AI will then selectively keep originals in `_sources/` when it judges them worth preserving.

### AI-native commit conventions
This project uses structured commit prefixes (`meta:` for system/instruction changes vs. plain messages for content changes). This is a small but useful practice for AI-native projects - repos designed to be opened with a code assistant. It lets both humans and agents understand at a glance whether a commit changed the system's behavior or just added content.

### Context optimization is self-maintaining
As your wiki grows, the instruction files your AI loads at startup tend to grow too - new conventions get logged, modules get extended, templates accumulate sections. Left unchecked, this bloats the context window and degrades every session. The system handles this by periodically reviewing its own instruction efficiency. Every 30 days (or when flagged by lint), it measures file sizes, identifies bloat, and proposes splitting or compacting - with your approval. The wiki doesn't just maintain your content. It maintains its own operating efficiency.

---

## FAQ

**On my first Claude Code session I saw something about a missing MEMORY.md - is that an error?**
No. Claude Code has a built-in memory system that stores notes about your project in a file outside the repo (`~/.claude/projects/.../memory/MEMORY.md`). On the very first session it tries to read that file, finds it doesn't exist yet, and creates it. You'll only see this once.

**Does this work with local/smaller models (Ollama, etc.)?**
Yes. All instructions are plain markdown - no special API calls or tool use required. Smaller models may need you to manually update the `Current Phase` field in `_config/config.md` rather than calculating it automatically, and may not follow the training behavior as precisely. The core value (metadata standard, directory structure, templates) works regardless of model capability.

**Why not just use [existing wiki tool]?**
Most LLM wiki implementations focus on ingestion and retrieval. This system adds a training period that adapts the structure to your specific needs, templates battle-tested over months of daily use, an Obsidian-ready vault with graph visualization, and a lint system that keeps things healthy over time. It also works with any LLM - not locked to one provider.

**Should I use one vault for everything or split by domain?**
Start with one. The cross-domain connections are where the most value emerges - a decision about tooling might reference a knowledge article about deployment which links to a project initiative. Splitting loses these connections. If it gets unwieldy, the training period will help you find the right boundaries.

---

## Extending vs. Contributing

This system is designed to be extended in your copy and contributed back to the community - but these are different things. Understanding the boundary helps you know when to customize locally vs. when to open a PR.

**Extend in your copy** (your customizations, your domain):
- New directories for your content types (`5-Recipes/`, `5-Strategy/`, `5-Research/`)
- Domain-specific templates (vendor evaluations, reading notes, patient records)
- Custom tags and naming conventions that reflect your workflow
- Additional instruction modules for behaviors specific to your use case
- Integration with your specific tools (Notion exports, Slack digests, CRM imports)

**Contribute upstream** (structural patterns that help everyone):
- A new template that covers a content type the bootstrap doesn't (retrospectives, book notes, interview records) - genericized so any domain can use it
- An instruction module that teaches the AI a broadly useful behavior (e.g., "summarize this week's changes")
- Training period improvements - better calibration questions, phase transition logic, preference discovery patterns
- Obsidian configurations or plugin recommendations that enhance the wiki pattern
- Bug fixes where instructions don't work well with a particular LLM

**The litmus test:** If your change requires knowing what *your* wiki is about, it's an extension. If it works regardless of domain, it's a contribution.

Your AI will occasionally suggest contributing useful patterns back. When it does, it helps you genericize your specific implementation into something the community can use - your `5-Recipes/` becomes a reusable "content collection" pattern, your refined decision template becomes everyone's starting point.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## Future Directions

This V1 is intentionally minimal - pure markdown, no build step, no automation. But the architecture is designed to support more over time. Areas where contributions would be especially valuable:

- **GitHub Actions** - Nightly wiki health checks, automated inbox triage reminders, stale file notifications
- **Team wikis** - Multi-user conventions, shared vs. private sections, merge conflict strategies for concurrent AI editors
- **MCP server integrations** - Connecting the wiki to external data sources (calendars, project trackers, communication tools) so the AI can pull context automatically
- **Specialized instruction modules** - Domain-specific AI behaviors (engineering runbooks, research methodology, content publishing workflows)
- **Export pipelines** - Automated rendering of wiki content into other formats (Pandoc, Marp slide decks, PDF reports)
- **Smarter training** - Better phase detection, more nuanced calibration, cross-session learning that works with models that don't have persistent memory
- **Agent skills** - As the [SKILL.md](https://github.com/anthropics/agent-skills-spec) standard matures, packaging wiki operations (capture, lint, query) as portable skills that work across tools

The goal is a system that grows from the collective experience of its users - a self-maintaining wiki powering a self-growing open source project.

---

## Credits

- **Pattern foundation:** [Andrej Karpathy's LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **Implementation:** Built from patterns developed by [Ariel Sakin](https://github.com/asakin), a personal operating system for personal knowledge management, refined over several months of daily use
- **Standard:** The metadata standard extends Karpathy's pattern with structured types, tags, and status fields for operational knowledge management

---

## License

Apache 2.0 - use the template, customize it, make it yours. See [LICENSE](LICENSE).
