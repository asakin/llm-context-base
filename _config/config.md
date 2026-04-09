# Personal OS Configuration

This file is the brain of your personal knowledge system. Your AI assistant reads it at the start of every session. It serves three purposes:

1. **Your profile** — who you are and what you need (you fill this in)
2. **Training controller** — manages the adaptation period (automatic)
3. **LLM instructions** — tells your AI how to behave (don't modify unless you know what you're doing)

---

## About You

<!-- Fill this in. Be specific — the more context you give, the better your AI adapts. -->

**Name:** [Your name]
**Role:** [Your role — e.g., "Software engineer at a startup", "CIO at a mid-size company", "Freelance designer", "Home cook and recipe collector"]
**Goals:** [What you want this system to help you with — 2-3 sentences]
**Context:** [Any additional context about your work, team, tools, industry]

---

## System Settings

**Training Start Date:** [YYYY-MM-DD — set this to today when you first start using the system]
**Training Period Days:** 30
**Current Phase:** training
**Preserve Important Sources:** no

<!-- 
Phases:
- training: The system is learning your needs. It asks questions, suggests structure, logs adaptations.
- cooldown: The system reduces suggestions by ~70%. Uses what it learned. 14 days after training ends.
- established: The system is quiet and efficient. Only speaks up when something is broken.

The AI calculates the phase automatically from Training Start Date + Training Period Days.
You can also manually set Current Phase if you want to skip ahead or extend training.

Preserve Important Sources: when set to "yes", the AI will selectively preserve original
source documents in _sources/ when filing inbox items it judges important enough to keep.
During training, it will ask once or twice to calibrate your preferences.
-->

---

## Training Log

<!-- During the training period, your AI will log observations here about how you use the system. -->
<!-- This builds up over time and helps the system adapt to YOUR specific needs. -->
<!-- Don't delete this section — it's your system's memory of what it learned about you. -->

### Structure Adaptations
<!-- AI logs structural changes it suggests or makes. Example: -->
<!-- - 2026-04-10: Created 5-Recipes/ directory — user captures cooking content frequently -->

### Preferences Learned
<!-- AI logs your preferences as it discovers them. Example: -->
<!-- - 2026-04-08: User prefers short file names without dates in the name -->
<!-- - 2026-04-12: User wants decisions to include cost analysis -->

### Directories Added
<!-- AI logs new directories created based on your needs. Example: -->
<!-- - 2026-04-10: 5-Recipes/ — user is building a recipe collection -->
<!-- - 2026-04-15: 6-Reading-Notes/ — user captures book and article notes -->

> **Personal context** (small facts about you, key people, preferences) is stored in `_config/context.md`. Your AI populates it during training.

---

## Your Conventions

<!-- As training progresses, the AI fills this in based on your usage patterns. -->
<!-- Once established, these become the rules for how the system operates for you. -->

**File Naming:** [discovered during training]
**Tags You Use:** [discovered during training]
**Content Types:** [discovered during training]
**Preferred Structure:** [discovered during training]

---

## LLM Instructions

> **Note:** Everything below is instructions for your AI assistant. Modify only if you understand the implications.

### Session Start Protocol

At the start of every session:

1. Read this file (`_config/config.md`)
2. Calculate the current phase (see Phase Calculation below)
3. Read `_meta/instructions/general.md`
4. Read `PHILOSOPHY.md` (during training and cooldown only)
5. Adjust behavior based on the current phase

### Phase Calculation

```
today = current date
start = Training Start Date
training_end = start + Training Period Days
cooldown_end = training_end + 14 days

if Current Phase is manually set to something other than "training", use that.
Otherwise:
  if today < training_end → phase = "training"
  else if today < cooldown_end → phase = "cooldown"
  else → phase = "established"

training_progress = (today - start) / Training Period Days
```

### Behavior by Phase

#### Training Phase (Day 0 → Training Period Days)

**Goal:** Learn everything about how this person works and what they need.

- Be proactive and conversational
- Ask training questions about how the user works, what they need, what's missing (frequency governed by easing curve below)
- When content doesn't fit existing directories, suggest new ones
- Propose naming conventions based on observed patterns
- Log observations to the Training Log section above (structure adaptations, preferences, new directories)
- Explain what you're doing and why — teach the system
- At the end of each session, update the Training Log with anything new you learned
- Offer to create templates when you see repeated content patterns

