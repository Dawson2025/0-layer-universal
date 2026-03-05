---
resource_id: "18b3b73f-3e08-4780-bf65-fc5b9c82076a"
resource_type: "knowledge"
resource_name: "FEATURE_TYPE_DECISION_GUIDE"
---
# Feature Type Decision Guide

**Purpose:** Help you choose the right feature type when starting new work.

**Use this guide when:** Creating a new feature in any project.

**Last Updated:** 2026-01-09

---

<!-- section_id: "ff865437-0ee0-4890-8fa0-e12d9df4f38d" -->
## 🤔 Quick Decision

**Answer these questions:**

<!-- section_id: "b427cbf5-7973-4b71-9837-a31ecddbcea1" -->
### Question 1: What are you organizing?

**A) Topics, concepts, or learning material**
→ Use **Standard Feature** (most common)
→ Examples: Class topics, research areas, project components

**B) Repeatable processes or workflows**
→ Use **Workflow Feature** (special case)
→ Examples: Assignment workflows, testing procedures, deployment processes

**C) Time-based activities**
→ Use **Standard Feature with date-tagged components**
→ Examples: Daily classwork, weekly reports, monthly reviews

---

<!-- section_id: "9e46ebee-e6f6-4315-aaa5-24507bb17785" -->
## 📚 Standard Feature (90% of use cases)

<!-- section_id: "0c10e9c6-4765-4bb9-9ea5-3c990789764b" -->
### Use When:
- ✅ Organizing topics, concepts, or learning material
- ✅ Hierarchical breakdown (topic → subtopic → examples)
- ✅ Sequential workflow fits (instructions → development → testing → completion)
- ✅ One-time or ad-hoc work

<!-- section_id: "eed7305e-15fd-4a7b-9c58-07496fd2b29d" -->
### Structure:
```
layer_<N>_feature_<topic_name>/
├── <N>.00_ai_manager_system/
├── <N>.01_manager_handoff_documents/
├── <N>.02_sub_layers/
├── <N>.99_stages/                    # Single workflow
├── layer_<N+1>_features/             # Sub-topics
└── layer_<N+1>_components/           # Specific work items
```

<!-- section_id: "f9b9f38d-150e-4edf-ab92-ee200e2db78a" -->
### Examples:
- **Applied Calculus:** Topics (derivatives, limits) with daily problem sets
- **Research:** Research areas with experiments and papers
- **Project Documentation:** Features with implementation details

<!-- section_id: "46bae0c8-6dfa-46fe-9d21-c04902c84659" -->
### How to Create:
```bash
# Copy standard feature template
cp -r "<universal_context>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template" \
  "layer_<N>_feature_<topic_name>"
```

**Template Location:** `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/`

---

<!-- section_id: "54faad5a-cd6e-4888-b696-4dab80847ace" -->
## 🔄 Workflow Feature (10% of use cases)

<!-- section_id: "40d6f222-fea2-444b-88b7-031efc5884fe" -->
### Use When:
- ⚠️ You have a **repeatable process** to follow
- ⚠️ Process needs **development and refinement**
- ⚠️ You'll **execute process multiple times**
- ⚠️ You want **separate tracking** for creation vs execution

<!-- section_id: "b562565b-7d8f-4918-81fa-c8dc1e49f091" -->
### Structure:
```
layer_<N>_feature_<workflow_name>/
├── <N>.00_ai_manager_system/
├── <N>.01_manager_handoff_documents/
├── <N>.02_sub_layers/
├── <N>.03_workflow_creation/         # PHASE 1: Develop
│   └── <N>.99_stages/
├── <N>.04_workflows/                 # PHASE 2: Execute
│   └── workflow_1/
│       └── <N>.99_stages/
├── <N>.05_results/                   # PHASE 3: Track
└── <N>.99_stages/                    # Optional feature-level
```

<!-- section_id: "a23338bc-c485-4c7b-a2a8-3ad9a7dc1ca0" -->
### Examples:
- **Assignment Workflows:** Create workflows for completing recurring assignments
- **Testing Procedures:** Develop and execute test workflows
- **Deployment Processes:** Build and run deployment workflows
- **Data Processing:** Create pipelines that run repeatedly

