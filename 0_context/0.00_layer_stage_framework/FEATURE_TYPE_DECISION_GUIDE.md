# Feature Type Decision Guide

**Purpose:** Help you choose the right feature type when starting new work.

**Use this guide when:** Creating a new feature in any project.

**Last Updated:** 2026-01-09

---

## 🤔 Quick Decision

**Answer these questions:**

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

## 📚 Standard Feature (90% of use cases)

### Use When:
- ✅ Organizing topics, concepts, or learning material
- ✅ Hierarchical breakdown (topic → subtopic → examples)
- ✅ Sequential workflow fits (instructions → development → testing → completion)
- ✅ One-time or ad-hoc work

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

### Examples:
- **Applied Calculus:** Topics (derivatives, limits) with daily problem sets
- **Research:** Research areas with experiments and papers
- **Project Documentation:** Features with implementation details

### How to Create:
```bash
# Copy standard feature template
cp -r "<universal_context>/0.00_layer_stage_framework/2_feature_template" \
  "layer_<N>_feature_<topic_name>"
```

**Template Location:** `0.00_layer_stage_framework/2_feature_template/`

---

## 🔄 Workflow Feature (10% of use cases)

### Use When:
- ⚠️ You have a **repeatable process** to follow
- ⚠️ Process needs **development and refinement**
- ⚠️ You'll **execute process multiple times**
- ⚠️ You want **separate tracking** for creation vs execution

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

### Examples:
- **Assignment Workflows:** Create workflows for completing recurring assignments
- **Testing Procedures:** Develop and execute test workflows
- **Deployment Processes:** Build and run deployment workflows
- **Data Processing:** Create pipelines that run repeatedly

### How to Create:
```bash
# Use workflow feature script
bash "<universal_context>/0.00_layer_stage_framework/scripts/create_workflow_feature.sh" <layer> <name>
```

**Pattern Guide:** `0.00_layer_stage_framework/WORKFLOW_FEATURE_PATTERN.md`

---

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

## 🎓 Real-World Scenarios

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

## 🚀 Getting Started

### For Standard Feature:

1. **Copy template:**
```bash
cd your_project/0_context/0_context/layer_2_features/
cp -r "../../../../0_ai_context/0_context/0.00_layer_stage_framework/2_feature_template" \
  "layer_2_feature_<your_topic>"
```

2. **Customize:**
   - Update README with your topic
   - Add to features tracker
   - Start in stage 01 (instructions)

3. **Use nesting as needed:**
   - Add `layer_3_features/` for subtopics
   - Add `layer_3_components/` for specific work

### For Workflow Feature:

1. **Run script:**
```bash
cd your_project/0_context/0_context/layer_2_features/
bash "../../../../0_ai_context/0_context/0.00_layer_stage_framework/scripts/create_workflow_feature.sh" 2 <name>
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

## 💡 Pro Tips

### Starting a New Project?
1. **Start with standard features** for your main content
2. **Add workflow features later** if you identify repeated processes
3. **Don't over-engineer** - most projects only need standard features

### Not Sure Which to Use?
1. **Default to standard feature** - it's more flexible
2. **Switch to workflow feature** if you find yourself:
   - Following the exact same steps multiple times
   - Wanting to refine and document a process
   - Needing separate tracking for creation vs execution

### Both Can Coexist!
You can have both in the same project:
```
layer_2_features/
├── layer_2_feature_class_topics/         # Standard: Learning content
├── layer_2_feature_assignments/          # Workflow: Assignment completion
└── layer_2_feature_research_areas/       # Standard: Research topics
```

---

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

**Location:** `C:\Users\Dawson\dawson-workspace\code\0_ai_context\0_context\0.00_layer_stage_framework\FEATURE_TYPE_DECISION_GUIDE.md`
**Last Updated:** 2026-01-09
**Version:** 1.0
