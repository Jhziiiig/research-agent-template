---
name: research-review
description: Review research code, experiment evidence, or explanatory Markdown against an approved task and report concrete findings without changing scientific scope. Use for requested review, verification, or pre-decision audit; do not use as authorization to implement fixes.
---

# Review Research Work

Read the active task, relevant plan section, actual diff, executed commands, saved outputs, and only the linked history needed to assess the work. Follow `workflow/REVIEW.md` and `workflow/WRITING.md`.

Review in this order:

1. Boundary compliance: data, inputs, targets, splits, labels, comparisons, interfaces, privacy, and scope.
2. Correctness: code behavior, calculations, evidence integrity, and meaningful tests.
3. Scientific validity: whether the comparison answers the recorded question and whether optimization or stability checks are sufficient.
4. Explanation: whether a reader can reconstruct what changed, what stayed fixed, and why the result supports the stated judgment.
5. Maintainability and optional improvements.

Write findings with exact file or evidence locations and separate:

- required corrections;
- unresolved scientific decisions;
- limitations that qualify the conclusion;
- optional improvements.

State which checks you personally ran. Label the review independent only when the independence conditions in `workflow/REVIEW.md` are met. Do not edit reviewed work unless the user separately asks for fixes.