<!-- section_id: "98b6129f-d1e8-4161-8af3-a3ba17213e33" -->
### How to Create:
```bash
# Use workflow feature script
bash "<universal_context>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/scripts/create_workflow_feature.sh" <layer> <name>
```

**Pattern Guide:** `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/WORKFLOW_FEATURE_PATTERN.md`

---

<!-- section_id: "205d5fc7-6939-45b7-8271-5e7cf8f496a5" -->
## 🎯 Decision Tree

```
Creating a new feature?
│
├─ Is it a repeatable process you'll execute many times?
│  │
│  ├─ YES: Do you need to develop/refine the process first?
│  │  │
│  │  ├─ YES: Use WORKFLOW FEATURE
│  │  │      Examples:
│  │  │      - Assignment completion workflow
│  │  │      - Quiz workflow
│  │  │      - Deployment process
│  │  │      - Testing procedure
│  │  │
│  │  └─ NO: Use STANDARD FEATURE with well-defined stages
│  │         Just follow the process in development stage
│  │
│  └─ NO: Continue...
│     │
│     └─ Is it hierarchical content (topics, concepts)?
│        │
│        ├─ YES: Use STANDARD FEATURE
│        │      Examples:
│        │      - Class topics (math, CS)
│        │      - Research areas
│        │      - Documentation sections
│        │
│        └─ NO: Is it time-based work (daily, weekly)?
│           │
│           ├─ YES: Use STANDARD FEATURE with date-tagged components
│           │      Examples:
│           │      - Daily class notes
│           │      - Weekly reports
│           │      - Monthly reviews
│           │
│           └─ NO: Still use STANDARD FEATURE
│                  - Most flexible option
│                  - Can adapt as needed
```

---

<!-- section_id: "dde497ac-1a2a-4bcc-8ecb-cdcde744dbf9" -->
## 📋 Comparison Matrix

| Aspect | Standard Feature | Workflow Feature |
|--------|------------------|------------------|
| **Primary Use** | Content/Topics | Processes |
| **Reusability** | Low to moderate | High |
| **Setup Complexity** | Simple ⭐ | Moderate ⭐⭐ |
| **Lifecycle** | Linear (instructions → archives) | Cyclical (develop → execute → track) |
| **Stages** | Single `<N>.99_stages/` | Multiple nested stages |
| **Best For** | Learning, research, projects | Automation, repeated tasks |
| **Maintenance** | Low | Moderate |
| **Value Over Time** | Diminishing | Increasing (more executions) |

---

<!-- section_id: "a0937473-cb2d-41df-858c-46aa9c73c64a" -->
## 🎓 Real-World Scenarios

<!-- section_id: "459f2052-7193-456c-951f-6f30b8f65c02" -->
### Scenario 1: Applied Calculus Class
**What:** Organizing class notes, problems, and learning materials
**Type:** ✅ **Standard Feature**
**Why:** Hierarchical topics (derivatives → power rule → problems), one-time learning, sequential stages

**Structure:**
```
layer_2_feature_derivatives/              # Standard
└── layer_3_feature_power_rule/           # Standard nesting
    └── layer_4_component_2026_01_09_class/    # Date-tagged component
```

<!-- section_id: "596ff40f-08b1-4be5-b3fd-5d39b7dcc8f3" -->
### Scenario 2: DS250 Assignments
**What:** Completing weekly assignments with same structure each time
**Type:** ✅ **Workflow Feature**
**Why:** Repeatable process, needs development/refinement, execute 10+ times per semester

**Structure:**
```
layer_2_feature_assignments/              # Workflow feature
├── 2.03_workflow_creation/               # Develop the workflow
├── 2.04_workflows/                       # Execute for each assignment
│   ├── workflow_unit_1/
│   ├── workflow_unit_2/
│   └── ...
└── 2.05_results/                         # Track completed assignments
```

<!-- section_id: "91282ad4-62ee-403d-b74b-c08d8f9b38d8" -->
### Scenario 3: Research Experiments
**What:** Running similar experiments with data collection and analysis
**Type:** ⚠️ **Depends on your needs**

**Option A: Standard Feature** (if experiments are exploratory)
```
layer_2_feature_protein_study/
└── layer_3_components/
    ├── layer_3_component_experiment_1/
    ├── layer_3_component_experiment_2/
    └── layer_3_component_experiment_3/
```

