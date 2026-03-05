---
resource_id: "1a1d00d8-6224-4cc0-9fe6-f1ce562d9aeb"
resource_type: "document"
resource_name: "bmad-method-guide"
---
# BMAD Method - Comprehensive Guide
*Breakthrough Method for Agile AI-Driven Development*

<!-- section_id: "982004a0-0d91-47a7-9548-13b792a31334" -->
## Overview

The BMAD (Breakthrough Method for Agile AI-Driven Development) Method introduces specialized AI agents that collaborate as a development team, streamlining the development process. Each agent has specific responsibilities, working together to transform vague requirements into production-ready software.

<!-- section_id: "ecddef74-b8ab-4eab-b97f-769b7f36a5a7" -->
## Key Concepts

<!-- section_id: "a6ff1a77-4eb2-4414-ab3c-b6b6107ef39d" -->
### What is Agentic Team Development?

Agentic team development is a methodology where:
- **Specialized AI Agents** work as a collaborative development team
- **Each Agent** has specific role responsibilities
- **Git-Based Versioning** tracks all artifacts (PRDs, architecture, stories)
- **Context-Engineered Development** uses hyper-detailed development stories
- **Human + AI Review** ensures quality through pull request reviews

<!-- section_id: "eb8de3b3-60c7-489b-af43-e394a795cd65" -->
### Core Philosophy

**Problem**: Traditional AI prompting lacks structure, traceability, and accountability.

**Solution**: Create a system where specialized AI agents collaborate like a real development team, with clear roles, responsibilities, and comprehensive audit trails.

<!-- section_id: "0437a546-ec79-4599-8a49-7c2f48eedb89" -->
## Key Features

<!-- section_id: "e2029d1b-4392-4e22-86b3-18b34968dd40" -->
### 1. Specialized AI Agents

Each agent has specific responsibilities:

- **Analyst**: Requirements gathering and analysis
- **Product Manager**: Product vision and roadmap
- **Architect**: System architecture and technical decisions
- **Scrum Master**: Process management and sprint planning
- **Product Owner**: Backlog management and prioritization
- **Developer**: Code implementation
- **QA**: Testing and quality assurance

<!-- section_id: "6b96a517-a7fe-441e-9f39-f1e66107283e" -->
### 2. Git-Based Artifact Versioning

All artifacts are version-controlled:
- PRDs (Product Requirement Documents)
- Architecture documents
- Development stories
- Code implementations
- Test results

<!-- section_id: "17cb2f70-c4ee-456f-bfa7-14c970a0c15d" -->
### 3. Context-Engineered Development

Hyper-detailed development stories ensure:
- Complete context preservation
- No information loss
- Traceable decision-making
- Single source of truth

<!-- section_id: "2397613e-e5c5-49bd-890f-14798909aa91" -->
### 4. Pull Request Reviews

Quality assurance through:
- Human review of AI-generated content
- AI agent review of implementations
- Automated testing
- Comprehensive validation

<!-- section_id: "ea9ad610-2617-4afa-81f1-c58a1ed43c84" -->
## Installation

<!-- section_id: "b89d02dc-3e60-4e4b-878d-3803856d9b6b" -->
### Prerequisites

- Node.js v20+
- `npx` command available
- Git repository initialized

<!-- section_id: "d7c7f37b-e531-408c-8b1b-d6187dbfb635" -->
### Install BMAD

```bash
npx bmad-method install
```

This command handles:
- New installations
- Upgrades
- Expansion packs

<!-- section_id: "4d84e779-8062-4161-ba71-8864ff2e1459" -->
### Verify Installation

```bash
# Check if BMAD is installed
ls -la .bmad/

# View available commands
bmad --help
```

<!-- section_id: "e80bdcda-2bc2-4f8a-836d-f6dc0e20f2c3" -->
## Getting Started

<!-- section_id: "cfad3204-9c77-44cd-b7e8-979999c26a48" -->
### Step 1: Set Up the Web UI

1. **Obtain the Full-Stack Team Bundle**
   - Download from https://github.com/bmad-code-org/BMAD-METHOD
   - Extract the bundle files

2. **Create a New AI Agent**
   - Use Gemini Gem or CustomGPT
   - Upload the bundle files

3. **Configure the Agent**
   - Upload instruction: "Your critical operating instructions are attached, do not break character as directed."

<!-- section_id: "5e8f9b9d-043d-44eb-8a82-07e8bff6f9cd" -->
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

<!-- section_id: "951c3326-bc2e-4496-bd6e-fdf644040ddd" -->
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

<!-- section_id: "af6a0cc2-d24e-4d77-8a7f-a8aefbf0a1df" -->
## Agent Responsibilities

<!-- section_id: "e438c592-178a-4a28-88c6-735ede40db75" -->
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

<!-- section_id: "0b00f089-458b-4566-a1d4-335f0ea18007" -->
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

