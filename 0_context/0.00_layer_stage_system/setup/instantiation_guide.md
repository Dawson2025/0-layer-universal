# Instantiation Guide

**Purpose:** Step-by-step instructions for creating new entities in the Layer + Stage Framework.

**Last Updated:** 2026-01-15

---

## Entity Types Overview

| Entity Type | Description | Template Location |
|-------------|-------------|-------------------|
| **Project** | Top-level container (Layer 1) | `0.01_layer_stage_framework/1_project_template/` |
| **Sub-project** | Project nested under project (sub*1, sub*2, etc.) | `0.01_layer_stage_framework/2_sub_project_template/` |
| **Feature** | Distinct capability within a project | `0.01_layer_stage_framework/2_feature_template/` |
| **Sub-feature** | Feature nested under feature | `0.01_layer_stage_framework/2_feature_template/` (reused) |
| **Component** | Implementation unit within a feature | `0.01_layer_stage_framework/3_component_template/` |
| **Sub-component** | Component nested under component | `0.01_layer_stage_framework/3_component_template/` (reused) |
| **Sub-layer** | Content slot within any entity (N.01-N.12) | Manual creation |
| **Stage** | Workflow phase within any entity | Included in templates |

---

## Naming Conventions

### General Pattern
```
layer_<N>_<type>_<name>/
```

### Type Prefixes

| Entity | Naming Pattern | Example |
|--------|----------------|---------|
| Project | `<N>_layer_<name>/` (top-level repo) | `1_layer_school/` |
| Sub-project | `layer_<N>_sub*<X>_project_<name>/` | `layer_2_sub*1_project_classes/` |
| Sub*2-project | `layer_<N>_sub*<X>_project_<name>/` | `layer_3_sub*2_project_computer_science/` |
| Feature | `layer_<N>_feature_<name>/` | `layer_2_feature_authentication/` |
| Sub-feature | `layer_<N>_sub_feature_<name>/` | `layer_3_sub_feature_oauth/` |
| Component | `layer_<N>_component_<name>/` | `layer_3_component_login_form/` |
| Sub-component | `layer_<N>_sub_component_<name>/` | `layer_4_sub_component_validation/` |

### The "sub" Prefix Rule

**Use "sub" prefix ONLY for same-type nesting:**
- Project containing project → `sub*X_project`
- Feature containing feature → `sub_feature`
- Component containing component → `sub_component`

**Do NOT use "sub" for different-type nesting:**
- Project containing feature → just `feature` (not sub_feature)
- Feature containing component → just `component` (not sub_component)

### Sub*X Numbering for Projects

When projects nest inside projects, track the nesting depth:
- `sub*1_project` = 1 level deep (project inside project)
- `sub*2_project` = 2 levels deep (project inside project inside project)
- `sub*N_project` = N levels deep

---

## Quick Reference: Where to Create What

```
1_layer_school/                              # Project (L1)
├── layer_1/                                 # L1 internals
└── layer_2/                                 # L2 content
    ├── layer_2_sub*1_projects/              # Sub-projects go here
    │   └── layer_2_sub*1_project_classes/   # A sub-project (L2)
    │       ├── layer_2/                     # Its L2 internals
    │       └── layer_3/                     # Its L3 content
    │           ├── layer_3_sub*2_projects/  # Sub*2-projects
    │           ├── layer_3_features/        # Features
    │           └── layer_3_components/      # Components
    ├── layer_2_features/                    # Features go here
    │   └── layer_2_feature_auth/            # A feature (L2)
    │       ├── layer_2/                     # Its L2 internals
    │       └── layer_3/                     # Its L3 content
    │           ├── layer_3_sub_features/    # Sub-features
    │           └── layer_3_components/      # Components
    └── layer_2_components/                  # Components go here
        └── layer_2_component_shared_ui/     # A component (L2)
            ├── layer_2/                     # Its L2 internals
            └── layer_3/                     # Its L3 content
                └── layer_3_sub_components/  # Sub-components
```

