---
resource_id: "cafebc8d-a1c6-45fd-a751-f6eec8a01165"
resource_type: "document"
resource_name: "EXTENDING_THE_FRAMEWORK"
---
# Extending the Layer/Stage Framework

**Purpose:** Advanced patterns for extending the standard framework beyond basic features, components, and stages.

**Audience:** Users who need custom organizational patterns beyond the standard structure.

**Last Updated:** 2026-01-09
**Version:** 2.0

---

<!-- section_id: "a932329c-50dc-4c64-8d61-fafb5536ac64" -->
## 🎯 When to Use This Guide

**Use the STANDARD framework** (`FLEXIBLE_LAYERING_SYSTEM.md`) when:
- ✅ Organizing topics, concepts, or learning materials
- ✅ Hierarchical breakdown (topic → subtopic → examples)
- ✅ Sequential workflow (instructions → development → testing → completion)
- ✅ Examples: Class notes, project documentation, learning materials

**Use EXTENSIONS** (this guide) when:
- ⚠️ Standard stages don't fit your workflow
- ⚠️ You need parallel or cyclical processes
- ⚠️ You have distinct phases beyond the 8 standard stages
- ⚠️ You need multiple instances of something (workflows, experiments, versions)
- ⚠️ Examples: Workflow management, experimentation, multi-phase processes

---

<!-- section_id: "fecda1b4-959b-4a89-af71-aa1133c4e449" -->
## 📐 Standard Structure Recap

```
layer_<N>_<type>_<name>/
├── <N>.00_ai_manager_system/           # REQUIRED: Manager
├── <N>.01_manager_handoff_documents/   # REQUIRED: Communication
├── <N>.02_sub_layers/                  # REQUIRED: Content slots (01-12)
├── <N>.99_stages/                      # REQUIRED: Workflow stages (01-08)
├── layer_<N+1>_features/               # OPTIONAL: Sub-features
└── layer_<N+1>_components/             # OPTIONAL: Components
```

**Standard Stages (8):**
1. `stage_N.01_instructions` - Requirements
2. `stage_N.02_planning` - Planning
3. `stage_N.03_design` - Design
4. `stage_N.04_development` - Active work
5. `stage_N.05_testing` - Testing/validation
6. `stage_N.06_criticism` - Review/critique
7. `stage_N.07_fixing` - Corrections
8. `stage_N.09_archives` - Completion

---

<!-- section_id: "8f023e8a-bbdc-4500-8af4-320db43ffec8" -->
## 🔧 Extension Pattern 1: Custom Numbered Directories

<!-- section_id: "db612ba8-1960-444c-93e0-6f13a747e0c5" -->
### What It Is

Add **custom numbered directories** (`.03-.98`) alongside standard ones for specific organizational needs.

<!-- section_id: "60c0f111-2e2d-41b6-bd07-858fb22d6621" -->
### Numbering Scheme

```
<N>.00  - ai_manager_system (REQUIRED)
<N>.01  - manager_handoff_documents (REQUIRED)
<N>.02  - sub_layers (REQUIRED)
<N>.03-.98  - CUSTOM DIRECTORIES (your choice)
<N>.99  - stages (REQUIRED)
```

**Rules:**
- Numbers `.00`, `.01`, `.02`, `.99` are **reserved**
- Numbers `.03` through `.98` are **available for custom use**
- Use **sequential numbering** (`.03`, `.04`, `.05`, ...)
- Each custom directory should have a **clear purpose**

<!-- section_id: "7788ec1c-4566-41ee-9de6-77ec359c0b6a" -->
### Example: Workflow Lifecycle Management

**Use Case:** Managing AI workflows with distinct phases (creation, production, results)

