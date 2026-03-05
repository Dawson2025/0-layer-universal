---
resource_id: "04f4ff9d-fac4-4c77-83f6-288df7ef3ec3"
resource_type: "document"
resource_name: "spec-kit-guide"
---
# GitHub Spec Kit - Comprehensive Guide
*Spec-Driven Development Framework for AI Coding Agents*

<!-- section_id: "2ecc888c-99a7-4a7e-a02b-5170541f4daa" -->
## Overview

GitHub Spec Kit is an open-source toolkit designed to facilitate spec-driven development with AI coding agents. It transforms ad-hoc prompting into structured, verifiable development workflows by organizing development into four gated phases with validation checkpoints.

<!-- section_id: "6439fa83-f3ab-46c1-b96c-c61f183bd1f0" -->
## Key Concepts

<!-- section_id: "53b45391-cb16-40a7-9e09-9a80a4f619ee" -->
### What is Spec-Driven Development?

Spec-driven development is a methodology where:
- **Specifications** are defined before implementation
- **Development** follows structured phases
- **Validation** occurs at each phase
- **Artifacts** are version-controlled alongside code

<!-- section_id: "9147156e-5bd0-42a1-b7ce-ac90d95e7050" -->
### Core Philosophy

**Problem**: AI coding agents are only as good as the instructions and context they receive.

**Solution**: Provide structured methodologies that transform vague prompts into precise, implementable specifications, significantly improving development velocity and code quality.

<!-- section_id: "c7014341-b59d-49c9-bcb7-948f8c738e0c" -->
## Key Features

<!-- section_id: "f460e9ba-e188-47b2-9047-c0e812e4f50c" -->
### 1. Four-Phase Validation Process

```
Phase 1: Specification → Phase 2: Planning → Phase 3: Tasks → Phase 4: Implementation
```

Each phase has validation checkpoints ensuring quality before proceeding.

<!-- section_id: "5dd04444-8956-4c42-9500-0164b02dd0dd" -->
### 2. CLI Tools and Templates

- **Specify CLI**: Command-line tool for managing specifications
- **Templates**: Pre-built templates for common project types
- **Steering Prompts**: Structured prompts to guide AI agents

<!-- section_id: "d42073fe-cdfe-471a-802a-1572056cff40" -->
### 3. Version-Controlled Specifications

- Specifications live alongside your code
- Git-based versioning of all artifacts
- Traceability from spec to implementation

<!-- section_id: "e888d834-cf95-4f25-ac3b-d51f164537ef" -->
### 4. AI Tool Integration

Works seamlessly with:
- **GitHub Copilot**
- **Claude Code**
- **Gemini CLI**
- Other AI coding tools

<!-- section_id: "d62166b7-2b1a-422b-9e37-60c4ab30d6c4" -->
## Installation

<!-- section_id: "d4ef419f-e2d2-4e2e-ba5e-a078366422af" -->
### Prerequisites

- Python 3.11+
- `uv` package manager

<!-- section_id: "a112328e-06b1-4fdd-a412-3cd37e146b71" -->
### Install Specify CLI

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

<!-- section_id: "0f7a6bca-c41e-4d58-a1a0-e28959877bb0" -->
### Verify Installation

```bash
specify --version
```

<!-- section_id: "e84f7894-925c-49d8-b76f-d775429d704e" -->
## Getting Started

<!-- section_id: "fd809338-40dd-4a99-9f09-3d4e7bcb2c57" -->
### Step 1: Initialize a New Project

```bash
specify init my-project --ai copilot
```

Replace `my-project` with your desired project name and `copilot` with your preferred AI tool.

<!-- section_id: "c2ecd6f2-611a-4b74-8112-78e3c63def7c" -->
### Step 2: Define Your Specification

Use the `/specify` command to outline your project:

```bash
/specify Build a task management app with user authentication, real-time collaboration, and mobile support.
```

This creates a specification document that guides all subsequent development.

