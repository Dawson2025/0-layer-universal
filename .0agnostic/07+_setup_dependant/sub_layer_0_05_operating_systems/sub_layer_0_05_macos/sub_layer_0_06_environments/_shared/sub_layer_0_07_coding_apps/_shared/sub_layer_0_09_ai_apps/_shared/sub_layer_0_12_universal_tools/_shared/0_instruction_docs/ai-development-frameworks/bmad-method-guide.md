---
resource_id: "b7a675ed-0c52-42b4-ab71-2a4c06d18be5"
resource_type: "document"
resource_name: "bmad-method-guide"
---
# BMAD Method - Comprehensive Guide
*Breakthrough Method for Agile AI-Driven Development*

<!-- section_id: "086d904a-e89e-4721-b3d7-25566c0e3f4c" -->
## Overview

The BMAD (Breakthrough Method for Agile AI-Driven Development) Method introduces specialized AI agents that collaborate as a development team, streamlining the development process. Each agent has specific responsibilities, working together to transform vague requirements into production-ready software.

<!-- section_id: "32b1af90-cae7-44b1-906b-fe202ac67616" -->
## Key Concepts

<!-- section_id: "1036f8f1-250e-48d8-aa5a-1bd0f338fb75" -->
### What is Agentic Team Development?

Agentic team development is a methodology where:
- **Specialized AI Agents** work as a collaborative development team
- **Each Agent** has specific role responsibilities
- **Git-Based Versioning** tracks all artifacts (PRDs, architecture, stories)
- **Context-Engineered Development** uses hyper-detailed development stories
- **Human + AI Review** ensures quality through pull request reviews

<!-- section_id: "8e88808d-04f7-43f8-bcc1-4e44049837df" -->
### Core Philosophy

**Problem**: Traditional AI prompting lacks structure, traceability, and accountability.

**Solution**: Create a system where specialized AI agents collaborate like a real development team, with clear roles, responsibilities, and comprehensive audit trails.

<!-- section_id: "b636e526-818b-4aec-8305-7a02d45727a2" -->
## Key Features

<!-- section_id: "fc92e750-24f5-4db8-8e37-971caa7f1441" -->
### 1. Specialized AI Agents

Each agent has specific responsibilities:

- **Analyst**: Requirements gathering and analysis
- **Product Manager**: Product vision and roadmap
- **Architect**: System architecture and technical decisions
- **Scrum Master**: Process management and sprint planning
- **Product Owner**: Backlog management and prioritization
- **Developer**: Code implementation
- **QA**: Testing and quality assurance

<!-- section_id: "0ed125e1-fa14-444a-bdab-ccbed886288a" -->
### 2. Git-Based Artifact Versioning

All artifacts are version-controlled:
- PRDs (Product Requirement Documents)
- Architecture documents
- Development stories
- Code implementations
- Test results

<!-- section_id: "e0e5151b-c739-48ee-863e-34cdc6d3f90b" -->
### 3. Context-Engineered Development

Hyper-detailed development stories ensure:
- Complete context preservation
- No information loss
- Traceable decision-making
- Single source of truth

<!-- section_id: "c1ace268-ea9d-4379-9b74-89d58066cb2d" -->
### 4. Pull Request Reviews

Quality assurance through:
- Human review of AI-generated content
- AI agent review of implementations
- Automated testing
- Comprehensive validation

<!-- section_id: "bd9f21d0-c433-423d-94e9-af21d37e6b5d" -->
## Installation

<!-- section_id: "a0c9b103-cd69-4123-aa71-c65139283c9c" -->
### Prerequisites

- Node.js v20+
- `npx` command available
- Git repository initialized

<!-- section_id: "269791f6-0a2b-4144-b574-d7279963be3f" -->
### Install BMAD

```bash
npx bmad-method install
```

This command handles:
- New installations
- Upgrades
- Expansion packs

<!-- section_id: "a298930b-fa68-4584-a923-3fa176d3bbaa" -->
### Verify Installation

```bash
# Check if BMAD is installed
ls -la .bmad/

# View available commands
bmad --help
```

<!-- section_id: "63de10ac-896f-4457-ab02-ed05e002f0fa" -->
## Getting Started

<!-- section_id: "9c3213ed-b2bc-491d-9589-6a7b7a8ee303" -->
### Step 1: Set Up the Web UI

1. **Obtain the Full-Stack Team Bundle**
   - Download from https://github.com/bmad-code-org/BMAD-METHOD
   - Extract the bundle files

2. **Create a New AI Agent**
   - Use Gemini Gem or CustomGPT
   - Upload the bundle files

3. **Configure the Agent**
   - Upload instruction: "Your critical operating instructions are attached, do not break character as directed."

<!-- section_id: "2856a031-c2a0-4526-84c6-4c46b41ac09c" -->
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

<!-- section_id: "a5bb16fc-ae17-4e2b-a919-8ba47d74aec2" -->
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

<!-- section_id: "77c56702-2739-414f-be70-9df57e8798ea" -->
## Agent Responsibilities

