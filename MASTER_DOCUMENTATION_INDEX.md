---
resource_id: "9de4c0f5-f69e-4525-b9df-14379d0fd7fd"
resource_type: "document"
resource_name: "MASTER_DOCUMENTATION_INDEX"
---
# Master Documentation Index
*Complete Index of All Organized Documentation*

> **Note:** This repo now uses the Layer + Stage framework. Canonical content lives under `layer_0/`, `layer_1_project/`, `layer_2_features/`, and `layer_3_components/` (slots in `*.01_sub_layers/sub_layer_<N.xx>_*`, stages in `*.99_stages/stage_<N.xx>_*`). Legacy `trickle_down_*` paths referenced below are kept for historical context; migrate or reference them via the new layer structure when practical.

<!-- section_id: "4308dda0-7a37-4b9d-903f-0516e03ef45a" -->
## 📋 Overview

This master index provides a comprehensive overview of all documentation organized within the trickle-down structure. All documents follow the standardized naming convention and are categorized by their purpose and content.

<!-- section_id: "8c12378c-8f4f-4b2a-b7f6-8e78e7a7082a" -->
## ⚠️ **IMPORTANT UPDATE - January 24, 2025**

**Status Documentation Update**: The previous status reports (October 2025) claimed 99% completion, but comprehensive testing revealed critical blocking issues. See `CURRENT_STATUS_JAN_24_2025.md` for the accurate current status after critical bug fixes.

**✅ DEVELOPMENT ENVIRONMENT OPERATIONAL**: As of January 24, 2025, the development environment is fully operational with Flask server running on port 5002, Firebase emulators configured, and 100% test pass rate achieved. See `DEVELOPMENT_ENVIRONMENT_OPERATIONAL_JAN_24_2025.md` for current operational status.

**📊 COMPREHENSIVE USER STORY TESTING COMPLETED**: All 71 user stories tested across 18 categories with 36 test runs. Results show 61.1% pass rate (22/36), identifying 4 completely broken categories (admin, cloud features). See `USER_STORY_TEST_RESULTS_JAN_24_2025.md` for detailed analysis.

**🔧 UNIVERSAL TERMINAL EXECUTION PROTOCOL**: Comprehensive terminal execution protocol for ALL AI agents (Cursor, Codex, Gemini CLI, Claude Code, Warp). Includes Python wrapper usage, Node.js command handling, and `; exit` workaround. See `trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md` for complete rules and `AGENT_DISCOVERY_GUIDE.md` for how agents discover this documentation.

**📝 AI AGENT DOCUMENTATION RULE**: Universal rule requiring all AI agents to create, update, and maintain comprehensive documentation for every single AI turn in every session. Includes mandatory git commit requirements. See `trickle_down_0_universal/0_instruction_docs/ai_agent_documentation_rule.md` for complete requirements and `trickle_down_0_universal/0_instruction_docs/git_commit_rule.md` for git commit standards.

**🧪 COMPREHENSIVE INTEGRATION TESTING COMPLETED**: All integration tests are 100% passing with comprehensive coverage of database operations, authentication, real-time synchronization, API integration, and business logic. See `trickle_down_3_testing/integration_tests/2025-01-27_comprehensive_integration_validation.md` for detailed test results and `trickle_down_3_testing/bug_reports/2025-01-27_bug_fixes_realtime_sync_transaction_logging.md` for bug fixes applied.

**🧪 TESTING SYSTEM FIXED**: User story testing system has been completely overhauled with server connectivity verification to eliminate false negatives. See `TESTING_SYSTEM_FIXED_JAN_24_2025.md` for comprehensive improvements and usage instructions.

**🔧 MEDIUM PRIORITY ITEMS COMPLETED**: URL routing fixes and comprehensive template creation completed. All templates now exist with consistent design and navigation patterns. See `MEDIUM_PRIORITY_ITEMS_COMPLETED_JAN_24_2025.md` for detailed accomplishments.