<!-- section_id: "12706038-1fe0-43c7-9eaf-d6bcd4b6f74d" -->
### Step 3: Generate Implementation Plan

Use the `/plan` command to create a technical implementation plan:

```bash
/plan Use React with TypeScript, Node.js backend, PostgreSQL database
```

This generates an implementation plan based on your specification.

<!-- section_id: "05be43f6-e107-49cb-a080-48291d27fb32" -->
### Step 4: Generate Task Breakdown

Use the `/tasks` command to break down the plan into actionable tasks:

```bash
/tasks
```

This creates a `tasks.md` file with tasks ordered by dependencies.

<!-- section_id: "fa7eaa79-065c-4ae0-a44a-b6274c985929" -->
### Step 5: Implement

Use the `/implement` command to execute the implementation:

```bash
/implement
```

The AI agent will execute tasks in the correct order, respecting dependencies.

<!-- section_id: "ce14168e-cfc4-4db8-895b-9ce6527b93c9" -->
## Command Reference

<!-- section_id: "3d0034a2-5644-451e-9691-87902d1ddc63" -->
### Core Commands

#### `/specify`
Define your project specification.

**Usage**:
```bash
/specify [description of what to build]
```

**Example**:
```bash
/specify Create a REST API for a blog system with user authentication, post management, and comment system.
```

#### `/plan`
Generate technical implementation plan.

**Usage**:
```bash
/plan [technical stack and requirements]
```

**Example**:
```bash
/plan Use FastAPI with Python, PostgreSQL database, JWT authentication, and Redis caching.
```

#### `/tasks`
Generate task breakdown from implementation plan.

**Usage**:
```bash
/tasks
```

**Output**: Creates `tasks.md` with:
- Task breakdown by user story
- Dependency management
- Parallel execution markers `[P]`
- File path specifications
- Checkpoint validation

#### `/implement`
Execute the implementation plan.

**Usage**:
```bash
/implement
```

**Behavior**:
- Validates prerequisites (constitution, spec, plan, tasks)
- Parses task breakdown from `tasks.md`
- Executes tasks in correct order
- Respects dependencies and parallel execution markers
- Follows TDD approach if defined
- Provides progress updates

<!-- section_id: "a7d78078-197a-4f10-83c4-95150890564e" -->
## Project Structure

After initialization, your project will have this structure:

