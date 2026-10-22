# Research workflow process map

This document separates the workflow into three views so each part can be reviewed independently:

1. **Stage and approval map:** when work moves forward and when the human must intervene.
2. **Exception map:** what happens when the agent discovers a problem or a new idea.
3. **Information map:** which file owns each kind of information.

The diagrams describe control and information flow. They do not grant tool permissions or external authorization.

## Roles

| Role | May do without a new scientific decision | Must not do without human approval |
| --- | --- | --- |
| Human researcher | Define questions, approve tasks, interpret evidence, choose disposition | Not applicable; the human is the scientific decision owner |
| Lead agent | Execute an approved task, run checks, repair mechanical failures, prepare evidence | Change the research question, activate backlog work, publish, or strengthen claims |
| Reviewer | Inspect scope, code, evidence, and explanation; report findings | Treat review as authorization, silently fix scope, or call a non-independent review independent |
| Validation scripts | Check deterministic structure, links, states, and suspicious publication content | Decide scientific validity, privacy, or publication readiness |

## 1. Stage and approval map

This is the complete task lifecycle. A **gate** is a point where work waits for an explicit human decision.

```mermaid
flowchart TB
    Start([Project idea]) --> G0{Gate 0<br/>Approve project definition?}
    G0 -- Revise --> Charter[Edit PROJECT.md<br/>question, boundaries, data classes, authority]
    Charter --> G0
    G0 -- Approve --> Plan[Write or select PLAN.md phase<br/>comparison, evidence, stop condition]

    Plan --> Draft[Draft work/ACTIVE_TASK.md<br/>one question and one bounded scope]
    Draft --> Ready{Task complete enough to review?}
    Ready -- No --> Draft
    Ready -- Yes --> G1{Gate 1<br/>Authorize this task?}
    G1 -- Reject or revise --> Draft
    G1 -- Approve --> Run[Agent executes within ACTIVE_TASK.md]

    Run --> Check[Run specified checks<br/>and inspect saved outputs]
    Check --> Mechanical{Mechanical failure?}
    Mechanical -- Yes --> Repair[Repair without changing<br/>the scientific question]
    Repair --> Check
    Mechanical -- No --> Exception{Unexpected finding<br/>or new idea?}

    Exception -- Yes --> ExceptionMap[Follow exception map below]
    ExceptionMap --> RunOrGate{Return to task<br/>or require human gate}
    RunOrGate -- Return --> Run
    RunOrGate -- Human decision needed --> G2{Gate 2<br/>Resolve blocker or scope change?}
    G2 -- Continue original task --> Run
    G2 -- Amend task or plan --> Draft
    G2 -- Stop or invalidate --> Evidence

    Exception -- No --> Evidence[Save experiment result<br/>facts, checks, limitations, disposition proposal]
    Evidence --> Review[Reviewer checks scope,<br/>correctness, evidence, and explanation]
    Review --> Findings{Required correction?}
    Findings -- Mechanical or implementation correction --> Repair
    Findings -- Scientific uncertainty --> G3
    Findings -- No blocking finding --> Packet[Create concise review packet]
    Packet --> G3{Gate 3<br/>Choose scientific disposition}

    G3 -- Retain --> Decision[Record decision and update CURRENT.md]
    G3 -- Investigate surprising failure --> BackToPlan[Define a direct diagnostic task]
    G3 -- Retire expected failure --> Decision
    G3 -- Unresolved --> Decision
    BackToPlan --> Draft

    Decision --> More{Another approved question?}
    More -- Yes --> Plan
    More -- No --> Hold([Wait with state preserved])

    Decision --> PublishCandidate{External release proposed?}
    PublishCandidate -- No --> Hold
    PublishCandidate -- Yes --> ReleaseChecks[Run release scan<br/>and manually inspect files, history, licenses]
    ReleaseChecks --> G4{Gate 4<br/>Approve exact destination and visibility?}
    G4 -- No --> Hold
    G4 -- Yes --> External([Publish or upload])
```

### Human intervention points

- **Gate 0:** approve the project question, boundaries, data classification, and authority.
- **Gate 1:** approve one task's exact input, output, changed element, fixed elements, checks, and stop conditions.
- **Gate 2:** decide whether a blocker or proposed scope change justifies continuing, amending, invalidating, or stopping.
- **Gate 3:** interpret the reviewed evidence and choose retain, investigate cause, retire, or unresolved.
- **Gate 4:** approve the exact external destination, visibility, and material being released.

The agent does not need human approval for every syntax repair, failed unit test, broken link, or rerun that remains inside the approved task.

## 2. Exception and detour map

This decision tree prevents a useful discovery from silently replacing the original question.

