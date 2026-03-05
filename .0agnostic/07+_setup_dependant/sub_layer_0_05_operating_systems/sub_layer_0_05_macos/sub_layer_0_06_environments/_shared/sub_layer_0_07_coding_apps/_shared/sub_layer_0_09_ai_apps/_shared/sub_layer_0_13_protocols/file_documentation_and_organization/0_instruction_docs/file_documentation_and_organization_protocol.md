---
resource_id: "f42cc068-98d9-4e5d-a4f9-d0e7467efb25"
resource_type: "document"
resource_name: "file_documentation_and_organization_protocol"
---
# File Documentation and Organization Protocol

<!-- section_id: "3facf5ac-c205-40f1-af10-d20dd9a55bf4" -->
## Applicability
**Context:** Use this protocol whenever you have a large or complex source file (chat transcript, research article, design doc, log, etc.) that you want to turn into durable, agent-friendly documentation and structure (e.g., like the `ai-manager-hierarchy-system-research.md` flow).  
**Scope:** OS: universal; Tools: universal – applies to any project, feature, or component that is using the `-1_research` area and/or layered context system, regardless of OS or AI coding tool.  
**Triggers:**  
- A raw file has grown large enough that agents struggle to load or navigate it in one shot.  
- You want to convert a “thing being researched” into a reusable spec (with `chat_history`, `things_learned`, and `overview` docs).  
- You need a repeatable way for agents to summarize, cross‑reference, and store learnings from any long file.

---

<!-- section_id: "2099cc8c-915d-4814-acc2-ab61bc303b97" -->
## 1. Inputs and Target Structure

- **Input:**  
  - One or more “source” files (often in `-1_research/chat_history/`), e.g. a long markdown transcript or research log.

- **Target structure (per researched topic):**  
  Under `-1_research/-1.01_things_researched/<topic_slug>/`:
  - `chat_history/`  
    - Raw or minimally processed source files (original transcripts, logs, notes).
  - `things_learned/`  
    - Distilled specs, designs, and “ideal system” docs derived from the raw material.
  - `overview/`  
    - Short, context‑window‑friendly README(s) that explain the topic and point to the detailed docs.

---

<!-- section_id: "e139a487-98c8-4e5f-bf1a-6e222aeb6f43" -->
## 2. Step 1 – Create/Select the “Thing Researched” Container

1. **Name the topic**  
   - Choose a short, stable slug for the subject (e.g., `ai_manager_hierarchy_system`, `ai_dynamic_memory_system`, `workflow_orchestration`, `security_principles`).

2. **Create or reuse the container directory**  
   - Path: `code/0_layer_universal/0_context/-1_research/-1.01_things_researched/<topic_slug>/`
   - Inside it, ensure these subdirectories exist:
     - `chat_history/`
     - `things_learned/`
     - `overview/`

3. **Place/link raw files**  
   - Move or copy the source file(s) into `chat_history/` (or create a clear pointer/README there if they must remain elsewhere).
   - Do **not** heavily edit the raw files; preserve them as ground truth.

---

<!-- section_id: "d7aba933-9adf-4c3c-a48e-fce79197abda" -->
## 3. Step 2 – Discovery Pass (Concept Mapping, No Filtering)

1. **Read the entire source file** (or as much as context allows, in batches if necessary).  
2. **Extract all notable concepts** into a scratch list or concept map:
   - Tools, models, frameworks.
   - Architectural patterns, protocols, and flows.
   - Pros/cons, limitations, failure modes, workarounds.
   - OS/env considerations.
   - Any explicit “rules”, “principles”, or “policies”.
3. **Tag each concept** (mentally or explicitly) with broad categories:
   - e.g., `[architecture]`, `[tooling]`, `[context]`, `[handoff]`, `[orchestration]`, `[OS]`, `[policy]`, `[failure_mode]`, `[meta]`.
4. **Do not discard anything** at this stage:
   - The goal is **coverage**, not prioritization.
   - Every distinct theme should be discoverable later in a “things learned” doc or appendix.
5. **Let themes emerge from the text**:
   - Notice which ideas are repeated, explicitly called out as important, or tied to many other parts of the system.
   - Do **not** decide in advance what the topic “is about” or which details “matter” until after this pass.
