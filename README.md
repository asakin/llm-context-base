# llm-context-base

**Turn the markdown folder you already have into a wiki your AI agent maintains.**

Point any coding agent at your notes (an Obsidian vault, a docs folder, an empty directory) and it captures, files, links and answers from them, following one set of rules in `AGENTS.md`. It learns how your folder is already organized instead of making you adopt a new structure, and it works the same in Claude Code, Codex, Cursor, Copilot, pi and the other agents that read `AGENTS.md`.

You supply the sources and the conversation; the agent maintains the wiki.

---

## Quick start

There are two ways in. Both use the same setup skill, which you hand to your agent as a link; nothing to clone or install first.

### Start a fresh wiki

Open your agent anywhere and say:

```text
Start a new llm-context-base wiki in ~/wiki by following
https://raw.githubusercontent.com/asakin/llm-context-base/main/.agents/skills/wiki-setup/SKILL.md
```

The agent creates the folder, offers `git init` so every change can be undone, adds the framework files, and creates an inbox. It asks what the wiki is for and offers a starter layout (Projects, Knowledge, Journal, Private), which you can decline and let the structure grow from what you capture. Open the folder as an Obsidian vault if you like to watch it fill in.

### Add it to notes you already have

Commit or back up your folder, open your agent in it (an Obsidian vault, a docs folder, any folder of markdown), and say:

```text
Set up llm-context-base in this folder by following
https://raw.githubusercontent.com/asakin/llm-context-base/main/.agents/skills/wiki-setup/SKILL.md
```

The agent first reads your folder's house rules: instruction files, sync or publishing tooling, linters, and how your notes are written (links, naming, frontmatter, intake folder). It then shows you how llm-context-base will fit in: it adopts your conventions where they already do the job, brings its own where you have none, and proposes a change only where it would improve your practice. Nothing is installed until you agree, and the result is recorded in `.agents/wiki/config.md`. Your notes are not moved, renamed or rewritten, and frontmatter is added to a note only when the agent next works on it. If you already have an `AGENTS.md` or `CLAUDE.md`, your text in them is kept.

A v1 wiki goes this way too; see [Coming from v1](#coming-from-v1).

### Either way

To update later, say "update llm-context-base". If you use Obsidian, see [Using with Obsidian](docs/obsidian.md).

Cloning this repository gets you the framework's source, set up for contributors, not a wiki; see [CONTRIBUTING.md](CONTRIBUTING.md).

## What it brings to your wiki

Every wiki is ahead on some things and behind on others. llm-context-base brings a common set of practices and fits them to what you already have, without breaking it:

- **Capture first, file later**, and fold new material into existing pages before creating new ones
- **Answers become pages**, cited and dated, with gaps admitted instead of filled
- **Decisions carry their outcomes**, so past choices come up when a similar one does
- **Nothing retires without a trail**, drafts get finished, every page can be found
- **Conventions are written down** the moment they're decided
- **Health checks end in fixes**, and a second agent audits what the first one wrote
- **Instructions stay small**, and every agent follows the same procedures

Setup checks each practice against your folder and tells you which you already have, which it adds, and which it adapts to your own rules. The full list is in [`practices.md`](.agents/skills/wiki-setup/references/practices.md).

## What you can say

| Say | What happens |
|---|---|
| "Capture this: here's how we set up monitoring…" | A dated note in the inbox, with an offer to file it now |
| "We chose Terraform over Pulumi; write down why" | A decision note with context, options, rationale, and an Outcome section for later |
| "What do we know about our hiring process?" | An answer synthesized from the relevant notes, citing each one and flagging stale ones |
| "File my inbox" | Items become new notes or updates to existing ones, linked to related notes |
| "Should we move to Kubernetes?" | Past decisions in the same area surface first, especially the ones that went badly |
| "Lint the wiki" | Stale inbox items, notes missing metadata, stale and stuck drafts, orphans, broken links |
| "From now on, name meeting notes by date" | The convention is written to config immediately and followed from then on |

## Meet Warren and Marlowe

Two agents ship with the wiki, as Claude Code subagents (and in pi through the pi agents extension, which setup offers if you use pi).

- **Warren** keeps the wiki: files the inbox, writes and updates notes, maintains links and metadata, merges and splits notes, tidies prose without changing what notes claim.
- **Marlowe** investigates: answers questions with citations, researches new sources and maps them onto what the wiki already says, and critiques the wiki for contradictions, stale claims, weak evidence and gaps. Marlowe proposes changes rather than rewriting notes.

During setup you tell them what the wiki is for, what Warren may do without asking, and which sources Marlowe should trust. Those answers live in a local section of each agent that updates never overwrite.

## What it adds to your folder

```text
AGENTS.md                  the rules, in a marked block; anything else in the file stays yours
CLAUDE.md                  @AGENTS.md, so Claude Code loads the same rules
.agents/wiki/config.md     your settings, house rules and the conventions learned so far
.agents/skills/            Agent Skills, adapted to your folder on install:
                             wiki-setup (with the practices list), wiki-capture (with the note templates),
                             wiki-query, wiki-lint, wiki-keep, wiki-investigate
.claude/agents/            warren.md, marlowe.md
inbox/                     a path you can change in config
```

The rest of the folder is yours. [How It Works](docs/how-it-works.md) explains each part and the design behind it.

## Works with

Any agent that reads `AGENTS.md` and can edit files: Claude Code, Codex, Cursor, GitHub Copilot, Antigravity CLI, pi, Devin Desktop and others. The skills use the [Agent Skills](https://agentskills.io) format in `.agents/skills/`. See [Supported Tools](docs/supported-tools.md) for what each one reads.

## Coming from v1

v2 replaces the per-tool shims with `AGENTS.md`, the `_config/` and `_meta/` folders with `.agents/`, and the 30-day training period with conventions learned as you go. Run setup in your v1 folder: it migrates your profile and conventions, keeps your content folders where they are, and offers to convert old-style metadata. See the [FAQ](docs/faq.md#im-on-v1-how-do-i-move-to-v2).

## Documentation

| Page | What's there |
|---|---|
| [How It Works](docs/how-it-works.md) | The files, a session, the metadata, design decisions |
| [Supported Tools](docs/supported-tools.md) | What each agent reads, chat apps, local models, privacy |
| [Using with Obsidian](docs/obsidian.md) | Setup next to a vault, Web Clipper template, Bases, plugins |
| [Journal Sync and Privacy](docs/journal-sync.md) | Three ways to sync a private folder across devices |
| [Linked Code Repos](docs/linked-code-repos.md) | Connecting project notes to the code repositories they describe |
| [FAQ](docs/faq.md) | Installing, updating, existing files, v1 |
| [Contributing](CONTRIBUTING.md) | Working on the framework, what makes a good contribution, releases |

The [`examples/`](examples/) folder has four sample notes showing the metadata in use.

## Author

[Ariel Sakin](https://github.com/asakin).

## License

Apache 2.0. See [LICENSE](LICENSE).
