# Writing for understanding

The goal is not merely grammatical text. A researcher should be able to explain what was done and why the result matters.

## Prefer concrete statements

Name the actor or sample, operation, input, output, comparison, and observed change when they matter.

Avoid replacing an operation with an abstract label. For example, instead of writing “the model gained individualized representation,” write what happened: “among records with the same stimulus and previous response, the model correctly distinguished more participants' next responses.” A short name may follow only if it will be reused.

## Controlled vocabulary

- Prefer a term already defined in `glossary/TERMS.md`.
- Introduce a new term only when it separates concepts that would otherwise be confused.
- Explain the concrete meaning first, then give the term.
- Use one preferred term consistently.
- Do not use a synonym merely to vary style.

## Required experiment explanation

On first description of a task or experiment, state:

1. What information enters the method.
2. What it predicts, estimates, or produces.
3. Whether training or fitting changes.
4. What is replaced, removed, or added.
5. What remains fixed.
6. Which observed value or label checks the output.

For numbers, state the sample unit, denominator, subset, number of repetitions, and averaging method. Do not compare numbers from different subsets as if they share a denominator.

## Comprehension test

Before handoff, the short explanation should let a reader answer without opening code:

- What question was tested?
- What entered the method?
- What was the output or target?
- What exactly changed?
- What stayed fixed?
- What evidence supports the conclusion?
- What does the result not establish?
- What decision is required next?

If the explanation does not answer these questions, revise the explanation before adding more terminology.
