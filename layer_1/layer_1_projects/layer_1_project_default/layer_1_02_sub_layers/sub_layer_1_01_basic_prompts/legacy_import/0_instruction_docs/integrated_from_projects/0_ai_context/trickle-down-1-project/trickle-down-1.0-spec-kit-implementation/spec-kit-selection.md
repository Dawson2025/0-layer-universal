---
resource_id: "d8f6b271-1bfb-405d-9ecd-e0449607d29c"
resource_type: "document"
resource_name: "spec-kit-selection"
---
# GitHub Spec Kit Implementation for Language Tracker
*Trickle-Down Level 1.0: Project AI Coding System Selection*

<!-- section_id: "14bb10ce-7b02-45ad-9ccd-78c9ee738e10" -->
## Our Choice: GitHub Spec Kit (Specification-Driven Development)

**Project Decision:** The Language Tracker project uses GitHub Spec Kit for AI-assisted development.

<!-- section_id: "09df00c5-adf1-430a-ac2c-438faac5e8e4" -->
## Why We Chose Spec Kit for This Project

**Complexity:** High - Complex phoneme hierarchy, multiple storage backends, TDD framework
**Quality Requirements:** Highest - Linguistic accuracy is critical
**Timeline:** Long-term - Sustainable development approach needed

<!-- section_id: "35519c9c-d3a6-4b1c-bff7-94d5aff1c848" -->
## Spec Kit Workflow for Language Tracker

<!-- section_id: "879d4354-566c-46d0-99fb-a1f0a81574af" -->
### Phase 1: Constitution
Command: /speckit.constitution
Input: TD1 constitution.md (our comprehensive project constitution)
Status: ✅ Ready - Constitution contains TDD framework, user stories, quality standards

<!-- section_id: "6f32a5d3-dd31-4f29-b2ac-1210ddf95a67" -->
### Phase 2: Feature Specification
Command: /speckit.specify [feature description]
Maps to: TD2 feature domains (authentication, learning, content, advanced, system)

<!-- section_id: "5ca5f1db-beaa-401a-b493-5e3981934841" -->
### Phase 3: Implementation Planning
Command: /speckit.plan
Context: WSL Ubuntu environment (TD0.5), project architecture standards

<!-- section_id: "0c6e7396-40ea-4dc3-a1e1-c54870d0f254" -->
### Phase 4: Task Generation
Command: /speckit.tasks
Output: Parallelizable tasks for AI agents and developers

<!-- section_id: "41a27723-cdf1-4448-9bb1-82f5685e815a" -->
### Phase 5: Implementation
Command: /speckit.implement
Result: Working code that matches specifications, updates TD3 documentation

<!-- section_id: "7921021a-a4f5-48a9-85ad-fa8c20320eda" -->
## Installation & Setup

<!-- section_id: "10a96c15-3f8d-438b-a7b4-982f4d5e9a29" -->
### Install Specify CLI (WSL Ubuntu)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

<!-- section_id: "f93f09f7-3fe0-4894-9e44-1055850be47f" -->
### Initialize Project
specify init lang-trak-features --ai claude --here
specify check
