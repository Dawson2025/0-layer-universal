---
resource_id: "38876a7d-fa6c-4e72-8209-a10ebd660ec3"
resource_type: "rule"
resource_name: "AI_CONTEXT_MODIFICATION_PROTOCOL"
---
# Filesystem Change Visualization Protocol

<!-- section_id: "781ced9e-310b-4db5-a20e-0b13171db4d4" -->
## Rule

Before making structural filesystem changes, the AI MUST show a diagram of the proposed changes and wait for approval. This rule has **two tiers** based on what's being modified:

<!-- section_id: "e345d17b-7fff-42fa-b828-896949e1a497" -->
### Tier 1: AI Context Changes (strict)

**Trigger**: Modifying AI context files (CLAUDE.md, .0agnostic/, rules, knowledge, stages, etc.)

1. **Store proposal in registry**
   - Location: `layer_X_00_layer_registry/proposals/YYYY-MM-DD_description/`
   - Create `SUMMARY.md` with full proposal details
   - For multi-layer changes: modular proposals per layer, summary at common parent

2. **Present a DIAGRAM** showing the proposed changes
   - Reference the stored proposal file
   - Show full file paths (not abbreviated)
   - Show before/after state where applicable
   - Summarize content of new files
   - For AI context: show propagation chain (source → sync → tool-specific)

3. **Wait for explicit user approval**
   - Do not proceed until user confirms
   - User may request modifications to the plan

4. **Proceed with modifications**
   - Follow the approved diagram exactly
   - Report completion when done

5. **Update proposal status**
   - Change status to "Executed" in SUMMARY.md
   - Mark approval checkboxes as complete

<!-- section_id: "903c5c1e-564a-431c-bbe7-6ff0cd31295e" -->
### Tier 2: General Filesystem Changes (standard)

**Trigger**: Any structural filesystem changes — creating directories, reorganizing files, adding multiple files, renaming/moving files, creating new directory structures.

1. **Present a DIAGRAM** showing the proposed changes
   - Show full absolute file paths (not abbreviated)
   - Show before/after state where applicable
   - Mark each item as NEW, UPDATE, MOVE, or DELETE
   - Summarize content of new files/directories

2. **Wait for explicit user approval**
   - Do not proceed until user confirms
   - User may request modifications to the plan

3. **Proceed with modifications**
   - Follow the approved diagram exactly
   - Report completion with inline paths and end-of-turn summary (per File Change Reporting Rule)

**When Tier 2 applies**: Creating new directory structures, reorganizing existing files/dirs, scaffolding entities or stages, bulk file creation, structural refactors. Does NOT apply to simple single-file edits or appends within an existing file — those just need the File Change Reporting Rule.

<!-- section_id: "a19585bd-e196-48ad-9b4a-86911537f3c3" -->
## Scope

<!-- section_id: "4e927b13-32a6-41fc-8c54-66eb7232e3c9" -->
### Tier 1 (AI context — strict, with proposal registry)

| Path Pattern | Description |
|--------------|-------------|
| `0AGNOSTIC.md` | Agnostic source of truth |
| `.0agnostic/` | Agnostic resource directories |
| `.1merge/` | Tool-specific merge directories |
| `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md` | Generated tool files |
| `.claude/`, `.cursor/`, `.codex/`, `.gemini/`, `.github/` | App config directories |
| `*_rules/` | Rules directories |
| `*_prompts/` | Prompts directories |
| `*_knowledge/` | Knowledge directories |
| `status.json`, `status_N.json` | Status files |
| `*.gab.jsonld`, `*.integration.md` | Agent definitions |

<!-- section_id: "17a7b2fe-1536-4e26-a3a0-4bb5b7c11a69" -->
### Tier 2 (General filesystem — standard, diagram only)

| Trigger | Description |
|---------|-------------|
| Creating 2+ directories | New directory structure being scaffolded |
| Creating 3+ files in one turn | Bulk file creation |
| Moving/renaming files across directories | Structural reorganization |
| Creating a new entity, stage, or feature | Entity scaffolding |
| Any operation the user requests that changes directory layout | User-requested restructuring |

