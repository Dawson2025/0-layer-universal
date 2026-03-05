---
resource_id: "3e27c181-746b-4bea-953d-8f02ff9ac31f"
resource_type: "document"
resource_name: "bmad-method-guide"
---
# BMAD Method - Comprehensive Guide
*Breakthrough Method for Agile AI-Driven Development*

<!-- section_id: "5ac42c69-7962-488b-a28f-bd2112517de2" -->
## Overview

The BMAD (Breakthrough Method for Agile AI-Driven Development) Method introduces specialized AI agents that collaborate as a development team, streamlining the development process. Each agent has specific responsibilities, working together to transform vague requirements into production-ready software.

<!-- section_id: "cefe996e-14c3-4c24-99a9-34a1069d239b" -->
## Key Concepts

<!-- section_id: "59c11b9b-125a-458b-a944-aa72136da738" -->
### What is Agentic Team Development?

Agentic team development is a methodology where:
- **Specialized AI Agents** work as a collaborative development team
- **Each Agent** has specific role responsibilities
- **Git-Based Versioning** tracks all artifacts (PRDs, architecture, stories)
- **Context-Engineered Development** uses hyper-detailed development stories
- **Human + AI Review** ensures quality through pull request reviews

<!-- section_id: "8bf50fc1-cb04-475b-9618-09aad4733a3d" -->
### Core Philosophy

**Problem**: Traditional AI prompting lacks structure, traceability, and accountability.

**Solution**: Create a system where specialized AI agents collaborate like a real development team, with clear roles, responsibilities, and comprehensive audit trails.

<!-- section_id: "75d00fcc-53e8-4588-b091-23a517cff453" -->
## Key Features

<!-- section_id: "7111128c-3852-4bbf-ba1d-8cd20464937c" -->
### 1. Specialized AI Agents

Each agent has specific responsibilities:

- **Analyst**: Requirements gathering and analysis
- **Product Manager**: Product vision and roadmap
- **Architect**: System architecture and technical decisions
- **Scrum Master**: Process management and sprint planning
- **Product Owner**: Backlog management and prioritization
- **Developer**: Code implementation
- **QA**: Testing and quality assurance

<!-- section_id: "31827223-a3e7-471d-8c5d-0bc8513840cf" -->
### 2. Git-Based Artifact Versioning

All artifacts are version-controlled:
- PRDs (Product Requirement Documents)
- Architecture documents
- Development stories
- Code implementations
- Test results

<!-- section_id: "7258acd9-886d-46d0-ba47-54f36231f8bb" -->
### 3. Context-Engineered Development

Hyper-detailed development stories ensure:
- Complete context preservation
- No information loss
- Traceable decision-making
- Single source of truth

<!-- section_id: "ce89e9b1-c8bf-45c2-b380-96ea07a54608" -->
### 4. Pull Request Reviews

Quality assurance through:
- Human review of AI-generated content
- AI agent review of implementations
- Automated testing
- Comprehensive validation

<!-- section_id: "72747ae4-f63b-41c7-9b8b-c429398ff955" -->
## Installation

<!-- section_id: "c738b676-b9cb-4c6f-a09b-382201ddb239" -->
### Prerequisites

- Node.js v20+
- `npx` command available
- Git repository initialized

<!-- section_id: "6a79f16d-5b1a-43e3-bd65-ac20d2c8cb79" -->
### Install BMAD

```bash
npx bmad-method install
```

This command handles:
- New installations
- Upgrades
- Expansion packs

<!-- section_id: "2f10c6fc-744e-46e4-94b7-dda1151636ee" -->
### Verify Installation

```bash
# Check if BMAD is installed
ls -la .bmad/

# View available commands
bmad --help
```

<!-- section_id: "351773f6-dffb-4669-b25e-316282c7cb6b" -->
## Getting Started

<!-- section_id: "74aadac1-f011-42ef-b872-94040c277e99" -->
### Step 1: Set Up the Web UI

1. **Obtain the Full-Stack Team Bundle**
   - Download from https://github.com/bmad-code-org/BMAD-METHOD
   - Extract the bundle files

