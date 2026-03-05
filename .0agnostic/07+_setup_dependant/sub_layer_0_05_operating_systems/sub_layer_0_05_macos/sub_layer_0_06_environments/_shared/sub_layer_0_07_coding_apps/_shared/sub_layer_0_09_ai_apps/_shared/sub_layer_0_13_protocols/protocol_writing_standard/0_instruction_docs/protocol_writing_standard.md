---
resource_id: "4653252c-0823-42a9-b838-0ef9ed08094d"
resource_type: "document"
resource_name: "protocol_writing_standard"
---
# Protocol Writing Standard

<!-- section_id: "0720105d-f3bd-47c5-b915-02c9a0b2c1f2" -->
## Applicability
**When to use:** Whenever creating or updating a protocol document at ANY layer (Universal, Project, Feature, or Component).
**Where to use:** The very first section of any `.md` file that defines a protocol or standard operating procedure (SOP).

<!-- section_id: "0bacc7c1-ec13-49d0-a216-9583e20e50ba" -->
## The Rule
Every protocol document **MUST** begin with an **Applicability** section immediately after the title.

<!-- section_id: "2c5d905c-0e45-47e5-9444-db78f52f3685" -->
### Structure
1.  **Title** (`# Protocol Name`)
2.  **Applicability** (`## Applicability`)
    *   **Context:** When does this apply?
    *   **Scope:** Where does this apply? (Universal, specific feature, specific OS?)
    *   **Triggers:** What specific user requests or error states trigger this protocol?
3.  **Body**: The actual rules and steps.

<!-- section_id: "aa673893-0296-473b-b35e-cc1113cb1a64" -->
## Why?
Efficiency. Agents scan documents to determine relevance. Placing "Applicability" at the top allows the agent to quickly decide whether to load the full context or skip it, saving context window space and processing time.

---

<!-- section_id: "829d6514-156f-4e90-9dfe-44d5efc2af77" -->
## OS and AI Tool Specificity Conventions

To make it clear whether a protocol is **OS/tool‑agnostic** or tied to specific environments/tools, use the following pattern inside the **Applicability → Scope** field:

- **Break Scope into explicit dimensions:**
  - `OS:` which OS variants this document applies to.
    - Use the same `os-id` values described in `os_and_quartets.md`, e.g. `universal`, `wsl`, `ubuntu`, `windows`, `macos`, `termux`, `custom-*`.
  - `Tools:` which AI tools this protocol is written for.
    - e.g. `universal`, or a list like `claude, gemini, codex, cursor`.

**Examples:**

- `**Scope:** OS: universal; Tools: universal (applies to any AI coding tool).`
- `**Scope:** OS: wsl | ubuntu; Tools: claude, gemini (examples given for these tools; others follow the same pattern).`

For **mixed documents** (mostly universal, with some OS/tool‑specific notes):

- Keep **most rules OS/tool‑agnostic**, but:
  - Mark specific sections with heading prefixes such as:
    - `### [OS: windows] PowerShell‑specific commands`
    - `### [Tool: codex] Codex CLI workflow example`
  - Or inline tags for short notes, e.g. “(applies to `[OS: wsl]` only)”.

This keeps a single protocol readable while still allowing agents (and wrapper scripts) to quickly identify:

- Which parts are **safe everywhere**, and
- Which parts must be **filtered or adapted** for a given OS or AI tool.

