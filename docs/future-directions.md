# Future Directions

This V1 is intentionally minimal: pure markdown, no build step, no automation. The architecture is designed to support more over time. Areas where contributions would be especially valuable:

- **GitHub Actions** — Nightly wiki health checks, automated inbox triage reminders, stale file notifications
- **Team wikis** — Multi-user conventions, shared vs. private sections, merge conflict strategies for concurrent AI editors
- **MCP server integrations** — Connecting the wiki to external data sources (calendars, project trackers, communication tools) so the AI can pull context automatically
- **Specialized instruction modules** — Domain-specific AI behaviors (engineering runbooks, research methodology, content publishing workflows)
- **Export pipelines** — Automated rendering of wiki content into other formats (Pandoc, Marp slide decks, PDF reports)
- **Smarter training** — Better phase detection, more nuanced calibration, cross-session learning that works with models without persistent memory
- **Agent skills** — As the [SKILL.md](https://github.com/anthropics/agent-skills-spec) standard matures, packaging wiki operations (capture, lint, query) as portable skills that work across tools

The goal is a system that grows from the collective experience of its users.