<!-- section_id: "7f1a654f-3e75-4664-8c5a-28436f44f88b" -->
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

<!-- section_id: "04caf912-fdf3-4730-9512-1c87e94878eb" -->
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

<!-- section_id: "a4368b55-8938-4d17-af8f-2b186a48174a" -->
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

<!-- section_id: "5d5c56a7-dd6f-41e8-b1e2-5219bc6b2e5e" -->
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

<!-- section_id: "a3352e1c-9d9a-467c-8607-fcbb332b044d" -->
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

<!-- section_id: "9d8f6d8f-59a2-472d-9728-02906544b47b" -->
## Workflow Example

<!-- section_id: "5ab531d2-d1ce-47c3-89eb-00b4d90718ad" -->
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

<!-- section_id: "7df7a717-eb1b-456e-b0d5-1d334af56461" -->
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

<!-- section_id: "adaddf68-2426-458a-acc3-fdf75f670458" -->
## Best Practices

<!-- section_id: "80e80a84-d71d-471b-af24-9b17add821de" -->
### Working with Agents

1. **Be Specific**: Provide clear, detailed instructions
2. **Use Proper Commands**: Follow the command syntax
3. **Review Outputs**: Always review agent outputs before proceeding
4. **Iterate**: Don't be afraid to refine and iterate

<!-- section_id: "ef731012-1111-491b-a5c1-fda6996558d0" -->
### Artifact Management

1. **Version Control**: All artifacts in Git
2. **Documentation**: Keep documentation up-to-date
3. **Sharding**: Break large documents into manageable pieces
4. **Organization**: Maintain clear directory structure

<!-- section_id: "00d34291-a753-4f0a-b2e7-aae0b6257809" -->
### Development Process

1. **Follow the Sprint Plan**: Stick to the plan during sprints
2. **Respect Dependencies**: Don't skip dependencies
3. **Test Continuously**: Run tests frequently
4. **Code Reviews**: Review AI-generated code before acceptance

<!-- section_id: "43222bfb-b5e7-48f5-802e-b2ac9a6f4446" -->
### Quality Assurance

1. **Test Early**: Write tests alongside code
2. **Automate Testing**: Use automated test suites
3. **Security Testing**: Don't skip security testing
4. **User Testing**: Include real user feedback

<!-- section_id: "fa891cd8-26d1-4cf0-be29-4261f299408a" -->
## Advanced Features

<!-- section_id: "678ebb31-cded-46de-8499-57f58e3b299f" -->
### Custom Agents

Create custom agents for specific needs:

1. **Define Agent Role**: What is the agent responsible for?
2. **Configure Behavior**: How should the agent behave?
3. **Set Outputs**: What should the agent produce?
4. **Test Agent**: Validate agent behavior

<!-- section_id: "f4f90440-824c-4ab1-95f4-a20f7101f5d9" -->
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

<!-- section_id: "307339f1-ad56-44cc-a73a-e877d5dcc8b3" -->
### Integration with Git

Git integration provides:
- Automatic artifact versioning
- Change tracking
- Rollback capabilities
- Collaboration support

<!-- section_id: "41f0bb1b-8cc5-4ba7-8060-a53b5754e05d" -->
### Continuous Integration

Integrate with CI/CD:
- Automated testing
- Deployment pipelines
- Quality checks
- Performance monitoring

<!-- section_id: "1333177b-0282-4883-9ebc-7aebb54171c2" -->
## Troubleshooting

<!-- section_id: "99a12194-fb32-4bb4-95f5-cb8cb33dd218" -->
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

<!-- section_id: "57569c3f-094d-4f7d-baf7-d8ffab9f45bb" -->
### Validation

Always validate agent outputs:
- Review for accuracy
- Check for completeness
- Verify alignment with requirements
- Test implementations

<!-- section_id: "1553a3e3-5ba0-493f-93f0-aca7f68543ca" -->
## Resources

<!-- section_id: "5556c602-7429-40fe-ae7c-3ed27a90c9ce" -->
### Official Documentation
- **Documentation**: https://bmadcodes.com/
- **User Guide**: https://deepwiki.com/bmad-code-org/BMAD-METHOD/3-user-guide
- **GitHub**: https://github.com/bmad-code-org/BMAD-METHOD

<!-- section_id: "1f9e2030-38f0-47be-80ba-9a31f63f3792" -->
### Community
- **Issues**: https://github.com/bmad-code-org/BMAD-METHOD/issues
- **Discussions**: GitHub Discussions

<!-- section_id: "0c5c078b-baad-423c-a279-31683dcdc76b" -->
### Examples
- **Quick Start**: See `docs/brief.md` in any initialized project
- **Templates**: Check `.bmad/agents/` directory

<!-- section_id: "97fb4fb0-d05e-49bb-b9ce-8b914ee65bca" -->
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