```mermaid
flowchart TB
    Finding([Agent observes an unexpected result,<br/>problem, or new idea]) --> Trust{Can the active result be trusted<br/>without resolving it?}

    Trust -- No --> Blocking[Classify as blocking]
    Blocking --> BlockRecord[Record affected result,<br/>evidence, paused work, smallest resolution]
    BlockRecord --> HumanBlock{Human decision needed<br/>for the resolution?}
    HumanBlock -- No; mechanical repair only --> Repair[Repair and rerun affected checks]
    Repair --> Return1([Return to named active-task step])
    HumanBlock -- Yes --> Gate2([Gate 2: pause and ask human])

    Trust -- Yes --> Needed{Is a limited check required<br/>to interpret the active result?}
    Needed -- Yes --> Fits{Can it keep the same data, target,<br/>comparison, claim, and resource limit?}
    Fits -- Yes --> Diagnostic[Record bounded diagnostic:<br/>parent, operation, maximum work,<br/>stop condition, evidence, return point]
    Diagnostic --> RunDiagnostic[Run only the recorded check]
    RunDiagnostic --> StopReached{Stop condition reached?}
    StopReached -- No, within recorded maximum --> RunDiagnostic
    StopReached -- Yes --> Return2([Return to named active-task step])
    Fits -- No --> ScopeProposal[Write a scope-change proposal]
    ScopeProposal --> Gate2

    Needed -- No --> Useful{Could it matter later?}
    Useful -- Yes --> Backlog[Add one candidate question<br/>to work/BACKLOG.md]
    Backlog --> NoExecution[Do not gather more evidence<br/>for that item now]
    NoExecution --> Return3([Continue original task])
    Useful -- No --> Note[Record only if needed<br/>to explain the current evidence]
    Note --> Return3
```

### Classification test

- **Blocking:** without resolution, a specific active result is invalid or untrustworthy.
- **Bounded diagnostic:** a limited check directly distinguishes explanations of the current result and has a written return point.
- **Backlog:** it may be valuable, but the current result does not depend on it.

If the agent cannot assign one category with concrete reasons, it pauses the affected step and asks the human instead of expanding the work.

## 3. Information ownership and flow

Each fact should have one authoritative home. Other files link to it instead of copying its full content.

```mermaid
flowchart LR
    Human[Human decisions and project intent] --> Project[PROJECT.md<br/>purpose, scope, data classes, authority]
    Human --> Plan[PLAN.md<br/>approved phase order and comparisons]
    Project --> Active[work/ACTIVE_TASK.md<br/>single authorized task]
    Plan --> Active
    Current[memory/CURRENT.md<br/>short state and next decision] --> Active

    Active --> Agent[Agent execution]
    Agent --> Experiment[experiments/ID/<br/>pre-recorded plan, outputs, results, checks]
    Agent --> Backlog[work/BACKLOG.md<br/>unapproved candidate questions]
    Agent --> Review[reviews/<br/>findings and concise decision packet]

    Experiment --> Review
    Review --> HumanGate[Human scientific decision]
    HumanGate --> Decisions[memory/DECISIONS.md<br/>durable choice and reason]
    HumanGate --> Current
    Decisions --> Plan
    Current --> Human

    Terms[glossary/TERMS.md<br/>one preferred term and plain meaning] --> Active
    Terms --> Experiment
    Terms --> Review

    Scripts[Validation scripts<br/>deterministic checks only] -. check .-> Active
    Scripts -. check .-> Experiment
    Scripts -. check .-> Review
    Scripts -. never decide science .-> HumanGate
```

## File update rules

| Information | Authoritative location | Update timing | Main reader |
| --- | --- | --- | --- |
| Project purpose, data policy, authority | `PROJECT.md` | When the human approves a durable project change | Everyone |
| Phase order and fixed comparisons | `PLAN.md` | Before affected work begins; preserve prior versions for material changes | Human and lead agent |
| Immediate current state | `memory/CURRENT.md` | After substantial work or a changed next decision | Human and next agent session |
| One authorized task | `work/ACTIVE_TASK.md` | Before execution and when an approved blocker changes its status | Lead agent and reviewer |
| Unapproved future ideas | `work/BACKLOG.md` | When discovered; no execution implied | Human planner |
| Experiment expectation and evidence | `experiments/<ID>/` | Plan before interpretation; results after execution | Reviewer and human |
| Review findings and decision summary | `reviews/` | After evidence exists and before Gate 3 | Human decision owner |
| Durable choices | `memory/DECISIONS.md` | After human decision | Future planners and reviewers |
| Preferred terminology | `glossary/TERMS.md` | When a stable new distinction is necessary | Writers and reviewers |

## State transitions for the active task

```mermaid
stateDiagram-v2
    [*] --> empty
    empty --> planned: task drafted
    planned --> approved: Gate 1 approval
    planned --> empty: rejected or withdrawn
    approved --> running: execution starts
    running --> blocked: trusted continuation is impossible
    blocked --> running: Gate 2 approves resolution
    blocked --> invalidated: evidence cannot support the task
    running --> review: completion evidence exists
    review --> running: implementation correction required
    review --> blocked: unresolved scientific issue
    review --> completed: Gate 3 accepts disposition
    completed --> superseded: later approved evidence replaces its decision
    invalidated --> [*]
    superseded --> [*]
    completed --> [*]
```

`completed` means the bounded task and its review are complete. It does not mean the scientific hypothesis is true.
