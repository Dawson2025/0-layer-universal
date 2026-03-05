---
resource_id: "c8079e3f-245a-4804-9bba-a3ab52b5ac0a"
resource_type: "document"
resource_name: "integration-guide"
---
# Integration Guide
*Integrating Spec Kit and BMAD with Your Existing AI Tools*

<!-- section_id: "acdfa9e9-4444-4845-b369-76b8555253e2" -->
## Overview

This guide shows you how to integrate GitHub Spec Kit and BMAD Method with your existing AI coding assistants like Cursor, Codex, and Claude Code. These frameworks enhance your existing tools rather than replacing them.

<!-- section_id: "41eaa204-cda2-4a6d-b011-5ad1a8f9b695" -->
## Tool Integration Matrix

<!-- section_id: "f72a2c6b-e057-46d7-bbd1-1d517e27cb66" -->
### Cursor IDE

#### Spec Kit Integration

**How it works**: Spec Kit provides structured prompts and specifications that Cursor can follow.

**Setup**:
```bash
# Initialize Spec Kit in your project
cd /path/to/your/project
specify init my-project --ai cursor

# Create specification
/specify Build a task management app with authentication
```

**Benefits**:
- ✅ Structured context for Cursor
- ✅ Version-controlled specifications
- ✅ Clear requirements for AI to follow
- ✅ Validation checkpoints ensure quality

**Usage**:
1. Define specs with `/specify`
2. Generate plan with `/plan`
3. Create tasks with `/tasks`
4. Implement in Cursor following the tasks

#### BMAD Integration

**How it works**: BMAD agents provide specialized context that Cursor can use.

**Setup**:
```bash
# Install BMAD
npx bmad-method install

# Configure for Cursor
# Use BMAD Web UI to generate artifacts
```

**Benefits**:
- ✅ Specialized role-based context
- ✅ Comprehensive requirements from Analyst
- ✅ Architecture guidance from Architect
- ✅ Development stories for context

**Usage**:
1. Generate PRD using BMAD Web UI
2. Import artifacts into Cursor
3. Use specialized agent outputs as context
4. Code in Cursor with rich context

<!-- section_id: "95f13760-a07b-42ec-a60d-ec8922906c9f" -->
### GitHub Copilot

#### Spec Kit Integration

**How it works**: Copilot uses Spec Kit specifications to generate better code.

**Setup**:
```bash
# Spec Kit is built with Copilot in mind
specify init my-project --ai copilot

# Copilot will automatically use specs for context
```

**Benefits**:
- ✅ Copilot has better understanding of requirements
- ✅ Code aligns with specifications
- ✅ Validation occurs automatically
- ✅ Consistent code quality

**Usage**:
1. Create specs in your project
2. Copilot references specs during coding
3. Validation ensures code matches specs
4. Quality gates prevent deviations

#### BMAD Integration

**How it works**: BMAD provides structured context that Copilot uses.

**Setup**:
```bash
# Install BMAD
npx bmad-method install

# Generate context documents
# Copilot will reference these
```

**Benefits**:
- ✅ Copilot has comprehensive context
- ✅ Better understanding of architecture
- ✅ Clear development stories
- ✅ Complete requirements context

<!-- section_id: "01602456-255e-4644-b9b9-026fed0de1bc" -->
### Claude Code

#### Spec Kit Integration

**How it works**: Claude Code follows Spec Kit's structured workflow.

**Setup**:
```bash
specify init my-project --ai claude-code

# Claude Code CLI commands
/specify <requirements>
/plan <technical-stack>
/tasks
/implement
```

**Benefits**:
- ✅ Claude Code executes structured workflow
- ✅ Validation at each phase
- ✅ Consistent development process
- ✅ Quality checkpoints

**Usage**:
```bash
# Claude Code can execute Spec Kit commands directly
/specify Build a REST API
/plan Use FastAPI with PostgreSQL
/tasks
/implement  # Claude Code executes implementation
```

#### BMAD Integration

**How it works**: Claude Code can interact with BMAD agents.

**Setup**:
```bash
# Install both
npx bmad-method install
specify init my-project --ai claude-code
```

**Benefits**:
- ✅ Claude Code can call BMAD agents
- ✅ Access to specialized agent outputs
- ✅ Both frameworks work together
- ✅ Maximum context and structure

**Usage**:
```bash
# Use both in sequence
# 1. BMAD agents create artifacts
# 2. Spec Kit structures the artifacts
# 3. Claude Code implements following Spec Kit workflow
```

