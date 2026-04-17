---
type: knowledge
summary: The canonical metadata standard for all files in this system — makes every document queryable by LLMs and writable by agents.
tags: [meta, standard]
status: active
updated: 2026-04-09
---

# Document Standard

## Standard Tiers

The standard has two tiers. This prevents the standard from becoming a blocker on legitimate use cases while keeping the core queryable.

**Tier 1 — Universal (always enforced)**
Required on every content file. Non-negotiable. Lint will flag missing Tier 1 fields.
- `type` — what kind of document this is
- `summary` — one sentence a future query can use
- `tags` — domain and type vocabulary
- `status` — lifecycle state
- `updated` — date of last meaningful change

**Tier 2 — Advisory (context-dependent)**
Use when relevant. Not required. Lint will not flag missing Tier 2 fields.
- `owner` — relevant for team wikis, shared knowledge
- `confidence` — relevant for research, claims, uncertain knowledge
- `failure_reason` — required when `status: archived` or `superseded`
- `related` — helpful for navigating dense knowledge graphs

---

## Why This Standard Exists

As your knowledge base grows, documents accumulate across directories. Without a common metadata layer, finding information requires manual navigation or loading entire files into context. This standard makes every document in the system:

1. **Queryable** — LLMs can scan summaries and tags without reading full files
2. **Writable** — Agents and automations know exactly how to create compliant files
3. **Cross-cuttable** — "What's happening with #deployment this week?" returns results across all content types
4. **Fresh-trackable** — The `Updated` field makes it easy to flag stale content