**📋 SESSION SUMMARY**: Comprehensive session summary documenting URL routing fixes, template creation, and documentation updates. See `SESSION_SUMMARY_JAN_24_2025.md` for complete session accomplishments.

<!-- section_id: "eaf670d5-425c-4dbc-bded-ab7c734e35b1" -->
## 🔄 **UNIVERSAL CONTENT CONSOLIDATED - November 11, 2025**

**Universal documentation has been consolidated** from multiple project 0_context directories across the codebase:

<!-- section_id: "2cf381c6-9dcf-4abb-878f-390d5aa52d8a" -->
### **New Universal Documentation Added**:

1. **SYSTEM_OVERVIEW.md** - Visual guide to the Universal Documentation System
   - Complete system architecture with diagrams
   - Flow examples showing Universal → Project pattern
   - Navigation guide for AI agents
   - Quick start checklist

2. **UNIVERSAL_DOCUMENTATION_SYSTEM.md** - Meta-documentation explaining the trickle-down hierarchy
   - Core concept and philosophy
   - Standard directory structure
   - Universal → Project implementation pattern
   - Creating new universal systems

3. **Testing Agent System** (Complete 5-file system):
   - `TESTING_AGENT_SYSTEM_README.md` - Complete guide to the Testing Agent Framework
   - `testing-agent-protocol.md` - Core protocol defining roles and workflows
   - `testing-agent-instructions.md` - Step-by-step guide for Testing Agents
   - `testing-agent-handoff-template.md` - Standard Development→Testing handoff template
   - `testing-agent-report-template.md` - Standard Testing Agent report template

4. **README.md** in `trickle_down_0_universal/0_instruction_docs/` - Overview of all universal systems

<!-- section_id: "4e931913-b0a6-41b3-a0ff-addedad11b4e" -->
### **Source Projects Consolidated**:
- ✅ `lang-trak-in-progress/docs/0_context` - Testing Agent System and meta-documentation
- ✅ `I-eat-repo/0_context` - Verified for unique content (none found)
- ✅ `Parallelism and Concurrency/0_context` - Verified (identical to main)
- ✅ `DS250-Course-Draft/0_context` - Project-specific only

**Location**: All new files added to `/home/dawson/code/0_layer_universal/0_context/`

**Purpose**: Consolidate universal, reusable documentation that applies to ANY project, making the 0_layer_universal directory the single source of truth for universal AI agent protocols.

<!-- section_id: "ef56050a-afc1-42cd-b393-36518476ee75" -->
## 🆕 SCHOOL WRAPPER PATTERN STANDARDIZED - November 11, 2025

- Wrapper directories named `school-<project>` carry:
  - Public repo (e.g., `pac20026_fall2025/` → `byui-math-dept/pac20026_fall2025`)
  - Private project context repo (`0_context/` → `Dawson2025/1-project-context-pac20026_fall2025`)
  - Workspace metadata (`.ai_workspace`) + README describing flow
- Universal context canonical location: `/home/dawson/code/0_layer_universal` (repo `Dawson2025/0-universal-context`)
- Public repos must exclude every AI artifact; all AI docs live inside private context repos
- This wrapper + dual-private-repo structure is now the baseline DS250 school workspace template

<!-- section_id: "910baf92-efd2-4483-bb92-18c3b09c45f0" -->
## 🏗️ **CANONICAL AGENT OS ARCHITECTURE - AI Manager Hierarchy System**

**The Ideal AI Manager Hierarchy System is the canonical architectural design for all AI work in this repository.**

This comprehensive system defines how AI agents are organized, coordinated, and executed across layers of abstraction using a **manager/worker pattern** with **handoff documents** for inter-agent communication.

<!-- section_id: "182d5ad9-777d-4c84-b376-be0bfe3d7049" -->
### **Core Documentation:**

