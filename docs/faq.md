# FAQ

## How do I install it?

Open your agent in the folder you want to use (an existing notes folder or vault, or an empty one) and say:

```text
Set up llm-context-base in this folder by following
https://raw.githubusercontent.com/asakin/llm-context-base/main/.agents/skills/wiki-setup/SKILL.md
```

The agent fetches the latest release, shows you what it will add, and asks a few questions. See the [README](../README.md#quick-start).

## How do I get updates?

Say "update llm-context-base". The installed `wiki-setup` skill fetches the latest release and replaces only the framework's parts: the block in `AGENTS.md`, the `wiki-*` skills, the shipped templates, and Warren and Marlowe outside their local sections. Your notes, `config.md`, your own templates, and anything you wrote outside the marked block are left alone.

## I'm on v1. How do I move to v2?

Run setup in your v1 folder, the same way as a fresh install. It recognizes the v1 layout, moves your profile, tone, training log and conventions into `.agents/wiki/config.md`, keeps `1-Projects/` to `4-Private/` where they are, removes the old shims and `_config/`/`_meta/` after showing you the list, and offers to convert any old `**Type:**`-style metadata to YAML with a dry run first. Commit before you start so you can review the change on its own.

## Does it change my existing notes?

No. Setup adds files; it doesn't move, rename or rewrite notes. Afterwards, the agent adds frontmatter to a note only when it works on that note, and every move, merge or rename on more than a handful of notes is proposed before it happens.

## What if my folder already has an AGENTS.md or CLAUDE.md?

Setup adds a marked block to `AGENTS.md` and an `@AGENTS.md` line to `CLAUDE.md`, and keeps everything else in both files. Updates replace only the marked block.

## Why are the files hidden?

So the framework doesn't clutter your notes. Obsidian and most file browsers hide dot-folders. `AGENTS.md` and `CLAUDE.md` stay at the root because that is where agents look for them.

## Do I need Claude Code?

No. Any agent that reads `AGENTS.md` gets the rules and the skills; see [Supported Tools](supported-tools.md). Warren and Marlowe are Claude Code subagents, and are also available in pi through the pi agents extension.

## Does it work with local models?

Yes. Everything is plain markdown. Smaller models handle capture, metadata and queries; setup and lint are multi-step and go better with a stronger model.

## Can I use it at work, behind a proxy?

llm-context-base has no runtime and makes no network calls: no telemetry, no CDN, no background process. The only question is whether your company allows the agent you use to read and write files, the same question you'd have without it. Setup itself fetches the release from GitHub once; you can also clone the repository yourself and point the agent at the local copy.

## Where did the 30-day training period go?

It was replaced in v2. The agent now writes a convention into `config.md` the moment you settle one, asks at most one organizing question per session, and proposes folders only when material keeps not fitting. No day counter, no footer, no greeting ritual.

## How do I sync a private journal across devices?

See [Journal Sync and Privacy](journal-sync.md): plaintext in a private repo, git-crypt, or a folder synced outside git.

## One wiki for everything, or one per domain?

Start with one. The links between domains are where much of the value is: a decision references a how-to, which links to a project. Split later if it gets unwieldy.

## Why not just use another LLM-wiki template?

Most assume a fresh folder, one agent, and a structure you adopt up front. llm-context-base installs into the folder you already have, adopts its conventions, works across agents through `AGENTS.md` and Agent Skills, and ships two agents for upkeep and critique. If you want to design everything yourself, start from [Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
