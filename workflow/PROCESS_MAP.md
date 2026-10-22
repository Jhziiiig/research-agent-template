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

The first diagram is the whole lifecycle at a glance. The smaller diagrams underneath show one phase at a time. A **gate** is a point where work waits for an explicit human decision. Across every diagram, blue marks human-controlled work, light gray marks agent or review work, and red is reserved for a problem that interrupts the normal route.

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"flowchart":{"curve":"linear","nodeSpacing":24,"rankSpacing":36,"htmlLabels":true}}}%%
flowchart LR
    P0([1 · Define project]):::human --> P1{Gate 0}:::gate
    P1 --> P2([2 · Authorize task]):::human --> P3{Gate 1}:::gate
    P3 --> P4([3 · Agent execution loop]):::agent
    P4 --> P5([4 · Evidence + review]):::evidence
    P5 --> P6{Gate 3}:::gate
    P6 --> P7([5 · Record decision]):::file
    P7 -. optional .-> P8{Gate 4<br/>external release}:::gate

    classDef human fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef gate fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef agent fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef evidence fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef file fill:#FFFFFF,stroke:#8A98A5,color:#334155,stroke-width:2px;
```

### Phase A — define the project and authorize one task

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"flowchart":{"curve":"linear","nodeSpacing":28,"rankSpacing":40,"htmlLabels":true}}}%%
flowchart TB
    Start([Project idea]):::human --> Charter[Write PROJECT.md<br/>question · boundaries · data classes · authority]:::file
    Charter --> G0{Gate 0<br/>Approve the project definition?}:::gate
    G0 -- Revise --> Charter
    G0 -- Approve --> Plan[Select one PLAN.md phase<br/>comparison · evidence · stop condition]:::file
    Plan --> Draft[Draft work/ACTIVE_TASK.md<br/>one question · one bounded scope]:::file
    Draft --> G1{Gate 1<br/>Authorize this exact task?}:::gate
    G1 -- Revise or reject --> Draft
    G1 -- Approve --> Run([Start agent execution]):::agent

    classDef human fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef gate fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef agent fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef file fill:#FFFFFF,stroke:#8A98A5,color:#334155,stroke-width:2px;
```

### Phase B — execute, check, and handle exceptions

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"flowchart":{"curve":"linear","nodeSpacing":28,"rankSpacing":40,"htmlLabels":true}}}%%
flowchart TB
    Run[Execute only ACTIVE_TASK.md]:::agent --> Check[Run specified checks<br/>inspect saved outputs]:::agent
    Check --> Failure{Mechanical failure?}:::decision
    Failure -- Yes --> Repair[Repair without changing<br/>the scientific question]:::agent
    Repair --> Check
    Failure -- No --> Finding{Unexpected finding<br/>or new idea?}:::decision
    Finding -- No --> Evidence([Save evidence]):::evidence
    Finding -- Yes --> Classify[Use the exception map<br/>blocking · bounded diagnostic · backlog]:::warning
    Classify -- Return to task --> Run
    Classify -- Human decision required --> G2{Gate 2<br/>Resolve blocker or scope change}:::gate
    G2 -- Continue --> Run
    G2 -- Amend task --> Revise([Return to Gate 1]):::human
    G2 -- Stop or invalidate --> Evidence

    classDef human fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef gate fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef agent fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef evidence fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef decision fill:#FFFFFF,stroke:#64748B,color:#1F2937,stroke-width:2px;
    classDef warning fill:#FDECEC,stroke:#C2413B,color:#5F1714,stroke-width:2px;