2. **Create a New AI Agent**
   - Use Gemini Gem or CustomGPT
   - Upload the bundle files

3. **Configure the Agent**
   - Upload instruction: "Your critical operating instructions are attached, do not break character as directed."

<!-- section_id: "12ac1d37-34c2-46ed-b14a-e6f011bf3193" -->
### Step 2: Begin Ideation and Planning

#### Start with Analyst Agent

```bash
*help                    # See available options
*analyst                 # Initiate creation of a brief
```

#### Generate Product Brief

```
*analyst

I need a product brief for a task management application called "Taskify"
with user authentication, real-time collaboration, and mobile support.
```

The Analyst agent will:
1. Gather requirements
2. Create a detailed brief
3. Document acceptance criteria
4. Generate the PRD

#### Progress Through Team

After PRD is complete:

```bash
*product_manager    # Define product vision and roadmap
*architect         # Design system architecture
*scrum_master      # Create sprint planning
*product_owner     # Manage backlog and prioritization
```

<!-- section_id: "0c07d3ff-8e73-4a20-8d17-9bd6399e60eb" -->
### Step 3: Transition to IDE

Once you have PRD, architecture, and briefs:

1. **Shard Your Documents**
   - Break down into manageable pieces
   - Import into your development environment

2. **Begin Implementation**
   - Developer agent implements code
   - Follow development stories
   - Respect architectural decisions

3. **QA Validation**
   - QA agent creates tests
   - Runs automated tests
   - Validates against acceptance criteria

<!-- section_id: "ba300ca3-5566-4e11-9c0a-e83be5c3bae2" -->
## Agent Responsibilities

<!-- section_id: "d9efa900-ebc8-403a-85ed-5b801783270c" -->
### Analyst Agent

**Role**: Requirements gathering and analysis

**Responsibilities**:
- Gather requirements from stakeholders
- Analyze business needs
- Create comprehensive briefs
- Document acceptance criteria
- Define user personas

**Output**:
- Product brief
- Requirements document
- User stories
- Acceptance criteria

<!-- section_id: "d28db889-6438-40f4-a41b-a186912863db" -->
### Product Manager Agent

**Role**: Product vision and roadmap

**Responsibilities**:
- Define product vision
- Create product roadmap
- Prioritize features
- Communicate with stakeholders
- Guide product direction

**Output**:
- Product roadmap
- Feature prioritization
- Market analysis
- Competitive positioning

<!-- section_id: "ab8564e3-7830-4535-b3a2-81f161772957" -->
### Architect Agent

**Role**: System architecture and technical decisions

**Responsibilities**:
- Design system architecture
- Make technical decisions
- Define technology stack
- Plan system integration
- Consider scalability and performance

**Output**:
- Architecture diagrams
- Technical specifications
- Technology decisions
- Integration plans

<!-- section_id: "90595838-c05d-4def-a23c-08cd2824c24b" -->
### Scrum Master Agent

**Role**: Process management and sprint planning

**Responsibilities**:
- Plan sprints
- Manage process
- Facilitate ceremonies
- Track progress
- Remove blockers

**Output**:
- Sprint plan
- Process documentation
- Progress reports
- Retrospective notes

<!-- section_id: "7d6447a0-5c01-4865-9e67-628173a9e871" -->
### Product Owner Agent

**Role**: Backlog management and prioritization

**Responsibilities**:
- Manage product backlog
- Prioritize features
- Refine user stories
- Accept completed work
- Communicate priorities

**Output**:
- Prioritized backlog
- Refined user stories
- Acceptance criteria
- Release planning

<!-- section_id: "b2d2104c-b17d-4281-b9c1-c798227c0b92" -->
### Developer Agent

**Role**: Code implementation

**Responsibilities**:
- Implement features
- Write clean code
- Follow coding standards
- Create documentation
- Perform code reviews

**Output**:
- Implemented features
- Code documentation
- Code reviews
- Technical notes

<!-- section_id: "8741b715-ef14-4118-a877-9d51c1f85384" -->
### QA Agent

**Role**: Testing and quality assurance

