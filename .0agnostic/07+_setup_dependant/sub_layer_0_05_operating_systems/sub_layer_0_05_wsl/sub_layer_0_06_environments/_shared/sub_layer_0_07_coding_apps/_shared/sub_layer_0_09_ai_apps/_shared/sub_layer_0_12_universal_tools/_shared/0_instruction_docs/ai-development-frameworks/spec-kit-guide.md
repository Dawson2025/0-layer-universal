---
resource_id: "f0cce9d7-d02f-4765-8159-932d6d467ede"
resource_type: "document"
resource_name: "spec-kit-guide"
---
# GitHub Spec Kit - Comprehensive Guide
*Spec-Driven Development Framework for AI Coding Agents*

<!-- section_id: "33d67a05-e46a-40aa-9255-c8d361f4c1ec" -->
## Overview

GitHub Spec Kit is an open-source toolkit designed to facilitate spec-driven development with AI coding agents. It transforms ad-hoc prompting into structured, verifiable development workflows by organizing development into four gated phases with validation checkpoints.

<!-- section_id: "7384bff0-4c12-4630-81ae-2926384b378c" -->
## Key Concepts

<!-- section_id: "141f4466-ccd1-41b7-ab84-7a6c1895f0e7" -->
### What is Spec-Driven Development?

Spec-driven development is a methodology where:
- **Specifications** are defined before implementation
- **Development** follows structured phases
- **Validation** occurs at each phase
- **Artifacts** are version-controlled alongside code

<!-- section_id: "9782aa8c-52c3-4dff-9314-92ff579f9c38" -->
### Core Philosophy

**Problem**: AI coding agents are only as good as the instructions and context they receive.

**Solution**: Provide structured methodologies that transform vague prompts into precise, implementable specifications, significantly improving development velocity and code quality.

<!-- section_id: "3ff3ca8a-e46c-4007-9636-fe9e791e47f8" -->
## Key Features

<!-- section_id: "3d9647bb-667c-47fb-b250-9f500469ac9d" -->
### 1. Four-Phase Validation Process

```
Phase 1: Specification → Phase 2: Planning → Phase 3: Tasks → Phase 4: Implementation
```

Each phase has validation checkpoints ensuring quality before proceeding.

<!-- section_id: "e17cbc9b-8e13-49ec-91d2-aa29b41034b6" -->
### 2. CLI Tools and Templates

- **Specify CLI**: Command-line tool for managing specifications
- **Templates**: Pre-built templates for common project types
- **Steering Prompts**: Structured prompts to guide AI agents

<!-- section_id: "a2ea403a-dd18-4178-b26c-73d598788deb" -->
### 3. Version-Controlled Specifications

- Specifications live alongside your code
- Git-based versioning of all artifacts
- Traceability from spec to implementation

<!-- section_id: "4e8619ac-e5ec-47d7-b360-92c8212fa831" -->
### 4. AI Tool Integration

Works seamlessly with:
- **GitHub Copilot**
- **Claude Code**
- **Gemini CLI**
- Other AI coding tools

<!-- section_id: "c8ca7b0d-b617-4067-b2f9-fc8479c48af8" -->
## Installation

<!-- section_id: "92a1c01c-3b11-44c8-8356-3d448a7b359c" -->
### Prerequisites

- Python 3.11+
- `uv` package manager

<!-- section_id: "7b5726c8-711d-431d-ae85-8705684c6fab" -->
### Install Specify CLI

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

<!-- section_id: "912d75f1-8461-4af7-b740-009f69ec4969" -->
### Verify Installation

```bash
specify --version
```

<!-- section_id: "d9318ca5-53b3-4e58-a456-eaa6e4931402" -->
## Getting Started

<!-- section_id: "28ed1317-6364-418d-b310-3e617445fda8" -->
### Step 1: Initialize a New Project

```bash
specify init my-project --ai copilot
```

Replace `my-project` with your desired project name and `copilot` with your preferred AI tool.

<!-- section_id: "1752c056-d178-4c4c-ab1c-a03faae3df11" -->
### Step 2: Define Your Specification

Use the `/specify` command to outline your project:

```bash
/specify Build a task management app with user authentication, real-time collaboration, and mobile support.
```

This creates a specification document that guides all subsequent development.

<!-- section_id: "57f6bf85-79ef-4600-b1a3-c8d2fd9ecffb" -->
### Step 3: Generate Implementation Plan

Use the `/plan` command to create a technical implementation plan:

```bash
/plan Use React with TypeScript, Node.js backend, PostgreSQL database
```

This generates an implementation plan based on your specification.

<!-- section_id: "b0bd13ba-a76a-451e-962f-c20fa743b0ff" -->
### Step 4: Generate Task Breakdown

Use the `/tasks` command to break down the plan into actionable tasks:

```bash
/tasks
```

This creates a `tasks.md` file with tasks ordered by dependencies.

<!-- section_id: "d79e7003-36be-4e41-b45f-0df5df14e38c" -->
### Step 5: Implement

Use the `/implement` command to execute the implementation:

```bash
/implement
```

The AI agent will execute tasks in the correct order, respecting dependencies.

<!-- section_id: "0a25c7d0-cce8-43dc-a516-8c9352637c95" -->
## Command Reference

<!-- section_id: "1704fb78-69c5-4c59-b096-965b192db066" -->
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

<!-- section_id: "1f3440f7-b147-473a-b0e7-6a1815cf35ed" -->
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

<!-- section_id: "e32325f4-eb5d-4a16-811c-a4e581295351" -->
## Workflow Example