```

### Phase C — review evidence and make the scientific decision

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"flowchart":{"curve":"linear","nodeSpacing":28,"rankSpacing":40,"htmlLabels":true}}}%%
flowchart TB
    Evidence[Save facts · checks · limitations<br/>and a proposed disposition]:::evidence
    Evidence --> Review[Reviewer checks scope<br/>correctness · evidence · explanation]:::review
    Review --> Finding{Blocking correction?}:::decision
    Finding -- Implementation correction --> Repair([Return to repair loop]):::agent
    Finding -- Scientific uncertainty --> G3{Gate 3<br/>Choose disposition}:::gate
    Finding -- No --> Packet[Create concise review packet]:::review
    Packet --> G3
    G3 -- Retain --> Record[Record decision<br/>update CURRENT.md]:::file
    G3 -- Investigate surprising failure --> Diagnostic([Authorize a direct diagnostic task]):::human
    G3 -- Retire expected failure --> Record
    G3 -- Unresolved --> Record

    classDef human fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef gate fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef agent fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef evidence fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef review fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef file fill:#FFFFFF,stroke:#8A98A5,color:#334155,stroke-width:2px;
    classDef decision fill:#FFFFFF,stroke:#64748B,color:#1F2937,stroke-width:2px;
```

### Phase D — continue, pause, or release externally

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"flowchart":{"curve":"linear","nodeSpacing":28,"rankSpacing":40,"htmlLabels":true}}}%%
flowchart TB
    Record[Decision recorded<br/>CURRENT.md updated]:::file --> More{Another approved question?}:::decision
    More -- Yes --> Next([Return to planning]):::human
    More -- No --> Hold([Wait with state preserved]):::stop
    Record --> Release{External release proposed?}:::decision
    Release -- No --> Hold
    Release -- Yes --> Checks[Scan files + Git history<br/>inspect licenses + destination]:::review
    Checks --> G4{Gate 4<br/>Approve exact material,<br/>destination, and visibility?}:::gate
    G4 -- No --> Hold
    G4 -- Yes --> External([Publish or upload]):::external

    classDef human fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef gate fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef review fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef file fill:#FFFFFF,stroke:#8A98A5,color:#334155,stroke-width:2px;
    classDef decision fill:#FFFFFF,stroke:#64748B,color:#1F2937,stroke-width:2px;
    classDef stop fill:#F1F5F9,stroke:#64748B,color:#334155,stroke-width:2px;
    classDef external fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
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
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"flowchart":{"curve":"linear","nodeSpacing":28,"rankSpacing":40,"htmlLabels":true}}}%%
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

    classDef gate fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef return fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef action fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef warning fill:#FDECEC,stroke:#C2413B,color:#5F1714,stroke-width:2px;
    classDef file fill:#FFFFFF,stroke:#8A98A5,color:#334155,stroke-width:2px;

    class Gate2 gate;
    class Return1,Return2,Return3 return;
    class Repair,Diagnostic,RunDiagnostic action;
    class Blocking,BlockRecord,ScopeProposal warning;
    class Backlog,NoExecution,Note file;
```

### Classification test

- **Blocking:** without resolution, a specific active result is invalid or untrustworthy.
- **Bounded diagnostic:** a limited check directly distinguishes explanations of the current result and has a written return point.
- **Backlog:** it may be valuable, but the current result does not depend on it.

If the agent cannot assign one category with concrete reasons, it pauses the affected step and asks the human instead of expanding the work.

## 3. Information ownership and flow

Each fact should have one authoritative home. Other files link to it instead of copying its full content.

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"flowchart":{"curve":"linear","nodeSpacing":28,"rankSpacing":40,"htmlLabels":true}}}%%
flowchart TB
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

    classDef human fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef gate fill:#EAF1F8,stroke:#355C7D,color:#183247,stroke-width:2px;
    classDef agent fill:#F4F7FA,stroke:#6B7F91,color:#243746,stroke-width:2px;
    classDef file fill:#FFFFFF,stroke:#8A98A5,color:#334155,stroke-width:2px;
    classDef check fill:#F1F5F9,stroke:#64748B,color:#334155,stroke-width:2px;

    class Human human;
    class HumanGate gate;
    class Agent agent;
    class Project,Plan,Active,Current,Experiment,Backlog,Review,Decisions,Terms file;
    class Scripts check;
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
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"16px","lineColor":"#64748B"},"state":{"useMaxWidth":true}}}%%
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
