---
resource_id: "3377587c-671e-4333-bb69-33d96bcc87c8"
resource_type: "readme
document"
resource_name: "README"
---
# Universal Protocols

This sub-layer contains standard operating procedures (SOPs) and protocols that apply across all projects and features, ensuring consistent and high-quality execution of tasks.

It is organized as a **workflow feature**, following the same pattern described in the layer/stage framework:

- `0_instruction_docs/` – protocol definitions and standards (what the protocols are).
- `0.03_workflow_creation/` – manager system + stages for designing/maintaining protocol workflows.
- `0.04_workflows/` – concrete protocol workflows (how the protocols are applied step-by-step).
- `0.05_results/` – aggregated results, metrics, and retrospectives from running those workflows.

<!-- section_id: "8a7ac77c-0f56-4d6f-a3d0-e5a42171667f" -->
## Protocols

<!-- section_id: "e32264e6-b951-469d-b6ff-c37a095f716f" -->
### 1. Verification
- **Small Batch Protocol**: `small_batch_verification/0_instruction_docs/small_batch_verification_protocol.md` - Guidelines for iterative testing and verification.

<!-- section_id: "b3e1d9bb-05bc-4d44-ade7-ee8e6b1c28ff" -->
### 2. Research File Documentation & Organization
- **File Documentation Protocol**: `file_documentation_and_organization/0_instruction_docs/file_documentation_and_organization_protocol.md` - Steps for turning large raw files (e.g., chat transcripts, research logs) into structured `chat_history`, `things_learned`, and `overview` docs that are easy for agents to use.

<!-- section_id: "2d5cb63f-56a8-412b-a634-04caef148421" -->
### 3. Protocol Writing Standard
- **Protocol Writing Standard**: `protocol_writing_standard/0_instruction_docs/protocol_writing_standard.md` - Standard format and conventions for writing protocol documents, including OS/tool specificity conventions.

<!-- section_id: "62ce6828-666a-482d-92c8-2dce54b10751" -->
### 4. Memory Handling
- **Memory Handling Protocol**: `memory_handling/0_instruction_docs/memory_handling_protocol.md` - Guidelines for handling "remember this" requests and long-term memory storage.

<!-- section_id: "10142f48-c707-473f-a527-62bb89a1c7ab" -->
### 5. Reordering Operations
- **Reordering Operations Protocol**: `reordering_operations/0_instruction_docs/reordering_operations_protocol.md` - Step-by-step guide for reordering numbered items (sub-layers, stages, etc.) in the context system, including required context loading and registry regeneration steps.

<!-- section_id: "b1b842cd-b439-4f09-a9ee-dd217dbfd62f" -->
### 6. Framework Orchestration
- **Framework Orchestration Overview**: `framework_orchestration/0_instruction_docs/framework_orchestration_overview.md` - Guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. Explains when to use framework-based orchestration vs. simple handoff-based coordination, with minimal integration examples.

<!-- section_id: "d9ced403-e3c1-4f37-a69f-91150cc45655" -->
### 7. CLI Recursion
- **CLI Recursion Syntax**: `cli_recursion/0_instruction_docs/cli_recursion_syntax.md` - Concrete CLI recursion patterns for creating deep agent hierarchies where managers spawn workers via CLI commands. Includes OS-adapted examples for WSL/Ubuntu with Claude Code, Codex CLI, and Gemini CLI.

<!-- section_id: "89a61770-91df-4653-b704-7eec08b220fa" -->
### 8. Observability and Logging
- **Observability Protocol**: `observability/README.md` - Structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. Defines log levels, structured formats, layer-specific requirements, handoff logging, manager/worker observability, metrics collection, distributed tracing, and audit trail requirements.

Over time, each protocol in `0_instruction_docs/` can be backed by:

- One or more **workflow definitions** in `0.03_workflow_creation/` and `0.04_workflows/`.
- Recorded **results and refinements** in `0.05_results/`.

This lets universal protocols evolve as first-class workflows, not just static documents.
