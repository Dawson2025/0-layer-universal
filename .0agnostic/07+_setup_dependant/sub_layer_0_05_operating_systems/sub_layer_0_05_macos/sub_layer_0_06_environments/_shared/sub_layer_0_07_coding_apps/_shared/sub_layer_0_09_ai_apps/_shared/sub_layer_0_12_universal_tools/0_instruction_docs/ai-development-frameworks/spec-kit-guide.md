---
resource_id: "126c7eba-1da4-4d24-a40a-2593428091a6"
resource_type: "document"
resource_name: "spec-kit-guide"
---
# GitHub Spec Kit - Comprehensive Guide
*Spec-Driven Development Framework for AI Coding Agents*

<!-- section_id: "55ea90f0-711b-47a1-bef6-6179b57181b1" -->
## Overview

GitHub Spec Kit is an open-source toolkit designed to facilitate spec-driven development with AI coding agents. It transforms ad-hoc prompting into structured, verifiable development workflows by organizing development into four gated phases with validation checkpoints.

<!-- section_id: "221d6e3e-1e91-48fe-a14d-3952d294eb66" -->
## Key Concepts

<!-- section_id: "1a5b37d1-f3d3-46aa-adaa-dec2184ebf47" -->
### What is Spec-Driven Development?

Spec-driven development is a methodology where:
- **Specifications** are defined before implementation
- **Development** follows structured phases
- **Validation** occurs at each phase
- **Artifacts** are version-controlled alongside code

<!-- section_id: "f4ed0ff9-e1c3-4a14-8bdf-f90f1902e18d" -->
### Core Philosophy

**Problem**: AI coding agents are only as good as the instructions and context they receive.

**Solution**: Provide structured methodologies that transform vague prompts into precise, implementable specifications, significantly improving development velocity and code quality.

<!-- section_id: "1265f5a1-28d4-4f74-8580-632de8a8f880" -->
## Key Features

<!-- section_id: "e60b95fe-385d-4ccb-9bb6-22db2494278a" -->
### 1. Four-Phase Validation Process

```
Phase 1: Specification → Phase 2: Planning → Phase 3: Tasks → Phase 4: Implementation
```

Each phase has validation checkpoints ensuring quality before proceeding.

<!-- section_id: "14d24c09-93a5-46ee-a7d3-344f7014dc29" -->
### 2. CLI Tools and Templates

- **Specify CLI**: Command-line tool for managing specifications
- **Templates**: Pre-built templates for common project types
- **Steering Prompts**: Structured prompts to guide AI agents

<!-- section_id: "88034d3f-fac1-4c0e-a5de-d724a003211b" -->
### 3. Version-Controlled Specifications

- Specifications live alongside your code
- Git-based versioning of all artifacts
- Traceability from spec to implementation

<!-- section_id: "2bc95da4-0662-4239-b966-19fee3f986ef" -->
### 4. AI Tool Integration

Works seamlessly with:
- **GitHub Copilot**
- **Claude Code**
- **Gemini CLI**
- Other AI coding tools

<!-- section_id: "f7c1274f-ef7d-410e-8c01-2cc7a0dc8f87" -->
## Installation

<!-- section_id: "6412f554-454f-4361-b7ff-066bffb0f6c5" -->
### Prerequisites

- Python 3.11+
- `uv` package manager

<!-- section_id: "8ebc87fe-3085-406f-b02c-47e9b35f3826" -->
### Install Specify CLI

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

<!-- section_id: "25708788-a446-4e95-ba61-7159805aa0f3" -->
### Verify Installation

```bash
specify --version
```

<!-- section_id: "e97704f8-98a8-483c-a0d8-6307d21a25ca" -->
## Getting Started

<!-- section_id: "05d90bcf-3546-4d4a-9960-51128f760ca1" -->
### Step 1: Initialize a New Project

```bash
specify init my-project --ai copilot
```

Replace `my-project` with your desired project name and `copilot` with your preferred AI tool.

<!-- section_id: "d08de312-3f57-456c-acff-1ef863a19c86" -->
### Step 2: Define Your Specification

Use the `/specify` command to outline your project:

```bash
/specify Build a task management app with user authentication, real-time collaboration, and mobile support.
```

This creates a specification document that guides all subsequent development.

<!-- section_id: "1ecfe49b-5021-435d-b3da-1fdcfba22e9f" -->
### Step 3: Generate Implementation Plan

Use the `/plan` command to create a technical implementation plan:

```bash
/plan Use React with TypeScript, Node.js backend, PostgreSQL database
```

This generates an implementation plan based on your specification.

<!-- section_id: "14638fd6-3384-4747-9bb1-2be509694e23" -->
### Step 4: Generate Task Breakdown

Use the `/tasks` command to break down the plan into actionable tasks:

```bash
/tasks
```

This creates a `tasks.md` file with tasks ordered by dependencies.

<!-- section_id: "c371322f-7f0c-42e9-b060-b741b7630130" -->
### Step 5: Implement

Use the `/implement` command to execute the implementation:

```bash
/implement
```

The AI agent will execute tasks in the correct order, respecting dependencies.

<!-- section_id: "465933f8-959c-423f-ac24-e2d055ff2a5e" -->
## Command Reference

<!-- section_id: "95560e62-c996-4d5f-8ffc-11372630d398" -->
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

<!-- section_id: "0ff49847-ca3c-4a1c-8654-4e9e19b321d1" -->
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

<!-- section_id: "dfe1c5c5-35b4-48e5-9604-67a0dfb71a69" -->
## Workflow Example

