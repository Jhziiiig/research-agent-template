# Repository instructions

## Purpose and authority

This repository uses a human-gated research workflow. The researcher controls scientific questions, claim strength, scope changes, and publication. Agents may work autonomously only inside an approved task.

Explicit user instructions take priority over these repository conventions. Plans and templates describe intended work; executed checks and saved evidence establish what actually happened.

## Read only what the task needs

For substantive work, read:

1. `PROJECT.md` for project boundaries and commands.
2. `memory/CURRENT.md` for current state.
3. `work/ACTIVE_TASK.md` for the only active scope.
4. The relevant section of `PLAN.md` and linked evidence.

Read historical decisions, experiments, and workflow references only when they are relevant. Do not load the entire history by default.

## One active task

Only `work/ACTIVE_TASK.md` authorizes current execution. Do not start a backlog item, a later plan phase, or a new scientific comparison unless the user activates it.

Within an approved task, repeat implementation, verification, repair, and re-verification as needed. Stop at the task's scientific decision gate.

Classify discoveries as:

- **Blocking:** the active result cannot be trusted until it is resolved. Pause affected work and report it.
- **Bounded diagnostic:** a limited check can explain a surprising result without changing the research question. Record its parent, limit, stop condition, and return point before running it.
- **Backlog:** useful but not required for the active task. Record it in `work/BACKLOG.md`; do not execute it now.

Read `workflow/OPERATING_MODEL.md` when planning or executing a substantive task. Use `$research-task` when available.

## Evidence and claims

Distinguish observations, interpretations, hypotheses, decisions, and unresolved questions. Never represent planned, inferred, skipped, or failed work as completed evidence.

Do not silently change data versions, sample definitions, splits, labels, metrics, baselines, exclusions, model inputs, public interfaces, or claim meanings. Record material changes and their reasons.

Preserve failed, negative, invalidated, and superseded results. Do not overwrite immutable source data or prior evidence.

## Review and understandable writing

Before calling substantial work complete, create a concise review packet using `templates/REVIEW_PACKET.md`. It must let a reader identify the input, target, changed element, unchanged elements, comparison, evidence, limitations, and decision required.

Use existing project terms when possible. When a new term is necessary, first explain the concrete operation or observation with existing words, then introduce the term as shorthand. Record stable project terms in `glossary/TERMS.md`.

Read `workflow/REVIEW.md` for reviews and `workflow/WRITING.md` for substantive explanations. Use `$research-review` when available.

## Durable state

Keep `memory/CURRENT.md` short: current question, active task, strongest current evidence, blockers, and next decision only. Put chronology in experiment records and durable choices in `memory/DECISIONS.md`.

After substantive work, update the relevant evidence, review packet, decision record, and current state. One writer updates shared state at a time.

## Privacy, publication, and external actions

Follow the classifications and allowed locations in `PROJECT.md`. Do not expose private data, identifiable records, credentials, sensitive paths, unpublished results, or proprietary materials in chat, commits, screenshots, external tools, or public repositories.

Do not upload, publish, push, deploy, send messages, or modify external systems unless the user explicitly authorizes that action and destination. Before public release, run the available checks and perform a manual review; automated scans are not privacy guarantees.

## Verification

Run checks proportional to the change. Report what actually ran, what failed or was skipped, and remaining uncertainty. Do not treat a passing format check as scientific validation.
