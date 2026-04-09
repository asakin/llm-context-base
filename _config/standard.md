# Document Standard

- **Type:** knowledge
- **Summary:** The canonical metadata standard for all files in this system — makes every document queryable by LLMs and writable by agents.
- **Tags:** #meta #standard
- **Status:** active
- **Updated:** 2026-04-09

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

Every file gets a metadata block at the top, immediately after the `# Title` line.

```markdown
- **Type:** [see types below]
- **Summary:** [One sentence describing what this file contains or its current state]
- **Tags:** #[domain] #[type] #[topic]
- **Status:** [see statuses below]
- **Owner:** [Person or role responsible]
- **Updated:** YYYY-MM-DD
- **Related:** [file1](path/file1.md), [file2](path/file2.md)
```

### Required vs Optional by Type

| Type | Required Fields | Optional Fields |
|------|----------------|-----------------|
| `knowledge` | Type, Summary, Tags, Status, Updated | Owner, Related |
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

**Tags** — Space-separated, always prefixed with `#`. Start with tags that make sense for your domain. During the training period, your AI will help you build a consistent tag vocabulary.

**Status** — Lifecycle state:
- `active` — in use, current, being maintained
- `draft` — work in progress, not finalized
- `archived` — no longer active but kept for reference
- `complete` — finished (for todos, initiatives, decisions)
- `blocked` — waiting on something external

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
- Examples: `#engineering`, `#design`, `#operations`, `#personal`, `#finance`, `#health`, `#cooking`

**Type tags** — What kind of content is this?
- Examples: `#how-to`, `#reference`, `#decision`, `#process`, `#architecture`

**Status/priority tags** — Optional, for filtering:
- Examples: `#urgent`, `#someday`, `#recurring`

**Rule:** Always use tags from your established vocabulary. If you need a new tag, add it intentionally — don't let tags proliferate randomly. Your AI will help manage this during training.

---

## Query Protocol

When answering a query, the AI should:

1. **Classify the question** — what type and domain is this about?
2. **Route to the right directory** using the query routing in `_meta/instructions/knowledge-query.md`
3. **Scan summaries first** — read file names and `**Summary:**` lines before reading full content
4. **Read 1-3 most relevant files** — don't read everything, use tags to filter
5. **Synthesize and cite** — always include source file path and `Updated` date in the response

---

## Write Protocol

When creating or modifying a file, the AI must:

1. **Add the metadata block** at the top, after the `# Title` line
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

**Metadata format:** Bullet list with bold labels (see below). This renders as a compact list in every CommonMark-compatible renderer, is readable in raw, and is AI-parseable without special handling.

---

## Format: Bullet List Metadata, Not YAML

This system uses `- **Field:** value` bullet list convention (not YAML `---` frontmatter) because:
- Renders as a clean compact list in any CommonMark renderer (GitHub, Obsidian, VS Code)
- Human-readable in raw form with no parser required
- Works with any LLM without special handling
- Simpler migration path for existing files

Note: bare `**Field:** value` lines (without `-`) are NOT used. Without bullet syntax, consecutive bold-field lines render as a single run-on paragraph in CommonMark. The `-` makes each field a distinct list item.

---

## Migration

**New files:** Always compliant. Templates generate the metadata block automatically.

**Existing files:** Add the metadata block when you next edit the file. Don't mass-backfill — the maintenance cost outweighs the benefit for rarely-accessed files.
