# Security Policy

`llm-context-base` is a **template for building a personal LLM wiki**, not runnable software
with an attack surface. There is no server, no dependency tree executing third-party code,
and no network listener. The security considerations here are about **content and use**.

## What "security" means for this repo

- **No secrets in the template.** The framework files (`_config/`, `_meta/`, templates,
  README) ship to downstream users. Never commit credentials, tokens, personal data, or
  private infrastructure details into a framework file. Personal content belongs in a
  *personal instance* of the template, not in this repo.
- **Lint hooks and scripts.** The template ships optional git hooks / lint scripts. Review
  any hook before enabling it (`git config core.hooksPath`); hooks run local commands on
  your machine.
- **Downstream use.** If you build your own wiki from this template and add integrations
  (sync scripts, API keys, automation), those are your responsibility and live outside this
  repo.

## Reporting a vulnerability

If you believe a framework file leaks information by default, or a shipped script does
something unsafe:

- Open a **private** report via GitHub ("Report a vulnerability" / Security Advisories)
  rather than a public issue, so it can be assessed before disclosure.
- For everything else (typos, docs, features), use normal issues / PRs — see
  `CONTRIBUTING.md`.

## Supported versions

This is a living template; only the latest `main` is considered. Pin a release tag if you
need a stable base.

By using this template you agree to use it lawfully and to keep your own secrets out of
files that ship publicly.
