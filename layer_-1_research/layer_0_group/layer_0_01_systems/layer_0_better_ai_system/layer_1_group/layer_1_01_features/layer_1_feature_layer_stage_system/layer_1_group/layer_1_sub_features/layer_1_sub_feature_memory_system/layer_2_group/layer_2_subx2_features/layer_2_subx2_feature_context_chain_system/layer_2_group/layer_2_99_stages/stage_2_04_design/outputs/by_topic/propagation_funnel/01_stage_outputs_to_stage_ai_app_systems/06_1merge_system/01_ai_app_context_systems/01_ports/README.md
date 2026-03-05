---
resource_id: "7c179973-c0b5-42bb-b24b-1e735ee9bd55"
resource_type: "readme
output"
resource_name: "README"
---
# AI App Context Systems — Porting Strategy for 5 Tools

**Date**: 2026-02-27
**Status**: Documentation complete for 4 of 5 apps

---

<!-- section_id: "1e419322-817a-4c6c-99b2-78f8051691bd" -->
## Overview

This directory contains comprehensive documentation for porting the 0AGNOSTIC.md system and .0agnostic/ directory into 5 different AI applications:

1. **Claude Code CLI** ✅ Complete (4 files)
2. **Codex CLI** ✅ Complete (4 files)
3. **Gemini SDK** ✅ Complete (3 files + 1 in progress)
4. **Cursor IDE** ✅ Mostly complete (3 files + 1 in progress)
5. **Cursor Agent CLI** ⚠️ Partial (1 file)

---

<!-- section_id: "bcdb58b6-382a-45b5-9a35-12c032ee4cee" -->
## File Structure

