# How It Works

llm-context-base is a set of instructions that turns any AI agent with file access into the maintainer of a markdown wiki. This page explains what it adds to a folder, how the agent uses it, and why it is built this way.

---

## What gets added to a folder

| File | Owner | Purpose |
|---|---|---|
| `AGENTS.md` (a marked block) | framework | The rules every session follows: capture first, metadata, links, logging, privacy, and which skill or agent handles what |
| `CLAUDE.md` (`@AGENTS.md`) | framework | Makes Claude Code load `AGENTS.md`, which it skips when a `CLAUDE.md` exists |
| `.agents/wiki/config.md` | you | Your folder's house rules and how llm-context-base adapted to them, plus profile, tone, structure, paths, link style, naming, lint adaptations and the conventions the agent has learned. Where it disagrees with `AGENTS.md`, it wins |
| `.agents/wiki/practices.md` | framework | The shared wiki practices and how each is applied or adapted |
| `.agents/wiki/templates/` | framework, plus yours | Note templates: decision, initiative, knowledge article, meeting notes, journal entry, inbox capture |
| `.agents/skills/wiki-*` | framework | The four skills: setup, capture, query, lint |
| `.claude/agents/warren.md`, `marlowe.md` | framework, plus a local section | The two wiki agents |
| `inbox/` | you | Where captures land; setup reuses an intake folder you already have |

Everything else in the folder is yours and stays where it is. Re-running setup updates the framework-owned parts and leaves the rest alone.

## How a session works

The agent reads `AGENTS.md` automatically (Codex, Cursor, Copilot, Devin Desktop, Antigravity, and Claude Code through `CLAUDE.md`). Before its first wiki action it reads `config.md`. It loads a skill only when a task needs it, so the always-loaded part stays under a few hundred lines however large the wiki grows.

There is no greeting ritual or status banner. The agent mentions the inbox only when something has been waiting more than a week.

## Relation to Karpathy's LLM Wiki

Andrej Karpathy's [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) describes three layers: raw sources, an LLM-maintained wiki, and a schema file (`CLAUDE.md` or `AGENTS.md`) that tells the LLM how to maintain it. llm-context-base is a ready-made schema layer for that pattern, with these differences:

| Aspect | Karpathy's gist | llm-context-base |
|---|---|---|
| Raw sources | `raw/`, kept permanently | An inbox that is filed and emptied; originals kept in `sources/` only when `preserve_sources` is on |
| Structure | Designed up front | Adopted from the existing folder, then grown as the agent proposes folders you approve |
| Schema | One file | `AGENTS.md` for the rules, Agent Skills loaded on demand |
| Metadata | Not specified | Five frontmatter fields on every note the agent writes |
| Finding things | Read pages | Scan file names and `summary` fields first, read one to three notes |
| Upkeep | Not specified | Lint skill, plus two agents for maintenance and critique |
| Starting point | Build your own | Installs into an empty folder or an existing vault |

If you want full control from day one and no conventions you didn't write, start from the gist instead.

## Metadata

Every note the agent creates or meaningfully edits gets YAML frontmatter:

```yaml
---
type: decision
summary: Chose PostgreSQL over MongoDB because the data is relational and the team knows SQL.
tags: [engineering, database]
status: active
updated: 2026-04-07
related: ["[[Database migration plan]]"]
---
```

| Field | Values |
|---|---|
| `type` | `knowledge`, `decision`, `initiative`, `meeting`, `journal`, `todo`, `status` |
| `summary` | One sentence a future search can use to decide relevance without opening the note. The most important field. |
| `tags` | A small, consistent vocabulary; no `#` prefix |
| `status` | `draft`, `active`, `complete`, `blocked`, `archived`, `superseded` |
| `updated` | Date of the last meaningful change |

Optional: `confidence` (`high`, `medium`, `low`), `related`, `source`, `owner`. Archived and superseded notes need `failure_reason` explaining why or what replaced them, so retired notes never become dead ends.

YAML frontmatter shows as Properties in Obsidian, a table on GitHub, and plain text everywhere else, and Obsidian Bases and Dataview can query it. If your folder already uses other fields, setup records them and the agent keeps using them. Notes are not backfilled in bulk: frontmatter is added when a note is next touched.

## Design decisions

**The folder stays plain.** llm-context-base has no runtime, no build step and no network activity of its own. It is markdown that any agent reads. Anything that needs code to run (a webhook that drops meeting transcripts into the inbox, a scheduled report, an MCP server over the wiki) belongs in a separate project that writes into the folder.

**One instruction file, read natively.** Earlier versions shipped a shim per tool. Since AGENTS.md became the shared convention, one file covers every major agent, and Agent Skills replace the hand-rolled just-in-time loading of v1.

**Adapt to the host.** Most people already have a folder of notes, and many folders have rules of their own: a sync to Outline or Notion that owns the frontmatter, a publisher that refuses wikilinks, an intake folder, an `AGENTS.md` nobody may edit. Setup reads those house rules first and fits llm-context-base to them: it adopts the folder's convention where it already does the job, brings its own where the folder has none, and proposes a change only where it would improve the user's practice. Even the lint checks are adapted: checks the house makes meaningless are turned off, and house rules worth enforcing become checks. The result lives in `config.md`, which outranks the framework's defaults. Setup never moves notes or edits the folder's own instruction files.

**Learn conventions instead of a training period.** v1 ran a 30-day training period with day counters and footers. v2 writes conventions to `config.md` the moment a conversation settles one, asks at most one organizing question per session, and proposes a new folder only when material keeps not fitting.

**Write back.** Answers that took real synthesis are offered back to the wiki as notes, and preferences go into config as they are stated, so nothing depends on the agent's memory between sessions.

**No index files.** A central index grows with every page and eventually doesn't fit in context. The agent finds notes by scanning names and `summary` fields instead.

**Decisions learn from outcomes.** The decision template has an Outcome section to fill in after the fact. When you face a similar choice, the query skill surfaces past decisions with their outcomes, failures included.

**Two registers.** Chat follows the tone you set. Files are durable content: plain CommonMark, professional, no emoji.

## When the system is working

You find things by asking. You stop explaining the same thing twice. Drafts become active notes instead of piling up. If maintaining the wiki starts to feel like a chore, or the agent is forcing structure that doesn't help, say so: it should adapt, and parts you don't use can be deleted.
