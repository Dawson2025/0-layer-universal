---
resource_id: "aeb2c6c9-04e3-4434-aae8-f405ee79f965"
resource_type: "document"
resource_name: "protocol_writing_standard"
---
# Protocol Writing Standard

## Applicability
**When to use:** Whenever creating or updating a protocol document at ANY layer (Universal, Project, Feature, or Component).
**Where to use:** The very first section of any `.md` file that defines a protocol or standard operating procedure (SOP).

## The Rule
Every protocol document **MUST** begin with an **Applicability** section immediately after the title.

### Structure
1.  **Title** (`# Protocol Name`)
2.  **Applicability** (`## Applicability`)
    *   **Context:** When does this apply?
    *   **Scope:** Where does this apply? (Universal, specific feature, specific OS?)
    *   **Triggers:** What specific user requests or error states trigger this protocol?
3.  **Body**: The actual rules and steps.

## Why?
Efficiency. Agents scan documents to determine relevance. Placing "Applicability" at the top allows the agent to quickly decide whether to load the full context or skip it, saving context window space and processing time.

---

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

