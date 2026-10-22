# Operating model

## The two loops

### Agent execution loop

Inside one approved task, an agent may repeat:

```text
implement or analyze
→ run the specified checks
→ observe saved outputs
→ repair mechanical failures
→ re-run the checks
→ prepare review evidence
```

Mechanical failures include syntax errors, failing tests, broken links, malformed outputs, and implementation defects that do not change the scientific question.

### Human-gated research loop

```text
research question
→ bounded task or experiment
→ evidence
→ interpretation
→ retain / investigate cause / retire
→ human approval of the next question
```

An agent may recommend the next decision but must not silently cross the decision gate.

## Starting work

A substantive task is ready only when `work/ACTIVE_TASK.md` states:

- one concrete question;
- input, output or target, and evaluation reference;
- exactly what changes and what remains fixed;
- expected result and its pre-existing basis;
- allowed and prohibited work;
- checks and evidence;
- completion and stop conditions;
- the decision reserved for the human.

If a required scientific choice is missing, prepare the missing choice for review instead of inventing it.

## Handling discoveries without losing the original task

For every unexpected discovery, choose one category.

### Blocking issue

Use this only when the active result cannot be trusted without resolution. Record:

- affected result;
- direct evidence of the problem;
- work that must pause;
- smallest resolution needed.

Do not broaden the repair into a new research program.

### Bounded diagnostic

Use this for a limited check that can distinguish explanations of a surprising result. Before execution, append this block to the active task or experiment record:

```text
Parent question:
Concrete uncertainty:
Diagnostic operation:
Maximum work or compute:
Stop condition:
Evidence produced:
Return point:
```

When the diagnostic ends, return to the named point. A diagnostic that requires a new target, dataset, major model family, or claim becomes a backlog proposal unless the human explicitly approves a scope change.

### Backlog item

Record the question and why it may matter. Do not gather extra evidence merely to make the backlog entry more persuasive.

## Closing a task

Before closure:

1. Verify saved outputs and links.
2. Separate observed results from interpretation.
3. State whether the expectation was supported, challenged, or not testable.
4. Recommend retain, investigate cause, retire, or remain unresolved.
5. Create a review packet.
6. Update current state and any durable decision after human review.
7. Stop. Do not activate the next task automatically.