- **Quick Overview**: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/README.md`](code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/README.md)
- **System Summary**: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`](code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md)

<!-- section_id: "9428e71c-e51a-489e-8f15-2397fa83e225" -->
### **Detailed Specifications:**

All detailed documentation is located in: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/`](code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/)

**Core Architecture:**
- `summary/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md` - Long-form specification
- `architecture.md` - Layers, stages, agents, handoffs, supervisors, and parallelism
- `tools_and_context_systems.md` - Claude/Codex/Gemini/Cursor behavior and context systems
- `os_and_quartets.md` - OS-specific layouts and context variants
- `token_and_policy_strategy.md` - Cost-aware routing and tool selection policies

**Implementation Guides:**
- `framework_orchestration.md` - Using LangGraph, AutoGen, CrewAI, MetaGPT
- `model_selection_strategy.md` - Choosing models (Qwen, StarCoder, Codestral) based on cost/quality
- `supervisor_patterns.md` - Concrete supervisor implementations
- `parallel_execution.md` - Parallelizing work across layers and components
- `cli_recursion_syntax.md` - CLI examples for recursive agent delegation

**Operational Concerns:**
- `observability_and_logging.md` - Structured logging, metrics, tracing, and dashboards
- `safety_and_governance.md` - Permissions, security boundaries, approval gates, budget controls
- `production_deployment.md` - Deployment architectures, scaling, reliability, and best practices

**Extensions:**
- `mcp_extensions.md` - Adding MCP servers for new tools and capabilities
- `persona_library.md` - Creating reusable agent personas (Security Reviewer, Test Generator, etc.)

<!-- section_id: "3ddcc9af-1892-4e88-b15e-047858bb76ac" -->
### **Key Concepts:**

- **Layers**: L0 (Universal) → L1 (Project) → L2 (Feature) → L3 (Component) → L4+ (Sub-component)
- **Stages**: request → instructions → planning → design → implementation → testing → criticism → fixing → archiving
- **Managers**: Coordinate work, spawn workers, aggregate results
- **Workers**: Execute bounded tasks, write handoffs, exit
- **Handoffs**: JSON/Markdown documents passing state between layers and stages
- **Tools**: Claude Code (managers), Codex CLI (workers), Gemini CLI (research), Cursor IDE (interactive)

This system provides the foundation for all agent orchestration, tool selection, and workflow patterns in this repository.

<!-- section_id: "033bbc8d-ae32-4070-ae5a-3ceea26752c3" -->
## 🗂️ Directory Structure Overview

```
0_context/
├── 0_basic_prompts_throughout/    # Core prompts for all AI agents
├── trickle_down_0_universal/
│   ├── 0_instruction_docs/     # Universal AI agent instructions
│   ├── 1_status_progress_docs/ # Current status and progress
│   ├── 2_archive_docs/         # Completed universal instructions
│   └── 2_testing_docs/         # Testing documentation
├── trickle_down_0.5_setup/
│   ├── 0_instruction_docs/     # Setup guides and procedures
│   ├── 1_status_progress_docs/ # Setup status and progress
│   ├── 2_archive_docs/         # Completed setup documentation
│   └── 2_testing_docs/         # Testing documentation
├── layer_0/0.02_sub_layers/
│   ├── sub_layer_0_06_environment_setup/            # Git/GitHub auth, credentials, cross-app environment rules
│   ├── sub_layer_0_09_ai_apps_tools_setup/          # AI apps/tools setup (required before MCP setup)
│   ├── sub_layer_0_10_mcp_servers_and_tools_setup/  # MCP server setup (depends on 0.09)
│   │   ├── 0.01_core-system/
│   │   ├── 0.02_mcp_config_options_0_file_tree_0/
│   │   └── 0.06_automation/
│   ├── sub_layer_0_11_ai_models/                    # AI models guidance
│   ├── sub_layer_0_12_universal_tools/              # Universal tools
│   └── sub_layer_0_13_agent_setup/                  # Agent setup (depends on 0.09–0.12)
│   ├── 1_status_progress_docs/ # Tool development status
│   ├── 2_archive_docs/         # Completed tool implementations
│   └── 2_testing_docs/         # Testing documentation
├── trickle_down_1_project/
│   ├── 0_instruction_docs/     # Project constitution and standards
│   ├── 1_status_progress_docs/ # Project status and progress
│   ├── 2_archive_docs/         # Project completion documentation
│   ├── 2_testing_docs/         # Testing documentation
│   └── 3_archive_docs/         # Additional archived documentation
├── trickle_down_1.5_project_tools/
│   ├── 0_instruction_docs/     # Project-specific tool guides
│   ├── 1_status_progress_docs/ # Tool development status
│   ├── 2_archive_docs/         # Completed project tools
│   └── 2_testing_docs/         # Testing documentation
├── trickle_down_2_features/
│   ├── 0_instruction_docs/     # Feature specifications and guides
│   ├── 1_status_progress_docs/ # Feature development status
│   └── 2_archive_docs/         # Completed feature implementations
├── trickle_down_2_implementation/
│   ├── 0_instruction_docs/     # Implementation guides
│   ├── 1_status_progress_docs/ # Implementation status
│   └── 2_archive_docs/         # Completed implementations
└── trickle_down_3_testing/
    ├── integration_tests/      # Integration test documentation
    ├── bug_reports/            # Bug reports and fixes
    └── technical_notes/        # Technical notes and analysis
