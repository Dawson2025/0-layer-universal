---
resource_id: "711ac0d9-52f6-4cec-9206-afeb93a4ac22"
resource_type: "document"
resource_name: "spec-kit-guide"
---
# GitHub Spec Kit - Comprehensive Guide
*Spec-Driven Development Framework for AI Coding Agents*

<!-- section_id: "40fcc23d-e394-4e81-acff-9e2ae67ea125" -->
## Overview

GitHub Spec Kit is an open-source toolkit designed to facilitate spec-driven development with AI coding agents. It transforms ad-hoc prompting into structured, verifiable development workflows by organizing development into four gated phases with validation checkpoints.

<!-- section_id: "3bc2fc57-6900-4777-924e-d98480534a89" -->
## Key Concepts

<!-- section_id: "5a150315-fb42-4cf6-958a-41ef5ffc1cdd" -->
### What is Spec-Driven Development?

Spec-driven development is a methodology where:
- **Specifications** are defined before implementation
- **Development** follows structured phases
- **Validation** occurs at each phase
- **Artifacts** are version-controlled alongside code

<!-- section_id: "107fcfbf-9793-4d42-8789-d0860d4643e0" -->
### Core Philosophy

**Problem**: AI coding agents are only as good as the instructions and context they receive.

**Solution**: Provide structured methodologies that transform vague prompts into precise, implementable specifications, significantly improving development velocity and code quality.

<!-- section_id: "e7d6c1ce-8d67-4992-944e-7f27ab219f57" -->
## Key Features

<!-- section_id: "4124dc0e-b9ff-4251-9911-671ebab00236" -->
### 1. Four-Phase Validation Process

```
Phase 1: Specification → Phase 2: Planning → Phase 3: Tasks → Phase 4: Implementation
```

Each phase has validation checkpoints ensuring quality before proceeding.

<!-- section_id: "7d1ab81e-30aa-470e-bbc2-82074d110a23" -->
### 2. CLI Tools and Templates

- **Specify CLI**: Command-line tool for managing specifications
- **Templates**: Pre-built templates for common project types
- **Steering Prompts**: Structured prompts to guide AI agents

<!-- section_id: "d59da5e9-123b-4459-a1e6-f9d5ab107796" -->
### 3. Version-Controlled Specifications

- Specifications live alongside your code
- Git-based versioning of all artifacts
- Traceability from spec to implementation

<!-- section_id: "68bec78d-33b0-4f44-9ac2-95f7df9eafc1" -->
### 4. AI Tool Integration

Works seamlessly with:
- **GitHub Copilot**
- **Claude Code**
- **Gemini CLI**
- Other AI coding tools

<!-- section_id: "c9eac836-6344-449c-875d-555767ddd8cd" -->
## Installation

<!-- section_id: "7300277c-87b0-4988-89d1-36f2aad4d220" -->
### Prerequisites

- Python 3.11+
- `uv` package manager

<!-- section_id: "b6d59d82-d5e4-4328-a691-a4fb52fa1469" -->
### Install Specify CLI

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

<!-- section_id: "b4837f00-3949-4403-a9f1-a88e8c37f508" -->
### Verify Installation

```bash
specify --version
```

<!-- section_id: "d3a091bc-08c8-45eb-9eda-3c6059a26ed8" -->
## Getting Started

<!-- section_id: "de003a70-226b-415b-9b0f-27d24c5c7304" -->
### Step 1: Initialize a New Project

```bash
specify init my-project --ai copilot
```

Replace `my-project` with your desired project name and `copilot` with your preferred AI tool.

<!-- section_id: "b4833334-c494-49f7-8e47-3a8489e5bd12" -->
### Step 2: Define Your Specification

Use the `/specify` command to outline your project:

```bash
/specify Build a task management app with user authentication, real-time collaboration, and mobile support.
```

This creates a specification document that guides all subsequent development.

<!-- section_id: "e94ef65f-42b0-4bcb-85d3-60946eaf142c" -->
### Step 3: Generate Implementation Plan

Use the `/plan` command to create a technical implementation plan:

```bash
/plan Use React with TypeScript, Node.js backend, PostgreSQL database
```

This generates an implementation plan based on your specification.

<!-- section_id: "8fc990b2-de9a-439d-83c2-55769740bdec" -->
### Step 4: Generate Task Breakdown

Use the `/tasks` command to break down the plan into actionable tasks:

```bash
/tasks
```

This creates a `tasks.md` file with tasks ordered by dependencies.

<!-- section_id: "010e23f5-8b12-4e19-bda0-c780ea936093" -->
### Step 5: Implement

Use the `/implement` command to execute the implementation:

```bash
/implement
```

The AI agent will execute tasks in the correct order, respecting dependencies.

<!-- section_id: "44ca80b8-d8ce-43d2-9f90-d6fff33fc403" -->
## Command Reference

<!-- section_id: "e5b0460a-d32a-4489-895c-fc58ec91ce6e" -->
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

<!-- section_id: "e67b3459-8e8a-4c85-8364-3085f6e9e965" -->
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

<!-- section_id: "bc638e54-a1c4-46d2-9a51-7d287b531c5f" -->
## Workflow Example

<!-- section_id: "0d76bd46-5db7-490d-bdb5-d951134a7d68" -->
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

