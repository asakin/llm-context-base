# Extending vs. Contributing

This system is designed to be extended in your copy and contributed back to the community. These are different things. Understanding the boundary helps you know when to customize locally vs. when to open a PR.

---

## Extend in Your Copy

Your customizations, your domain:

- New directories for your content types (`5-Recipes/`, `5-Strategy/`, `5-Research/`)
- Domain-specific templates (vendor evaluations, reading notes, patient records)
- Custom tags and naming conventions that reflect your workflow
- Additional instruction modules for behaviors specific to your use case
- Integration with your specific tools (Notion exports, Slack digests, CRM imports)

## Contribute Upstream

Structural patterns that help everyone:

- A new template that covers a content type the bootstrap doesn't (retrospectives, book notes, interview records), genericized so any domain can use it
- An instruction module that teaches the AI a broadly useful behavior (e.g., "summarize this week's changes")
- Training period improvements: better calibration questions, phase transition logic, preference discovery patterns
- Obsidian configurations or plugin recommendations that enhance the wiki pattern
- Bug fixes where instructions don't work well with a particular LLM

## The Litmus Test

If your change requires knowing what *your* wiki is about, it's an extension. If it works regardless of domain, it's a contribution.

Your AI will occasionally suggest contributing useful patterns back. When it does, it helps you genericize your specific implementation into something the community can use. Your `5-Recipes/` becomes a reusable "content collection" pattern. Your refined decision template becomes everyone's starting point.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.