```

<!-- section_id: "a287af98-33cf-4c9e-a3c0-2db4be7e47cc" -->
## 📚 Documentation Categories

<!-- section_id: "bf8b1bd4-b5e0-41e0-bb9a-d24ac6658b58" -->
### **0_instruction_docs** - How-to Guides and Procedures
- **Universal Instructions**: AI agent protocols, terminal tools, manual steps automation, Cursor terminal issues
- **Basic Prompts Throughout**: Core "what to do next" prompt for all AI agents (customize per project)
- **Setup Guides**: Environment setup, deployment procedures, configuration guides
- **Universal Tools**: Meta-intelligent orchestration, browser automation, API sync tracking
- **Project Standards**: Constitution, development workflow, project-specific guidelines
- **Feature Guides**: Feature specifications, system specifications, implementation guides
- **Component Guides**: Feature summaries, implementation guides, testing procedures

<!-- section_id: "4a607ebc-7bcc-4d6f-9992-368f5f1e1367" -->
### **1_status_progress_docs** - Current Status and Progress
- **Project Status**: Current development status, progress reports, active work
- **AI Development**: Parallel development status, testing results, implementation progress
- **Feature Development**: Current feature status, blockers, next steps
- **Component Development**: Component implementation status, testing progress

<!-- section_id: "0206dc8f-f0ef-41a4-987b-19c14767219a" -->
### **2_archive_docs** - Completed Work and Resolutions
- **Resolutions**: Problem statements, investigations, solutions implemented
- **Implementations**: Complete implementation summaries, deployment records
- **Feature Documentation**: Completed feature specifications, testing results
- **Historical Records**: Evolution of systems, lessons learned, best practices

<!-- section_id: "4f56cc74-d0fd-4d13-94b8-c8a64dc392c9" -->
### **2_testing_docs** - Testing Documentation
- **Test Suites**: Comprehensive test coverage documentation
- **Test Results**: Test execution results and analysis
- **Test Strategies**: Testing approaches and methodologies
- **Quality Assurance**: QA documentation and verification

<!-- section_id: "52522a79-22a8-45a2-8e88-ecd108332ad1" -->
### **3_archive_docs** - Additional Archived Documentation
- **Extended Archives**: Additional historical records and completed work
- **Deep Archive**: Long-term archived documentation

<!-- section_id: "079db7c6-8d15-4ad5-88c0-145dd38a3b17" -->
## 🔗 Cross-References

<!-- section_id: "459e51aa-4f74-4bb1-a75b-8926e4a860bd" -->
### **Universal Level Cross-References**
- **Instructions → Setup**: Universal instructions reference setup procedures
- **Setup → Tools**: Setup procedures reference universal tools
- **Tools → Project**: Universal tools support project-specific implementations
- **Supabase Integration**: JavaScript-only database operations rule enforced across all levels

<!-- section_id: "7b8d6468-858c-4033-add4-9ffc3bc7b9b3" -->
### **Project Level Cross-References**
- **Project → Features**: Project standards guide feature development
- **Features → Components**: Feature specifications guide component implementation
- **Components → Archive**: Component implementations become archived documentation

<!-- section_id: "c0a04d77-3979-4e10-899d-595029b4dbd8" -->
### **Archive Cross-References**
- **Resolution Links**: Each resolution links to related implementations
- **Implementation Links**: Each implementation links to related features
- **Feature Links**: Each feature links to related components

<!-- section_id: "8c087db2-1ea0-454b-ba1e-cff4e8fa79a1" -->
## 📊 Documentation Statistics

<!-- section_id: "b5cadfeb-37d0-42d8-b363-5aec03511494" -->
### **Total Documents by Category**
- **Instruction Documents**: 150+ (How-to guides, procedures, specifications)
- **Status/Progress Documents**: 50+ (Current status, progress reports, active work)
- **Archive Documents**: 25+ (Completed work, resolutions, historical records)

<!-- section_id: "d9619ace-6beb-43d1-94e1-2c51e68f8270" -->
### **Total Documents by Level**
- **Universal Instructions**: 20+ documents
- **Setup and Configuration**: 25+ documents
- **Universal Tools**: 15+ documents
- **Project Standards**: 30+ documents
- **Project Tools**: 20+ documents
- **Feature Development**: 40+ documents
- **Component Implementation**: 35+ documents

<!-- section_id: "ebce8dce-5013-4602-b70c-47f0e1a66ad4" -->
## 🎯 Navigation Guide

<!-- section_id: "caad64c2-272e-40d8-8cdb-773620684975" -->
### **For New Users**
1. Start with `trickle_down_0_universal_instructions/0_instruction_docs/`
2. Review `trickle_down_1_project/0_instruction_docs/constitution.md`
3. Check current status in `1_status_progress_docs/` folders
4. Reference completed work in `2_archive_docs/` folders

<!-- section_id: "466bca74-51dc-4b66-9fe1-9c6a813807bd" -->
### **For Developers**
1. Review project standards in `trickle_down_1_project/0_instruction_docs/`
2. Check feature specifications in `trickle_down_2_features/0_instruction_docs/`
3. Monitor progress in `1_status_progress_docs/` folders
4. Reference implementations in `2_archive_docs/` folders

<!-- section_id: "58e9e639-cf73-40da-b72e-e3ede4b59a5e" -->
### **For AI Agents**
1. **START HERE**: Read `0_basic_prompts_throughout/what_to_do_next.md` for core instructions
2. **UNDERSTAND THE SYSTEM**: Read `SYSTEM_OVERVIEW.md` for visual guide to the documentation system
3. **META-DOCUMENTATION**: Read `trickle_down_0_universal/0_instruction_docs/UNIVERSAL_DOCUMENTATION_SYSTEM.md` for the trickle-down philosophy
4. Follow universal instructions in `trickle_down_0_universal/0_instruction_docs/`
5. **CRITICAL**: Read `trickle_down_0_universal/0_instruction_docs/cursor_terminal_issues.md` for terminal handling
6. **MANDATORY**: Follow `trickle_down_0_universal/0_instruction_docs/terminal_execution_protocol.md` for all commands
7. **MANDATORY**: Follow `trickle_down_0_universal/0_instruction_docs/supabase_javascript_integration_rule.md` for all database operations
8. **TESTING**: Use `trickle_down_0_universal/0_instruction_docs/testing-agent-protocol.md` for comprehensive testing
9. Use setup procedures in `trickle_down_0.5_setup/0_instruction_docs/`
10. Apply universal tools from `trickle_down_0.75_universal_tools/0_instruction_docs/`
11. Reference completed work in `2_archive_docs/` folders

<!-- section_id: "7e62c2fb-b9d7-4cd3-8c9d-fbdca85ab1ee" -->
## 🔍 Search and Discovery

<!-- section_id: "87b27065-efc4-4a0e-8dc4-df87525cad54" -->
### **By Document Type**
- **Instructions**: Look in `0_instruction_docs/` folders
- **Status**: Look in `1_status_progress_docs/` folders
- **Completed Work**: Look in `2_archive_docs/` folders

<!-- section_id: "32c6646a-4097-4504-836b-691b3f3f27d9" -->
### **By Content Area**
- **Meta-Documentation**: `SYSTEM_OVERVIEW.md` and `UNIVERSAL_DOCUMENTATION_SYSTEM.md` (System philosophy and structure)
- **Testing Agent System**: `trickle_down_0_universal/0_instruction_docs/testing-agent-*` (Complete testing framework)
- **AI Agent Protocols**: `trickle_down_0_universal/`
- **Basic Prompts Throughout**: `0_basic_prompts_throughout/` (CRITICAL for all AI agents)
- **Environment Setup**: `trickle_down_0.5_setup/`
  - **GitHub SSO Setup**: `layer_0/0.02_sub_layers/sub_layer_0_06_environment_setup/trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md` (Complete guide for SAML SSO token authorization)
- **Universal Tools**: `trickle_down_0.75_universal_tools/`
- **Project Standards**: `trickle_down_1_project/`
- **Project Tools**: `trickle_down_1.5_project_tools/`
- **Feature Development**: `trickle_down_2_features/`
- **Component Implementation**: `trickle_down_3_components/`
- **Testing Documentation**: `trickle_down_3_testing/` (Integration tests, bug reports)
- **Supabase Integration Rule**: `trickle_down_0_universal/0_instruction_docs/supabase_javascript_integration_rule.md` (MANDATORY)

<!-- section_id: "d13e2229-e2ed-455d-879c-d90e0bad6f4e" -->
### **Testing Documentation**
- **Universal Testing Agent System** (NEW - Nov 11, 2025):
  - `TESTING_AGENT_SYSTEM_README.md` - Complete testing framework guide
  - `testing-agent-protocol.md` - Core protocol for development/testing separation
  - `testing-agent-instructions.md` - Step-by-step guide for Testing Agents
  - `testing-agent-handoff-template.md` - Standard handoff template
  - `testing-agent-report-template.md` - Standard report template
- **Integration Tests**: `trickle_down_3_testing/integration_tests/2025-01-27_comprehensive_integration_validation.md` (100% passing)
- **Bug Reports**: `trickle_down_3_testing/bug_reports/2025-01-27_bug_fixes_realtime_sync_transaction_logging.md`
- **Firebase Integration Tests**: `trickle_down_2_features/2_testing_docs/` (Multiple test suites)
- **Cloud Template Tests**: `trickle_down_2_features/2_testing_docs/20251023_CloudTemplateTests_TestReport_v1.0.md`
- **Testing Strategy**: `trickle_down_2_features/2_testing_docs/Firebase_Testing_Strategy_Analysis.md`

<!-- section_id: "13d1b18e-a1f4-4c14-8e73-fc5c725818d4" -->
### **Universal Systems Inventory** (Consolidated Nov 11, 2025)

#### **1. Meta-Documentation System** 📚
- **SYSTEM_OVERVIEW.md** - Visual guide with architecture diagrams and navigation
- **UNIVERSAL_DOCUMENTATION_SYSTEM.md** - Trickle-down philosophy and implementation patterns
- **Purpose**: Explain the documentation system itself to AI agents and developers
- **Status**: ✅ Complete

#### **2. Testing Agent System** 🧪 (NEW)
- **TESTING_AGENT_SYSTEM_README.md** - Complete overview of the testing framework
- **testing-agent-protocol.md** - Core protocol defining roles, responsibilities, and workflows
- **testing-agent-instructions.md** - Step-by-step guide for AI Testing Agents
- **testing-agent-handoff-template.md** - Standard template for dev-to-testing handoffs
- **testing-agent-report-template.md** - Standard template for testing reports
- **Purpose**: Separation of concerns between development and testing activities
- **Status**: ✅ Complete and production-ready

#### **3. Terminal Execution System** 💻
- **cursor_terminal_issues.md** - Universal terminal issues in Cursor IDE
- **terminal_execution_protocol.md** - Safe command execution protocol
- **terminal-tool-replacement.md** - Alternative tools for terminal operations
- **terminal-quick-reference.md** - Quick reference guide
- **Purpose**: Best practices for terminal command execution
- **Status**: ✅ Complete

#### **4. Manual Steps Automation** 🤖
- **manual-steps-automation.md** - Protocol for automating all manual steps
- **Purpose**: AI agents execute all steps programmatically, never delegate to users
- **Status**: ✅ Complete

#### **5. Browser Management** 🌐
- **browser_management_policy.md** - Keep automation browsers open and persistent across sessions
- **browser_opening_rule.md** - Use MCP browser servers (cursor-browser-extension preferred)
- **Purpose**: Persistent browser automation with cross-session state preservation
- **Key Features**: 
  - Browser sessions persist across AI chat sessions
  - Authenticated sessions maintained indefinitely
  - No re-authentication required between sessions
  - State preservation (cookies, local storage, session data)
- **Status**: ✅ Complete and Updated (Nov 11, 2025)

#### **6. OAuth Production Setup** 🔐
- **google_oauth_production_ready.md** - Production OAuth configuration
- **Purpose**: Secure OAuth setup for any project
- **Status**: ✅ Complete

#### **7. Security Protocols** 🔒
- **sudo_password_management.md** - Secure credential handling
- **Purpose**: Security best practices for AI agents
- **Status**: ✅ Complete

#### **8. Documentation Standards** 📝
- **ai_agent_documentation_rule.md** - Documentation requirements for AI agents
- **git_commit_rule.md** - Git commit standards
- **post-completion-documentation-protocol.md** - How to document completed work
- **Purpose**: Maintain high-quality documentation across all sessions
- **Status**: ✅ Complete

#### **9. Software Engineering Knowledge System** 🎓
- **software_engineering_knowledge_system/** - Complete knowledge map IC → CTO
- **Purpose**: Comprehensive learning path for software engineering
- **Status**: ✅ Active development

<!-- section_id: "06b46696-c511-4853-9b3c-55ba6321dd95" -->
### **MCP Tools (Model Context Protocol)**
- **MCP System Guide**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.01_core-system/MCP_SYSTEM_GUIDE.md`
- **MCP Configuration Guide**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.01_core-system/MCP_CONFIGURATION_GUIDE.md`
- **MCP Server Matrix**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.01_core-system/MCP_SERVER_MATRIX.md`
- **Browser MCP Routing Table**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md`

<!-- section_id: "719a861a-9fbf-4248-8e13-13c12d4a55f4" -->
### **By Timeline**
- **Current Work**: Check `1_status_progress_docs/` folders
- **Recent Completions**: Check `2_archive_docs/` folders
- **Historical Context**: Review all `2_archive_docs/` folders

---

**Master Index Maintained By**: Documentation Organization System
**Last Updated**: 2025-11-11 (Browser persistence policies updated, GitHub SSO guide added)
**Next Review**: 2025-12-11