<!-- section_id: "c59f6678-0131-4334-bec6-7c34f015c79f" -->
### Codex (GitHub)

#### Spec Kit Integration

**How it works**: Spec Kit provides clear structure for Codex to follow.

**Setup**:
```bash
# Initialize with Codex support
specify init my-project --ai codex

# Codex references specs for context
```

**Benefits**:
- ✅ Codex has clear structure to follow
- ✅ Specs guide implementation direction
- ✅ Validation ensures alignment
- ✅ Quality through checkpoints

#### BMAD Integration

**How it works**: BMAD provides context documents for Codex.

**Setup**:
```bash
# Use BMAD to generate context
npx bmad-method install
# Generate PRDs, architecture, stories
# Codex uses these as context
```

<!-- section_id: "2516586d-65fc-49af-be07-bfd2c8113761" -->
## Implementation Strategies

<!-- section_id: "43f0ba52-bbd6-45a1-bd5c-2135b46e477a" -->
### Strategy 1: Spec-Driven with Cursor

**Best For**: Solo developers or small teams wanting structure

**Setup**:
1. Install Spec Kit in your Cursor project
2. Create specifications for features
3. Let Cursor implement following specs
4. Validate at checkpoints

**Example**:
```bash
# In Cursor project
specify init task-app --ai cursor

# Create spec
/specify User authentication with JWT tokens

# Cursor now has structured context
# Type code as normal, Cursor references spec
```

<!-- section_id: "aecb1ec4-bc64-42d0-ba94-dfc88f679ddc" -->
### Strategy 2: Agentic Development with BMAD

**Best For**: Teams wanting team-like collaboration

**Setup**:
1. Install BMAD
2. Configure agents in Web UI
3. Generate artifacts (PRD, architecture, stories)
4. Import into your IDE
5. Implement with rich context

**Example**:
```bash
# Install BMAD
npx bmad-method install

# In Web UI, use agents
*analyst: Create PRD for user authentication
*architect: Design auth architecture
*developer: Implement authentication

# Use outputs in your IDE
```

<!-- section_id: "c7ddd6b2-e6b3-4830-a300-fbcae13dfbc8" -->
### Strategy 3: Combined Approach

**Best For**: Complex projects needing both structure and collaboration

**Setup**:
1. Use BMAD for ideation and planning (Analyst, Architect)
2. Use Spec Kit for execution (/specify, /plan, /tasks, /implement)
3. Use BMAD for QA (QA agent)
4. Maintain artifacts in both systems

**Example**:
```bash
# Phase 1: BMAD ideation
*analyst: Create requirements document
*architect: Design system architecture

# Phase 2: Spec Kit execution
/specify Build based on BMAD requirements
/plan Use architecture from BMAD
/tasks
/implement

# Phase 3: BMAD QA
*qa: Test implemented features
```

<!-- section_id: "4bd85c5e-001e-4f06-a603-3941376afe49" -->
## Context Management

<!-- section_id: "85f8c910-1ef6-46db-80f9-2babfdea4fd6" -->
### Spec Kit Context Files

Spec Kit creates context files that AI tools can reference:

```
specs/
├── 001-feature-name/
│   ├── spec.md          # Requirements context
│   ├── plan.md          # Implementation context
│   └── tasks.md          # Task execution context
```

AI tools should reference these files for context.

<!-- section_id: "73b2e5cb-2a53-4485-aacb-3b5162fddcf9" -->
### BMAD Context Artifacts

BMAD generates rich context artifacts:

```
.bmad/
├── artifacts/
│   ├── prd.md           # Requirements context
│   ├── architecture.md  # Design context
│   └── stories.md        # Development context
```

Import these into your IDE for AI to reference.

<!-- section_id: "fa56d89f-868c-4b62-bd90-bc8c3672225c" -->
### Best Practices

1. **Keep Context Updated**: Update specs/artifacts as code evolves
2. **Version Control**: Commit context changes alongside code
3. **Reference Explicitly**: Tell AI to reference specific context files
4. **Maintain Sync**: Keep specs and code in sync

<!-- section_id: "f0ad5fbe-5d92-426a-85bc-d4d714ce6b98" -->
## Specific Tool Configurations

<!-- section_id: "fd8054d6-a244-406d-bd04-03d75366d98f" -->
### Cursor Configuration

#### With Spec Kit

```json
// .cursor/rules (if using)
{
  "specifications": [
    "specs/**/spec.md",
    "specs/**/plan.md",
    "specs/**/tasks.md"
  ],
  "validation": true,
  "checkpoints": true
}
```