**Responsibilities**:
- Create test plans
- Write test cases
- Execute tests
- Report bugs
- Validate quality

**Output**:
- Test plans
- Test cases
- Test results
- Bug reports

<!-- section_id: "f9592079-ba74-40df-9ac4-ba15efe5af1d" -->
## Workflow Example

<!-- section_id: "37eb2792-8e9b-4636-a4e1-ddb9bce009a7" -->
### Scenario: Building a Task Management App

#### Phase 1: Ideation (Analyst + Product Manager)

```bash
*analyst

I need to build a task management application. Key requirements:
- User authentication
- Real-time collaboration
- Drag-and-drop task boards
- Mobile support
- Push notifications
```

**Output**: Product brief with requirements, acceptance criteria, user personas

#### Phase 2: Architecture (Architect)

```bash
*architect

Based on the analyst's brief, I need to design the system architecture:
- Frontend: React with TypeScript
- Backend: Node.js with Express
- Database: PostgreSQL with Redis caching
- Real-time: Socket.io
- Auth: OAuth 2.0
```

**Output**: Architecture diagrams, technical specifications, technology decisions

#### Phase 3: Sprint Planning (Scrum Master + Product Owner)

```bash
*scrum_master

Create sprint plan for first 2-week sprint:
- User authentication
- Basic CRUD operations
- Simple real-time updates
```

**Output**: Sprint plan with tasks, estimates, dependencies

```bash
*product_owner

Prioritize and refine the backlog based on product goals:
- Highest priority: User authentication
- Medium priority: Basic CRUD
- Lower priority: Advanced features
```

**Output**: Prioritized backlog with refined user stories

#### Phase 4: Implementation (Developer)

```bash
*developer

Implement User Authentication feature:
- Login/logout functionality
- JWT token management
- Protected routes
- Error handling
```

**Output**: Implemented code with tests and documentation

#### Phase 5: QA (QA Agent)

```bash
*qa

Test User Authentication feature:
- Unit tests for auth logic
- Integration tests for API endpoints
- E2E tests for user flow
- Security testing
```

**Output**: Test results, bug reports, validation report

<!-- section_id: "e139e9ed-1b55-4fd9-bb8e-48b4af213aff" -->
## Directory Structure

After initialization, your project will have this structure:

```
.
├── .bmad/
│   ├── agents/              # Agent configurations
│   ├── artifacts/           # Generated artifacts
│   ├── briefs/              # Analyst briefs
│   ├── prds/                # Product Requirement Documents
│   ├── architecture/        # Architecture documents
│   ├── sprints/             # Sprint plans and artifacts
│   └── stories/             # Development stories
├── docs/
│   ├── brief.md             # Current brief
│   ├── prd.md               # Current PRD
│   ├── architecture.md      # System architecture
│   └── development/        # Development documentation
├── code/
│   ├── frontend/
│   ├── backend/
│   └── tests/
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```

<!-- section_id: "3c8026bb-0cc6-4724-8d74-676c5f6d98ad" -->
## Best Practices

<!-- section_id: "11f40c22-ec1e-4e28-b377-3560ccda9542" -->
### Working with Agents

1. **Be Specific**: Provide clear, detailed instructions
2. **Use Proper Commands**: Follow the command syntax
3. **Review Outputs**: Always review agent outputs before proceeding
4. **Iterate**: Don't be afraid to refine and iterate

<!-- section_id: "ca3b4ba6-6f11-46ba-ac68-3b552260783f" -->
### Artifact Management

1. **Version Control**: All artifacts in Git
2. **Documentation**: Keep documentation up-to-date
3. **Sharding**: Break large documents into manageable pieces
4. **Organization**: Maintain clear directory structure

<!-- section_id: "32da5574-07fa-41f4-ab72-edea7fdd03da" -->
### Development Process

1. **Follow the Sprint Plan**: Stick to the plan during sprints
2. **Respect Dependencies**: Don't skip dependencies
3. **Test Continuously**: Run tests frequently
4. **Code Reviews**: Review AI-generated code before acceptance

<!-- section_id: "b237740b-07aa-4b7a-aba6-e3d994180be7" -->
### Quality Assurance