6. **Keep raw notes neutral**:
   - Treat this step as data collection; interpretation and structuring come later in the “things learned” docs.

---

<!-- section_id: "f531b142-c4f0-43f0-9a9d-01e439f6f1b7" -->
## 4. Step 3 – Build “Things Learned” Documents

1. **Create a topic‑specific subfolder (optional but recommended):**
   - e.g., `things_learned/ideal_ai_manager_hierarchy_system/`
2. **Create the following, tailored to the topic (names are examples, not mandatory):**
   - `summary/README.md`  
     - Short overview: purpose, core ideas, and pointers to deeper docs.  
     - Designed to fit easily within an AI agent’s context window.
   - `summary/<TOPIC>_SPEC.md` (or similar)  
     - Long‑form “ideal system”/specification derived from the research.  
     - Pattern‑first, summary‑neutral, and open‑world (does not exclude unmentioned details).
   - Additional focused docs as needed (examples):
     - `architecture.md` – layers, stages, managers/workers, handoffs, supervisors.
     - `tools_and_context_systems.md` – roles and behaviors of tools/models and their context files.
     - `os_and_quartets.md` – OS variants, environment‑specific context, and quartets.
     - `token_and_policy_strategy.md` – cost and responsibility assignment.
   - For large topics, prefer **several focused documents** over one giant spec (e.g., one each for architecture, tools, OS variants, and policy), all linked from the summary.

3. **Link back to the source**  
   - In the main spec and/or overview, include a “Sources” or “Derived from” line that points back to the canonical `chat_history/` file(s).

---

<!-- section_id: "a59980f7-96b4-46f2-978e-c25474394784" -->
## 5. Step 4 – Summary‑Neutral, Pattern‑First Writing Rules

When authoring the “things learned” docs:

1. **Don’t assume the topic scope in advance**  
   - Base the document structure on what actually appears in the source: recurring themes, explicit goals, relationships.
2. **Use patterns before instances**  
   - Define generic patterns (e.g., “Tool Interface”, “Layered hierarchy”, “Handoff schema”), then show concrete instances (Claude, Codex, Gemini, specific OSes).
3. **Non‑exclusion principle**  
   - Make it clear that unmentioned tools or future concepts are not “forbidden”; any element that fits the patterns is allowed.
4. **Coverage check at the end**  
   - Re‑scan the concept map vs. the final docs.  
   - Ensure every major topic from the source shows up at least once (in main sections or in an “Additional Concepts and Notes” area).
5. **Explicit scope, not hidden assumptions**  
   - In each major spec, briefly state *why* it focuses on particular themes (e.g., “this document emphasizes X/Y/Z because the research repeatedly highlights them”), and list other themes that appear in the source even if they are secondary.
6. **No silent discards**  
   - If a theme from the source does not fit the main structure, surface it in an appendix or “Additional Concepts and Notes” section rather than omitting it entirely.
7. **Allow flexible structure**  
   - Use the pattern sections above as a starting point, but add or reorder sections when the source strongly emphasizes new themes (e.g., security/governance, human‑in‑the‑loop ergonomics, failure modes).

---

<!-- section_id: "1a19740b-0420-41bd-ac4f-ad5050dfc582" -->
## 6. Step 5 – Overview Documents for Agents

1. **In `overview/` for each topic**, create a very short `README.md` that:
   - Explains the topic in 1–3 short sections.
   - States where the detailed specs live (paths in `things_learned/`).
   - States where the raw chat history lives.
2. **Use this `overview/README.md` as the default context** when priming an AI agent:
   - It should be small enough to include in almost any session.
   - It should make it obvious which other documents to load for more depth.

---

<!-- section_id: "946d0f51-eabf-4653-8bf4-d55ededa72d7" -->
## 7. Maintenance Rules

1. **Never delete raw `chat_history/` files** once organized; only append or supersede them with clearly versioned successors.  
2. **Update “things learned” docs incrementally** as new research accumulates:
   - Append new sections.
   - Add new linked docs rather than bloating existing ones beyond what fits reasonably in an agent’s context.  
3. **Keep overviews small and stable**:
   - If overviews grow too large, refactor: push detail down into `things_learned/` and keep only the key pointers and mental model at the top.


