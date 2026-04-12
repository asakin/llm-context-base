# Directory Structure

```
llm-context-base/
  _config/                    # Your configuration (the brain)
    config.md                 # Profile + training controller + LLM instructions
    standard.md               # Document metadata standard

  _meta/                      # System instructions (the engine)
    instructions/             # How the AI operates
    templates/                # Document templates

  _inbox/                     # Frictionless capture zone
  _output/                    # Generated artifacts (presentations, exports, reports)
  _sources/                   # Preserved originals (opt-in, see config.md)
  1-Projects/                 # Active multi-artifact work
  2-Knowledge/                # What you know
    HowTo/                    # Step-by-step guides
    Decisions/                # Decision records
    References/               # Manuals, specs, architecture docs
  3-Journal/                  # What you think (private reflections, gitignored by default - see journal-sync.md)
  4-Private/                  # Sensitive content (gitignored)
  examples/                   # Example files showing the standard in action
```

## Why Only 4 Content Directories?

The system starts minimal on purpose. During training, the AI suggests new directories based on your actual usage. A recipe collector might end up with `5-Recipes/` and `6-MealPlans/`. A CIO might end up with `5-Strategy/` and `6-Operations/`.

This prevents the empty-folder problem where you set up a beautiful taxonomy and never use half of it.
