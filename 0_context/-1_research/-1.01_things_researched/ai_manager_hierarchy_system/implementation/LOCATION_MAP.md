# AI Manager Hierarchy System - Location Map

**Purpose**: Quick reference for finding specific types of documentation
**Use**: "Where do I find X?" lookup guide

---

## Quick Lookup by Need

### "I need to understand the hierarchy"
→ Start here: `/code/0_ai_context/0_context/SYSTEM_OVERVIEW.md`
→ Complete guide: `/code/0_ai_context/0_context/USAGE_GUIDE.md`
→ Quick start: `layer_0_universal/.../HIERARCHY_QUICK_START.md`

### "I need the normative specifications"
→ Overview: `-1_research/.../ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`
→ All specs: `-1_research/.../ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/`
  - `architecture.md`
  - `os_and_quartets.md`
  - `framework_orchestration.md`
  - `cli_recursion_syntax.md`
  - `observability_and_logging.md`
  - `safety_and_governance.md`
  - `production_deployment.md`

### "I want to adopt this in my project"
→ Rollout plan: `/home/dawson/.cursor/plans/ai_manager_hierarchy_rollout_plan.md`
→ Adoption checklist: `layer_0_universal/.../HIERARCHY_ADOPTION_CHECKLIST.md`
→ Migration guide: `layer_0_universal/.../MIGRATION_GUIDE.md`
→ Quick start: `layer_0_universal/.../HIERARCHY_QUICK_START.md`

### "I need OS-specific context for my tool"
→ Layer 0: `layer_0_universal/0.99_stages/stage_0.01_instructions/ai_agent_system/os/{wsl|linux_ubuntu}/`
→ Layer 1: `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/{wsl|linux_ubuntu}/`
→ Layer 2: `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/{wsl|linux_ubuntu}/`
→ Layer 3: `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/{wsl|linux_ubuntu}/`

Files in each: `CLAUDE.md` (managers), `AGENTS.md` (workers), `GEMINI.md` (planning)

### "I need to understand manager/worker patterns"
→ Layer 0: `layer_0_universal/0.00_ai_manager_system/README.md`
→ Layer 1: `layer_1_project/1.00_ai_manager_system/README.md`
→ Layer 2: `layer_2_features/2.00_ai_manager_system/README.md`
→ Layer 3: `layer_3_components/3.00_ai_manager_system/README.md`

### "I need the handoff schema"
→ Canonical schema: `layer_0_universal/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
→ Usage examples: In schema doc + manager system READMEs

### "I need framework orchestration patterns"
→ Overview: `sub_layer_0.13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`
→ Normative spec: `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