```
.
├── CLAUDE.md
├── memory
│   └── constitution.md              # Project constitution
├── scripts
│   ├── check-prerequisites.sh
│   ├── common.sh
│   ├── create-new-feature.sh
│   ├── setup-plan.sh
│   └── update-claude-md.sh
├── specs
│   └── 001-create-taskify
│       ├── contracts
│       │   ├── api-spec.json        # API specifications
│       │   └── signalr-spec.md       # Real-time specifications
│       ├── data-model.md            # Data model
│       ├── plan.md                  # Implementation plan
│       ├── quickstart.md            # Quick start guide
│       ├── research.md              # Technology research
│       └── spec.md                  # Feature specification
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

<!-- section_id: "e53f82f4-5638-4c35-9f1d-fc0035d9e77b" -->
## Workflow Example

<!-- section_id: "aaeeb0e7-2b16-4a7a-899f-a9433660fd91" -->
### Scenario: Building a Task Management App

#### 1. Define Specification

```bash
/specify Build a task management application called "Taskify" with:
- User authentication (email/password)
- Project and task CRUD operations
- Real-time collaboration using SignalR
- Drag-and-drop task boards
- Mobile support
```

**Output**: `specs/001-create-taskify/spec.md`

#### 2. Generate Technical Plan

```bash
/plan We are going to generate this using .NET Aspire, using Postgres as the database. 
The frontend should use Blazor server with drag-and-drop task boards, real-time updates. 
There should be a REST API created with a projects API, tasks API, and a notifications API.
```

**Output**: `specs/001-create-taskify/plan.md`

#### 3. Review and Refine

Check the `research.md` document to ensure the right tech stack is used.

If needed, refine:
```bash
I want you to go through the implementation plan and implementation details, looking for 
areas that could benefit from additional research as .NET Aspire is a rapidly changing 
library. For those areas that you identify that require further research, I want you to 
update the research document with additional details about the specific versions that 
we are going to be using in this Taskify application.
```

#### 4. Validate the Plan

```bash
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks 
that you need to be doing that are obvious from reading this. Because I don't know if 
there's enough here. For example, when I look at the core implementation, it would be 
useful to reference the appropriate places in the implementation details where it can find 
the information as it walks through each step in the core implementation or in the refinement.
```

#### 5. Generate Tasks

```bash
/tasks
```

**Output**: `tasks.md` with structured tasks

#### 6. Implement

```bash
/implement
```

The AI agent will now execute all tasks in the correct order.

<!-- section_id: "3636ae77-9a58-4b08-bc47-7180abb82639" -->
## Directory Structure Details

<!-- section_id: "63a7b24d-1823-4835-944f-ffcdc8cc527b" -->
### `specs/`
Contains all feature specifications organized by feature number.

#### `specs/001-create-taskify/`
Each feature directory contains:

- **`spec.md`**: Feature specification with requirements and acceptance criteria
- **`plan.md`**: Technical implementation plan
- **`tasks.md`**: Task breakdown (generated by `/tasks`)
- **`data-model.md`**: Database schema and data models
- **`research.md`**: Technology research and decisions
- **`quickstart.md`**: Quick start guide for the feature
- **`contracts/`**: API and interface specifications
  - **`api-spec.json`**: OpenAPI/REST API specification
  - **`signalr-spec.md`**: Real-time communication specifications

<!-- section_id: "f26319e0-3f3b-4e6d-be63-f39da7baceab" -->
### `memory/`
Project memory and constitution.

- **`constitution.md`**: Project standards, coding guidelines, and principles

<!-- section_id: "4826ebdb-b711-4b86-b913-f66db93af88e" -->
### `scripts/`
Helper scripts for managing specifications.

- **`check-prerequisites.sh`**: Validate system requirements
- **`setup-plan.sh`**: Initialize new feature
- **`create-new-feature.sh`**: Create new feature specification
- **`update-claude-md.sh`**: Update Claude configuration

<!-- section_id: "82a168c0-01b2-421b-b712-a57cbe810511" -->
### `templates/`
Template files for creating new specifications.

- **`spec-template.md`**: Feature specification template
- **`plan-template.md`**: Implementation plan template
- **`tasks-template.md`**: Task breakdown template
- **`CLAUDE-template.md`**: Claude agent configuration template

<!-- section_id: "f17fa77d-7b1a-4a3a-b1c1-af7d61431161" -->
## Best Practices

<!-- section_id: "48b7a809-6148-4bbf-9879-2cd426cf93a8" -->
### Specification Writing

1. **Be Specific**: Include acceptance criteria and technical requirements
2. **Include Context**: Explain the business problem being solved
3. **Define Scope**: Clearly state what's included and what's not
4. **Use Examples**: Provide concrete examples of expected behavior

<!-- section_id: "2607e1b8-ce5b-4c5f-9129-7d4164d7310b" -->
### Planning

1. **Research First**: Check `research.md` before making technology decisions
2. **Consider Dependencies**: Plan for dependency management
3. **Think About Testing**: Include testing strategy in your plan
4. **Estimate Effort**: Consider complexity and timeline

<!-- section_id: "61081b65-9692-4864-8dca-8c8cb10ece35" -->
### Task Generation

1. **Check Prerequisites**: Ensure all prerequisites are defined
2. **Order Matters**: Tasks must respect dependencies
3. **Mark Parallel**: Use `[P]` for tasks that can run in parallel
4. **Include Checkpoints**: Add validation steps between phases

<!-- section_id: "8667f6e6-a66e-4814-b73c-1bf472973a0e" -->
### Implementation

1. **Follow the Plan**: Stick to the technical decisions in your plan
2. **Respect Dependencies**: Execute tasks in the correct order
3. **Test Incrementally**: Test after each phase
4. **Document Changes**: Update specs if requirements change

<!-- section_id: "6bdd1c2b-10c5-4fb6-88b7-581f3a5a9e5b" -->
## Advanced Features

<!-- section_id: "8d3d02b8-d63a-40d7-b5a9-5843463b70d1" -->
### Multi-Feature Development

Create multiple features within the same project:

```bash
/specify Create user authentication feature with OAuth support
# Generates: specs/002-user-authentication/spec.md