---

## Instantiation Procedures

### 1. Creating a Project

**When:** Starting a new top-level project repository

**Steps:**

1. **Create repository:**
   ```bash
   mkdir <N>_layer_<project_name>
   cd <N>_layer_<project_name>
   git init
   ```

2. **Copy template:**
   ```bash
   cp -r <path_to>/0.01_layer_stage_framework/1_project_template/* .
   ```

3. **Rename layer folders to match your layer number:**
   ```bash
   mv layer_N layer_1
   mv layer_N+1 layer_2
   # Rename all internal folders from layer_N_* to layer_1_*
   ```

4. **Create the three nested content folders:**
   ```bash
   mkdir -p layer_2/layer_2_sub*1_projects
   mkdir -p layer_2/layer_2_features
   mkdir -p layer_2/layer_2_components
   ```

5. **Initialize status file:**
   ```bash
   cp layer_1/layer_1_99_stages/status_template.json layer_1/layer_1_99_stages/status_1.json
   ```

6. **Populate sub_layers with project-specific content**

7. **Commit:**
   ```bash
   git add -A && git commit -m "Initialize project structure"
   ```

**See:** `project_creation_checklist.md` for detailed checklist

---

### 2. Creating a Sub-Project

**When:** A project needs to contain another project (same-type nesting)

**Location:** `<parent>/layer_N+1/layer_N+1_sub*X_projects/`

**Steps:**

1. **Navigate to parent's sub-projects folder:**
   ```bash
   cd <parent_project>/layer_<N+1>/layer_<N+1>_sub*<X>_projects/
   ```

2. **Copy sub-project template:**
   ```bash
   cp -r <path_to>/0.01_layer_stage_framework/2_sub_project_template/ layer_<N+1>_sub*<X>_project_<name>/
   ```

3. **Rename internal layer folders:**
   - Rename `layer_N/` → `layer_<N+1>/`
   - Rename `layer_N+1/` → `layer_<N+2>/`
   - Rename all `layer_N_*` to `layer_<N+1>_*`

4. **Create the three nested content folders:**
   ```bash
   mkdir -p layer_<N+2>/layer_<N+2>_sub*<X+1>_projects
   mkdir -p layer_<N+2>/layer_<N+2>_features
   mkdir -p layer_<N+2>/layer_<N+2>_components
   ```

5. **Initialize status file**

6. **If using git submodules:**
   ```bash
   cd ..  # Back to parent
   git submodule add <remote_url> layer_<N+1>_sub*<X>_projects/layer_<N+1>_sub*<X>_project_<name>
   ```

**Example:** Creating `layer_3_sub*2_project_computer_science` inside `layer_2_sub*1_project_classes`:
```bash
cd layer_2_sub*1_project_classes/layer_3/layer_3_sub*2_projects/
cp -r .../2_sub_project_template/ layer_3_sub*2_project_computer_science/
# Rename internals to layer_3/layer_4
```

---

### 3. Creating a Feature

**When:** Adding a distinct capability to a project or sub-project

**Location:** `<parent>/layer_N+1/layer_N+1_features/`

**Steps:**

1. **Navigate to parent's features folder:**
   ```bash
   cd <parent>/layer_<N+1>/layer_<N+1>_features/
   ```

2. **Copy feature template:**
   ```bash
   cp -r <path_to>/0.01_layer_stage_framework/2_feature_template/ layer_<N+1>_feature_<name>/
   ```

3. **Rename internal layer folders:**
   - Rename `layer_N/` → `layer_<N+1>/`
   - Rename `layer_N+1/` → `layer_<N+2>/`
   - Rename all `layer_N_*` to `layer_<N+1>_*`

4. **Create nested content folders:**
   ```bash
   mkdir -p layer_<N+2>/layer_<N+2>_sub_features
   mkdir -p layer_<N+2>/layer_<N+2>_components
   ```

5. **Initialize status file**

6. **Populate feature-specific sub_layers**