### "I need CLI recursion examples"
→ Adapted syntax: `sub_layer_0.13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
→ Normative spec: `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/cli_recursion_syntax.md`

### "I need observability guidance"
→ Protocol: `sub_layer_0.13_universal_protocols/observability/README.md`
→ Normative spec: `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`

### "I need safety/governance rules"
→ Rules: `sub_layer_0.04_universal_rules/safety_governance.md`
→ Normative spec: `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/safety_and_governance.md`

### "I need deployment guidance"
→ AI Manager deployment: `sub_layer_0.05_os_setup/.../deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`
→ Application deployment: `sub_layer_0.05_os_setup/.../DEPLOYMENT_GUIDE.md`
→ Normative spec: `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/production_deployment.md`

### "I want to see what was implemented"
→ Implementation overview: `implementation/IMPLEMENTATION_OVERVIEW.md`
→ All artifacts: `implementation/ARTIFACTS_INDEX.md`
→ Phase summaries: `implementation/phase_summaries/`
→ Planning docs: `/home/dawson/.cursor/plans/*hierarchy*.md`

---

## By Document Type

### Entry Points & Navigation
| What | Where |
|------|-------|
| Master index | `/code/0_ai_context/0_context/MASTER_DOCUMENTATION_INDEX.md` |
| System overview | `/code/0_ai_context/0_context/SYSTEM_OVERVIEW.md` |
| Usage guide | `/code/0_ai_context/0_context/USAGE_GUIDE.md` |
| Quick start | `layer_0_universal/.../sub_layer_0.01.../HIERARCHY_QUICK_START.md` |

### Framework & Standards
| What | Where |
|------|-------|
| Layer/stage framework | `0.00_layer_stage_framework/README.md` |
| L0 manager system | `layer_0_universal/0.00_ai_manager_system/README.md` |
| L1 manager system | `layer_1_project/1.00_ai_manager_system/README.md` |
| L2 manager system | `layer_2_features/2.00_ai_manager_system/README.md` |
| L3 manager system | `layer_3_components/3.00_ai_manager_system/README.md` |
| Handoff schema | `layer_0_universal/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md` |

### OS/Tool Context Files
| Layer | WSL Location | Linux Ubuntu Location |
|-------|--------------|----------------------|
| L0 | `layer_0_universal/.../stage_0.01_instructions/ai_agent_system/os/wsl/` | `.../os/linux_ubuntu/` |
| L1 | `layer_1_project/.../stage_1.01_instructions/ai_agent_system/os/wsl/` | `.../os/linux_ubuntu/` |
| L2 | `layer_2_features/.../stage_2.01_instructions/ai_agent_system/os/wsl/` | `.../os/linux_ubuntu/` |
| L3 | `layer_3_components/.../stage_3.01_instructions/ai_agent_system/os/wsl/` | `.../os/linux_ubuntu/` |

In each directory: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`

### Operational Protocols
| What | Where |
|------|-------|
| Framework orchestration | `sub_layer_0.13_universal_protocols/framework_orchestration/0_instruction_docs/` |
| CLI recursion | `sub_layer_0.13_universal_protocols/cli_recursion/0_instruction_docs/` |
| Observability | `sub_layer_0.13_universal_protocols/observability/` |
| Safety/governance | `sub_layer_0.04_universal_rules/safety_governance.md` |
| Deployment | `sub_layer_0.05_os_setup/.../deployment/` |

### Adoption Resources
| What | Where |
|------|-------|
| Rollout plan | `/home/dawson/.cursor/plans/ai_manager_hierarchy_rollout_plan.md` |
| Adoption checklist | `sub_layer_0.01_basic_prompts_throughout/HIERARCHY_ADOPTION_CHECKLIST.md` |
| Migration guide | `sub_layer_0.01_basic_prompts_throughout/MIGRATION_GUIDE.md` |
| Quick start | `sub_layer_0.01_basic_prompts_throughout/HIERARCHY_QUICK_START.md` |
| Lessons learned | `-1_research/.../ai_manager_hierarchy_system/implementation_lessons_learned.md` |

### Implementation Documentation
| What | Where |
|------|-------|
| Implementation README | `implementation/README.md` |
| Overview | `implementation/IMPLEMENTATION_OVERVIEW.md` |
| Artifacts index | `implementation/ARTIFACTS_INDEX.md` |
| Location map | `implementation/LOCATION_MAP.md` (this file) |
| Phase summaries | `implementation/phase_summaries/phase_N_summary.md` |
| Guides | `implementation/guides/` |
| Artifacts | `implementation/artifacts/` |

### Normative Specifications
| What | Where |
|------|-------|
| Overview | `-1_research/.../ai_manager_hierarchy_system/overview/` |
| Architecture | `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/architecture.md` |
| OS & Quartets | `.../os_and_quartets.md` |
| Frameworks | `.../framework_orchestration.md` |
| CLI Recursion | `.../cli_recursion_syntax.md` |
| Observability | `.../observability_and_logging.md` |
| Safety | `.../safety_and_governance.md` |
| Deployment | `.../production_deployment.md` |

---

## By Layer

### Universal (Layer 0)
```
layer_0_universal/
├── 0.00_ai_manager_system/README.md
├── 0.01_manager_handoff_documents/
│   ├── README.md
│   └── 0.00_to_universal/handoff_schema.md
├── 0.02_sub_layers/
│   ├── sub_layer_0.01_basic_prompts_throughout/
│   │   ├── HIERARCHY_QUICK_START.md
│   │   ├── HIERARCHY_ADOPTION_CHECKLIST.md
│   │   └── MIGRATION_GUIDE.md
│   ├── sub_layer_0.04_universal_rules/
│   │   ├── README.md
│   │   └── safety_governance.md
│   ├── sub_layer_0.05_os_setup/
│   │   └── .../deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md
│   ├── sub_layer_0.12_universal_tools/README.md
│   └── sub_layer_0.13_universal_protocols/
│       ├── README.md
│       ├── framework_orchestration/
│       ├── cli_recursion/
│       └── observability/
└── 0.99_stages/
    └── stage_0.01_instructions/ai_agent_system/os/
        ├── wsl/{CLAUDE.md, AGENTS.md, GEMINI.md}
        └── linux_ubuntu/{CLAUDE.md, AGENTS.md, GEMINI.md}
```

### Project (Layer 1)
```
layer_1_project/
├── 1.00_ai_manager_system/README.md
├── 1.01_manager_handoff_documents/README.md
└── 1.99_stages/
    └── stage_1.01_instructions/ai_agent_system/os/
        ├── wsl/{CLAUDE.md, AGENTS.md, GEMINI.md}
        └── linux_ubuntu/{CLAUDE.md, AGENTS.md, GEMINI.md}
```

### Features (Layer 2)
```
layer_2_features/
├── 2.00_ai_manager_system/README.md
├── 2.01_manager_handoff_documents/README.md
└── 2.99_stages/
    └── stage_2.01_instructions/ai_agent_system/os/
        ├── wsl/{CLAUDE.md, AGENTS.md, GEMINI.md}
        └── linux_ubuntu/{CLAUDE.md, AGENTS.md, GEMINI.md}
```

### Components (Layer 3)
```
layer_3_components/
├── 3.00_ai_manager_system/README.md
├── 3.01_manager_handoff_documents/README.md
└── 3.99_stages/
    └── stage_3.01_instructions/ai_agent_system/os/
        ├── wsl/{CLAUDE.md, AGENTS.md, GEMINI.md}
        └── linux_ubuntu/{CLAUDE.md, AGENTS.md, GEMINI.md}
```

---

## By Phase

### Phase 1: Navigation & Overview
- `MASTER_DOCUMENTATION_INDEX.md` (updated)
- `SYSTEM_OVERVIEW.md` (updated)
- `USAGE_GUIDE.md` (updated)

### Phase 2: Framework Alignment
- `0.00_layer_stage_framework/README.md` (updated)

### Phase 3: Manager/Worker Standardization
- `layer_*/N.00_ai_manager_system/README.md` (4 files)
- `handoff_schema.md` (1 file)

### Phase 4: OS/Tool Variants
- `layer_*/stage_*.01_instructions/ai_agent_system/os/` (16 directories)
- `{CLAUDE|AGENTS|GEMINI}.md` in wsl/ and linux_ubuntu/ (24 files)
- Updated tool documentation (2 files)

### Phase 5: Orchestration & CLI
- `framework_orchestration/` directory and docs (1 file)
- `cli_recursion/` directory and docs (1 file)
- Updated protocols README (1 file)

### Phase 6: Ops/Safety/Deployment
- `observability/` directory and docs (1 file)
- `safety_governance.md` (1 file)
- `deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md` (1 file)
- Updated rules README (1 file)

### Phase 7: Rollout & Migration
- `ai_manager_hierarchy_rollout_plan.md` (planning directory)
- `HIERARCHY_ADOPTION_CHECKLIST.md` (1 file)
- `MIGRATION_GUIDE.md` (1 file)
- `HIERARCHY_QUICK_START.md` (1 file)
- `implementation_lessons_learned.md` (1 file)

---

## Absolute Path Examples

### Most Common Paths
```bash
# Top-level navigation
/home/dawson/code/0_ai_context/0_context/SYSTEM_OVERVIEW.md