**Exemptions** (Tier 2 not required):
- Editing content within a single existing file
- Creating a single file in an existing directory
- Appending to an existing file

<!-- section_id: "e04a9dcd-e20d-4696-95c9-19ec8b96ce59" -->
## Rationale

- **Visibility**: User can see exactly what will change before it happens — directories, files, and their relationships
- **Control**: User maintains authority over their filesystem structure
- **Intentionality**: Prevents accidental or unintended modifications, especially in deep hierarchies
- **Auditability**: Creates a clear record of approved changes
- **Orientation**: In deep paths (7+ levels), seeing the proposed structure helps the user stay oriented

<!-- section_id: "e70dd3d3-cdb8-4499-ade4-60dab6e13e03" -->
## Diagram Requirements

The diagram MUST include:

1. **Full paths** — Complete path from root, not abbreviated (same rule as File Change Reporting)
2. **Directory tree** — Show directory structure before and after using ASCII tree format
3. **Content summary** — Brief description of new file/directory contents
4. **Action type** — Mark each item as `◄── NEW`, `◄── UPDATE`, `◄── MOVE from ...`, or `◄── DELETE`
5. **Annotations** — Brief purpose of each new directory or file (what it's for)

<!-- section_id: "96d1a55a-1b1d-4da7-afcb-51ab011c31cf" -->
## Example: Tier 1 (AI Context)

```
Propagation: 0AGNOSTIC.md → agnostic-sync.sh → CLAUDE.md, AGENTS.md, GEMINI.md

Location: /home/dawson/dawson-workspace/code/0_layer_universal/
  └── .0agnostic/
      └── 02_rules/
          └── static/
              └── new_rule.md          ◄── NEW — Describes X behavior

Content: Rule definition with scope, rationale, and examples.
After sync: Will appear in CLAUDE.md Promoted Rules table.
```

<!-- section_id: "5014036f-3a9d-45e4-bd6d-f07c02e9d8c2" -->
## Example: Tier 2 (General Filesystem)

```
Proposed structure at:
/home/dawson/dawson-workspace/code/0_layer_universal/.../stage_3_07_testing/outputs/

BEFORE:
outputs/
├── run_all_tests.sh
├── stage_report.md
├── test_results_summary.md
├── test_*.sh (5 scripts, flat)
└── by_topic/
    └── test_design/ (8 files)

AFTER:
outputs/
├── run_all_tests.sh                          ◄── KEEP (unchanged)
└── by_suite/                                 ◄── NEW — replaces flat structure
    ├── README.md                             ◄── NEW — suite index
    ├── context_chain_validation/             ◄── NEW — test suite
    │   ├── design/                           ◄── NEW — test designs
    │   │   └── test_design.md               ◄── MOVE from by_topic/test_design/
    │   ├── tests/                            ◄── NEW — test scripts
    │   │   └── test_context_chain.sh        ◄── MOVE from outputs/
    │   ├── results/                          ◄── NEW — run outputs
    │   └── insights/                         ◄── NEW — analysis
    └── agnostic_sync/                        ◄── NEW — test suite
        ├── design/
        ├── tests/
        ├── results/
        └── insights/

REMOVED:
- outputs/stage_report.md                    ◄── MOVE to .0agnostic/.../01_to_above/
- outputs/test_results_summary.md            ◄── MOVE to .0agnostic/.../01_to_above/
```

<!-- section_id: "f8d2229c-1275-4982-919a-6aceae60c31b" -->
## Date Added
2026-01-26 (original AI context scope)
2026-02-24 (expanded to general filesystem changes)

<!-- section_id: "52f6b432-3110-4ea7-accb-826186408cb0" -->
## Related
- **File Change Reporting Rule**: `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md` — reports changes after they happen; this rule shows them before
- **Agnostic Update Protocol**: `.0agnostic/02_rules/static/agnostic_update_protocol.md` — specific protocol for .0agnostic/ changes