Each application has:
- **ai_app_system/** directory with 3 files:
  - `NATIVE_FEATURES.md` — What the tool provides natively (mechanisms)
  - `APPLICATION_IMPLEMENTED.md` — What users must create (strategy & content)
  - `COMPLETE_ARCHITECTURE.md` — How they work together

- **port_system/** directory with 1 file:
  - `PORTING_STRATEGY.md` — How to map 0AGNOSTIC.md and .0agnostic/ into the tool's native system

---

<!-- section_id: "d80c2528-60e8-4053-9df8-7e18bab2c78a" -->
## Key Concepts

<!-- section_id: "ecae449c-98b6-4645-946c-08ca93dcb7f9" -->
### Native vs. Application-Implemented

**Native** (Tool Provides):
- Mechanisms and features built into the tool
- Cannot be changed by users (except configuration)
- Examples: Gemini's system instructions, Cursor's .cursor/rules loading, Claude Code's context window management

**Application-Implemented** (User Provides):
- Content, strategy, and decisions
- What goes INTO native mechanisms
- Examples: Writing actual .cursor/rules content, deciding what to remember in Memory Bank, choosing which MCP servers to configure

<!-- section_id: "c206f7e3-a02f-4188-b5fc-177bb7f38784" -->
### Three-Part Pattern

Every application documentation follows:

1. **NATIVE_FEATURES.md** (300-400 lines)
   - 10 native mechanisms
   - "What does / doesn't do" format
   - Tool-specific capabilities

2. **APPLICATION_IMPLEMENTED.md** (350-450 lines)
   - 7-8 areas where users make decisions
   - "You must provide / decide" format
   - User responsibility sections

3. **COMPLETE_ARCHITECTURE.md** (350-450 lines)
   - System overview diagrams
   - Request-response flows
   - Context composition
   - Integration examples

4. **PORTING_STRATEGY.md** (600-800 lines)
   - How to map 0AGNOSTIC.md STATIC → tool's system instruction/config
   - How to map 0AGNOSTIC.md DYNAMIC → user runtime code
   - How to implement .0agnostic/ directories in tool's native system
   - Complete integration examples
   - Migration checklists

---

<!-- section_id: "ad570521-547b-4457-b911-b8a57496563d" -->
## Completed Applications

<!-- section_id: "8909e8f3-c72a-40ff-8fea-1ad1ad492a6f" -->
### 1. Claude Code CLI

**Status**: ✅ Complete

**Key Insights**:
- Native: MEMORY.md (200 lines in context), CLAUDE.md cascade, context window management, subagents
- Porting: 0AGNOSTIC.md STATIC → CLAUDE.md auto-generated, DYNAMIC → MEMORY.md (first 200 lines)
- .0agnostic/ → ~/.claude/ (skills, rules, episodic_memory)

**Files**:
- `01_claude_code_cli/ai_app_system/NATIVE_FEATURES.md` (280 lines)
- `01_claude_code_cli/ai_app_system/APPLICATION_IMPLEMENTED.md` (320 lines)
- `01_claude_code_cli/ai_app_system/COMPLETE_ARCHITECTURE.md` (400 lines)
- `01_claude_code_cli/port_system/PORTING_STRATEGY.md` (750 lines)

<!-- section_id: "f4109776-44d8-4088-a63d-9ce7a34d4f96" -->
### 2. Codex CLI

**Status**: ✅ Complete

**Key Insights**:
- Native: Three-level AGENTS.md hierarchy, config.toml, session persistence, IDE extensions
- Porting: 0AGNOSTIC.md STATIC → AGENTS.md files (global, project, directory-specific)
- .0agnostic/ → config.toml + .codex/ directory structure

**Files**:
- `02_codex_cli/ai_app_system/NATIVE_FEATURES.md` (1,000+ lines)
- `02_codex_cli/ai_app_system/APPLICATION_IMPLEMENTED.md` (400 lines)
- `02_codex_cli/ai_app_system/COMPLETE_ARCHITECTURE.md` (500 lines)
- `02_codex_cli/port_system/PORTING_STRATEGY.md` (900 lines)

<!-- section_id: "ffc50ef3-eca4-4f05-b6f2-3c8fcec8daed" -->
### 3. Gemini SDK

**Status**: ✅ Nearly Complete (3/4 files)

**Key Insights**:
- Native: System instructions, session management, file upload/caching, generation parameters, cost tracking
- Porting: 0AGNOSTIC.md STATIC → system_instruction parameter
- .0agnostic/ → Application code (config classes, session managers, budget trackers)

**Files**:
- `03_gemini/ai_app_system/NATIVE_FEATURES.md` (365 lines) ✅
- `03_gemini/ai_app_system/APPLICATION_IMPLEMENTED.md` (360 lines) ✅
- `03_gemini/ai_app_system/COMPLETE_ARCHITECTURE.md` (380 lines) ✅
- `03_gemini/port_system/PORTING_STRATEGY.md` (750 lines) ✅

<!-- section_id: "1bf97a63-1f38-4b18-b498-9cadce46e3fe" -->
### 4. Cursor IDE

**Status**: ✅ Mostly Complete (3/4 files)

**Key Insights**:
- Native: .cursor/rules system, semantic search, Memory Bank, MCP integration, hooks, Agent CLI
- Porting: 0AGNOSTIC.md STATIC → .cursor/rules YAML files
- .0agnostic/ → Project configuration (hooks.json, memory bank structure)

**Files**:
- `04_cursor_ide/ai_app_system/NATIVE_FEATURES.md` (420 lines) ✅
- `04_cursor_ide/ai_app_system/APPLICATION_IMPLEMENTED.md` (400 lines) ✅
- `04_cursor_ide/ai_app_system/COMPLETE_ARCHITECTURE.md` (350 lines) ✅
- `04_cursor_ide/port_system/PORTING_STRATEGY.md` (⏳ In Progress)

<!-- section_id: "5c073bc3-d876-4672-9d5c-703ec7239cff" -->
### 5. Cursor Agent CLI

**Status**: ⚠️ Partial (1/4 files)

**Key Insights**:
- Native: Autonomous task execution, session persistence, shell commands, MCP tools, error handling
- Porting: Tasks require explicit definition, no native 0AGNOSTIC.md equivalent
- .0agnostic/ → Task definitions, approval policies, session state

**Files**:
- `05_cursor_agent_cli/ai_app_system/NATIVE_FEATURES.md` (285 lines) ✅
- `05_cursor_agent_cli/ai_app_system/APPLICATION_IMPLEMENTED.md` (⏳ In Progress)
- `05_cursor_agent_cli/ai_app_system/COMPLETE_ARCHITECTURE.md` (⏳ Pending)
- `05_cursor_agent_cli/port_system/PORTING_STRATEGY.md` (⏳ Pending)

---

<!-- section_id: "47aea5b6-e23d-4a00-a913-0adaa91f88be" -->
## Common Patterns

All applications follow the same pattern:

<!-- section_id: "abbe6e04-c4d2-4eb1-b48b-9a018658c2ae" -->
### Pattern: Static Context Loading

```
0AGNOSTIC.md STATIC section
    ↓
Tool's native system instruction/configuration
    ↓
Loaded for every interaction
    ↓
Influences response generation
```

<!-- section_id: "2fd58b39-4cc6-40c2-8220-5e0b19166598" -->
### Pattern: Dynamic Context Management

```
0AGNOSTIC.md DYNAMIC section
    ↓
User implements as application code
    ↓
Triggered on-demand based on context
    ↓
Reads from .0agnostic/ resources
```

<!-- section_id: "77563e32-e2b1-4fe1-9a75-566c2bfa632c" -->
### Pattern: .0agnostic/ Directory Implementation

```
.0agnostic/01_knowledge/ → Documentation/comments
.0agnostic/02_rules/ → Application logic (static + dynamic)
.0agnostic/03_protocols/ → Step-by-step procedures (code templates)
.0agnostic/04_episodic_memory/ → Session storage (filesystem/database)
.0agnostic/05_handoff_documents/ → State serialization
.0agnostic/06_context_avenue_web/ → Configuration/skills
.0agnostic/07+_setup_dependant/ → Application-specific setup
```

---

<!-- section_id: "86876af3-b28a-4db3-8e2c-8c4620fecf72" -->
## How to Use This Documentation

<!-- section_id: "cd7de555-7aba-4968-b83d-62b435b0f2fb" -->
### For Understanding a Specific Tool:
1. Read `NATIVE_FEATURES.md` — understand what the tool provides
2. Read `APPLICATION_IMPLEMENTED.md` — understand your responsibilities
3. Read `COMPLETE_ARCHITECTURE.md` — see how they work together

<!-- section_id: "2c63915d-81c7-4648-945b-59f3c51c94fc" -->
### For Porting Your System:
1. Read `PORTING_STRATEGY.md` for the tool
2. Follow the step-by-step migration guide
3. Use the provided checklist to validate completion

<!-- section_id: "58074f09-d560-410c-af32-a2f70bb2f8e5" -->
### For Comparing Tools:
- Each `NATIVE_FEATURES.md` lists 10 mechanisms
- Each `APPLICATION_IMPLEMENTED.md` covers 7-8 decision areas
- Compare tables in each to see what's unique to each tool

---

<!-- section_id: "91b783f6-0776-4830-97fd-d7425845bb15" -->
## Key Takeaways

1. **Every tool has native mechanisms** — you understand these by reading NATIVE_FEATURES.md

2. **Every user makes strategic decisions** — understand these by reading APPLICATION_IMPLEMENTED.md

3. **The system works when both are aligned** — see examples in COMPLETE_ARCHITECTURE.md

4. **Porting is predictable** — follow the step-by-step guides in PORTING_STRATEGY.md files

5. **Patterns are consistent** — the same 0AGNOSTIC.md porting pattern works for all 5 tools, just maps to different native systems

---

<!-- section_id: "92a6e062-d850-4b22-b9fb-9968bd8faa52" -->
## Research Sources

Documentation based on:
- **Claude Code**: Official CLI documentation + hands-on testing
- **Codex**: Official API docs + claude-code community examples
- **Gemini**: Official SDK docs + practical implementation examples
- **Cursor IDE**: IDE configuration files + semantic search documentation
- **Cursor Agent CLI**: CLI command reference + execution model documentation

---

<!-- section_id: "c7685cbc-163b-4668-afe6-bbbbbc698ade" -->
## Next Steps

To complete all documentation:
1. Create Cursor IDE `port_system/PORTING_STRATEGY.md`
2. Create Cursor Agent CLI remaining 3 files
3. Optional: Create comparison matrices across all 5 tools

All documentation follows proven pattern — extension is straightforward.

