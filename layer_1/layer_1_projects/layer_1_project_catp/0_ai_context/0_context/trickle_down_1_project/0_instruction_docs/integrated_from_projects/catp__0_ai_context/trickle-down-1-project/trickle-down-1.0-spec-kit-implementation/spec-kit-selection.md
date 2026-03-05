---
resource_id: "a90c8244-52a1-4db2-ae1e-23a1aee82101"
resource_type: "document"
resource_name: "spec-kit-selection"
---
# GitHub Spec Kit Implementation for Language Tracker
*Trickle-Down Level 1.0: Project AI Coding System Selection*

<!-- section_id: "d2acbac1-dbc3-44aa-a246-ef7f3d9e7733" -->
## Our Choice: GitHub Spec Kit (Specification-Driven Development)

**Project Decision:** The Language Tracker project uses GitHub Spec Kit for AI-assisted development.

<!-- section_id: "7a8aa516-f8bf-4a55-b09b-50ce312fbf7e" -->
## Why We Chose Spec Kit for This Project

**Complexity:** High - Complex phoneme hierarchy, multiple storage backends, TDD framework
**Quality Requirements:** Highest - Linguistic accuracy is critical
**Timeline:** Long-term - Sustainable development approach needed

<!-- section_id: "071fe6af-887d-4586-86d6-14cf444dfeb2" -->
## Spec Kit Workflow for Language Tracker

<!-- section_id: "8e2d7c5c-af9a-4bae-aef4-df3887190672" -->
### Phase 1: Constitution
Command: /speckit.constitution
Input: TD1 constitution.md (our comprehensive project constitution)
Status: ✅ Ready - Constitution contains TDD framework, user stories, quality standards

<!-- section_id: "130ad915-52d6-412f-9b19-b1a654d4dc00" -->
### Phase 2: Feature Specification
Command: /speckit.specify [feature description]
Maps to: TD2 feature domains (authentication, learning, content, advanced, system)

<!-- section_id: "70794d45-4b6a-413e-87d3-b8d95f04ded3" -->
### Phase 3: Implementation Planning
Command: /speckit.plan
Context: WSL Ubuntu environment (TD0.5), project architecture standards

<!-- section_id: "6674f1d0-7293-49a8-82e3-b9c0bf96276c" -->
### Phase 4: Task Generation
Command: /speckit.tasks
Output: Parallelizable tasks for AI agents and developers

<!-- section_id: "151faafc-6057-4e47-acd4-68515b61f09b" -->
### Phase 5: Implementation
Command: /speckit.implement
Result: Working code that matches specifications, updates TD3 documentation

<!-- section_id: "15ae2e87-6a18-455b-bdcc-7d72f9672fd5" -->
## Installation & Setup

<!-- section_id: "e2f3adbc-1b2c-4b67-ab80-bebe1bb954d3" -->
### Install Specify CLI (WSL Ubuntu)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

<!-- section_id: "d32aede3-264e-47fa-a765-d4ad4cd52f0f" -->
### Initialize Project
specify init lang-trak-features --ai claude --here
specify check
