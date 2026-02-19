# Universal Rules

Rules that apply across all layers, stages, OS, and tool contexts.

---

## Directory Structure

```
02_rules/
├── README.md                           # This file
├── static/                             # Rules that apply on EVERY API turn
│   ├── I0_FILE_CHANGE_REPORTING.md     # [I0] Report all file changes every turn
│   ├── MANAGER_DELEGATION_RULE.md      # Managers delegate, don't operate
│   ├── STAGE_BOUNDARY_RULE.md          # Stage agents stay in scope
│   └── STAGE_REPORT_RULE.md            # Stage agents write reports before exiting
└── dynamic/                            # Rules loaded when triggered by scenario
    ├── I0_source_of_truth_rule.md      # [I0] Source of truth protocol — MUST execute when asked
    ├── PARALLEL_STAGES_RULE.md         # When stages can run in parallel
    └── STAGE_LOOP_RULE.md              # When stages loop back (07→08→09→07)
```

---

## Importance Ranking

Rules have an importance ranking prefix (`I0_`, `I1_`, etc.) where **0 is most important** and importance increases numerically as priority decreases. Rules without a prefix are standard importance (equivalent to I2).

| Importance | Prefix | Meaning | Behavior |
|------------|--------|---------|----------|
| 0 | `I0_` | Critical | Static: always enforced. Dynamic: MUST load when triggered — no exceptions |
| 1 | `I1_` | High | Should be loaded/enforced — can defer only if severely context-constrained |
| 2 | (none) | Standard | Normal rule behavior — load when relevant |
| 3+ | `I3_` | Advisory | Guidance that can be skipped under tight context budgets |

---

## Static Rules (Every API Turn)

These rules MUST be followed on EVERY interaction. They should be **summarized in CLAUDE.md files**.

| Rule | Importance | Summary |
|------|------------|---------|
| **I0_FILE_CHANGE_REPORTING** | 0 | Report all files changed/added/updated/removed with full paths every turn |
| **MANAGER_DELEGATION_RULE** | 2 | Managers delegate to stage agents; they don't carry operational knowledge |
| **STAGE_BOUNDARY_RULE** | 2 | Stage agents stay within their stage scope |
| **STAGE_REPORT_RULE** | 2 | Every stage agent writes stage_report.md before exiting |

---

## Dynamic Rules (Scenario-Triggered)

These rules apply when specific conditions are met.

| Rule | Importance | Trigger |
|------|------------|---------|
| **I0_source_of_truth_rule** | 0 | User asks about source of truth, context chain, or where something is defined |
| **PARALLEL_STAGES_RULE** | 2 | When determining if stages can execute concurrently |
| **STAGE_LOOP_RULE** | 2 | When stages need to loop (testing → criticism → fixing → re-testing) |

---

## How to Reference in CLAUDE.md

Static rules are summarized inline. Dynamic rules are referenced by trigger.

```markdown
## Critical Rules
### File Change Reporting
On every turn with file operations, report full paths of added/updated/moved/removed files.
**Full rule**: `layer_0/.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md`

## Scenario-Based Rules (Read When Triggered)
| Trigger | Rule |
|---------|------|
| "Where is the source of truth for X?" | `layer_0/.0agnostic/02_rules/dynamic/I0_source_of_truth_rule.md` |
```