```
layer_2_feature_assignments/
├── 2.00_ai_manager_system/              # STANDARD
├── 2.01_manager_handoff_documents/      # STANDARD
├── 2.02_sub_layers/                     # STANDARD
├── 2.03_workflow_creation/              # CUSTOM - Development phase
│   ├── 2.00_ai_manager_system/          # Nested standard structure
│   ├── 2.01_manager_handoff_documents/
│   ├── 2.02_sub_layers/
│   └── 2.99_stages/                     # Stages for workflow development
│       ├── stage_2.01_instructions/
│       ├── stage_2.02_planning/
│       ├── stage_2.03_design/
│       ├── stage_2.04_development/
│       └── ...
├── 2.04_workflows/                      # CUSTOM - Production storage
│   ├── workflow_1/                      # Slot for instance 1
│   │   ├── workflow_ds250_assignments_v1.md
│   │   └── 2.99_stages/                 # Stages for workflow execution
│   │       ├── stage_2.01_instructions/
│   │       ├── stage_2.04_development/
│   │       └── ...
│   └── workflow_2/                      # Slot for instance 2
├── 2.05_results/                        # CUSTOM - Output tracking
│   ├── result_links.md
│   └── completed_assignments/
└── 2.99_stages/                         # STANDARD - Feature-level stages
```

**Why This Works:**
- `.03` = **Creation/Development** - Where workflows are designed
- `.04` = **Production/Execution** - Validated workflows ready to use
- `.05` = **Results/Output** - Links to what workflows produced
- Each custom directory has **nested standard structure**

<!-- section_id: "9acafa68-4626-453c-936e-cb99535ed88a" -->
### Example: Experimentation Pipeline

**Use Case:** Scientific experiments with distinct phases

```
layer_2_feature_protein_analysis/
├── 2.00_ai_manager_system/
├── 2.01_manager_handoff_documents/
├── 2.02_sub_layers/
├── 2.03_experimental_design/            # CUSTOM - Design experiments
│   └── 2.99_stages/
├── 2.04_data_collection/                # CUSTOM - Collect data
│   ├── experiment_1/
│   ├── experiment_2/
│   └── experiment_3/
├── 2.05_analysis/                       # CUSTOM - Analyze results
│   └── 2.99_stages/
├── 2.06_publication/                    # CUSTOM - Prepare papers
│   └── 2.99_stages/
└── 2.99_stages/                         # STANDARD - Overall project stages
```

<!-- section_id: "975581c6-cdc0-43b2-871b-ca069a4645c7" -->
### When to Use Custom Directories

**Use custom numbered directories when:**
- ✅ You have **distinct phases** that don't map to standard stages
- ✅ Phases are **parallel** or **cyclical** (not sequential)
- ✅ You need to **store multiple instances** (workflows, experiments, versions)
- ✅ Phases have their **own workflows** (nested stages)

**Don't use when:**
- ❌ Standard stages work fine
- ❌ Simple sequential workflow
- ❌ Adding unnecessary complexity

---

<!-- section_id: "297362b7-8ab7-418b-b362-a90f5f6c00f8" -->
## 🔧 Extension Pattern 2: Slot Directories

<!-- section_id: "41b78a67-a45b-44f2-82a8-d41878b29c75" -->
### What It Is

**Slots** are numbered directories that hold multiple **instances** of something.

<!-- section_id: "94bad968-b118-4ed1-ad29-82dfd40ceb05" -->
### Pattern

```
<N>.<XX>_<purpose>/
├── <instance_1>/
│   └── <N>.99_stages/
├── <instance_2>/
│   └── <N>.99_stages/
└── <instance_3>/
    └── <N>.99_stages/
```

<!-- section_id: "cbb07902-6b81-4ce0-839e-30858c3738ac" -->
### Example: Multiple Workflow Instances

```
2.04_workflows/                          # Slot directory
├── workflow_1/                          # Instance 1
│   ├── workflow_ds250_unit_setup_v1.md
│   └── 2.99_stages/                     # Execution stages for workflow 1
│       ├── stage_2.01_instructions/
│       └── ...
├── workflow_2/                          # Instance 2
│   ├── workflow_ds250_template_completion_v1.md
│   └── 2.99_stages/
└── workflow_3/                          # Instance 3
    ├── workflow_ds250_verification_v1.md
    └── 2.99_stages/
```

