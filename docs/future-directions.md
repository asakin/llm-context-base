# Future Directions

This V1 is intentionally minimal. The architecture is designed to support more over time. The core principle: the repo is a substrate — a pile of markdown — and tools that act on it live outside. This keeps the system portable and lock-in free. See [Design Decisions](design-decisions.md) for the substrate principle.

Areas where contributions would be especially valuable:

- **GitHub Actions** — Nightly wiki health checks, automated inbox triage reminders, stale file notifications. For multi-agent setups: a **heartbeat system** where each agent declares `heartbeat: true` in their own `config.md` and a daily GHA wakes them for reflection and minimum living tasks. Agents self-manage their schedule — opt in, unregister when done, subscribe to framework events defined in `_meta/events.md`.
- **Team wikis** — Multi-user conventions, shared vs. private sections, merge conflict strategies for concurrent AI editors
- **MCP server integrations** — Connecting the wiki to external data sources (calendars, project trackers, communication tools) so the AI can pull context automatically
- **Specialized instruction modules** — Domain-specific AI behaviors (engineering runbooks, research methodology, content publishing workflows)
- **Export pipelines** — Additional rendering tools beyond Marp (Pandoc for academic docs, LaTeX for papers). Add entries to `_config/tools.md` following the existing pattern.
- **Event-driven agent orchestration** — Agents subscribe to framework events (`commit.post`, `session.start`, `agent.hatched`, etc.) rather than polling or spawning bespoke jobs. The framework dispatches; agents respond. Custom behaviors are agents' own GH Actions, not framework concerns.
- **Smarter training** — Better phase detection, more nuanced calibration, cross-session learning that works with models without persistent memory
- **Agent skills** — As the [SKILL.md](https://github.com/anthropics/agent-skills-spec) standard matures, packaging wiki operations (capture, lint, query) as portable skills that work across tools

The goal is a system that grows from the collective experience of its users.
