---
resource_id: "a2ce2ed1-35f2-44c2-ac51-75ac87089b66"
resource_type: "document"
resource_name: "FEATURE_TYPE_DECISION_GUIDE"
---
# Feature Type Decision Guide

**Purpose:** Help you choose the right feature type when starting new work.

**Use this guide when:** Creating a new feature in any project.

**Last Updated:** 2026-01-09

---

<!-- section_id: "4b236738-77db-49eb-bb5c-20c7ce1daad9" -->
## 🤔 Quick Decision

**Answer these questions:**

<!-- section_id: "398b7933-bdab-43c6-833a-f8a7f7f55a70" -->
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

<!-- section_id: "e6360a0c-6ffe-4b72-98ed-81b958d1715b" -->
## 📚 Standard Feature (90% of use cases)

<!-- section_id: "c2d1cf58-ee96-457e-b865-68899176922c" -->
### Use When:
- ✅ Organizing topics, concepts, or learning material
- ✅ Hierarchical breakdown (topic → subtopic → examples)
- ✅ Sequential workflow fits (instructions → development → testing → completion)
- ✅ One-time or ad-hoc work

<!-- section_id: "e1c4fdb3-1caa-426f-b5d0-f8ed6173f04f" -->
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

<!-- section_id: "bffa1895-1adf-4b13-aeb3-1c628f2eaee3" -->
### Examples:
- **Applied Calculus:** Topics (derivatives, limits) with daily problem sets
- **Research:** Research areas with experiments and papers
- **Project Documentation:** Features with implementation details

<!-- section_id: "b8f2c590-9eea-449a-9633-39aef32793ce" -->
### How to Create:
```bash
# Copy standard feature template
cp -r "<universal_context>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template" \
  "layer_<N>_feature_<topic_name>"
```

**Template Location:** `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/`

---

<!-- section_id: "88756eed-0a30-4c33-9a1f-8594c9d72f05" -->
## 🔄 Workflow Feature (10% of use cases)

<!-- section_id: "439da97f-99a7-4510-b51b-57f75091ff9d" -->
### Use When:
- ⚠️ You have a **repeatable process** to follow
- ⚠️ Process needs **development and refinement**
- ⚠️ You'll **execute process multiple times**
- ⚠️ You want **separate tracking** for creation vs execution

<!-- section_id: "9a5fc26a-ac9b-47ea-b4c6-b733244f7394" -->
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

<!-- section_id: "b7b07a40-6d52-46f6-9744-b931324695da" -->
### Examples:
- **Assignment Workflows:** Create workflows for completing recurring assignments
- **Testing Procedures:** Develop and execute test workflows
- **Deployment Processes:** Build and run deployment workflows
- **Data Processing:** Create pipelines that run repeatedly

<!-- section_id: "0d2a8af0-35d5-4137-8718-e15bab10ba88" -->
### How to Create:
```bash
# Use workflow feature script
bash "<universal_context>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/scripts/create_workflow_feature.sh" <layer> <name>
```

**Pattern Guide:** `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/WORKFLOW_FEATURE_PATTERN.md`

---

<!-- section_id: "4a05e04d-4594-4689-b880-952d61ad68dc" -->
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

<!-- section_id: "5a880675-bd2d-408d-aebe-e3083c15d736" -->
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

<!-- section_id: "1a784fab-7106-4ab6-9509-80246d11b4f6" -->
## 🎓 Real-World Scenarios

<!-- section_id: "1b7c7708-fcb7-4c90-ac91-7813bb3c90d3" -->
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

<!-- section_id: "5b487275-e9f4-4240-ac65-7fab011b9594" -->
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

<!-- section_id: "63470ac1-1124-4a15-b471-37efaeb55485" -->
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

<!-- section_id: "3ea04451-42f1-4a0c-8f5b-b403e5e62e79" -->
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

<!-- section_id: "91a1a571-83ca-44c3-915f-540b3f5111ae" -->
## 🚀 Getting Started

<!-- section_id: "ce6df1a4-c8de-47de-83a0-26a2dcc37bf0" -->
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

<!-- section_id: "6ff69ca4-c513-46d1-ae2d-89c96f210ace" -->
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

<!-- section_id: "04db834a-556d-497a-8a59-5dce3e6e7a52" -->
## 💡 Pro Tips

<!-- section_id: "dcb509b7-761d-46bd-bf55-960a0f5ad0c9" -->
### Starting a New Project?
1. **Start with standard features** for your main content
2. **Add workflow features later** if you identify repeated processes
3. **Don't over-engineer** - most projects only need standard features

<!-- section_id: "d5758131-609e-4628-9be2-9b8d2e5f331f" -->
### Not Sure Which to Use?
1. **Default to standard feature** - it's more flexible
2. **Switch to workflow feature** if you find yourself:
   - Following the exact same steps multiple times
   - Wanting to refine and document a process
   - Needing separate tracking for creation vs execution

<!-- section_id: "7286f16f-8c8e-4f75-82f4-a06b0d951e68" -->
### Both Can Coexist!
You can have both in the same project:
```
layer_2_features/
├── layer_2_feature_class_topics/         # Standard: Learning content
├── layer_2_feature_assignments/          # Workflow: Assignment completion
└── layer_2_feature_research_areas/       # Standard: Research topics
```

---

<!-- section_id: "6d34e348-bb72-4d83-bd27-a19cd9ee136b" -->
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