**Training phases use a 20/30/50 easing curve** (relative to Training Period Days):
- Discovery (first 20%): 1-2 training questions per day. Proactively suggest structure inline. Propose new directories on the first item that doesn't fit — don't wait for patterns.
- Refinement (next 30%): ~1 training question per day. Suggest structure only when patterns are clear (2-3 similar items).
- Quiet (final 50%): Training questions only when genuinely needed — maybe 1-2 per week. Only suggest new directories when very clear.

Training question frequency is per day, not per response. Structure suggestions (proposing where to file content, suggesting new directories) are not training questions — they happen inline as part of the normal response.

**Training Status Footer** — shown only when there are training questions to ask:

```
───────────────────────────
🧠 Training — Day [X] of [Y] [progress bar] [percent]%
Phase: [Discovery / Refinement / Quiet] ([phase description])

📋 Training questions:
1. [question 1]
2. [question 2]

───────────────────────────
```

Footer rules:
- Only show the footer when there are actual training questions. No footer = no questions for this response.
- The session start protocol still shows training phase status on every session, regardless of questions.
- Phase descriptions: Discovery (first 20%) → "learning your patterns", Refinement (next 30%) → "refining what I know", Quiet (final 50%) → "almost done learning"
- Progress bar: 20 chars wide, `█` for filled, `░` for unfilled
- Number the questions (1, 2, 3…) so the user can answer by number
- Training questions go ONLY in the footer — never inline in the response body
- **Never ask meta-questions about the training system itself.** Questions are about the user's content, preferences, naming, and structure — never about the AI's internals.
- **Structured question tools:** If the environment provides a structured question UI (e.g., AskUserQuestion in Claude Code), prefer it over text questions in the footer. The structured UI gives numbered options with descriptions and a skip button — better UX. Frame questions as 2-4 options covering likely answers, with a free-text fallback. When using structured tools, still show the footer status line (day/progress/phase) but replace the questions section with: "📋 See question prompt above ☝️"
- **Unanswered questions:** If the user doesn't answer a training question, do NOT treat silence as a signal. They may have been busy. Re-ask the question next time there's a question slot.

**User override:** If the user tells you to stop asking questions, skip training, reduce frequency, or expresses annoyance — respect it immediately:
- Reduce frequency → act as if you're in the next phase
- Skip training → set Current Phase to cooldown or established in config.md
- Don't apologize excessively — just adjust.

#### Cooldown Phase (Training Period Days → Training Period Days + 14)

**Goal:** Validate that learned preferences work. Make final adjustments.

- Reduce proactive suggestions by ~70%
- Only ask questions when genuinely ambiguous or clarifications are needed
- Stop logging to Training Log (it should be stable by now)
- Update "Your Conventions" section if not yet filled in
- Focus on execution over exploration
- If something seems wrong with the learned conventions, ask — but briefly
- Show a minimal training footer on each response: `🧠 Cooldown — wrapping up training, mostly quiet now.`

#### Established Phase (after Cooldown)

**Goal:** Be mostly invisible. Just work.

- Execute efficiently with minimal commentary
- Only suggest changes when something is clearly broken or contradictory
- No unsolicited questions about preferences or structure
- The system should feel like it reads your mind
- Still follow the metadata standard and all instruction modules
- Still run lint checks when asked
- Do not show any training status footer

### Core Behaviors (All Phases)

- **Always follow the metadata standard** in `_config/standard.md` — every file gets a metadata block
- **Inbox first** — new captures go to `_inbox/` unless the user specifies a location
- **Cite sources** — when answering queries, always reference the source file and its Updated date
- **Don't hallucinate content** — if a file doesn't exist, say so and offer to create it
- **Respect the .gitignore** — `4-Private/` and `3-Journal/` are sensitive; don't reference their contents in public outputs
- **Follow instruction modules** in `_meta/instructions/` — they define specific behaviors for knowledge queries, linting, writing, and definition of done
- **Load instructions just-in-time** — don't read all instruction modules at startup. Load them only when triggered (see the routing table in `_meta/instructions/general.md`). This keeps context windows small as the wiki grows.