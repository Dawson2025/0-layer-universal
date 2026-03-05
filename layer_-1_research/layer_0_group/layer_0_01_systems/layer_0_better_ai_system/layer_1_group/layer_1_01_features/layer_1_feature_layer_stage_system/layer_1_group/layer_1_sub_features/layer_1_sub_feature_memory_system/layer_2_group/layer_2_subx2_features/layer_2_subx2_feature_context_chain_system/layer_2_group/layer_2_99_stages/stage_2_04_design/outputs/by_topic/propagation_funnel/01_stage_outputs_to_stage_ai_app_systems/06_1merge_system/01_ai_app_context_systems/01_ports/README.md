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

## Overview

This directory contains comprehensive documentation for porting the 0AGNOSTIC.md system and .0agnostic/ directory into 5 different AI applications:

1. **Claude Code CLI** ✅ Complete (4 files)
2. **Codex CLI** ✅ Complete (4 files)
3. **Gemini SDK** ✅ Complete (3 files + 1 in progress)
4. **Cursor IDE** ✅ Mostly complete (3 files + 1 in progress)
5. **Cursor Agent CLI** ⚠️ Partial (1 file)

---

## File Structure

Each application has:
- **ai_app_system/** directory with 3 files:
  - `NATIVE_FEATURES.md` — What the tool provides natively (mechanisms)
  - `APPLICATION_IMPLEMENTED.md` — What users must create (strategy & content)
  - `COMPLETE_ARCHITECTURE.md` — How they work together

- **port_system/** directory with 1 file:
  - `PORTING_STRATEGY.md` — How to map 0AGNOSTIC.md and .0agnostic/ into the tool's native system

---

## Key Concepts

### Native vs. Application-Implemented

**Native** (Tool Provides):
- Mechanisms and features built into the tool
- Cannot be changed by users (except configuration)
- Examples: Gemini's system instructions, Cursor's .cursor/rules loading, Claude Code's context window management

**Application-Implemented** (User Provides):
- Content, strategy, and decisions
- What goes INTO native mechanisms
- Examples: Writing actual .cursor/rules content, deciding what to remember in Memory Bank, choosing which MCP servers to configure

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

## Completed Applications

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

## Common Patterns

All applications follow the same pattern:

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

## How to Use This Documentation

### For Understanding a Specific Tool:
1. Read `NATIVE_FEATURES.md` — understand what the tool provides
2. Read `APPLICATION_IMPLEMENTED.md` — understand your responsibilities
3. Read `COMPLETE_ARCHITECTURE.md` — see how they work together

### For Porting Your System:
1. Read `PORTING_STRATEGY.md` for the tool
2. Follow the step-by-step migration guide
3. Use the provided checklist to validate completion

### For Comparing Tools:
- Each `NATIVE_FEATURES.md` lists 10 mechanisms
- Each `APPLICATION_IMPLEMENTED.md` covers 7-8 decision areas
- Compare tables in each to see what's unique to each tool

---

## Key Takeaways

1. **Every tool has native mechanisms** — you understand these by reading NATIVE_FEATURES.md

2. **Every user makes strategic decisions** — understand these by reading APPLICATION_IMPLEMENTED.md

3. **The system works when both are aligned** — see examples in COMPLETE_ARCHITECTURE.md

4. **Porting is predictable** — follow the step-by-step guides in PORTING_STRATEGY.md files

5. **Patterns are consistent** — the same 0AGNOSTIC.md porting pattern works for all 5 tools, just maps to different native systems

---

## Research Sources

Documentation based on:
- **Claude Code**: Official CLI documentation + hands-on testing
- **Codex**: Official API docs + claude-code community examples
- **Gemini**: Official SDK docs + practical implementation examples
- **Cursor IDE**: IDE configuration files + semantic search documentation
- **Cursor Agent CLI**: CLI command reference + execution model documentation

---

## Next Steps

To complete all documentation:
1. Create Cursor IDE `port_system/PORTING_STRATEGY.md`
2. Create Cursor Agent CLI remaining 3 files
3. Optional: Create comparison matrices across all 5 tools

All documentation follows proven pattern — extension is straightforward.

