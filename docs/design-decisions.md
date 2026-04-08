# Design Decisions

Deliberate choices worth understanding if you want to extend or modify the system.

---

## No Index Files

Many wiki systems use a central index file that grows with every page. This breaks at scale: the index becomes too large for context windows, and maintaining it becomes a chore.

Instead, this system uses **query routing**. Your AI scans file names and `**Summary:**` lines to find relevant content without loading everything. This scales to hundreds of files without degradation.

## Write-Back is the Core Mechanism

Most knowledge systems focus on ingestion, getting information in. This system focuses on **write-back**: the AI writes observations, conventions, and structural adaptations back into `_config/config.md` during training.

Knowledge compounds through use, not just capture. The training period is fundamentally a write-back loop.

## Related Links Create a Knowledge Graph

The `**Related:**` field isn't decoration. It creates a navigable graph of connections between documents. Your AI follows these links to surface related context when answering queries. In Obsidian, these render as clickable links in the graph view, color-coded by directory.

## Minimal Structure by Design

The system ships with only 4 content directories. Your AI suggests new ones during training based on what you actually create. This prevents the empty-folder problem where you set up a beautiful taxonomy and never use half of it.

## Decision Learning Loop

Decision records include an `## Outcome` section designed to be filled in after the decision plays out. When you face a similar decision later, your AI checks past decisions and their outcomes, including failures.

The system doesn't just remember what you decided. It learns from how those decisions turned out.

## Ephemeral Inbox, Optional Source Preservation

Karpathy's pattern recommends a `raw/` directory for immutable source documents. This system uses an ephemeral `_inbox/` with a 7-day TTL instead. Captures are filed into the wiki and the originals are discarded.

For users who want to preserve important sources (for re-ingestion when better models arrive, or as permanent reference), set `Preserve Important Sources: yes` in `_config/config.md`. The AI will selectively keep originals in `_sources/`.

## AI-Native Commit Conventions

This project uses structured commit prefixes (`meta:` for system/instruction changes vs. plain messages for content changes). This lets both humans and agents understand at a glance whether a commit changed the system's behavior or just added content.

## Context Optimization is Self-Maintaining

As your wiki grows, the instruction files your AI loads at startup tend to grow too. New conventions get logged, modules get extended, templates accumulate sections. Left unchecked, this bloats the context window and degrades every session.

The system handles this by periodically reviewing its own instruction efficiency. Every 30 days (or when flagged by lint), it measures file sizes, identifies bloat, and proposes splitting or compacting, with your approval.

## WIKI-LOG.md and Simpler Models

The append-only `WIKI-LOG.md` works well with capable models (Claude, GPT-4, Gemini Pro) but may confuse smaller or local models. If you're using a simpler model, you can safely ignore or delete this file. It's useful for tracking evolution but not required.

## Bold Fields Instead of YAML Frontmatter

See [Metadata Standard](metadata-standard.md) for the full rationale.

## The Repo Stays Dumb

llm-context-base is a substrate. It's a pile of markdown files that AI tools read, write, and act on. It has no runtime. It runs no code. It requires no build step.

This is a deliberate architectural choice, not a limitation. It means:

**Any tool can use it.** Claude Code, Cursor, Copilot, Cowork, a future tool that doesn't exist yet — they all work because they all read files. The substrate doesn't care what reads it.

**Sophisticated behaviors belong in the intelligence layer above.** A Cloudflare Worker that routes meeting transcripts into the inbox, a Cowork scheduled task that monitors social media and writes reports, an MCP server that exposes the wiki as a queryable API — these are all valid and useful. They just don't live in the repo. They live above it, acting on the substrate.

**Extensions follow the same split.** A markdown extension spec (instructions, templates, routing entries) is substrate — it lives in the repo. A Cloudflare Worker that runs as part of an integration is intelligence layer — it lives on Tessl or deployed infrastructure. The spec tells your AI how to wire things in. The Worker does the actual work outside.

**Scaffolding is the one acceptable use of npm as delivery.** `npx create-llm-wiki` (or `npx create-adhd-focus` for a distro) clones the template and disappears. After that command, npm is out of the picture.

**Local tool installs don't violate the principle.** The substrate principle governs what goes in the repo, not what the AI does on your machine. The AI can install CLI tools (Marp, Pandoc, etc.) locally on demand. What's in the repo is `_config/tools.md` — a markdown manifest declaring what tools are needed and how to install them. Binaries go in `_tools/` (gitignored) or as global installs. The repo stays clean.

When evaluating whether something belongs in the repo: if it's a binary or runtime dependency, it doesn't. If it's a markdown description of what to install, it does.
