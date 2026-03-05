---
resource_id: "b943b87a-b870-4cdd-a208-914295b0f347"
resource_type: "document"
resource_name: "integration-guide"
---
# Integration Guide
*Integrating Spec Kit and BMAD with Your Existing AI Tools*

<!-- section_id: "c1e43bad-403a-4506-9306-b3bd1d7e30db" -->
## Overview

This guide shows you how to integrate GitHub Spec Kit and BMAD Method with your existing AI coding assistants like Cursor, Codex, and Claude Code. These frameworks enhance your existing tools rather than replacing them.

<!-- section_id: "4cad25c2-d72a-41d1-97d0-1f83b80f0bd1" -->
## Tool Integration Matrix

<!-- section_id: "6aef06f3-9cb7-4aff-b827-7dfee45cff5d" -->
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

<!-- section_id: "7fbb7b8a-66b8-4c1a-8201-9796e849c81c" -->
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

<!-- section_id: "027ec7d9-9948-4971-9974-2f211a905ac5" -->
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

<!-- section_id: "a28dd08e-068d-4698-94b3-d651170da370" -->
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

<!-- section_id: "172408db-da75-42aa-8c0e-2aeca6a06c47" -->
## Implementation Strategies

<!-- section_id: "76fa69b9-59d2-4050-afbf-be704eca14d1" -->
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

<!-- section_id: "ff6be659-6610-4ca4-8d03-94c05cca78c0" -->
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

<!-- section_id: "7ceb3b21-1991-4049-9b21-a594f47e6e7b" -->
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

<!-- section_id: "a8c2696f-7fc5-46c2-8f87-915ab0c573c0" -->
## Context Management

<!-- section_id: "4be5ac9d-2852-476a-8ac4-e93a49b4bfa2" -->
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

<!-- section_id: "c5d1a40e-4241-4fc4-a0e2-87e877a9e42e" -->
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

<!-- section_id: "ee5a5736-b06c-4dcf-9532-8db05034adb6" -->
### Best Practices

1. **Keep Context Updated**: Update specs/artifacts as code evolves
2. **Version Control**: Commit context changes alongside code
3. **Reference Explicitly**: Tell AI to reference specific context files
4. **Maintain Sync**: Keep specs and code in sync

<!-- section_id: "3c9af55e-ce88-4cdd-a840-43917578597a" -->
## Specific Tool Configurations

<!-- section_id: "76f2256a-0583-4032-b88d-9632c82c4d57" -->
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

<!-- section_id: "da4c5941-ad8d-47d3-9243-2a777a4363ca" -->
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

<!-- section_id: "726205c7-36d5-426c-9137-ae53f073523e" -->
### JetBrains IDEs

Install plugins:
- Spec Kit plugin (if available)
- BMAD plugin (if available)

Or add settings to project configuration.

<!-- section_id: "70be2e64-1ef0-4e40-8457-47cee7c5ccef" -->
## Troubleshooting Integration

<!-- section_id: "c51f262d-2e6d-43ff-bbb2-9619baa8e0cf" -->
### Issue: AI Not Following Specs

**Solution**: Ensure specs are up-to-date and AI can access them.

```bash
# Update specs
specify update

# Verify AI can access
ls -la specs/
```

<!-- section_id: "7c39d4df-cc57-409e-b60e-8dc5ea8a6200" -->
### Issue: Context Too Large

**Solution**: Use sharding or filtering.

```bash
# Shard large context
bmad shard:create [large-doc] --max-size 5000

# Filter context
specify filter --keep-only "requirements,architecture"
```

<!-- section_id: "d97a1d82-837b-4351-a51e-5c2eb3d894a5" -->
### Issue: Conflicting Guidance

**Solution**: Prioritize source of truth.

```bash
# Define primary context
specify primary-context specs/
bmad primary-context .bmad/artifacts/
```

<!-- section_id: "999ef8da-d81e-4a30-bfd1-a9fdeb4e495e" -->
### Issue: Performance Degradation

**Solution**: Optimize context loading.

```bash
# Lazy load context
specify lazy-load
bmad optimize-context
```

<!-- section_id: "c7a94f91-3563-4e7a-8caa-eda737edcab4" -->
## Advanced Patterns

<!-- section_id: "f14f3051-b0f5-424f-835c-1bf5421844d3" -->
### Pattern 1: Spec-First Development

1. Always write specs before code
2. AI implements from specs
3. Validate implementation against specs
4. Update specs if requirements change

<!-- section_id: "30a8c1fe-20c5-4248-9d7c-47afe6f9340d" -->
### Pattern 2: Agent-Driven Development

1. Analyst defines requirements
2. Architect designs solution
3. Developer implements
4. QA validates
5. Human reviews and approves

<!-- section_id: "9cb4f833-72c0-4b58-b24f-b56a49e36687" -->
### Pattern 3: Hybrid Approach

1. BMAD agents for planning (Analyst, Architect)
2. Spec Kit for structured execution
3. BMAD for QA and review
4. Both for complete traceability

<!-- section_id: "48514867-14ce-4dbf-abee-f39c8422a0fc" -->
## Success Metrics

Track these metrics to measure success:

<!-- section_id: "a9a0e111-1103-4527-8ac7-16c4e2a47ada" -->
### Spec Kit Metrics
- Spec completion rate
- Validation checkpoint pass rate
- Time from spec to implementation
- Deviation rate from specs

<!-- section_id: "6c0d5bc7-4b3d-49ac-87a5-92c8ad16b3ec" -->
### BMAD Metrics
- Agent utilization rate
- Artifact completeness
- Time from artifact to implementation
- Audit trail usage

<!-- section_id: "ea358f2d-fcca-42ea-84c2-eedafb359d63" -->
### Combined Metrics
- Total time from ideation to deployment
- Quality improvements
- Context retention rate
- Developer satisfaction

<!-- section_id: "77308300-ad2c-409f-8abc-686f545e2478" -->
## Next Steps

1. **Choose Your Tools**: Decide which AI tools you're using
2. **Pick Framework**: Select Spec Kit, BMAD, or both
3. **Follow Integration Steps**: Use this guide to integrate
4. **Measure Success**: Track metrics
5. **Iterate and Improve**: Refine based on results

---

*Remember: These frameworks enhance your existing tools. Start with simple integration and gradually adopt more advanced features.*