Based on [Andrej Karpathy's LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), extended to cover structured knowledge management.

---

## The Metadata Block

Every wiki file gets a YAML frontmatter block at the very top, before the `# Title` line. **Exceptions: `docs/` files, `_meta/` system files, and `README.md` files do not get frontmatter.**

```yaml
---
type: [see types below]
summary: One sentence describing what this file contains or its current state.
tags: [domain, type, topic]
status: [see statuses below]
owner: Person or role responsible
updated: YYYY-MM-DD
related: "[file1](path/file1.md), [file2](path/file2.md)"
---
```

### Required vs Optional by Type

| Type | Required Fields | Optional Fields |
|------|----------------|-----------------|
| `knowledge` | Type, Summary, Tags, Status, Updated | Owner, Related, Confidence |
| `decision` | Type, Summary, Tags, Status, Owner, Updated | Related |
| `initiative` | Type, Summary, Tags, Status, Owner, Updated | Related |
| `meeting` | Type, Summary, Tags, Updated | Status, Owner, Related |
| `journal` | Type, Summary, Updated | Tags, Status, Owner, Related |
| `todo` | Type, Summary, Tags, Status, Updated | Owner, Related |
| `status` | Type, Summary, Updated | Tags, Status, Owner, Related |
| `template` | Type, Summary, Tags | Status, Owner, Updated, Related |

### Field Definitions

**Type** — What kind of document this is (see Types section below).

**Summary** — One sentence, present tense, describing what the file contains OR its current state. This is the most important field — a future query will use it to decide relevance without reading the whole file.

**Tags** — YAML array, no `#` prefix (e.g. `[engineering, how-to]`). Start with tags that make sense for your domain. During the training period, your AI will help you build a consistent tag vocabulary.

**Status** — Lifecycle state:
- `active` — in use, current, being maintained
- `draft` — work in progress, not finalized
- `archived` — no longer active but kept for reference. When setting this, also add `failure_reason:` (see below).
- `superseded` — replaced by a newer file or approach. Requires `failure_reason:` explaining what replaced it.
- `complete` — finished (for todos, initiatives, decisions)
- `blocked` — waiting on something external

**Failure_reason** — Required when `status: archived` or `status: superseded`. One sentence explaining why the file was retired or replaced. Prevents "ghost" archived pages with no explanation.
```yaml
failure_reason: Replaced by 2-Knowledge/new-approach.md after the April 2026 refactor.
```

**Confidence** — Optional. Use on knowledge articles where claims may be uncertain or based on incomplete information.
- `high` — well-sourced, verified, stable
- `medium` — reasonable confidence, may need revisiting
- `low` — speculative, early-stage, needs more sourcing

Omit the field entirely when confidence is not relevant (tasks, journals, templates).

**Owner** — Person or role responsible. Use whatever naming makes sense for you.

**Updated** — ISO date (YYYY-MM-DD) of last meaningful content change. Not just metadata tweaks.

**Related** — Comma-separated relative links to related files. Use relative paths from the file's location.

---

## Document Types

| Type | Use for | Default directory |
|------|---------|-------------------|
| `knowledge` | How-tos, guides, reference material, processes | `2-Knowledge/` |
| `decision` | Recorded decisions with context, options, rationale | `2-Knowledge/Decisions/` |
| `initiative` | Multi-artifact projects in flight | `1-Projects/` |
| `meeting` | Meeting notes and action items | `3-Journal/` or wherever you keep meeting notes |
| `journal` | Reflections, observations, daily notes | `3-Journal/` |
| `todo` | Task lists and action items | Root or wherever you track tasks |
| `status` | Current state snapshots | Root |
| `template` | Templates for generating other files | `_meta/templates/` |

---

## Tags

Tags are free-form but should be consistent. During the training period, your AI will help you develop a vocabulary that fits your domain. Some starter categories:

**Domain tags** — What area does this relate to?
- Examples: `engineering`, `design`, `operations`, `personal`, `finance`, `health`, `cooking`

**Type tags** — What kind of content is this?
- Examples: `how-to`, `reference`, `decision`, `process`, `architecture`

**Status/priority tags** — Optional, for filtering:
- Examples: `urgent`, `someday`, `recurring`

**Rule:** Always use tags from your established vocabulary. If you need a new tag, add it intentionally — don't let tags proliferate randomly. Your AI will help manage this during training.

---

## Query Protocol

When answering a query, the AI should:

1. **Classify the question** — what type and domain is this about?
2. **Route to the right directory** using the query routing in `_meta/instructions/knowledge-query.md`
3. **Scan summaries first** — read file names and `summary:` frontmatter fields before reading full content
4. **Read 1-3 most relevant files** — don't read everything, use tags to filter
5. **Synthesize and cite** — always include source file path and `Updated` date in the response

---

## Write Protocol

When creating or modifying a file, the AI must:

1. **Add YAML frontmatter** at the very top of the file, before the `# Title` line
2. **Use the correct type** from the types table above
3. **Write a useful Summary** — one sentence a future query can use to decide relevance
4. **Pick 2-5 tags** from the established vocabulary
5. **Set Status** appropriately (new files default to `draft`)
6. **Set Updated** to today's date
7. **Add Related links** to 1-3 related files if obvious connections exist

---

## House Style

All files in this system follow plain CommonMark-compatible markdown. The goal is consistent rendering across GitHub, Obsidian, VS Code, raw text, and AI parsing — with no renderer-specific hacks.

**Structural elements to use:**
- Headings (`#`, `##`, `###`)
- Paragraphs (blank line between)
- Bullet lists (`-`) — tight (no blank lines between items) unless items need internal spacing
- Numbered lists for sequences where order matters
- Fenced code blocks (` ``` `)
- Mermaid blocks for diagrams
- `---` horizontal rules to separate major sections
- Markdown links `[text](path)` — never bare HTML

**Avoid:**
- Using HTML as a substitute for real markdown structure — if a heading, list, or code block can do it, use that
- Soft line breaks as a formatting tool (they render as spaces in CommonMark)
- Loose list formatting unless items genuinely need breathing room
- Patterns that only render correctly in one tool

HTML is acceptable when there is no markdown equivalent (e.g., `<sub>`, `<kbd>`, collapsible sections). The test: does this need HTML, or am I using HTML because I didn't think of the markdown alternative?

**Metadata format:** YAML frontmatter. Renders as Obsidian's Properties panel (reading view), a bordered table on GitHub, and clean structured text in raw. No dots, no special syntax in the document body.

---

## Migration

**New files:** Always compliant. Templates generate the metadata block automatically.

**Existing files:** Add the metadata block when you next edit the file. Don't mass-backfill — the maintenance cost outweighs the benefit for rarely-accessed files.
