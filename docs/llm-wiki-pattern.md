# The LLM Wiki Pattern — and How llm-context-base Implements It

Andrej Karpathy published a [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) describing a pattern for using an LLM to maintain a personal wiki. This page explains the pattern, how llm-context-base implements it, and where it intentionally differs.

---

## The Pattern (Karpathy's Version)

Three layers:

```
raw/          ← immutable source documents (articles, PDFs, notes)
wiki/         ← LLM-maintained structured knowledge pages
CLAUDE.md     ← schema config: tells the LLM how to write wiki pages
```

The LLM reads raw sources, writes and maintains wiki pages according to the schema, and answers queries by reading wiki pages rather than raw documents. The key insight: the LLM maintains a structured intermediate layer, so every query doesn't start from scratch.

---

## How llm-context-base Implements Each Layer

### Raw sources → `_inbox/` + `_sources/`

The `_inbox/` directory is the capture zone — anything that needs to be in the system but hasn't been processed yet lands here. It has a 7-day TTL: the LLM surfaces inbox items at session start and offers to file or discard them.

`_sources/` is optional — for users who want to preserve original documents (set `Preserve Important Sources: yes` in config). Most users don't need it: once a document is processed into a wiki entry, the original is no longer load-bearing.

**Where it differs from the base pattern:** The base pattern treats `raw/` as a permanent archive. llm-context-base treats the inbox as ephemeral — capture first, file or discard later. This reduces friction and prevents accumulation of documents that are never queried.

### Wiki pages → `2-Knowledge/` + other content directories

Structured knowledge lives in `2-Knowledge/` (HowTo, Decisions, References), `1-Projects/` (active work), `3-Journal/` (private reflections), and `4-Private/` (sensitive content).

Every file gets a metadata block:

```markdown
**Type:** knowledge
**Summary:** One sentence the LLM uses to decide relevance without reading the full file.
**Tags:** #domain #type
**Status:** active
**Updated:** 2026-04-08
```

The Summary field is the critical addition. Instead of loading full documents to answer queries, the LLM scans summaries — which is fast and scales to hundreds of files without degrading session quality.

**Where it differs:** The base pattern doesn't specify a metadata standard. llm-context-base enforces one on every file, which enables query routing (find relevant files by scanning summaries) and the lint system (flag stale or incomplete files).

### Schema config → `_config/config.md` + `_meta/instructions/`

The base pattern uses a single `CLAUDE.md` or `AGENTS.md` file as the schema config. llm-context-base splits this into:

- `_config/config.md` — user profile, training settings, conventions discovered during training
- `_meta/instructions/general.md` — session protocol, core behaviors, module routing
- `_meta/instructions/*.md` — specific modules loaded just-in-time (lint, query, write, etc.)

**Where it differs:** The base pattern loads everything at startup. llm-context-base uses just-in-time loading — only the core files load at session start, and specific modules load when triggered. This keeps context windows efficient as the wiki grows.

---

## The Training Period — Not in the Base Pattern

The biggest addition llm-context-base makes to the base pattern is the training period.

The base pattern assumes you design your schema upfront. llm-context-base inverts this: the system starts chatty, asks questions, suggests directories, and logs what it learns about you. By day 30 it transitions to cooldown (quieter). By day 44 it's established — mostly silent, just works.

The structure adapts to what you actually use, not what you planned to use.

---

## Comparison Table

| Aspect | Karpathy's Pattern | llm-context-base |
|--------|-------------------|-----------------|
| Source documents | `raw/` — permanent archive | `_inbox/` — ephemeral, 7-day TTL |
| Wiki structure | User-designed upfront | Adapts during 30-day training period |
| Schema config | Single file (`CLAUDE.md`) | Split: profile + core + JIT modules |
| Metadata | Not specified | Enforced standard on every file |
| Query routing | Full file reads | Summary scanning first |
| Health maintenance | Not specified | Lint system, optimization review |
| LLM support | Single tool | Multi-tool bootstrap shims |
| Starting point | Build from scratch | Ready-to-use template |

---

## When to Use the Base Pattern Instead

llm-context-base is opinionated. If you want:
- Full control over every convention from day one
- A minimal setup without the training period machinery
- Something to build your own system on top of

...the base pattern is the right starting point. Karpathy's gist is intentionally minimal so you can take it in any direction.

llm-context-base is for people who want the system to work out of the box and adapt to them, rather than designing it themselves.
