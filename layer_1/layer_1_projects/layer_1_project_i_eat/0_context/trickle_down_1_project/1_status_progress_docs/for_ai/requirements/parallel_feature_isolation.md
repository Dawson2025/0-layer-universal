---
resource_id: "b812a960-05ab-4191-b1ca-560ee40a45ed"
resource_type: "document"
resource_name: "parallel_feature_isolation"
---
# Parallel Feature Isolation

- **Source Prompt**: Live session request (Codex CLI, parallel work guidance)

<!-- section_id: "fcab5b39-b3b6-4525-9195-b26b8e71a0c7" -->
## Goal
Establish conventions that let multiple contributors (human or AI) work on separate features without stepping on each other’s changes by keeping implementations, assets, and tests scoped to feature-specific files or directories.

<!-- section_id: "1aa71f09-d0f2-44b8-bfe3-5fe743733992" -->
## Functional Requirements
- Introduce or reinforce a file and directory structure where every feature has a clearly named home (e.g., `features/<feature_name>/`) for its views, logic, and tests.
- When implementing or updating a feature, confine edits to that feature’s directory unless platform-wide changes are explicitly required.
- Add guidance for cross-cutting updates (styles, shared components, data migrations) that explains how to stage them so they minimize conflicts (e.g., staging utility refactors before feature work).
- Ensure each feature directory includes colocated automated tests that can be executed independently.
- Document the naming and organization rules in the Codex instructions so future prompts automatically follow the same isolation pattern.

<!-- section_id: "06e71f4a-01ec-4571-8bd2-527160296b14" -->
## Acceptance Criteria
- Codex instructions explicitly tell contributors to create or reuse feature-scoped directories before starting implementation.
- The repository structure includes clear examples (existing or newly added) that show how to place feature code, assets, and tests together (e.g., `features/firebase/`, `features/projects/`).
- When future features are added, their commits touch only the relevant feature directories plus shared infrastructure where justified in the prompt or spec.
- Running the feature’s tests does not require touching unrelated modules because dependencies live in its directory or shared utility layers.

<!-- section_id: "141f6555-2f89-4105-a4b5-5026740e89d6" -->
## Notes
- Existing mixed-content directories should be gradually split during the next time they are touched rather than through a disruptive repo-wide refactor.
- Consider enforcing the conventions with linting or CI checks (e.g., validating directory placement) once the structure stabilizes.
