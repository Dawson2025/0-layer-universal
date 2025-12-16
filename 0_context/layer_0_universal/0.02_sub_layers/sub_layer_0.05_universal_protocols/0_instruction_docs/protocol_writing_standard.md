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