<!-- section_id: "776aaf0b-0a24-431a-bf86-e1eb10da559c" -->
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

<!-- section_id: "414fc7c8-f9f0-45db-ad3f-e1bbf1bb26a2" -->
## Directory Structure Details

<!-- section_id: "abc3d7d7-18a3-4c9e-af6e-6eefb7873359" -->
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

<!-- section_id: "65b69573-464c-445e-ab7d-cfbb5d81b5fd" -->
### `memory/`
Project memory and constitution.

- **`constitution.md`**: Project standards, coding guidelines, and principles

<!-- section_id: "47ccf463-e4e6-4dd1-8de3-c5c75abe4e41" -->
### `scripts/`
Helper scripts for managing specifications.

- **`check-prerequisites.sh`**: Validate system requirements
- **`setup-plan.sh`**: Initialize new feature
- **`create-new-feature.sh`**: Create new feature specification
- **`update-claude-md.sh`**: Update Claude configuration

<!-- section_id: "2ea79913-d652-49bf-8a91-c5ada1db5047" -->
### `templates/`
Template files for creating new specifications.

- **`spec-template.md`**: Feature specification template
- **`plan-template.md`**: Implementation plan template
- **`tasks-template.md`**: Task breakdown template
- **`CLAUDE-template.md`**: Claude agent configuration template

<!-- section_id: "e43e45b2-8eb3-4755-bbd4-fd6142eee5b9" -->
## Best Practices

<!-- section_id: "5e85f041-9941-42c9-9707-520ce85a6388" -->
### Specification Writing

1. **Be Specific**: Include acceptance criteria and technical requirements
2. **Include Context**: Explain the business problem being solved
3. **Define Scope**: Clearly state what's included and what's not
4. **Use Examples**: Provide concrete examples of expected behavior

<!-- section_id: "1a77d91c-e7d1-4a13-a21e-f2bca7a6adbe" -->
### Planning

1. **Research First**: Check `research.md` before making technology decisions
2. **Consider Dependencies**: Plan for dependency management
3. **Think About Testing**: Include testing strategy in your plan
4. **Estimate Effort**: Consider complexity and timeline

<!-- section_id: "2268c925-f837-4514-86df-cb8d9bd71165" -->
### Task Generation

1. **Check Prerequisites**: Ensure all prerequisites are defined
2. **Order Matters**: Tasks must respect dependencies
3. **Mark Parallel**: Use `[P]` for tasks that can run in parallel
4. **Include Checkpoints**: Add validation steps between phases

<!-- section_id: "8c78fdaf-2980-45fe-b905-e25fa6ee4b32" -->
### Implementation

1. **Follow the Plan**: Stick to the technical decisions in your plan
2. **Respect Dependencies**: Execute tasks in the correct order
3. **Test Incrementally**: Test after each phase
4. **Document Changes**: Update specs if requirements change

<!-- section_id: "cc671980-f4fc-48a3-b9dd-660e7a6897bc" -->
## Advanced Features

<!-- section_id: "48aec5ac-8b61-466c-9de1-f7e364f52d30" -->
### Multi-Feature Development

Create multiple features within the same project:

```bash
/specify Create user authentication feature with OAuth support
# Generates: specs/002-user-authentication/spec.md

/specify Add notification system with email and in-app notifications
# Generates: specs/003-notification-system/spec.md
```

Each feature can be developed independently while sharing the same constitution and base configuration.

<!-- section_id: "03ca6828-08fe-4fd6-a178-daf4b2949d5f" -->
### Custom Templates

Create project-specific templates:

1. Add custom template to `templates/`
2. Reference in feature specification
3. Use in `/specify` command

<!-- section_id: "e39097d9-ab1b-4d9e-94f9-8c6eb1b95d5a" -->
### Integration with Existing Projects

You can add Spec Kit to existing projects:

```bash
# Navigate to existing project
cd /path/to/existing-project

# Initialize Spec Kit
specify init --ai copilot --existing

# This preserves your existing code while adding specification structure
```

<!-- section_id: "dd920130-6404-4153-971c-1c7324dfa4a8" -->
## Troubleshooting

<!-- section_id: "52119740-0801-4fb9-b9e4-c685c2f53754" -->
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

<!-- section_id: "0429c456-14bf-4163-a5d0-17155d6373d2" -->
### Validation Checkpoints

If implementation fails validation:

1. Review error messages
2. Check `tasks.md` for missing dependencies
3. Verify `spec.md` is complete and clear
4. Ensure `constitution.md` is properly configured

<!-- section_id: "5c8821c7-9eee-4ad6-ae26-4b6551106ac1" -->
## Resources

<!-- section_id: "458ae373-037c-4676-a6b9-1eb0c456d0db" -->
### Official Documentation
- **Website**: https://speckit.org/
- **Documentation**: https://speckit.org/guide
- **GitHub**: https://github.com/github/spec-kit

<!-- section_id: "2ab03f53-15cb-4fdb-8231-a009b054572e" -->
### Community
- **Issues**: https://github.com/github/spec-kit/issues
- **Discussions**: https://github.com/github/spec-kit/discussions

<!-- section_id: "aba96cde-32c9-4248-bcca-15b17bba0210" -->
### Examples
- **Quick Start**: See `specs/[feature]/quickstart.md` in any initialized project
- **Templates**: Check `templates/` directory

<!-- section_id: "ac45ed7c-f481-4c98-a8ce-34ec7bb18577" -->
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

