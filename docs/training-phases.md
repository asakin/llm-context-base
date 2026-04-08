# Training Phases

When you first create your copy, the system doesn't know you. A recipe collector needs different structure than an engineering lead. So rather than asking you to design your wiki upfront, the system walks the pattern with you, an initial period of active collaboration where the AI learns how you think, what you need, and how to organize your knowledge.

By the end, the system is transformed into something uniquely yours.

---

## The Three Phases

| Phase | Duration | Behavior |
|-------|----------|----------|
| **Training** | Days 1–30 (configurable) | Chatty. Asks about your role, suggests directories, learns preferences, logs adaptations. |
| **Cooldown** | Days 31–44 | Quieter. ~70% fewer suggestions. Uses what it learned. |
| **Established** | Day 45+ | Silent efficiency. Just works. Only speaks up when something is broken. |

## What Happens During Training

Your AI will:

- Ask questions about how you work
- Suggest new directories when content doesn't fit
- Propose naming conventions based on your patterns
- Log everything it learns in `_config/config.md`

Chattiness decreases linearly. In the first third, expect 3–5 questions per session. By the final third, the AI asks only when genuinely needed.

## Just-in-Time Context Loading

Your AI doesn't read every instruction file at startup. It loads `_config/config.md` first (always), then pulls in specific instruction modules only when triggered. For example, the lint module loads only when you say "lint the wiki." This keeps context windows efficient as your wiki grows.

## Configuration

In `_config/config.md`:

```markdown
**Training Start Date:** 2026-04-07
**Training Period Days:** 30
```

Set the start date to today when you begin. The period length is up to you.