**Example:** Creating `layer_2_feature_authentication` in a project:
```bash
cd my_project/layer_2/layer_2_features/
cp -r .../2_feature_template/ layer_2_feature_authentication/
# Rename internals to layer_2/layer_3
```

---

### 4. Creating a Sub-Feature

**When:** A feature needs to contain another feature (same-type nesting)

**Location:** `<parent_feature>/layer_N+1/layer_N+1_sub_features/`

**Steps:**

1. **Navigate to parent feature's sub_features folder:**
   ```bash
   cd <parent_feature>/layer_<N+1>/layer_<N+1>_sub_features/
   ```

2. **Copy feature template (reused for sub-features):**
   ```bash
   cp -r <path_to>/0.01_layer_stage_framework/2_feature_template/ layer_<N+1>_sub_feature_<name>/
   ```

3. **Rename internal folders to correct layer numbers**

4. **Create nested content folders:**
   ```bash
   mkdir -p layer_<N+2>/layer_<N+2>_sub_features  # For deeper nesting if needed
   mkdir -p layer_<N+2>/layer_<N+2>_components
   ```

5. **Initialize status file**

**Example:** Creating `layer_3_sub_feature_oauth` inside `layer_2_feature_authentication`:
```bash
cd layer_2_feature_authentication/layer_3/layer_3_sub_features/
cp -r .../2_feature_template/ layer_3_sub_feature_oauth/
# Rename internals to layer_3/layer_4
```

---

### 5. Creating a Component

**When:** Adding an implementation unit to a feature

**Location:** `<parent>/layer_N+1/layer_N+1_components/`

**Steps:**

1. **Navigate to parent's components folder:**
   ```bash
   cd <parent>/layer_<N+1>/layer_<N+1>_components/
   ```

2. **Copy component template:**
   ```bash
   cp -r <path_to>/0.01_layer_stage_framework/3_component_template/ layer_<N+1>_component_<name>/
   ```

3. **Rename internal layer folders**

4. **Create nested content folder (for sub-components if needed):**
   ```bash
   mkdir -p layer_<N+2>/layer_<N+2>_sub_components
   ```

5. **Initialize status file**

**Example:** Creating `layer_3_component_login_form` inside `layer_2_feature_authentication`:
```bash
cd layer_2_feature_authentication/layer_3/layer_3_components/
cp -r .../3_component_template/ layer_3_component_login_form/
# Rename internals to layer_3/layer_4
```

---

### 6. Creating a Sub-Component

**When:** A component needs to contain another component (same-type nesting)

**Location:** `<parent_component>/layer_N+1/layer_N+1_sub_components/`

**Steps:**

1. **Navigate to parent component's sub_components folder:**
   ```bash
   cd <parent_component>/layer_<N+1>/layer_<N+1>_sub_components/
   ```

2. **Copy component template (reused for sub-components):**
   ```bash
   cp -r <path_to>/0.01_layer_stage_framework/3_component_template/ layer_<N+1>_sub_component_<name>/
   ```

3. **Rename internal folders to correct layer numbers**

4. **Create nested content folder:**
   ```bash
   mkdir -p layer_<N+2>/layer_<N+2>_sub_components
   ```

5. **Initialize status file**

---

### 7. Adding a Sub-Layer

**When:** Adding a new content slot (N.01-N.12) to any entity

**Location:** `<entity>/layer_N/layer_N_02_sub_layers/`

**Steps:**

1. **Navigate to entity's sub_layers folder:**
   ```bash
   cd <entity>/layer_<N>/layer_<N>_02_sub_layers/
   ```

2. **Create the sub_layer folder:**
   ```bash
   mkdir sub_layer_<N>.<XX>_<name>
   ```

   Where `<XX>` is 01-12 (standard slots) or 13+ (custom slots)

3. **Add standard content structure:**
   ```bash
   cd sub_layer_<N>.<XX>_<name>
   mkdir -p 0_instruction_docs
   mkdir -p 1_status_progress_docs
   mkdir -p 2_testing_docs
   mkdir -p 3_archive_docs
   touch README.md
   ```