/specify Add notification system with email and in-app notifications
# Generates: specs/003-notification-system/spec.md
```

Each feature can be developed independently while sharing the same constitution and base configuration.

<!-- section_id: "55c70bba-32e8-40af-90e3-4fd15fc64e46" -->
### Custom Templates

Create project-specific templates:

1. Add custom template to `templates/`
2. Reference in feature specification
3. Use in `/specify` command

<!-- section_id: "d753807c-ac3f-43fc-932b-f66c115a3979" -->
### Integration with Existing Projects

You can add Spec Kit to existing projects:

```bash
# Navigate to existing project
cd /path/to/existing-project

# Initialize Spec Kit
specify init --ai copilot --existing

# This preserves your existing code while adding specification structure
```

<!-- section_id: "813e6bc0-cf7a-4855-a2b4-3f844a307d1a" -->
## Troubleshooting

<!-- section_id: "f2c87ff4-01f2-434e-b941-aff00c9ce4b1" -->
### Common Issues

#### Issue: Tasks not generating

**Solution**: Check that prerequisites are met:
```bash
bash scripts/check-prerequisites.sh
```

#### Issue: AI agent not following spec

**Solution**: Verify constitution is properly configured:
```bash
cat memory/constitution.md
```

#### Issue: Implementation diverging from plan

**Solution**: Review and refine the plan:
```bash
# Edit specs/[feature]/plan.md to align with implementation direction
```

<!-- section_id: "735b9234-751c-4aee-9ab3-b7e6f89776aa" -->
### Validation Checkpoints

If implementation fails validation:

1. Review error messages
2. Check `tasks.md` for missing dependencies
3. Verify `spec.md` is complete and clear
4. Ensure `constitution.md` is properly configured

<!-- section_id: "7a30c315-ff00-4fff-95eb-53cc9bdfc9c5" -->
## Resources

<!-- section_id: "83476c26-a619-45c3-836b-949ef3398121" -->
### Official Documentation
- **Website**: https://speckit.org/
- **Documentation**: https://speckit.org/guide
- **GitHub**: https://github.com/github/spec-kit

<!-- section_id: "401e8a94-33ae-4d68-9090-d1dcb9fdfd86" -->
### Community
- **Issues**: https://github.com/github/spec-kit/issues
- **Discussions**: https://github.com/github/spec-kit/discussions

<!-- section_id: "f108a332-2a17-44ec-bdcb-206218f50253" -->
### Examples
- **Quick Start**: See `specs/[feature]/quickstart.md` in any initialized project
- **Templates**: Check `templates/` directory

<!-- section_id: "910d653b-07e6-4d67-97e0-8bcd5c0f5607" -->
## Summary

GitHub Spec Kit provides:

- ✅ **Structured Development**: 4-phase validation process
- ✅ **Version Control**: Specifications alongside code
- ✅ **AI Integration**: Works with Copilot, Claude Code, Gemini CLI
- ✅ **Quality Assurance**: Validation checkpoints at each phase
- ✅ **Traceability**: Complete audit trail from spec to code

**Key Benefit**: Transforms vague prompts into precise, implementable specifications that significantly improve development velocity and code quality.

---

*For detailed API documentation, architecture patterns, and advanced usage, refer to the official documentation at https://speckit.org/.*

