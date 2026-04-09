# _inbox/

- **Type:** knowledge
- **Summary:** Universal capture zone for anything that needs to be in the system but hasn't been filed yet.
- **Tags:** #meta
- **Status:** active
- **Updated:** 2026-04-09

---

## Purpose

The inbox is the frictionless capture point. Anything that belongs in the system but doesn't have a clear home yet lands here. This prevents two failure modes:
1. **Lost knowledge** - "I should document this" → never happens
2. **Premature structure** - forcing everything into a folder before you know where it belongs

**Use the inbox when:**
- You want to capture something but don't have time to structure it
- You're in a meeting and want to capture something for later
- You want to document something but aren't sure where it goes

---

## How to Capture

Tell your AI: `"capture this: [content]"` or `"add to inbox: [content]"`

It will create a file here with the standard metadata block and offer to file it immediately or defer.

### File naming
```
YYYY-MM-DD-[short-slug].md
```

---

## Filing Rule

The `**Type:**` field determines where items get filed:

| Type | Files to | Template |
|------|----------|----------|
| `knowledge` | `2-Knowledge/HowTo/` or `References/` | `knowledge-article.md` |
| `decision` | `2-Knowledge/Decisions/` | `decision.md` |
| `initiative` | `1-Projects/` | `initiative.md` |
| `meeting` | `3-Journal/` | `meeting-notes.md` |
| `journal` | `3-Journal/` | `journal-entry.md` |
| `todo` | Wherever you track tasks | - |

---

## TTL (Time to Live)

Inbox items are meant to be **temporary**. After 7 days, your AI will surface them for triage at the start of a session - but it will never delete them without asking you. The 7-day mark is a nudge, not a deadline.

If you come back after a longer break, expect a longer triage list. That's fine - the AI will help you batch-process them.
