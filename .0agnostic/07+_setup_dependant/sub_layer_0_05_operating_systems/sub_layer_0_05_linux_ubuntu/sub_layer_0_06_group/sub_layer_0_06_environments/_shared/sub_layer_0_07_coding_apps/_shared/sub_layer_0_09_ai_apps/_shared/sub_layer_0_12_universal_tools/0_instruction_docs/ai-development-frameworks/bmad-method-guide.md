---
resource_id: "9c8c49d6-a2ac-4a19-8a90-a4b5c7b3c0c6"
resource_type: "document"
resource_name: "bmad-method-guide"
---
# BMAD Method - Comprehensive Guide
*Breakthrough Method for Agile AI-Driven Development*

<!-- section_id: "18218544-430e-435a-9e1e-d01e8cb18a2f" -->
## Overview

The BMAD (Breakthrough Method for Agile AI-Driven Development) Method introduces specialized AI agents that collaborate as a development team, streamlining the development process. Each agent has specific responsibilities, working together to transform vague requirements into production-ready software.

<!-- section_id: "35ff8ab9-82af-443e-b8f4-3620064ae112" -->
## Key Concepts

<!-- section_id: "2186f7e6-1ea1-4d2c-bf4c-2a31491fd124" -->
### What is Agentic Team Development?

Agentic team development is a methodology where:
- **Specialized AI Agents** work as a collaborative development team
- **Each Agent** has specific role responsibilities
- **Git-Based Versioning** tracks all artifacts (PRDs, architecture, stories)
- **Context-Engineered Development** uses hyper-detailed development stories
- **Human + AI Review** ensures quality through pull request reviews

<!-- section_id: "1296d061-9f99-437b-b91d-ef09365eab5a" -->
### Core Philosophy

**Problem**: Traditional AI prompting lacks structure, traceability, and accountability.

**Solution**: Create a system where specialized AI agents collaborate like a real development team, with clear roles, responsibilities, and comprehensive audit trails.

<!-- section_id: "d5236063-5ceb-4957-a87e-58213c5cb533" -->
## Key Features

<!-- section_id: "c9024502-ff66-41ad-87dc-d9101c407f03" -->
### 1. Specialized AI Agents

Each agent has specific responsibilities:

- **Analyst**: Requirements gathering and analysis
- **Product Manager**: Product vision and roadmap
- **Architect**: System architecture and technical decisions
- **Scrum Master**: Process management and sprint planning
- **Product Owner**: Backlog management and prioritization
- **Developer**: Code implementation
- **QA**: Testing and quality assurance

<!-- section_id: "ad476576-6ec9-428c-a782-83bea39ea0e2" -->
### 2. Git-Based Artifact Versioning

All artifacts are version-controlled:
- PRDs (Product Requirement Documents)
- Architecture documents
- Development stories
- Code implementations
- Test results

<!-- section_id: "5b17747f-d908-4f2c-90cc-6998108d87ef" -->
### 3. Context-Engineered Development

Hyper-detailed development stories ensure:
- Complete context preservation
- No information loss
- Traceable decision-making
- Single source of truth

<!-- section_id: "ea58ecbe-042c-455c-a7e1-90c22ab3dfda" -->
### 4. Pull Request Reviews

Quality assurance through:
- Human review of AI-generated content
- AI agent review of implementations
- Automated testing
- Comprehensive validation

<!-- section_id: "7cb64b5b-f161-4dab-b920-78a4f15c6fec" -->
## Installation

<!-- section_id: "a5882360-263a-4e8f-962a-08553d8f1d75" -->
### Prerequisites

- Node.js v20+
- `npx` command available
- Git repository initialized

<!-- section_id: "31bd074f-27eb-4639-a93f-7d57ec81f7d9" -->
### Install BMAD

```bash
npx bmad-method install
```

This command handles:
- New installations
- Upgrades
- Expansion packs

<!-- section_id: "37b8775b-d967-4d4a-af3c-28a96b0d39dc" -->
### Verify Installation

```bash
# Check if BMAD is installed
ls -la .bmad/

# View available commands
bmad --help
```

<!-- section_id: "7f423620-0eb4-4874-ac2b-59ed29ad18df" -->
## Getting Started

<!-- section_id: "c21fe02e-1d10-4b4a-b3a8-931000c78686" -->
### Step 1: Set Up the Web UI

1. **Obtain the Full-Stack Team Bundle**
   - Download from https://github.com/bmad-code-org/BMAD-METHOD
   - Extract the bundle files

2. **Create a New AI Agent**
   - Use Gemini Gem or CustomGPT
   - Upload the bundle files

3. **Configure the Agent**
   - Upload instruction: "Your critical operating instructions are attached, do not break character as directed."

<!-- section_id: "b7bd0a08-a704-412f-a4b6-0c2dc79e0eaa" -->
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

<!-- section_id: "fc89c69f-d68b-4fee-a683-a9ff0d0bc979" -->
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

<!-- section_id: "2b4523be-738c-4f76-88cb-c290866b5cb9" -->
## Agent Responsibilities

