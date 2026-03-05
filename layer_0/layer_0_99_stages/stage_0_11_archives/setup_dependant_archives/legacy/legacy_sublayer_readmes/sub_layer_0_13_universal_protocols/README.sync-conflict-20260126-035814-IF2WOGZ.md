---
resource_id: "298fd170-0bca-4913-b35c-5978311ff4ba"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-035814-IF2WOGZ"
---
# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0_05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

## Migration Path

All setup documentation is now located in:
```
sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/
```

Navigate the file tree by your configuration:
1. Choose your OS: `0.05_operating_systems/<os>/`
2. Choose your environment: `0.06_environments/<env>/`
3. Choose your coding app: `0.07_coding_apps/<app>/`
4. Continue through all levels to find your specific setup documentation

## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# Universal Protocols

This sub-layer contains standard operating procedures (SOPs) and protocols that apply across all projects and features, ensuring consistent and high-quality execution of tasks.

It is organized as a **workflow feature**, following the same pattern described in the layer/stage framework:

- `0_instruction_docs/` – protocol definitions and standards (what the protocols are).
- `0.03_workflow_creation/` – manager system + stages for designing/maintaining protocol workflows.
- `0.04_workflows/` – concrete protocol workflows (how the protocols are applied step-by-step).
- `0.05_results/` – aggregated results, metrics, and retrospectives from running those workflows.

## Protocols

### 1. Verification
- **Small Batch Protocol**: `small_batch_verification/0_instruction_docs/small_batch_verification_protocol.md` - Guidelines for iterative testing and verification.

### 2. Research File Documentation & Organization
- **File Documentation Protocol**: `file_documentation_and_organization/0_instruction_docs/file_documentation_and_organization_protocol.md` - Steps for turning large raw files (e.g., chat transcripts, research logs) into structured `chat_history`, `things_learned`, and `overview` docs that are easy for agents to use.

### 3. Protocol Writing Standard
- **Protocol Writing Standard**: `protocol_writing_standard/0_instruction_docs/protocol_writing_standard.md` - Standard format and conventions for writing protocol documents, including OS/tool specificity conventions.

### 4. Memory Handling
- **Memory Handling Protocol**: `memory_handling/0_instruction_docs/memory_handling_protocol.md` - Guidelines for handling "remember this" requests and long-term memory storage.

### 5. Reordering Operations
- **Reordering Operations Protocol**: `reordering_operations/0_instruction_docs/reordering_operations_protocol.md` - Step-by-step guide for reordering numbered items (sub-layers, stages, etc.) in the context system, including required context loading and registry regeneration steps.

### 6. Framework Orchestration
- **Framework Orchestration Overview**: `framework_orchestration/0_instruction_docs/framework_orchestration_overview.md` - Guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. Explains when to use framework-based orchestration vs. simple handoff-based coordination, with minimal integration examples.

### 7. CLI Recursion
- **CLI Recursion Syntax**: `cli_recursion/0_instruction_docs/cli_recursion_syntax.md` - Concrete CLI recursion patterns for creating deep agent hierarchies where managers spawn workers via CLI commands. Includes OS-adapted examples for WSL/Ubuntu with Claude Code, Codex CLI, and Gemini CLI.

### 8. Observability and Logging
- **Observability Protocol**: `observability/README.md` - Structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. Defines log levels, structured formats, layer-specific requirements, handoff logging, manager/worker observability, metrics collection, distributed tracing, and audit trail requirements.

Over time, each protocol in `0_instruction_docs/` can be backed by:

- One or more **workflow definitions** in `0.03_workflow_creation/` and `0.04_workflows/`.
- Recorded **results and refinements** in `0.05_results/`.

This lets universal protocols evolve as first-class workflows, not just static documents.