#### With BMAD

```json
// .cursor/rules
{
  "context_artifacts": [
    ".bmad/artifacts/**/*.md",
    ".bmad/briefs/**/*.md"
  ],
  "agent_outputs": true
}
```

<!-- section_id: "72a0a2d7-9c08-46bb-8841-e438daffcfc7" -->
### VS Code Configuration

Add to `.vscode/settings.json`:

```json
{
  "specKit.enabled": true,
  "specKit.specPath": "specs",
  "bmad.enabled": true,
  "bmad.artifactsPath": ".bmad/artifacts"
}
```

<!-- section_id: "e2ecd01b-eed1-454d-88dd-8763a41553b4" -->
### JetBrains IDEs

Install plugins:
- Spec Kit plugin (if available)
- BMAD plugin (if available)

Or add settings to project configuration.

<!-- section_id: "83767f1e-a1e8-4416-9b89-0ecddb899a94" -->
## Troubleshooting Integration

<!-- section_id: "01bb66e9-0bb3-41b7-9243-9e9c21212a9e" -->
### Issue: AI Not Following Specs

**Solution**: Ensure specs are up-to-date and AI can access them.

```bash
# Update specs
specify update

# Verify AI can access
ls -la specs/
```

<!-- section_id: "7fd1474e-5645-456b-ba02-ede74661782f" -->
### Issue: Context Too Large

**Solution**: Use sharding or filtering.

```bash
# Shard large context
bmad shard:create [large-doc] --max-size 5000

# Filter context
specify filter --keep-only "requirements,architecture"
```

<!-- section_id: "25c54a62-377e-4168-ac48-4e664711b277" -->
### Issue: Conflicting Guidance

**Solution**: Prioritize source of truth.

```bash
# Define primary context
specify primary-context specs/
bmad primary-context .bmad/artifacts/
```

<!-- section_id: "a03e2b65-29de-469d-9a16-a6c6d0a3935c" -->
### Issue: Performance Degradation

**Solution**: Optimize context loading.

```bash
# Lazy load context
specify lazy-load
bmad optimize-context
```

<!-- section_id: "118215cb-7bbd-42dd-952d-bf6d1d384cf4" -->
## Advanced Patterns

<!-- section_id: "554705ae-c6a4-4dc2-86e4-915cc39291da" -->
### Pattern 1: Spec-First Development

1. Always write specs before code
2. AI implements from specs
3. Validate implementation against specs
4. Update specs if requirements change

<!-- section_id: "8419d909-25a3-4ac6-9b69-b282d3db56b0" -->
### Pattern 2: Agent-Driven Development

1. Analyst defines requirements
2. Architect designs solution
3. Developer implements
4. QA validates
5. Human reviews and approves

<!-- section_id: "3af8fc7a-e4f1-46c8-b8e1-0993887ac771" -->
### Pattern 3: Hybrid Approach

1. BMAD agents for planning (Analyst, Architect)
2. Spec Kit for structured execution
3. BMAD for QA and review
4. Both for complete traceability

<!-- section_id: "d589671e-9f5f-449c-957f-f5ff558057a9" -->
## Success Metrics

Track these metrics to measure success:

<!-- section_id: "1db99ca9-bd03-4afa-98a3-ab90e1b9416b" -->
### Spec Kit Metrics
- Spec completion rate
- Validation checkpoint pass rate
- Time from spec to implementation
- Deviation rate from specs

<!-- section_id: "2137c1be-ec4c-4c56-8f21-b2fe9ec5e7f0" -->
### BMAD Metrics
- Agent utilization rate
- Artifact completeness
- Time from artifact to implementation
- Audit trail usage

<!-- section_id: "06239d21-42d3-4117-8690-511b784af6f6" -->
### Combined Metrics
- Total time from ideation to deployment
- Quality improvements
- Context retention rate
- Developer satisfaction

<!-- section_id: "fc76b401-a5e9-4ca8-a906-cc2c35e3ff1d" -->
## Next Steps

1. **Choose Your Tools**: Decide which AI tools you're using
2. **Pick Framework**: Select Spec Kit, BMAD, or both
3. **Follow Integration Steps**: Use this guide to integrate
4. **Measure Success**: Track metrics
5. **Iterate and Improve**: Refine based on results

---

*Remember: These frameworks enhance your existing tools. Start with simple integration and gradually adopt more advanced features.*

