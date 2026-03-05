---
resource_id: "1d935a9b-e95e-4569-bfcc-83e1ef7b08fd"
resource_type: "document"
resource_name: "spec-kit-guide"
---
# GitHub Spec Kit - Comprehensive Guide
*Spec-Driven Development Framework for AI Coding Agents*

<!-- section_id: "4bf7692a-3dce-44c9-8edc-3f639f82435e" -->
## Overview

GitHub Spec Kit is an open-source toolkit designed to facilitate spec-driven development with AI coding agents. It transforms ad-hoc prompting into structured, verifiable development workflows by organizing development into four gated phases with validation checkpoints.

<!-- section_id: "4bc2859c-560c-4ae9-9191-e3618929d31a" -->
## Key Concepts

<!-- section_id: "35885617-e4cb-46a7-89ae-ec2b11465b48" -->
### What is Spec-Driven Development?

Spec-driven development is a methodology where:
- **Specifications** are defined before implementation
- **Development** follows structured phases
- **Validation** occurs at each phase
- **Artifacts** are version-controlled alongside code

<!-- section_id: "1b042a9d-ed80-4e55-901f-e96aadeef4f5" -->
### Core Philosophy

**Problem**: AI coding agents are only as good as the instructions and context they receive.

**Solution**: Provide structured methodologies that transform vague prompts into precise, implementable specifications, significantly improving development velocity and code quality.

<!-- section_id: "40d8f557-7133-4de0-add5-f11c8a557903" -->
## Key Features

<!-- section_id: "11e6398b-8e5c-46dd-8b58-79542c2815ce" -->
### 1. Four-Phase Validation Process

```
Phase 1: Specification → Phase 2: Planning → Phase 3: Tasks → Phase 4: Implementation
```

Each phase has validation checkpoints ensuring quality before proceeding.

<!-- section_id: "86fd9d9d-a7ac-4958-9dfc-bd88aba1d8a2" -->
### 2. CLI Tools and Templates

- **Specify CLI**: Command-line tool for managing specifications
- **Templates**: Pre-built templates for common project types
- **Steering Prompts**: Structured prompts to guide AI agents

<!-- section_id: "f5052e61-0868-4883-822c-61006c6c8b6e" -->
### 3. Version-Controlled Specifications

- Specifications live alongside your code
- Git-based versioning of all artifacts
- Traceability from spec to implementation

<!-- section_id: "fd5447d4-dde8-429c-9d74-765c7ef363d5" -->
### 4. AI Tool Integration

Works seamlessly with:
- **GitHub Copilot**
- **Claude Code**
- **Gemini CLI**
- Other AI coding tools

<!-- section_id: "a3ceda2d-93b5-479c-b6ac-d8363d706d2a" -->
## Installation

<!-- section_id: "75924d36-06ff-456f-9ec4-76e1049e1624" -->
### Prerequisites

- Python 3.11+
- `uv` package manager

<!-- section_id: "2c571954-5e6d-492a-ab86-dcb375ecf961" -->
### Install Specify CLI

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

<!-- section_id: "833c34ee-f0b7-4c96-a66e-567c442b425f" -->
### Verify Installation

```bash
specify --version
```

<!-- section_id: "4daa65d6-b66d-498d-ac57-be49319e3a30" -->
## Getting Started

<!-- section_id: "074b77ae-11d1-4937-9ad1-44a66182c323" -->
### Step 1: Initialize a New Project

```bash
specify init my-project --ai copilot
```

Replace `my-project` with your desired project name and `copilot` with your preferred AI tool.

<!-- section_id: "225cfae8-f659-48e1-8eae-37861a6864ea" -->
### Step 2: Define Your Specification

Use the `/specify` command to outline your project:

```bash
/specify Build a task management app with user authentication, real-time collaboration, and mobile support.
```

This creates a specification document that guides all subsequent development.

<!-- section_id: "8a0f7942-a292-44c3-a43d-f264016884a0" -->
### Step 3: Generate Implementation Plan

Use the `/plan` command to create a technical implementation plan:

```bash
/plan Use React with TypeScript, Node.js backend, PostgreSQL database
```

This generates an implementation plan based on your specification.

<!-- section_id: "9ff23e93-cc4b-45ab-a1b9-fd29267719bb" -->
### Step 4: Generate Task Breakdown

Use the `/tasks` command to break down the plan into actionable tasks:

```bash
/tasks
```

This creates a `tasks.md` file with tasks ordered by dependencies.

<!-- section_id: "b75bb2f0-84b4-4d8e-b53c-ae2e483d43a3" -->
### Step 5: Implement

Use the `/implement` command to execute the implementation:

```bash
/implement
```

The AI agent will execute tasks in the correct order, respecting dependencies.

<!-- section_id: "fd98b766-954e-4f66-a896-18a4b8b19c5d" -->
## Command Reference

<!-- section_id: "4c613b8d-9859-4af3-b700-3be368f1a58f" -->
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

<!-- section_id: "b347c2c8-3fd3-424c-8969-dbe24b95fcef" -->
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

<!-- section_id: "26f41359-893b-49ca-ab7f-154385c1e8dd" -->
## Workflow Example

<!-- section_id: "cfc3a978-e157-45ce-a36b-3f7e9a77442e" -->
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