<!-- section_id: "84a794ec-6c49-4bbc-a06e-11bade084379" -->
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

<!-- section_id: "d426e2bd-5259-4fa7-a5a7-24bce3a2a801" -->
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

<!-- section_id: "a5774769-3983-4a17-98ad-52e7087ea200" -->
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

<!-- section_id: "0d3df608-7095-4000-b4f4-fb081803cc42" -->
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

<!-- section_id: "e29cb44f-e5d8-48a0-b362-121077dea385" -->
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

<!-- section_id: "691e304e-b339-4aa9-9281-01456afb4b12" -->
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

<!-- section_id: "478dc53d-7793-45ae-85fb-7812e8f00e1b" -->
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

<!-- section_id: "2399e722-0cc1-46ba-bb57-8e61dde0dbfe" -->
## Workflow Example

<!-- section_id: "97734688-e024-4f4a-a930-a82ba8f638c4" -->
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

<!-- section_id: "0babf20b-6d29-491f-8d32-63959e6a4340" -->
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

<!-- section_id: "4b55dc47-cdaa-45cf-8f28-e5b5f4ceddc2" -->
## Best Practices

<!-- section_id: "7f50eac6-9da9-4941-a999-033ab133d6bd" -->
### Working with Agents

1. **Be Specific**: Provide clear, detailed instructions
2. **Use Proper Commands**: Follow the command syntax
3. **Review Outputs**: Always review agent outputs before proceeding
4. **Iterate**: Don't be afraid to refine and iterate

<!-- section_id: "4bdfd86a-6c8e-49f5-929b-c26844cbbfd1" -->
### Artifact Management

1. **Version Control**: All artifacts in Git
2. **Documentation**: Keep documentation up-to-date
3. **Sharding**: Break large documents into manageable pieces
4. **Organization**: Maintain clear directory structure

<!-- section_id: "b0d7fd3e-f5df-4a40-b539-921cd08fa420" -->
### Development Process

1. **Follow the Sprint Plan**: Stick to the plan during sprints
2. **Respect Dependencies**: Don't skip dependencies
3. **Test Continuously**: Run tests frequently
4. **Code Reviews**: Review AI-generated code before acceptance

<!-- section_id: "f27ce95d-ea55-49d7-a697-5e6a8254cb46" -->
### Quality Assurance

1. **Test Early**: Write tests alongside code
2. **Automate Testing**: Use automated test suites
3. **Security Testing**: Don't skip security testing
4. **User Testing**: Include real user feedback

<!-- section_id: "4ab5241d-fad6-430f-9bac-2c59e2cca9b0" -->
## Advanced Features

<!-- section_id: "9ce72a68-1853-4013-bf11-472b8d438355" -->
### Custom Agents

Create custom agents for specific needs:

1. **Define Agent Role**: What is the agent responsible for?
2. **Configure Behavior**: How should the agent behave?
3. **Set Outputs**: What should the agent produce?
4. **Test Agent**: Validate agent behavior

<!-- section_id: "6745b99c-9a37-4dc9-9fd4-201eb52718e4" -->
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

<!-- section_id: "273859c5-d636-46ed-b954-01b592c1172c" -->
### Integration with Git

Git integration provides:
- Automatic artifact versioning
- Change tracking
- Rollback capabilities
- Collaboration support

<!-- section_id: "60239227-a43b-489d-a8a7-c9a1dcc3dfff" -->
### Continuous Integration

Integrate with CI/CD:
- Automated testing
- Deployment pipelines
- Quality checks
- Performance monitoring

<!-- section_id: "97def70b-1ca9-43c8-bd77-69414af756a3" -->
## Troubleshooting

<!-- section_id: "4dc7a786-15b9-41c9-9dcb-b066b91d7f49" -->
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

<!-- section_id: "10e4de1e-9c07-46a3-9605-b9b1971c1253" -->
### Validation

Always validate agent outputs:
- Review for accuracy
- Check for completeness
- Verify alignment with requirements
- Test implementations

<!-- section_id: "6ef6cef3-5a47-4af3-bb66-0280e9f76c4b" -->
## Resources

<!-- section_id: "4dc8f4ae-cca1-4353-9afd-64ddfaadecec" -->
### Official Documentation
- **Documentation**: https://bmadcodes.com/
- **User Guide**: https://deepwiki.com/bmad-code-org/BMAD-METHOD/3-user-guide
- **GitHub**: https://github.com/bmad-code-org/BMAD-METHOD

<!-- section_id: "db6ff53e-268f-49d5-9e57-fdfa3b1536e0" -->
### Community
- **Issues**: https://github.com/bmad-code-org/BMAD-METHOD/issues
- **Discussions**: GitHub Discussions

<!-- section_id: "74e5151c-4eaa-4114-ab65-e09d8b45964c" -->
### Examples
- **Quick Start**: See `docs/brief.md` in any initialized project
- **Templates**: Check `.bmad/agents/` directory

<!-- section_id: "e0c6f680-0b8d-4fb1-995c-00be463c64af" -->
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