<!-- section_id: "7de1d3d1-9f29-4d41-a01b-e4eee346babe" -->
### Example: Version Management

```
2.05_versions/                           # Slot directory
├── v1.0/
│   ├── code/
│   └── 2.99_stages/                     # Release stages for v1.0
├── v1.1/
│   ├── code/
│   └── 2.99_stages/                     # Release stages for v1.1
└── v2.0/
    ├── code/
    └── 2.99_stages/                     # Release stages for v2.0
```

<!-- section_id: "b490a91c-7882-4681-8578-8d873c7a13be" -->
### When to Use Slots

**Use slot directories when:**
- ✅ You need **multiple instances** of the same type of thing
- ✅ Each instance has its own **lifecycle** (stages)
- ✅ Instances are **similar in structure** but different in content
- ✅ You want to **manage** multiple items in one place

**Examples:**
- Workflows (workflow_1, workflow_2, workflow_3)
- Experiments (experiment_1, experiment_2)
- Versions (v1.0, v1.1, v2.0)
- Sessions (session_1, session_2)
- Iterations (iteration_1, iteration_2)

---

<!-- section_id: "5f144bd3-7613-4888-8b35-152cf3c825ec" -->
## 🔧 Extension Pattern 3: Nested Stages

<!-- section_id: "9d693d9d-440d-4a59-bfa1-8b7d37be918d" -->
### What It Is

Having **multiple `<N>.99_stages/` directories** at different levels of your hierarchy.

<!-- section_id: "63ac016c-6d22-4342-bd08-1b8b69355af2" -->
### Pattern

```
layer_<N>_feature_<name>/
├── <N>.99_stages/                       # Feature-level stages
└── <N>.03_<custom_dir>/
    ├── <N>.99_stages/                   # Custom directory stages
    └── <instance_1>/
        └── <N>.99_stages/               # Instance-level stages
```

<!-- section_id: "0afdfbb4-13fa-4848-ac08-d7728456de71" -->
### Example: Three Levels of Stages

```
layer_2_feature_assignments/
├── 2.99_stages/                         # LEVEL 1: Feature lifecycle
│   ├── stage_2.01_instructions/         # Planning assignments feature
│   ├── stage_2.04_development/          # Developing workflows
│   └── stage_2.09_archives/             # Feature complete
├── 2.03_workflow_creation/
│   └── 2.99_stages/                     # LEVEL 2: Workflow development
│       ├── stage_2.01_instructions/     # Define workflow requirements
│       ├── stage_2.04_development/      # Build workflow
│       ├── stage_2.05_testing/          # Test workflow
│       └── stage_2.09_archives/         # Workflow validated
└── 2.04_workflows/
    └── workflow_1/
        └── 2.99_stages/                 # LEVEL 3: Workflow execution
            ├── stage_2.01_instructions/ # Workflow instructions
            ├── stage_2.04_development/  # Execute workflow
            ├── stage_2.05_testing/      # Verify results
            └── stage_2.09_archives/     # Execution complete
```

**Three Different Purposes:**
1. **Feature stages** - Overall feature lifecycle (planning → completion)
2. **Creation stages** - Developing workflows (design → validation)
3. **Execution stages** - Running workflows (setup → completion)

<!-- section_id: "0577b2d4-1e24-46fe-a53e-e83df0f59692" -->
### When to Use Nested Stages

**Use nested stages when:**
- ✅ Different parts of your hierarchy have **independent lifecycles**
- ✅ Custom directories represent **phases with their own workflows**
- ✅ Instances need **execution tracking**
- ✅ You need to track **progress at multiple levels**

---

<!-- section_id: "039411cf-b2a1-416f-bed2-5682bcd81dd8" -->
## 🎨 Extension Pattern 4: Hybrid Features/Components + Custom Directories

<!-- section_id: "8b755fa0-4dce-4dea-a33a-5a4dc344bfab" -->
### What It Is

Combining standard nesting (features/components) with custom directories.

<!-- section_id: "04f74ca6-c388-4bc8-8b17-36f040d1c757" -->
### Pattern