<!-- section_id: "a5d6306c-303d-4645-ae83-63dcc99effae" -->
## Directory Structure Details

<!-- section_id: "3a38b48b-bbf0-4a48-baa7-31cf69114d0c" -->
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

<!-- section_id: "eec21ecd-ea0b-4fec-8e30-7709fc042d3e" -->
### `memory/`
Project memory and constitution.

- **`constitution.md`**: Project standards, coding guidelines, and principles

<!-- section_id: "9a54f8f0-2290-4441-aa99-db4549eeb2d4" -->
### `scripts/`
Helper scripts for managing specifications.

- **`check-prerequisites.sh`**: Validate system requirements
- **`setup-plan.sh`**: Initialize new feature
- **`create-new-feature.sh`**: Create new feature specification
- **`update-claude-md.sh`**: Update Claude configuration

<!-- section_id: "6a224cbb-9ee5-4c6f-a673-64c6c4440988" -->
### `templates/`
Template files for creating new specifications.

- **`spec-template.md`**: Feature specification template
- **`plan-template.md`**: Implementation plan template
- **`tasks-template.md`**: Task breakdown template
- **`CLAUDE-template.md`**: Claude agent configuration template

<!-- section_id: "900cb5cf-f89b-4243-8182-d579330c741c" -->
## Best Practices

<!-- section_id: "1ea94358-1a50-4a4d-bab6-193d8bcbeae5" -->
### Specification Writing

1. **Be Specific**: Include acceptance criteria and technical requirements
2. **Include Context**: Explain the business problem being solved
3. **Define Scope**: Clearly state what's included and what's not
4. **Use Examples**: Provide concrete examples of expected behavior

<!-- section_id: "8b57494a-84c3-4c5a-8c05-832635155da4" -->
### Planning

1. **Research First**: Check `research.md` before making technology decisions
2. **Consider Dependencies**: Plan for dependency management
3. **Think About Testing**: Include testing strategy in your plan
4. **Estimate Effort**: Consider complexity and timeline

<!-- section_id: "3dad2929-f84e-4e4e-af04-2164e87c6812" -->
### Task Generation

1. **Check Prerequisites**: Ensure all prerequisites are defined
2. **Order Matters**: Tasks must respect dependencies
3. **Mark Parallel**: Use `[P]` for tasks that can run in parallel
4. **Include Checkpoints**: Add validation steps between phases

<!-- section_id: "54b21191-59bc-4953-8015-629d7b7b4b72" -->
### Implementation

1. **Follow the Plan**: Stick to the technical decisions in your plan
2. **Respect Dependencies**: Execute tasks in the correct order
3. **Test Incrementally**: Test after each phase
4. **Document Changes**: Update specs if requirements change

<!-- section_id: "4bf928f6-fa99-4eab-85e8-1765048c4d8c" -->
## Advanced Features

<!-- section_id: "79446982-6981-485d-b1fa-1463cfaf6b29" -->
### Multi-Feature Development

Create multiple features within the same project:

```bash
/specify Create user authentication feature with OAuth support
# Generates: specs/002-user-authentication/spec.md

/specify Add notification system with email and in-app notifications
# Generates: specs/003-notification-system/spec.md
```

Each feature can be developed independently while sharing the same constitution and base configuration.

<!-- section_id: "941a12cc-398a-456b-b1a5-1f71e5f77b1d" -->
### Custom Templates

Create project-specific templates:

1. Add custom template to `templates/`
2. Reference in feature specification
3. Use in `/specify` command

<!-- section_id: "f4e81e80-1987-42d0-ae40-9a59f691bc8b" -->
### Integration with Existing Projects

You can add Spec Kit to existing projects:

```bash
# Navigate to existing project
cd /path/to/existing-project

# Initialize Spec Kit
specify init --ai copilot --existing

# This preserves your existing code while adding specification structure
```

<!-- section_id: "7f274eb6-971b-4582-930d-62b46e14fe3b" -->
## Troubleshooting

<!-- section_id: "af58a2a5-10a1-4193-ad44-1be2e600735e" -->
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

<!-- section_id: "d4788da7-e8d2-4eae-88d8-faea0127e844" -->
### Validation Checkpoints

If implementation fails validation:

1. Review error messages
2. Check `tasks.md` for missing dependencies
3. Verify `spec.md` is complete and clear
4. Ensure `constitution.md` is properly configured

<!-- section_id: "27276f80-9541-44b0-baa7-b54d5bd6a47c" -->
## Resources

<!-- section_id: "9e1d1616-91e4-44a0-82a1-dac7e47c8c0a" -->
### Official Documentation
- **Website**: https://speckit.org/
- **Documentation**: https://speckit.org/guide
- **GitHub**: https://github.com/github/spec-kit

<!-- section_id: "6ce1c4e6-86b7-47d3-bb85-c7f34732f480" -->
### Community
- **Issues**: https://github.com/github/spec-kit/issues
- **Discussions**: https://github.com/github/spec-kit/discussions

<!-- section_id: "ec21fda5-1530-471c-984a-24608f738bd9" -->
### Examples
- **Quick Start**: See `specs/[feature]/quickstart.md` in any initialized project
- **Templates**: Check `templates/` directory

<!-- section_id: "42eb8732-a1a9-4858-a908-7749249e2502" -->
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

