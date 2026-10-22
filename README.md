# Research Agent Template

A GitHub template repository for research projects that use coding agents without giving up human control of the research direction.

The template is designed around one practical rule:

> Let an agent iterate autonomously inside one bounded task, but require a human decision before the research question changes.

It works with plain Markdown and Git. Codex-specific skills are included, but the repository remains usable with other coding agents or without an agent.

## What this template solves

Long research conversations often drift. A task begins with question A, a problem suggests investigation C, and the original route B disappears. At the same time, generated reports may be technically correct but difficult for the researcher to explain or review.

This template addresses those failures with:

- **One active task:** `work/ACTIVE_TASK.md` is the only place where current execution scope is authorized.
- **A return rule for detours:** every side investigation must name its parent question, limit, stop condition, and return point.
- **Two separate loops:** agents may repeat implementation and verification, while changes to the scientific question stop at a human decision gate.
- **Evidence before completion:** planned work, executed checks, observations, interpretations, and decisions remain distinct.
- **Review-first handoff:** each substantial task produces a short review packet before the reader opens long logs or diffs.
- **Understandable writing:** new terms must be explained with existing words before they are used as shorthand.
- **Small durable state:** `memory/CURRENT.md` is a dashboard, not a historical archive.
- **Public/private separation:** the template includes rules and a heuristic release scan to reduce accidental publication of paths, secrets, or private project material.

## Repository contents

```text
.
├── AGENTS.md                         Stable repository instructions and routing
├── PROJECT.md                        Project purpose, boundaries, data policy, and commands
├── PLAN.md                           Approved phase sequence and decision gates
├── memory/
│   ├── CURRENT.md                    Short current-state dashboard
│   └── DECISIONS.md                  Durable decision history
├── work/
│   ├── ACTIVE_TASK.md                The single authorized task
│   └── BACKLOG.md                    Ideas that must not silently enter active scope
├── workflow/
│   ├── OPERATING_MODEL.md            Execution loop, research loop, and detour rules
│   ├── PROCESS_MAP.md                Detailed approval, exception, and information-flow diagrams
│   ├── REVIEW.md                     Code, document, and experiment review requirements
│   └── WRITING.md                    Concrete-language and controlled-term rules
├── templates/
│   ├── experiment/PLAN.md            Experiment contract
│   ├── experiment/RESULTS.md         Evidence and interpretation record
│   ├── REVIEW_PACKET.md              One-page human review handoff
│   └── DECISION.md                   Decision entry template
├── .agents/skills/
│   ├── research-task/                Run one bounded task and stop at its gate
│   └── research-review/              Review evidence and explanations without changing scope
├── scripts/
│   ├── initialize_project.py         Replace starter fields after copying the template
│   ├── validate_workflow.py          Check structure, state, and local links
│   └── check_public_release.py       Heuristic pre-publication scan
├── tests/                             Standard-library tests for the scripts
├── experiments/README.md             Experiment storage convention
└── reviews/README.md                 Review artifact convention
```

## Workflow map

The overview is kept as a separate scalable file so the full lifecycle and every return path remain readable.

**[Open the full-screen workflow map](workflow/WORKFLOW_MAP.svg)**

The map shows the normal route, mechanical repair loop, backlog detour, blocker/scope gate, review decision, and return to the next authorized task. See the [detailed process map](workflow/PROCESS_MAP.md) for the rule behind each branch and information destination; see [the operating model](workflow/OPERATING_MODEL.md) for the corresponding procedures.

## Quick start

### GitHub

1. Mark this repository as a **Template repository** in GitHub settings.
2. Select **Use this template** to create a new repository.
3. Clone the new repository.
4. Initialize its project-specific fields:

```bash
python3 scripts/initialize_project.py \
  --name "My research project" \
  --purpose "Test whether ..." \
  --owner "Research team"
```

5. Complete `PROJECT.md` and `PLAN.md`.
6. Create the first bounded task in `work/ACTIVE_TASK.md`.
7. Validate the repository:

```bash
python3 scripts/validate_workflow.py
python3 -m unittest discover -s tests -v
```

### ZIP

Download a release ZIP, extract it, and run the same initialization command. Git is recommended for auditability but is not required for the Markdown workflow.

### Add it to an existing project

Do not extract the archive directly over an important working repository. First unpack it beside the project, then compare and merge:

1. Preserve the project's existing `AGENTS.md`, `.gitignore`, plan, and research records.
2. Copy the workflow, template, skill, and script directories that the project needs.
3. Merge the root instructions so each fact has one authoritative location.
4. Map existing status, decisions, experiments, and backlog items into the new files without deleting history.
5. Run the validator and review the complete Git diff before accepting the migration.

The template intentionally does not automate this merge because overwriting an established project's instructions or memory is unsafe.

## Daily use

For substantial work:

1. Define one task in `work/ACTIVE_TASK.md`.
2. Approve its scope, expected evidence, stop conditions, and decision gate.
3. Let the agent implement, verify, repair mechanical failures, and re-verify.
4. Put unrelated discoveries in `work/BACKLOG.md`.
5. Store experiment evidence under `experiments/<ID>/` when applicable.
6. Create a review packet under `reviews/`.
7. Make the scientific decision, record it in `memory/DECISIONS.md`, and only then authorize the next task.

Codex users can explicitly invoke `$research-task` for execution and `$research-review` for review. Automatic skill discovery depends on the Codex environment; the root `AGENTS.md` remains the primary entry point.

## What the template does not do

- It does not decide whether a scientific claim is true.
- It does not make an agent or named reviewer technically read-only; permissions must be configured in the execution environment.
- It does not guarantee privacy or detect every secret. The release scanner is only a heuristic check.
- It does not require every project to use machine learning, multiple agents, pull requests, or a particular programming language.
- It does not replace domain methods, ethics review, data governance, or statistical expertise.

## Design choices

The root instructions are intentionally short. Detailed procedures live in workflow documents and narrowly triggered skills so unrelated tasks do not load every rule. The template avoids a database or orchestration service: durable state remains reviewable as Markdown and evidence files.

Independent review is useful when risk justifies it, but multiple agents are not required. Dependent steps and edits to shared state should remain coordinated by one writer.

The structure is informed by the public `AGENTS.md` convention and OpenAI's published Codex planning and long-running workflow examples. The research controls, detour-return rule, writing checks, and templates in this repository are independently written for this project.

## Version

The current template version is recorded in `VERSION`. Releases should use the same semantic version in the Git tag and release ZIP name.

## Preparing a public release

Before publishing a repository created from this template:

```bash
python3 scripts/check_public_release.py --forbid "PRIVATE_PROJECT_NAME"
```

Then manually inspect:

- `git status` and the complete diff;
- tracked files and Git history;
- data, model weights, results, logs, figures, and metadata;
- local paths, credentials, participant information, and proprietary names;
- third-party licenses and attribution requirements.

Passing the script is not proof that a repository is safe to publish.

## License

The template is released under the MIT License. Projects created from it may replace the license before publication.

## Further reading

- [OpenAI: Iterating Development Workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)
- [OpenAI: Run long horizon tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
- [AGENTS.md](https://agents.md/)
