# Stage Delegation Principles

These principles govern how agents delegate and operate across the stage hierarchy.

## 1. Managers Delegate, Agents Operate

Entity managers maintain the big picture. Stage agents do the work. A manager reads stage reports and decides what to delegate next — it does not carry operational methodology for any stage.

## 2. Explicit Scope Boundaries

Every stage agent knows what it IS and what it IS NOT. The "NOT" list is as important as the "IS" description. When work falls outside scope, the agent stops, documents it, and hands off to the correct stage.

## 3. Three-Tier Knowledge

Knowledge flows through three tiers:
- **Pointers** (0AGNOSTIC.md) — what this entity IS, where things are
- **Distilled** (.0agnostic/01_knowledge/) — domain knowledge, principles, key docs
- **Full** (stage outputs) — complete research, design specs, test results

Managers work at the pointer tier. Stage agents load distilled knowledge on demand. Full detail stays within stages.

## 4. Stage Reports Are the Communication Channel

Stage agents communicate with managers through stage reports, not through shared context. The report is the async handoff — it tells the manager what was done, what's left, and what the next stage needs.

## 5. Stages Are Reentrant

Stages can be entered multiple times. Research can loop back from design. Testing can loop through criticism and fixing. Requirements can be revised after criticism. Each reentry starts by reading the stage's current state (0AGNOSTIC.md, existing outputs, stage report).

## 6. Output-First, Not Process-First

Stage agents produce deliverables, not process logs. The value is in the outputs/ directory — the requirements, research findings, design specs, test results. Process notes are secondary.

## 7. Selective Context Loading

Never load all parent knowledge at once. Read the specific file relevant to the task at hand. Context windows are finite — every byte loaded must earn its place.
