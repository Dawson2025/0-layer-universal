---
resource_id: "ad1c92a1-9401-40c9-9533-9d56276be546"
resource_type: "rule"
resource_name: "AI_DOCUMENTATION_PROTOCOL"
---
# AI Documentation Protocol

<!-- section_id: "42c11759-551f-47b3-982a-635263bede65" -->
## Rule
Whenever the AI performs ANY activity, it MUST document in:
1. The CORRECT LAYER (layer_N) where the work belongs
2. The CORRECT SUB-LAYER hierarchy within that layer
3. The CORRECT STAGE corresponding to the activity type

<!-- section_id: "57b2e57e-8612-439f-b2e3-db3073679785" -->
## Hierarchy Structure
```
layer_N/                           ← Correct layer for the work
└── sub_layer_N_XX.../             ← Navigate to correct sub-layer
    └── sub_layer_N_99_stages/     ← Stages container
        └── stage_N_XX_<name>/     ← Correct stage for activity
            └── outputs/           ← Documentation goes here
```

<!-- section_id: "b5a6f58d-810c-4efa-a1e1-01195260c180" -->
## Stage-Activity Mapping (All Required When Applicable)

| Stage | Name              | REQUIRED When AI Does This                       |
|-------|-------------------|--------------------------------------------------|
| 00    | stage_manager     | Modifies stage system itself                     |
| 01    | request_gathering | Receives/clarifies a new user request            |
| 02    | research          | Researches solutions, explores problem space     |
| 03    | instructions      | Defines constraints, guidelines, rules           |
| 04    | design            | Makes architecture/design decisions              |
| 05    | planning          | Breaks work into subtasks, creates plans         |
| 06    | development       | Implements code, scripts, configurations         |
| 07    | testing           | Tests, verifies, validates anything              |
| 08    | criticism         | Identifies issues, problems, root causes         |
| 09    | fixing            | Applies fixes, corrections, patches              |
| 10    | current_product   | Updates final/active configuration               |
| 11    | archives          | Archives old versions                            |

<!-- section_id: "ed706359-c7ef-4cb1-acc5-6ccbf78c3603" -->
## Example: Linux Setup Fix
Work location: Linux Ubuntu local setup
Full path hierarchy:
```
0_layer_universal/
└── layer_0/
    └── layer_0_04_sub_layers/
        └── sub_layer_0_05+_setup_dependant/
            └── sub_layer_0_05_operating_systems/
                └── sub_layer_0_05_linux_ubuntu/
                    └── sub_layer_0_06_content/
                        └── sub_layer_0_06_environments/
                            └── sub_layer_0_06_local/
                                └── setup/
                                    └── sub_layer_0_06_99_stages/
                                        ├── stage_0_07_testing/outputs/
                                        ├── stage_0_08_criticism/outputs/  ← if issues found
                                        ├── stage_0_09_fixing/outputs/     ← if fix applied
                                        ├── stage_0_10_current_product/outputs/
                                        └── status.json                    ← always update
```

<!-- section_id: "234ed14f-33ff-4af2-b7d8-6017c0ee16e4" -->
## Determining Correct Location
1. Identify WHAT is being worked on (project, feature, setup, etc.)
2. Navigate to its layer and sub-layer in the hierarchy
3. Find or create the stages container (sub_layer_N_99_stages/)
4. Document in the stage matching the activity performed

<!-- section_id: "c5da6c4c-a6a4-4b02-bbf2-2fdf8fe5c284" -->
## File Naming Convention
Format: `<ID>_<description>.md`
Examples:
- `REQ_001_audio_improvement.md` (for requests)
- `ISSUE_003_gsd_display_fix.md` (for issues)

<!-- section_id: "dc5999d7-45df-4795-ba3e-2e73b965dced" -->
## Always Update status.json
When issues or requests change status, update the corresponding status.json file.

<!-- section_id: "4f48a7cb-0404-444c-aa6f-90426ee047c1" -->
## Date Added
2026-01-26

<!-- section_id: "b4e52f3a-26c4-4daa-a5fd-3011195e456b" -->
## Related Rules
- AI_CONTEXT_MODIFICATION_PROTOCOL.md - Show diagram before modifying
- AI_CONTEXT_COMMIT_PUSH_RULE.md - Commit and push after changes