# OS context for Layer 0, WSL, Claude
/home/dawson/code/0_ai_context/0_context/layer_0_universal/0.99_stages/stage_0.01_instructions/ai_agent_system/os/wsl/CLAUDE.md

# Handoff schema
/home/dawson/code/0_ai_context/0_context/layer_0_universal/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md

# Observability protocol
/home/dawson/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.13_universal_protocols/observability/README.md

# Quick start guide
/home/dawson/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/HIERARCHY_QUICK_START.md

# Rollout plan
/home/dawson/.cursor/plans/ai_manager_hierarchy_rollout_plan.md

# Implementation docs
/home/dawson/code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/implementation/
```

---

## Path Patterns to Remember

### Layer-specific manager systems
`layer_{0_universal|1_project|2_features|3_components}/{0|1|2|3}.00_ai_manager_system/README.md`

### OS context at any layer
`layer_N_.../N.99_stages/stage_N.01_instructions/ai_agent_system/os/{wsl|linux_ubuntu|windows|macos}/{CLAUDE|AGENTS|GEMINI}.md`

### Universal protocols
`layer_0_universal/0.02_sub_layers/sub_layer_0.13_universal_protocols/{protocol_name}/`

### Universal rules
`layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/{rule_name}.md`

### Normative specs
`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/{spec_name}.md`

---

## Navigation Shortcuts

### From project root
```bash
cd /home/dawson/code/0_ai_context/0_context
```

### To specific areas
```bash
# Universal layer
cd layer_0_universal

# OS context (Layer 0, WSL)
cd layer_0_universal/0.99_stages/stage_0.01_instructions/ai_agent_system/os/wsl

# Protocols
cd layer_0_universal/0.02_sub_layers/sub_layer_0.13_universal_protocols

# Adoption guides
cd layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout

# Implementation docs
cd -1_research/-1.01_things_researched/ai_manager_hierarchy_system/implementation

# Planning docs
cd ~/.cursor/plans
```

---

**Last Updated**: 2025-12-24
**Purpose**: Quick location reference for all hierarchy documentation
**Use**: "Where do I find X?" lookup