4. **Or minimal structure:**
   ```bash
   touch README.md
   touch .gitkeep
   ```

**Standard Sub-Layer Numbers:**
| Number | Purpose |
|--------|---------|
| N.01 | Basic prompts |
| N.02 | SE knowledge |
| N.03 | Principles |
| N.04 | Rules |
| N.05 | OS setup |
| N.06 | Coding app setup |
| N.07 | Apps/browsers/extensions |
| N.08 | AI apps/tools |
| N.09 | MCP servers and tools |
| N.10 | AI models |
| N.11 | Tools |
| N.12 | Agent setup |

---

### 8. Working with Stages

**Location:** `<entity>/layer_N/layer_N_99_stages/`

**Standard Stages:**
| Stage | Name | Purpose |
|-------|------|---------|
| N.00 | request_gathering | Clarify requirements |
| N.01 | instructions | Define constraints |
| N.02 | planning | Break into subtasks |
| N.03 | design | Architecture decisions |
| N.04 | development | Implementation |
| N.05 | testing | Verification |
| N.06 | criticism | Review |
| N.07 | fixing | Corrections |
| N.08 | archives | Completion |

**Each stage folder contains:**
```
stage_N.XX_<name>/
├── hand_off_documents/    # Briefs, decisions, outputs
│   └── .gitkeep
└── ai_agent_system/       # Agent configs for this stage
    └── .gitkeep
```

**Status tracking:**
- Update `status_N.json` when moving between stages
- Format:
  ```json
  {
    "current_stage": "N.04_development",
    "stages": {
      "N.01_instructions": { "state": "done" },
      "N.04_development": { "state": "in_progress" }
    }
  }
  ```

---

## Decision Guide: Which Entity Type?

| Question | If Yes → |
|----------|----------|
| Is it a standalone project with its own repo? | **Project** |
| Is it a project inside another project? | **Sub-project** (sub*X) |
| Is it a distinct capability/feature? | **Feature** |
| Is it a feature inside another feature? | **Sub-feature** |
| Is it an implementation unit/artifact? | **Component** |
| Is it a component inside another component? | **Sub-component** |

**Rule of thumb:**
- Projects = organizational containers (classes, semesters, major initiatives)
- Features = capabilities or topics (authentication, data-visualization, chapter-1)
- Components = concrete implementations (login-form, bar-chart, quiz-1)

---

## Common Patterns

### Pattern A: School/Classes Structure
```
1_layer_school/                           # Project
└── layer_2/
    └── layer_2_sub*1_projects/
        └── layer_2_sub*1_project_classes/  # Sub-project
            └── layer_3/
                └── layer_3_sub*2_projects/
                    └── layer_3_sub*2_project_cs101/  # Sub*2-project
                        └── layer_4/
                            ├── layer_4_features/
                            │   └── layer_4_feature_week1/  # Feature
                            └── layer_4_components/
                                └── layer_4_component_hw1/  # Component
```

### Pattern B: Software Project Structure
```
1_layer_webapp/                           # Project
└── layer_2/
    ├── layer_2_features/
    │   ├── layer_2_feature_auth/         # Feature
    │   │   └── layer_3/
    │   │       ├── layer_3_sub_features/
    │   │       │   └── layer_3_sub_feature_oauth/  # Sub-feature
    │   │       └── layer_3_components/
    │   │           └── layer_3_component_login/    # Component
    │   └── layer_2_feature_dashboard/
    └── layer_2_components/
        └── layer_2_component_shared_ui/  # Shared component
```

---

## Related Documents

- `project_creation_checklist.md` - Detailed project creation checklist
- `../changes/restructuring_migration_protocol.md` - When restructuring existing entities
- `../../0.01_layer_stage_framework/README.md` - Framework overview
- `../../0.01_layer_stage_framework/FLEXIBLE_LAYERING_SYSTEM.md` - Layer system details
