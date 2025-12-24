# Universal Protocols

This sub-layer contains standard operating procedures (SOPs) and protocols that apply across all projects and features, ensuring consistent and high-quality execution of tasks.

It is organized as a **workflow feature**, following the same pattern described in the layer/stage framework:

- `0_instruction_docs/` – protocol definitions and standards (what the protocols are).
- `0.03_workflow_creation/` – manager system + stages for designing/maintaining protocol workflows.
- `0.04_workflows/` – concrete protocol workflows (how the protocols are applied step-by-step).
- `0.05_results/` – aggregated results, metrics, and retrospectives from running those workflows.

## Protocols

### 1. Verification
- **Small Batch Protocol**: `0_instruction_docs/small_batch_verification_protocol.md` - Guidelines for iterative testing and verification.

### 2. Research File Documentation & Organization
- **File Documentation Protocol**: `0_instruction_docs/file_documentation_and_organization_protocol.md` - Steps for turning large raw files (e.g., chat transcripts, research logs) into structured `chat_history`, `things_learned`, and `overview` docs that are easy for agents to use.

Over time, each protocol in `0_instruction_docs/` can be backed by:

- One or more **workflow definitions** in `0.03_workflow_creation/` and `0.04_workflows/`.
- Recorded **results and refinements** in `0.05_results/`.

This lets universal protocols evolve as first-class workflows, not just static documents.