```
layer_<N>_feature_<name>/
├── <N>.00_ai_manager_system/
├── <N>.01_manager_handoff_documents/
├── <N>.02_sub_layers/
├── <N>.03_<custom_dir>/                 # Custom directory
├── <N>.04_<custom_dir>/                 # Custom directory
├── <N>.99_stages/
├── layer_<N+1>_features/                # Standard nesting
│   └── layer_<N+1>_feature_<subname>/
└── layer_<N+1>_components/              # Standard nesting
    └── layer_<N+1>_component_<compname>/
```

<!-- section_id: "d115ef75-9dcd-4238-b2e9-b1589fa3a88c" -->
### Example: Class with Assignments AND Topics

```
layer_2_feature_ds250_course/
├── 2.02_sub_layers/
├── 2.03_assignments_workflows/          # CUSTOM - Assignment management
│   ├── 2.03_workflow_creation/
│   ├── 2.04_workflows/
│   └── 2.05_results/
├── 2.04_coding_challenges/              # CUSTOM - Challenge management
│   ├── 2.03_workflow_creation/
│   ├── 2.04_workflows/
│   └── 2.05_results/
├── 2.99_stages/
└── layer_3_features/                    # STANDARD - Course topics
    ├── layer_3_feature_pandas/          # Topic 1
    │   └── layer_4_components/
    │       ├── layer_4_component_2024_09_15_class/
    │       └── layer_4_component_2024_09_17_class/
    ├── layer_3_feature_visualization/   # Topic 2
    └── layer_3_feature_databases/       # Topic 3
```

**Why This Works:**
- Custom directories (`.03`, `.04`) for **workflow management**
- Standard features/components for **learning content**
- Separation of **process** (workflows) from **content** (topics)

---

<!-- section_id: "e3397a96-d0f3-4722-88d6-37f3d64c4aad" -->
## 🧭 Decision Framework

<!-- section_id: "95783aea-f139-45df-9639-063942b34b86" -->
### Step 1: Start with Standard Structure

**Always start here:**
```
layer_<N>_<type>_<name>/
├── <N>.00_ai_manager_system/
├── <N>.01_manager_handoff_documents/
├── <N>.02_sub_layers/
└── <N>.99_stages/
```

**Ask:** Does this work for my needs?
- **YES** → Use standard structure with features/components nesting
- **NO** → Continue to Step 2

<!-- section_id: "ab720749-dcd4-4d92-b5af-3878c58327de" -->
### Step 2: Consider Standard Nesting First

**Add features/components:**
```
├── layer_<N+1>_features/       # For hierarchical topics/concepts
└── layer_<N+1>_components/     # For work artifacts
```

**Ask:** Can I organize my work using features and components?
- **YES** → Use standard nesting (most cases!)
- **NO** → Continue to Step 3

<!-- section_id: "dbde8d0f-7d08-4dfc-a908-39d0dcb42a2c" -->
### Step 3: Identify Your Specific Need

**What doesn't fit?**

| Need | Solution | Pattern |
|------|----------|---------|
| Distinct phases (creation → production) | Custom directories | Pattern 1 |
| Multiple instances (workflows, experiments) | Slot directories | Pattern 2 |
| Different lifecycles at each level | Nested stages | Pattern 3 |
| Mix of process and content | Hybrid approach | Pattern 4 |

<!-- section_id: "e7204a8d-0930-4eae-9f4f-da2b79dd4f50" -->
### Step 4: Implement Extension

**Choose your extension pattern:**
1. Add custom numbered directories (`.03-.98`)
2. Create slot directories for instances
3. Add nested stages where needed
4. Combine with standard features/components if helpful

---

<!-- section_id: "cd806b3f-13f2-409e-9108-33ab98d0e679" -->
## 📋 Real-World Examples

<!-- section_id: "a95886fb-eaca-4037-a60a-c136cac91983" -->
### Example 1: Applied Calculus (Standard + Minimal Extension)

**Use Case:** Class notes with Proactor AI + Excalidraw + BYUI Math