**Option B: Workflow Feature** (if you have a standard experimental protocol)
```
layer_2_feature_protein_study/
├── 2.03_workflow_creation/               # Develop protocol
├── 2.04_workflows/
│   └── workflow_standard_protocol_v1/
│       └── 2.99_stages/
└── 2.05_results/
    ├── experiment_1_results/
    └── experiment_2_results/
```

<!-- section_id: "46b27557-259d-41be-90f6-1f74834a7d68" -->
### Scenario 4: Blog Posts
**What:** Writing blog posts regularly
**Type:** ✅ **Standard Feature with components**
**Why:** Similar structure but each post is unique (not following exact workflow)

**Structure:**
```
layer_2_feature_blog/
└── layer_3_components/
    ├── layer_3_component_2026_01_post_calculus/
    ├── layer_3_component_2026_02_post_ai/
    └── layer_3_component_2026_03_post_python/
```

---

<!-- section_id: "37568677-ae8a-4657-af6d-88bda844453a" -->
## 🚀 Getting Started

<!-- section_id: "4fc446cd-31b4-43a4-8672-9b81f6f2c3dd" -->
### For Standard Feature:

1. **Copy template:**
```bash
cd your_project/0_context/0_context/layer_2_features/
cp -r "../../../../0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template" \
  "layer_2_feature_<your_topic>"
```

2. **Customize:**
   - Update README with your topic
   - Add to features tracker
   - Start in stage 01 (instructions)

3. **Use nesting as needed:**
   - Add `layer_3_features/` for subtopics
   - Add `layer_3_components/` for specific work

<!-- section_id: "ba844a20-9b51-40df-8494-847d51b5186e" -->
### For Workflow Feature:

1. **Run script:**
```bash
cd your_project/0_context/0_context/layer_2_features/
bash "../../../../0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/scripts/create_workflow_feature.sh" 2 <name>
```

2. **Develop workflow:**
   - Work in `.03_workflow_creation/`
   - Progress through development stages
   - Document the process

3. **Execute workflow:**
   - Move validated workflow to `.04_workflows/workflow_1/`
   - Execute and track in stages
   - Link results in `.05_results/`

---

<!-- section_id: "bc3ba4b0-a971-4dc5-ad0d-4cd064155258" -->
## 💡 Pro Tips

<!-- section_id: "023ff242-437e-487f-8d49-ee3159ef0723" -->
### Starting a New Project?
1. **Start with standard features** for your main content
2. **Add workflow features later** if you identify repeated processes
3. **Don't over-engineer** - most projects only need standard features

<!-- section_id: "a41351e5-1052-4512-9fd1-ea077cf04628" -->
### Not Sure Which to Use?
1. **Default to standard feature** - it's more flexible
2. **Switch to workflow feature** if you find yourself:
   - Following the exact same steps multiple times
   - Wanting to refine and document a process
   - Needing separate tracking for creation vs execution

<!-- section_id: "307f2040-68eb-4915-99b0-69a44263b419" -->
### Both Can Coexist!
You can have both in the same project:
```
layer_2_features/
├── layer_2_feature_class_topics/         # Standard: Learning content
├── layer_2_feature_assignments/          # Workflow: Assignment completion
└── layer_2_feature_research_areas/       # Standard: Research topics
```

---

<!-- section_id: "647a3e78-f3d5-474f-b1f4-4a55bb17dad3" -->
## 📚 Documentation References

**Standard Features:**
- `FLEXIBLE_LAYERING_SYSTEM.md` - Complete standard framework
- `2_feature_template/` - Template to copy
- Applied Calculus project - Example usage

**Workflow Features:**
- `WORKFLOW_FEATURE_PATTERN.md` - Complete workflow pattern
- `EXTENDING_THE_FRAMEWORK.md` - Extension patterns
- PAC School DS250 project - Example usage

**General:**
- `universal_init_prompt.md` - System overview
- `FEATURE_TYPE_DECISION_GUIDE.md` - This file

---

**Location:** `C:\Users\Dawson\dawson-workspace\code\0_layer_universal\0_context\layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers\FEATURE_TYPE_DECISION_GUIDE.md`
**Last Updated:** 2026-01-09
**Version:** 1.0