<!-- section_id: "03d3822a-e705-435e-bedc-7353dc38c3dc" -->
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

<!-- section_id: "cf9e6954-4d92-43bf-8999-da3fd20632a4" -->
## Directory Structure Details

<!-- section_id: "61a90c2a-0c65-4259-b1b1-828b98856c6e" -->
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

<!-- section_id: "3b83529c-6a6f-4756-a102-dee53e8119d5" -->
### `memory/`
Project memory and constitution.

- **`constitution.md`**: Project standards, coding guidelines, and principles

<!-- section_id: "97024eb8-8eb7-4ba1-b18f-d39a938a19c2" -->
### `scripts/`
Helper scripts for managing specifications.

- **`check-prerequisites.sh`**: Validate system requirements
- **`setup-plan.sh`**: Initialize new feature
- **`create-new-feature.sh`**: Create new feature specification
- **`update-claude-md.sh`**: Update Claude configuration

<!-- section_id: "3d2d03ca-12e7-4dfb-b1fa-b732473c9e93" -->
### `templates/`
Template files for creating new specifications.

- **`spec-template.md`**: Feature specification template
- **`plan-template.md`**: Implementation plan template
- **`tasks-template.md`**: Task breakdown template
- **`CLAUDE-template.md`**: Claude agent configuration template

<!-- section_id: "5b3a983e-c7d2-4393-9d1d-6103254b81a8" -->
## Best Practices

<!-- section_id: "d8f58126-3cb9-47a3-afc0-c2c91732042b" -->
### Specification Writing

1. **Be Specific**: Include acceptance criteria and technical requirements
2. **Include Context**: Explain the business problem being solved
3. **Define Scope**: Clearly state what's included and what's not
4. **Use Examples**: Provide concrete examples of expected behavior

<!-- section_id: "aa05a789-abf2-487c-beb6-e18f3a301581" -->
### Planning

1. **Research First**: Check `research.md` before making technology decisions
2. **Consider Dependencies**: Plan for dependency management
3. **Think About Testing**: Include testing strategy in your plan
4. **Estimate Effort**: Consider complexity and timeline

<!-- section_id: "5239cb50-ff22-4c56-a2a0-6b7b6c29c8dc" -->
### Task Generation

1. **Check Prerequisites**: Ensure all prerequisites are defined
2. **Order Matters**: Tasks must respect dependencies
3. **Mark Parallel**: Use `[P]` for tasks that can run in parallel
4. **Include Checkpoints**: Add validation steps between phases

<!-- section_id: "f4d7aa46-69f4-4bc0-ade4-208acf9ec01a" -->
### Implementation

1. **Follow the Plan**: Stick to the technical decisions in your plan
2. **Respect Dependencies**: Execute tasks in the correct order
3. **Test Incrementally**: Test after each phase
4. **Document Changes**: Update specs if requirements change

<!-- section_id: "0eacc3c1-a7ff-4120-8290-bbe3a9d0b793" -->
## Advanced Features

<!-- section_id: "e60c552f-b339-4254-b060-f9c29ea76fa8" -->
### Multi-Feature Development

Create multiple features within the same project:

```bash
/specify Create user authentication feature with OAuth support
# Generates: specs/002-user-authentication/spec.md

/specify Add notification system with email and in-app notifications
# Generates: specs/003-notification-system/spec.md
```

Each feature can be developed independently while sharing the same constitution and base configuration.

<!-- section_id: "012e9d83-6cdc-4793-850a-c7d3d0a3fe59" -->
### Custom Templates

Create project-specific templates:

1. Add custom template to `templates/`
2. Reference in feature specification
3. Use in `/specify` command

<!-- section_id: "8c591943-f225-4075-b6e7-f2e4f018c0ce" -->
### Integration with Existing Projects

You can add Spec Kit to existing projects:

```bash
# Navigate to existing project
cd /path/to/existing-project

# Initialize Spec Kit
specify init --ai copilot --existing

# This preserves your existing code while adding specification structure
```

<!-- section_id: "eb8715de-cf27-4839-bac6-e4d505536cec" -->
## Troubleshooting

<!-- section_id: "269e63c2-e5c5-42f4-8b4a-970dee3f4e01" -->
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

<!-- section_id: "811929c0-c1c8-435e-81f8-b60b0d11372f" -->
### Validation Checkpoints

If implementation fails validation:

1. Review error messages
2. Check `tasks.md` for missing dependencies
3. Verify `spec.md` is complete and clear
4. Ensure `constitution.md` is properly configured

<!-- section_id: "68f4d1b3-e790-4f61-9a75-3bfafac2759f" -->
## Resources

<!-- section_id: "ef957b7b-98ef-4739-8c82-1afe9afea588" -->
### Official Documentation
- **Website**: https://speckit.org/
- **Documentation**: https://speckit.org/guide
- **GitHub**: https://github.com/github/spec-kit

<!-- section_id: "4741f505-b54e-4853-94df-154b4996e463" -->
### Community
- **Issues**: https://github.com/github/spec-kit/issues
- **Discussions**: https://github.com/github/spec-kit/discussions

<!-- section_id: "217ed5a2-e418-49af-be74-0be441a1cc77" -->
### Examples
- **Quick Start**: See `specs/[feature]/quickstart.md` in any initialized project
- **Templates**: Check `templates/` directory

<!-- section_id: "7bb6ff05-4329-4bba-9faa-252a0da3e539" -->
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