1. **Test Early**: Write tests alongside code
2. **Automate Testing**: Use automated test suites
3. **Security Testing**: Don't skip security testing
4. **User Testing**: Include real user feedback

<!-- section_id: "d4bdaf07-8155-4eac-8dc6-65775cd9730a" -->
## Advanced Features

<!-- section_id: "e77c6b39-0f17-4299-9be0-bfa20adc871f" -->
### Custom Agents

Create custom agents for specific needs:

1. **Define Agent Role**: What is the agent responsible for?
2. **Configure Behavior**: How should the agent behave?
3. **Set Outputs**: What should the agent produce?
4. **Test Agent**: Validate agent behavior

<!-- section_id: "b826159d-8560-44d0-bb13-5c4be47b733e" -->
### Multi-Agent Coordination

Coordinate multiple agents working together:

```bash
# Start multiple agents
*analyst:start
*architect:start
*developer:start

# Coordinate work
*analyst -> *architect: Transfer requirements
*architect -> *developer: Transfer architecture
```

<!-- section_id: "0d427a59-6d7f-41ef-9311-5e93af5bfb5c" -->
### Integration with Git

Git integration provides:
- Automatic artifact versioning
- Change tracking
- Rollback capabilities
- Collaboration support

<!-- section_id: "5773e2d1-258a-4332-bd6c-221d15200742" -->
### Continuous Integration

Integrate with CI/CD:
- Automated testing
- Deployment pipelines
- Quality checks
- Performance monitoring

<!-- section_id: "cec177fc-60a3-4f27-aa43-6a9316e36c98" -->
## Troubleshooting

<!-- section_id: "4455bd85-806a-42c3-a356-dbcf17e6b21f" -->
### Common Issues

#### Issue: Agent not responding

**Solution**: Check agent configuration and ensure all dependencies are installed:
```bash
bmad agent:check [agent-name]
```

#### Issue: Missing artifacts

**Solution**: Regenerate artifacts using agent commands:
```bash
*analyst:regenerate
*architect:regenerate
```

#### Issue: Context loss

**Solution**: Use sharding to maintain context:
```bash
bmad shard:create [document] --max-size 5000
```

<!-- section_id: "2b465313-5433-4726-9ae4-da34fd19f100" -->
### Validation

Always validate agent outputs:
- Review for accuracy
- Check for completeness
- Verify alignment with requirements
- Test implementations

<!-- section_id: "a7bdbf4e-28d9-475f-b446-fafd7a8e8f3a" -->
## Resources

<!-- section_id: "8161b902-c742-403b-8cfd-5a5a06c65bdd" -->
### Official Documentation
- **Documentation**: https://bmadcodes.com/
- **User Guide**: https://deepwiki.com/bmad-code-org/BMAD-METHOD/3-user-guide
- **GitHub**: https://github.com/bmad-code-org/BMAD-METHOD

<!-- section_id: "248323f0-8579-4392-aea0-28b9336ca61f" -->
### Community
- **Issues**: https://github.com/bmad-code-org/BMAD-METHOD/issues
- **Discussions**: GitHub Discussions

<!-- section_id: "727787c2-7ebd-4697-9a0f-372b989ac5fd" -->
### Examples
- **Quick Start**: See `docs/brief.md` in any initialized project
- **Templates**: Check `.bmad/agents/` directory

<!-- section_id: "369b957f-b9e3-4b3d-8c37-abe51e81337e" -->
## Summary

BMAD Method provides:

- ✅ **Agentic Team Collaboration**: Specialized AI agents working together
- ✅ **Traceability**: Comprehensive audit trails from ideation to implementation
- ✅ **Context Engineering**: Hyper-detailed development stories
- ✅ **Quality Assurance**: Human + AI review of AI-generated content
- ✅ **Scalability**: Works for projects of any size

**Key Benefit**: Provides accountability, traceability, and structured workflows that prevent context loss and accelerate development cycles.

---

*For detailed agent documentation, workflow patterns, and advanced usage, refer to the official documentation at https://bmadcodes.com/.*

