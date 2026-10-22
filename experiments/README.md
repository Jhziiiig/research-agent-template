# Experiments

Use stable identifiers such as `E001`, `E002`, and one directory per experiment. Copy the files under `templates/experiment/` rather than editing the templates.

Suggested structure:

```text
experiments/E001-short-name/
├── PLAN.md
├── RESULTS.md
├── config/          optional, non-secret configuration
├── analysis/        code or notebooks specific to the experiment
└── evidence/        permitted machine-readable checks and summaries
```

Do not place restricted data, credentials, unapproved row-level outputs, or large artifacts in Git. Record approved stable references instead. Preserve failed, invalidated, and superseded experiments.