<!-- section_id: "bd32e01b-561e-44d4-a117-acd9980c4b14" -->
## Directory Structure Details

<!-- section_id: "6170822d-2fe1-4639-a4e8-06da4185ce3d" -->
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

<!-- section_id: "87145e9f-b116-437b-a230-58ea7756b3a9" -->
### `memory/`
Project memory and constitution.

- **`constitution.md`**: Project standards, coding guidelines, and principles

<!-- section_id: "d30a413e-f083-4959-8249-3a2ebfa7fe02" -->
### `scripts/`
Helper scripts for managing specifications.

- **`check-prerequisites.sh`**: Validate system requirements
- **`setup-plan.sh`**: Initialize new feature
- **`create-new-feature.sh`**: Create new feature specification
- **`update-claude-md.sh`**: Update Claude configuration

<!-- section_id: "3530228b-785e-44e4-8c7e-d4e02fce69b1" -->
### `templates/`
Template files for creating new specifications.

- **`spec-template.md`**: Feature specification template
- **`plan-template.md`**: Implementation plan template
- **`tasks-template.md`**: Task breakdown template
- **`CLAUDE-template.md`**: Claude agent configuration template

<!-- section_id: "aaa29bb8-6cc9-4452-8a1e-58e72da35408" -->
## Best Practices

<!-- section_id: "5d32bb8a-f934-4a5f-b76e-312eeb41b7df" -->
### Specification Writing

1. **Be Specific**: Include acceptance criteria and technical requirements
2. **Include Context**: Explain the business problem being solved
3. **Define Scope**: Clearly state what's included and what's not
4. **Use Examples**: Provide concrete examples of expected behavior

<!-- section_id: "3aaeccdd-ceb2-4463-8355-faeff841fe5e" -->
### Planning

1. **Research First**: Check `research.md` before making technology decisions
2. **Consider Dependencies**: Plan for dependency management
3. **Think About Testing**: Include testing strategy in your plan
4. **Estimate Effort**: Consider complexity and timeline

<!-- section_id: "39326565-36a7-4c09-a033-c7af253d93f9" -->
### Task Generation

1. **Check Prerequisites**: Ensure all prerequisites are defined
2. **Order Matters**: Tasks must respect dependencies
3. **Mark Parallel**: Use `[P]` for tasks that can run in parallel
4. **Include Checkpoints**: Add validation steps between phases

<!-- section_id: "941dbc3e-bb73-400d-b24e-a8aff5531b3e" -->
### Implementation

1. **Follow the Plan**: Stick to the technical decisions in your plan
2. **Respect Dependencies**: Execute tasks in the correct order
3. **Test Incrementally**: Test after each phase
4. **Document Changes**: Update specs if requirements change

<!-- section_id: "b607d2a7-1502-47d4-8085-3a1eb0c2647b" -->
## Advanced Features

<!-- section_id: "b726854a-6d5e-4d33-baee-8900046d7527" -->
### Multi-Feature Development

Create multiple features within the same project:

```bash
/specify Create user authentication feature with OAuth support
# Generates: specs/002-user-authentication/spec.md

/specify Add notification system with email and in-app notifications
# Generates: specs/003-notification-system/spec.md
```

Each feature can be developed independently while sharing the same constitution and base configuration.

<!-- section_id: "7add32b2-2ef9-41ec-8ddc-6aa67bffa40f" -->
### Custom Templates

Create project-specific templates:

1. Add custom template to `templates/`
2. Reference in feature specification
3. Use in `/specify` command

<!-- section_id: "52818477-5653-4de3-b1b9-dcb154d6bf70" -->
### Integration with Existing Projects

You can add Spec Kit to existing projects:

```bash
# Navigate to existing project
cd /path/to/existing-project

# Initialize Spec Kit
specify init --ai copilot --existing

# This preserves your existing code while adding specification structure
```

<!-- section_id: "1cd31009-6694-4ae7-ba6a-9f185f77fece" -->
## Troubleshooting

<!-- section_id: "b3814245-5f9f-4d08-8048-bf1223daa7fa" -->
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

<!-- section_id: "5c33da79-f41a-4435-8d95-6f1ceeb7c08d" -->
### Validation Checkpoints

If implementation fails validation:

1. Review error messages
2. Check `tasks.md` for missing dependencies
3. Verify `spec.md` is complete and clear
4. Ensure `constitution.md` is properly configured

<!-- section_id: "658c0969-0cd8-4572-a8b1-e66d2173257e" -->
## Resources

<!-- section_id: "a46c2e09-e50f-43da-ae40-90091c013892" -->
### Official Documentation
- **Website**: https://speckit.org/
- **Documentation**: https://speckit.org/guide
- **GitHub**: https://github.com/github/spec-kit

<!-- section_id: "dd5f173a-e3ee-435b-8d66-c417a6b298ad" -->
### Community
- **Issues**: https://github.com/github/spec-kit/issues
- **Discussions**: https://github.com/github/spec-kit/discussions

<!-- section_id: "59deb6ba-b9ef-4666-904f-be1b9715fe71" -->
### Examples
- **Quick Start**: See `specs/[feature]/quickstart.md` in any initialized project
- **Templates**: Check `templates/` directory

<!-- section_id: "1bcd7da7-8ff3-4f63-8d74-4744b9c7b9bc" -->
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

