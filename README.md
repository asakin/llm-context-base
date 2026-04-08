# [Project Name]

> This README will be personalized during your first session.

---

<!-- llm-context-base:framework-readme -->

# llm-context-base

**A bootstrap repo for building your own LLM-powered knowledge base.**

Use the template, point your AI assistant at it, and start talking. Over time, it learns how you work and adapts its structure to your needs without you having to design anything upfront.

This is an implementation of [Andrej Karpathy's LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), extended with a metadata standard, an adaptive training period, inbox-first capture, health checks, and multi-LLM support.

---

## Quick Start

**1. Create your copy.** Click **"Use this template"** on GitHub. Make it private. Clone it.

```bash
git clone https://github.com/YOUR-USERNAME/my-wiki.git
cd my-wiki
```

**2. Fill in your profile.** Open `_config/config.md`, fill in the **About You** section, and set `Training Start Date` to today.

**3. Start talking.** Open in your AI tool of choice and go:

- *"Capture this: here's how our onboarding process works..."*
- *"We decided to use PostgreSQL over MongoDB, let me document why"*
- *"What do we know about our deployment process?"*
- *"Lint the wiki, what needs attention?"*

That's it. The system adapts to what you actually need.

---

## What Makes This Different

**It learns how you work.** The first 30 days are a training period. Your AI asks questions, suggests directories, and logs what it learns. By day 45, it's quiet and efficient. You never design a taxonomy upfront. [Full details &rarr;](docs/training-phases.md)

**Capture first, organize later.** Everything lands in `_inbox/` with a 7-day TTL. You never hesitate to capture because you don't have to decide where it goes yet. Your AI files it later.

**Your README stays yours.** This file has two sections split by a marker. Above it: your personal project README, maintained by your AI as the wiki evolves. Below it: the framework docs, which track upstream cleanly. You get living documentation without merge conflicts.

**Patterns are captured as they emerge.** When your AI learns a new convention or preference during a conversation, it writes it down immediately, not at commit time. Nothing is lost if you commit from the command line without AI involvement.

**Every file is queryable.** A [metadata standard](docs/metadata-standard.md) on every document means your AI can scan summaries and tags without loading full files. This scales to hundreds of documents.

**It maintains itself.** Lint checks surface stale files, missing metadata, and orphaned docs. The system even reviews its own instruction efficiency to prevent context window bloat as your wiki grows.

---

## What You Can Do

| Say this | What happens |
|----------|-------------|
| *"Capture this: here's how we set up monitoring..."* | Creates a file in `_inbox/`, offers to file it |
| *"We decided to use Terraform over Pulumi, document why"* | Decision record with context, options, rationale, and an outcome section to fill in later |
| *"What do we know about our hiring process?"* | Scans summaries, synthesizes an answer with source citations |
| *"Lint the wiki"* | Surfaces stale files, missing metadata, orphaned docs |
| *"Start a new initiative: migrate to Kubernetes"* | Project workspace with brief, timeline, artifact tracking |
| *"Create a slide deck summarizing Q1 decisions"* | Generates output in `_output/`, dated and organized |

These form a cycle. Capture feeds queries, queries inform decisions, decisions get tracked, lint keeps it all healthy. The system compounds over time.

---

## Go Deeper

| Topic | What's there |
|-------|-------------|
| [Training Phases](docs/training-phases.md) | How the system adapts to you over 30 days |
| [Directory Structure](docs/directory-structure.md) | What each folder is for, why there are only 4 |
| [Metadata Standard](docs/metadata-standard.md) | The format that makes everything queryable |
| [Supported Tools](docs/supported-tools.md) | Claude Code, Cursor, Copilot, Windsurf, ChatGPT, and others |
| [Obsidian Setup](docs/obsidian-setup.md) | Pre-configured vault, plugins, web clipper |
| [Design Decisions](docs/design-decisions.md) | Why the system works the way it does |
| [FAQ](docs/faq.md) | Common questions |
| [Extending & Contributing](docs/extending-and-contributing.md) | Customize locally vs. contribute upstream |
| [Future Directions](docs/future-directions.md) | Where this is headed |
| [Philosophy](PHILOSOPHY.md) | The deeper thinking behind the system |

The `examples/` directory has four sample files showing the metadata standard in action. Read them, then delete them when you're comfortable.

---

## Credits

Built on [Andrej Karpathy's LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Implementation by [Ariel Sakin](https://github.com/asakin), refined over several months of daily use managing business operations.

## License

Apache 2.0. See [LICENSE](LICENSE).