**Solution:** STANDARD framework works perfectly!

```
layer_2_feature_derivatives/              # Standard feature
└── layer_3_features/
    └── layer_3_feature_power_rule/       # Standard nesting
        └── layer_4_components/
            └── layer_4_component_2026_01_09_class/  # Standard component
                ├── 4.02_sub_layers/      # STANDARD
                │   └── sub_layer_4.01_visual_notes/
                │       └── excalidraw/   # Excalidraw work
                └── 4.99_stages/          # STANDARD
                    └── stage_4.05_testing/
                        └── hand_off_documents/
                            ├── proactor_lecture_2026_01_09.md
                            └── byui_math_problems_jan09.md
```

**Extensions used:** NONE - standard structure is perfect!

<!-- section_id: "4c73918c-7009-46bb-ac3d-703610a063d5" -->
### Example 2: PAC School DS250 (Full Extensions)

**Use Case:** Managing assignments with workflow creation, execution, and results

**Solution:** Custom directories + slots + nested stages

```
layer_2_feature_assignments/
├── 2.00_ai_manager_system/              # STANDARD
├── 2.01_manager_handoff_documents/      # STANDARD
├── 2.02_sub_layers/                     # STANDARD
├── 2.03_workflow_creation/              # EXTENSION: Custom directory
│   ├── 2.00_ai_manager_system/
│   ├── 2.01_manager_handoff_documents/
│   ├── 2.02_sub_layers/
│   └── 2.99_stages/                     # EXTENSION: Nested stages
├── 2.04_workflows/                      # EXTENSION: Custom directory + slots
│   ├── workflow_1/                      # EXTENSION: Slot instance
│   │   ├── workflow_ds250_unit_setup_v1.md
│   │   └── 2.99_stages/                 # EXTENSION: Nested stages
│   ├── workflow_2/
│   │   └── 2.99_stages/
│   └── workflow_3/
│       └── 2.99_stages/
├── 2.05_results/                        # EXTENSION: Custom directory
└── 2.99_stages/                         # STANDARD
```

**Extensions used:**
- ✅ Custom directories (`.03`, `.04`, `.05`)
- ✅ Slot directories (`workflow_1`, `workflow_2`, `workflow_3`)
- ✅ Nested stages (feature level, creation level, execution level)

<!-- section_id: "8b5107bf-129a-413c-b60c-0d809f4cc684" -->
### Example 3: Research Lab (Hybrid Approach)

**Use Case:** Research with experiments, papers, and topic organization

**Solution:** Hybrid (custom + features/components)

```
layer_2_feature_protein_research/
├── 2.02_sub_layers/
├── 2.03_experimental_pipeline/          # EXTENSION: Custom directory
│   ├── 2.03_design/
│   ├── 2.04_data_collection/
│   │   ├── experiment_1/                # EXTENSION: Slots
│   │   └── experiment_2/
│   ├── 2.05_analysis/
│   └── 2.06_publication/
├── 2.99_stages/
└── layer_3_features/                    # STANDARD: Features for topics
    ├── layer_3_feature_structural_analysis/
    ├── layer_3_feature_binding_affinity/
    └── layer_3_feature_mutation_effects/
        └── layer_4_components/          # STANDARD: Components for specific studies
            ├── layer_4_component_study_2024_01/
            └── layer_4_component_study_2024_03/
```

**Extensions used:**
- ✅ Custom directories for experimental pipeline
- ✅ Slot directories for experiments
- ✅ Standard features/components for research topics

---

<!-- section_id: "815b5e7a-1da0-4b8e-a5e7-3bc17179b447" -->
## ⚠️ Best Practices

<!-- section_id: "33a3deb3-1737-45dc-8a99-561766766acd" -->
### 1. Start Simple

**Always start with standard structure** and only add extensions when you have a clear need.

```
Start: layer_<N>_<type>_<name>/ with standard directories
Add: features/components nesting if needed
Extend: custom directories only if standard doesn't fit
```