<!-- section_id: "8e915daa-3228-41f6-b335-78f73fddbcd0" -->
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

<!-- section_id: "357e9cf0-ea69-4e42-92cb-0bafd7c066ff" -->
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

<!-- section_id: "5dbb31ce-95f1-4003-8c8e-e45f1b30735c" -->
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

<!-- section_id: "6a8d7407-faa7-46f5-a7ed-5cfe33bafb95" -->
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

<!-- section_id: "85a6fd4e-22f7-401e-9653-58db0c718c80" -->
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

<!-- section_id: "1a94012b-ba27-430c-a3f7-b2d0f95bf4fd" -->
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

<!-- section_id: "7ae634cd-c9b0-4336-ba90-2424f3ea8564" -->
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

<!-- section_id: "e86fcd09-4110-4d53-a631-546e9efa61bb" -->
## Workflow Example

<!-- section_id: "8a5f7f20-e085-442e-b89d-a1a57227e9a6" -->
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

<!-- section_id: "1aa7912a-7721-4017-907c-67dd4c98f0e1" -->
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

<!-- section_id: "a941e5cb-4a96-49d8-b65f-5ebb58a79e98" -->
## Best Practices

<!-- section_id: "832355ff-b43d-46a8-ad4b-a4ae16b7f207" -->
### Working with Agents

1. **Be Specific**: Provide clear, detailed instructions
2. **Use Proper Commands**: Follow the command syntax
3. **Review Outputs**: Always review agent outputs before proceeding
4. **Iterate**: Don't be afraid to refine and iterate

<!-- section_id: "08cc2981-6d43-4c37-b922-3ce09f0970c6" -->
### Artifact Management

1. **Version Control**: All artifacts in Git
2. **Documentation**: Keep documentation up-to-date
3. **Sharding**: Break large documents into manageable pieces
4. **Organization**: Maintain clear directory structure

<!-- section_id: "7841cc00-609e-4eea-9d9d-0fe31e2e5752" -->
### Development Process

1. **Follow the Sprint Plan**: Stick to the plan during sprints
2. **Respect Dependencies**: Don't skip dependencies
3. **Test Continuously**: Run tests frequently
4. **Code Reviews**: Review AI-generated code before acceptance

<!-- section_id: "5b5722db-6920-4ca2-bce5-8e7b0fc32a73" -->
### Quality Assurance

1. **Test Early**: Write tests alongside code
2. **Automate Testing**: Use automated test suites
3. **Security Testing**: Don't skip security testing
4. **User Testing**: Include real user feedback

<!-- section_id: "17eacd46-4379-4484-8796-e9c5046a67de" -->
## Advanced Features

<!-- section_id: "91e4004a-e2ff-4a25-b7d4-240f37858936" -->
### Custom Agents

Create custom agents for specific needs:

1. **Define Agent Role**: What is the agent responsible for?
2. **Configure Behavior**: How should the agent behave?
3. **Set Outputs**: What should the agent produce?
4. **Test Agent**: Validate agent behavior

<!-- section_id: "e3f645e6-501a-40de-8b2c-38cc4fbb059e" -->
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

<!-- section_id: "974f86ea-4c49-4bc7-97be-609c7983e71d" -->
### Integration with Git

Git integration provides:
- Automatic artifact versioning
- Change tracking
- Rollback capabilities
- Collaboration support

<!-- section_id: "85b87316-d3a0-4a80-834a-4991d7e2c020" -->
### Continuous Integration

Integrate with CI/CD:
- Automated testing
- Deployment pipelines
- Quality checks
- Performance monitoring

<!-- section_id: "b3cab4dd-bdc0-4456-8feb-0a32c6132043" -->
## Troubleshooting

<!-- section_id: "327c4e72-5ee7-4db7-8ad8-5dabdd78f40b" -->
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

<!-- section_id: "0cda7199-0a17-4961-96d3-59067b1415bb" -->
### Validation

Always validate agent outputs:
- Review for accuracy
- Check for completeness
- Verify alignment with requirements
- Test implementations

<!-- section_id: "058b7656-c74c-4fb2-b647-913eb0f32fcf" -->
## Resources

<!-- section_id: "35e3d742-38a4-464d-95fe-6a30d3ed957e" -->
### Official Documentation
- **Documentation**: https://bmadcodes.com/
- **User Guide**: https://deepwiki.com/bmad-code-org/BMAD-METHOD/3-user-guide
- **GitHub**: https://github.com/bmad-code-org/BMAD-METHOD

<!-- section_id: "c999bf09-a2ce-45b5-9258-c6848719c54d" -->
### Community
- **Issues**: https://github.com/bmad-code-org/BMAD-METHOD/issues
- **Discussions**: GitHub Discussions

<!-- section_id: "78644324-605c-4f27-806f-1c3e16b1cbd5" -->
### Examples
- **Quick Start**: See `docs/brief.md` in any initialized project
- **Templates**: Check `.bmad/agents/` directory

<!-- section_id: "a9b3158b-5835-4b2c-b9d8-96ebeb027fd1" -->
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

