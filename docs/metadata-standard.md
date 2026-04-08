# The Metadata Standard

Every file gets a metadata block at the top. This is what makes the system queryable. Your AI can scan summaries and tags without reading full documents.

---

## Example: Personal Wiki

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

## Example: Developer Wiki

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

## What Each Field Does

| Field | Purpose |
|-------|---------|
| **Summary** | Enables query routing. Your AI reads summaries to find relevant files without loading entire documents. |
| **Status** | Prevents draft accumulation. The Definition of Done module uses this to distinguish live knowledge from work-in-progress. |
| **Related** | Creates a navigable knowledge graph. Your AI follows these links to surface connected context. Obsidian renders them in the graph view. |
| **Tags** | Secondary discovery. When summary-based routing doesn't surface what you need, tags provide cross-cutting categories. |
| **Updated** | Powers the lint system. Active files not updated in 90+ days get flagged for review. |

## Why Bold Fields Instead of YAML Frontmatter

Karpathy's pattern recommends YAML frontmatter, which works natively with Obsidian's Dataview plugin. This system uses `**Type:** value` (bold inline fields) instead because:

- They render correctly in any markdown viewer without a parser
- They work with any LLM without special handling
- They're human-readable in raw form

The trade-off: Dataview compatibility requires switching to double-colon syntax (`**Type**:: value`). See the [Obsidian setup](obsidian-setup.md) for details.

## Full Specification

See `_config/standard.md` for the complete spec and rationale.

## Examples

The `examples/` directory contains four files showing the standard in action:

- `example-knowledge-article.md` — A personal how-to guide (meal planning)
- `example-decision-record.md` — A technical decision with full context and outcome tracking
- `example-initiative.md` — A multi-artifact project (documentation overhaul)
- `example-inbox-capture.md` — A quick capture from the inbox (cooking notes)

Read these to understand the patterns, then delete them when you're comfortable.