<!-- section_id: "41812024-0098-4a13-bd4f-812b282f3722" -->
### 2. Document Your Extensions

**Create a README** in your project explaining:
- What custom directories you're using (`.03`, `.04`, etc.)
- Why you need them
- How they relate to each other
- Examples of what goes where

**Example README:**
```markdown
## Custom Directory Structure

This project extends the standard framework with:

- `2.03_workflow_creation/` - Developing AI workflows
- `2.04_workflows/` - Production-ready workflows (slots: workflow_1, workflow_2, ...)
- `2.05_results/` - Links to workflow outputs

See EXTENDING_THE_FRAMEWORK.md in universal context for pattern details.
```

<!-- section_id: "4c923695-dc5b-48c2-b210-f7fc829efee7" -->
### 3. Be Consistent

**Once you choose a pattern**, use it consistently:
- Same custom directory numbers across features
- Same slot naming conventions
- Same purposes for each custom directory

<!-- section_id: "562e30fc-a386-4720-a25f-5dd35748c6b3" -->
### 4. Maintain Standard Core

**Always keep the required directories:**
- `<N>.00_ai_manager_system/`
- `<N>.01_manager_handoff_documents/`
- `<N>.02_sub_layers/`
- `<N>.99_stages/`

**Never repurpose these** - they're the foundation of the system.

<!-- section_id: "d8b23bb3-dfcb-409f-9797-d5a4e0d6ff13" -->
### 5. Use Features/Components First

**Before adding custom directories**, ask:
- Can I model this as a feature?
- Can I model this as a component?
- Can I use deeper nesting?

**Most of the time, the answer is YES!**

---

<!-- section_id: "2c071ae6-a9f7-4d7d-8488-20282c0ab831" -->
## 🎯 Summary

<!-- section_id: "cd604d80-424d-4761-b8f2-3b2a3c5c2659" -->
### The Framework Supports:

| Pattern | Use Case | Complexity |
|---------|----------|------------|
| **Standard** | Most projects | ⭐ Simple |
| **Standard + Nesting** | Hierarchical content | ⭐⭐ Moderate |
| **Custom Directories** | Distinct phases | ⭐⭐⭐ Advanced |
| **Slot Directories** | Multiple instances | ⭐⭐⭐ Advanced |
| **Nested Stages** | Multi-level workflows | ⭐⭐⭐⭐ Expert |
| **Hybrid** | Complex projects | ⭐⭐⭐⭐⭐ Expert |

<!-- section_id: "c0e16df9-e1c7-4333-acff-b57c8fd84c78" -->
### Quick Decision Tree

```
Need organization?
├─ YES: Hierarchical topics/concepts?
│  ├─ YES: Use features/components → DONE ✅
│  └─ NO: Continue...
│      └─ Distinct phases?
│         ├─ YES: Custom directories → Pattern 1
│         └─ NO: Multiple instances?
│            ├─ YES: Slot directories → Pattern 2
│            └─ NO: Different lifecycles?
│               ├─ YES: Nested stages → Pattern 3
│               └─ NO: Reevaluate - might need standard after all
└─ NO: You probably don't need this guide!
```

<!-- section_id: "a7377845-8148-464c-ae08-60cd590f54bf" -->
### Remember

- **90% of projects** work with standard framework + features/components
- **8% of projects** need one simple extension (custom directories)
- **2% of projects** need complex extensions (multiple patterns)

**Start simple, extend only when necessary!**

---

<!-- section_id: "9366a731-b17b-4b6d-80d3-2a8497dc0d11" -->
## 📚 Related Documentation

- `FLEXIBLE_LAYERING_SYSTEM.md` - Standard framework (read this first!)
- `universal_init_prompt.md` - Complete system overview
- `UNIVERSAL_SYSTEM_EVALUATION.md` - Framework capabilities analysis

---

**Location:** `C:\Users\Dawson\dawson-workspace\code\0_layer_universal\0_context\layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers\EXTENDING_THE_FRAMEWORK.md`
**Last Updated:** 2026-01-09
**Version:** 2.0
