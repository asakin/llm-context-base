# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## STEP 0: Framework mode check (run this first)

Check whether `_config/.framework-mode` exists.

If it does, you are in **framework mode** — this repo is being used to develop or maintain the llm-context-base framework itself, not as a personal knowledge base. In that case:

- **Skip the Session Start Protocol entirely.** Do not run init. Do not print a session summary. Do not treat this as a personal knowledge base.
- **Never write personal information into any repo file.** `_config/config.md`, `_config/context.md`, `_inbox/`, the README, commit messages — all of it ships publicly to downstream users. Anything personal the user mentions stays in the conversation only.
- **Behave as a normal engineering assistant for an open-source project.** Read `CONTRIBUTING.md` for conventions. Help with docs, instruction modules, templates, design decisions, releases, and tests.
- Then proceed directly to the user's actual request.

Otherwise → you are in a personal instance. Continue with the protocol below.

---

## MANDATORY FIRST ACTION

**Before responding to anything, you MUST complete the Session Start Protocol.**

**Exception:** If the user's first message is a `/init` command or a meta question about the repo setup, complete that first — then run the Session Start Protocol on the next exchange.

**Your first response MUST begin with exactly:**
```
Allow me to get ready first!
```

**DO NOT engage with any user request until the Session Start Protocol is complete.**

---

Follow the Session Start Protocol defined in `_config/config.md`, then `_meta/instructions/general.md`. All instructions are there.

This file exists only to bootstrap Claude Code into the system. The real instructions are LLM-agnostic and live in the files above.
