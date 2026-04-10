# The Metadata Standard

Every file gets a metadata block at the top. This is what makes the system queryable. Your AI can scan summaries and tags without reading full documents.

---

## Example: Personal Wiki

```yaml
---
type: knowledge
summary: Weekly meal prep workflow including grocery list generation and batch cooking schedule.
tags: [cooking, how-to, meal-prep]
status: active
owner: Jane
updated: 2026-04-07
related: "[favorite-recipes.md](2-Knowledge/References/favorite-recipes.md)"
---

# How I Organize My Weekly Meal Prep
```

## Example: Developer Wiki

```yaml
---
type: knowledge
summary: Step-by-step deployment process including rollback procedures and monitoring checks.
tags: [engineering, how-to, deployment]
status: active
owner: Jane
updated: 2026-04-07
related: "[ci-pipeline-setup.md](2-Knowledge/HowTo/ci-pipeline-setup.md)"
---

# How We Deploy to Production
```

## What Each Field Does

| Field | Purpose |
|-------|---------|
| **Summary** | Enables query routing. Your AI reads summaries to find relevant files without loading entire documents. |
| **Status** | Prevents draft accumulation. The Definition of Done module uses this to distinguish live knowledge from work-in-progress. |
| **Related** | Creates a navigable knowledge graph. Your AI follows these links to surface connected context. Obsidian renders them in the graph view. |
| **Tags** | Secondary discovery. When summary-based routing doesn't surface what you need, tags provide cross-cutting categories. |
| **Updated** | Powers the lint system. Active files not updated in 90+ days get flagged for review. |

## Why YAML Frontmatter

This system uses standard YAML frontmatter because:

- Renders as Obsidian's **Properties panel** in reading view — clean labeled rows, no dots, collapsible
- Renders as a **bordered table** on GitHub — labeled and scannable
- Human-readable and widely understood in raw form
- Native to the markdown ecosystem — every static site generator, documentation tool, and AI model handles it

Tags use the YAML array format (`[engineering, how-to]`) with no `#` prefix — this is the correct format for frontmatter tags in Obsidian and most other tools.

## Full Specification

See `_config/standard.md` for the complete spec and rationale.

## Examples

The `examples/` directory contains four files showing the standard in action:

- `example-knowledge-article.md` — A personal how-to guide (meal planning)
- `example-decision-record.md` — A technical decision with full context and outcome tracking
- `example-initiative.md` — A multi-artifact project (documentation overhaul)
- `example-inbox-capture.md` — A quick capture from the inbox (cooking notes)

Read these to understand the patterns, then delete them when you're comfortable.
