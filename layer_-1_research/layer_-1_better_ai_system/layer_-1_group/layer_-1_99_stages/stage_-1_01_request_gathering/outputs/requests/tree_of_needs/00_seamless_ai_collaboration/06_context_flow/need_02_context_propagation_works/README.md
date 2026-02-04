# Need: Context Propagation Works

## Parent Branch
`06_context_flow`

---

## Problem Statement

Context exists in many places (rules, knowledge, skills, status), but agents don't reliably receive it. The "propagation chain" from source to agent is broken or inconsistent.

**Current Issues:**
- Agent might read CLAUDE.md but miss critical rules in sub_layers
- Triggers say "load X when Y" but agent doesn't follow them
- Context scattered across files with no clear loading order
- Some context never reaches the agent at all

---

## What We Need

A reliable **propagation chain** that ensures context flows from source to agent:

```
Source Files                    Propagation              Agent Context
─────────────                   ───────────              ─────────────
rules/                    →     Entry point says    →    Agent knows rules
knowledge/                →     "load from here"    →    Agent has knowledge
skills/                   →     with triggers       →    Agent can use skills
status.json               →                         →    Agent knows state
```

---

## Solution: Propagation Chain Architecture

### Level 1: Entry Point (index.jsonld / CLAUDE.md)
```
What: Identity, critical rules, triggers, pointers
When: Always loaded first
Detail: Minimal - just enough to direct
```

### Level 2: Triggered Loads
```
What: Stage workflows, action skills
When: Triggered by context (entering stage, starting action)
Detail: Moderate - specific to task
```

### Level 3: On-Demand Loads
```
What: Deep knowledge, reference docs
When: Agent realizes it needs more info
Detail: Full - comprehensive reference
```

---

## Propagation Chain Diagram

```
Session Start
     │
     ▼
┌─────────────────────────────────────────┐
│ 1. Read index.jsonld                    │
│    → Identity, nav:*, trigger:*         │
└─────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────┐
│ 2. Execute trigger:onSessionStart       │
│    → Read CLAUDE.md                     │
│    → Read status.json (if exists)       │
└─────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────┐
│ 3. Context-triggered loads              │
│    → Entering stage? Load stage skill   │
│    → Creating entity? Load creation skill│
└─────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────┐
│ 4. On-demand navigation                 │
│    → Need rules? Follow nav:rules       │
│    → Need knowledge? Follow nav:knowledge│
└─────────────────────────────────────────┘
```

---

## Success Criteria

- [ ] Agent receives all critical context within 3 file reads
- [ ] Triggers are machine-readable and reliably executed
- [ ] No context is "lost" due to unclear pointers
- [ ] Agent can explain its context loading path

---

## Related Needs

- `need_05_entry_points_right_detail` - Entry point content
- `need_06_navigation_to_deeper_details` - How agent finds more

---

## Status

- **Priority**: High
- **Complexity**: High
- **Prototype**: JSON-LD navigation system addresses this
