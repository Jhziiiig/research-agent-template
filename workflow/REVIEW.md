# Review workflow

Review is a separate activity from implementation. A review may inspect code, documents, experiments, or all three, but it does not silently change scientific scope.

## Review order

1. Read the active task and its completion conditions.
2. Inspect the actual diff, commands, outputs, and saved evidence.
3. Check correctness and boundary compliance before style.
4. Check whether the explanation lets a reader reconstruct the operation.
5. Record findings with concrete file or evidence locations.
6. Distinguish required fixes, unresolved scientific decisions, and optional improvements.

## Code review

Check:

- whether the code performs the operation described by the task;
- input, target, split, label, and leakage boundaries;
- changed interfaces and downstream effects;
- error handling and preservation of source data;
- tests that would fail for a meaningful defect;
- commands actually run and checks not run;
- unrelated changes.

Do not infer that a named reviewer or read-only instruction enforces permissions. Confirm environment permissions and inspect actual changes.

## Experiment review

Check:

- the question and expectation were recorded before interpreting the result;
- the direct comparison changes only the intended element;
- sample unit, denominator, subset, repetitions, and averaging are explicit;
- tuning uses only permitted data and required diagnostics are complete;
- failed runs and excluded results remain visible;
- metrics are tied to actual predictions or observations;
- the proposed disposition follows the evidence.

## Document review

Check:

- claims trace to evidence;
- plans are not described as observations;
- new terms are defined concretely;
- one concept does not acquire multiple unexplained names;
- limitations qualify the affected claim rather than being hidden at the end;
- the reader can answer the comprehension test in `workflow/WRITING.md`.

## Review independence

Call a review independent only when a separate reviewer or agent receives the task requirements and raw evidence without being given the implementer's intended conclusion, and does not modify the reviewed work during that pass. Otherwise label it self-review or non-independent review.
