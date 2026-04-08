# Contributing to llm-context-base

## The Vision

Every copy of this project is a living experiment. As you walk the pattern and the system adapts to your needs, you'll discover structural patterns that could help others - new templates, instruction modules, directory conventions, or workflow ideas.

This project is designed to grow from the collective experience of its users. Your `5-Recipes/` directory with a custom template might become a generic "content collection" pattern. Your decision learning loop refinement might improve the template for everyone. The wiki maintains itself - and so does this project.

## What Makes a Good Contribution

**Contribute structure, not content.** Your personal knowledge stays in your copy. What's valuable to the community is the *patterns* you discovered.

Great contributions:
- **New templates** - You created a template for something the bootstrap doesn't cover (retrospectives, reading notes, vendor evaluations, etc.)
- **Instruction modules** - You wrote an instruction file that teaches the AI a useful new behavior
- **Directory patterns** - You discovered a directory structure that solves a common problem
- **Training improvements** - You found a better way to calibrate during the training period
- **Obsidian configurations** - You found a plugin or setting that enhances the wiki pattern
- **Bug fixes** - Something in the instructions doesn't work well with a particular LLM

Not contributions:
- Your personal content, knowledge articles, or decisions
- Company-specific conventions or workflows
- Changes that only make sense for your specific use case

## How to Contribute

### The Simple Way (Today)

1. Open an [issue](../../issues) describing the pattern you discovered
2. Include: what problem it solves, how you implemented it, and why it would be useful to others
3. If you can, include a genericized version - strip your specific content and make it domain-agnostic

### With a Pull Request

1. Fork the repo
2. Add your contribution (template, instruction module, etc.)
3. **Genericize it** - replace your specific domain content with placeholders and examples that work across use cases
4. Make sure it follows the metadata standard in `_config/standard.md`
5. Open a PR with a clear description of what pattern this captures

### What "Genericize" Means

Your copy might have:
```markdown
# Recipe: {{title}}
**Cuisine:** [Italian | Japanese | Mexican | ...]
**Prep Time:** ...
**Ingredients:** ...
```

The contribution should be:
```markdown
# [Item Title]
**Category:** [user-defined categories]
**Key Attributes:** ...
**Details:** ...
```

The specific becomes the general. Your experience becomes everyone's starting point.

## The Future

We're working toward a system where your AI can help package useful patterns into contributions automatically - genericizing your specific implementation into something the community can use, and opening a PR on your behalf. The wiki that maintains itself, contributing to the project that powers it.

For now, issues and PRs are the way. But the goal is to make contributing as frictionless as using the system itself.

## Code of Conduct

Be kind. This project exists because people shared their patterns. Keep that spirit going.
