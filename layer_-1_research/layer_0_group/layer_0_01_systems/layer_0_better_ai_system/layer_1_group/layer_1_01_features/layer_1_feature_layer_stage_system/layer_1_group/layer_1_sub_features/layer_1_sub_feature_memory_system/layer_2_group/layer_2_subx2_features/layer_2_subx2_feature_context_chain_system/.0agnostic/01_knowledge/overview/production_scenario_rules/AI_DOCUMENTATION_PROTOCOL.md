---
resource_id: "81743498-38c8-4d91-b027-1af9ec56dbe6"
resource_type: "knowledge"
resource_name: "AI_DOCUMENTATION_PROTOCOL"
---
# AI Documentation Protocol

<!-- section_id: "6f0b66e2-40b5-4837-a324-8497e7c32c25" -->
## Rule
Whenever the AI performs ANY activity, it MUST document in:
1. The CORRECT LAYER (layer_N) where the work belongs
2. The CORRECT SUB-LAYER hierarchy within that layer
3. The CORRECT STAGE corresponding to the activity type

<!-- section_id: "6c361d26-3230-4afa-b408-176a241f7f29" -->
## Hierarchy Structure
```
layer_N/                           ← Correct layer for the work
└── sub_layer_N_XX.../             ← Navigate to correct sub-layer
    └── sub_layer_N_99_stages/     ← Stages container
        └── stage_N_XX_<name>/     ← Correct stage for activity
            └── outputs/           ← Documentation goes here
```

<!-- section_id: "0db64482-916b-47a7-8ff2-78050549c2bf" -->
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

<!-- section_id: "bf4001c2-d881-4897-a74f-bfc8bf39e9b9" -->
## Example: Linux Setup Fix
Work location: Linux Ubuntu local setup
Full path hierarchy:
```
0_layer_universal/
└── layer_0/
    └── layer_0_03_sub_layers/
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

<!-- section_id: "bae34ae4-d1fb-4787-82f8-985960a92f45" -->
## Determining Correct Location
1. Identify WHAT is being worked on (project, feature, setup, etc.)
2. Navigate to its layer and sub-layer in the hierarchy
3. Find or create the stages container (sub_layer_N_99_stages/)
4. Document in the stage matching the activity performed

<!-- section_id: "4a589178-9d5a-45d9-9fa7-093692309f4f" -->
## File Naming Convention
Format: `<ID>_<description>.md`
Examples:
- `REQ_001_audio_improvement.md` (for requests)
- `ISSUE_003_gsd_display_fix.md` (for issues)

<!-- section_id: "abb22198-ec10-43c7-a7c7-f2f22f57bdde" -->
## Always Update status.json
When issues or requests change status, update the corresponding status.json file.

<!-- section_id: "2bcf3839-1fb1-4b3b-aebd-26190badfac4" -->
## Date Added
2026-01-26

<!-- section_id: "f88df019-6362-4e54-ba3d-01c205e6ac41" -->
## Related Rules
- AI_CONTEXT_MODIFICATION_PROTOCOL.md - Show diagram before modifying
- AI_CONTEXT_COMMIT_PUSH_RULE.md - Commit and push after changes
