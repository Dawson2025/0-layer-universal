---
resource_id: "85d4de28-a293-408c-b2e5-f4c7208494be"
resource_type: "document"
resource_name: "bmad-method-guide"
---
# BMAD Method - Comprehensive Guide
*Breakthrough Method for Agile AI-Driven Development*

<!-- section_id: "f89bda89-25df-43b6-9509-4e90913ed1e6" -->
## Overview

The BMAD (Breakthrough Method for Agile AI-Driven Development) Method introduces specialized AI agents that collaborate as a development team, streamlining the development process. Each agent has specific responsibilities, working together to transform vague requirements into production-ready software.

<!-- section_id: "c7ab961c-5299-4c65-a790-651f31fe2c66" -->
## Key Concepts

<!-- section_id: "a5e74ab3-4695-46bd-9ecf-b39be54fa6aa" -->
### What is Agentic Team Development?

Agentic team development is a methodology where:
- **Specialized AI Agents** work as a collaborative development team
- **Each Agent** has specific role responsibilities
- **Git-Based Versioning** tracks all artifacts (PRDs, architecture, stories)
- **Context-Engineered Development** uses hyper-detailed development stories
- **Human + AI Review** ensures quality through pull request reviews

<!-- section_id: "6beef427-7c60-49e0-ab67-6504a9a78343" -->
### Core Philosophy

**Problem**: Traditional AI prompting lacks structure, traceability, and accountability.

**Solution**: Create a system where specialized AI agents collaborate like a real development team, with clear roles, responsibilities, and comprehensive audit trails.

<!-- section_id: "6a545612-1571-4fa6-b98c-83484e4ab780" -->
## Key Features

<!-- section_id: "8b284f56-90cf-4915-a047-65093940989e" -->
### 1. Specialized AI Agents

Each agent has specific responsibilities:

- **Analyst**: Requirements gathering and analysis
- **Product Manager**: Product vision and roadmap
- **Architect**: System architecture and technical decisions
- **Scrum Master**: Process management and sprint planning
- **Product Owner**: Backlog management and prioritization
- **Developer**: Code implementation
- **QA**: Testing and quality assurance

<!-- section_id: "b30ffcfb-f9f0-4dbb-afe9-ec67b21c3cac" -->
### 2. Git-Based Artifact Versioning

All artifacts are version-controlled:
- PRDs (Product Requirement Documents)
- Architecture documents
- Development stories
- Code implementations
- Test results

<!-- section_id: "0ede5baf-0df2-40b2-b0e8-65523ddad6ce" -->
### 3. Context-Engineered Development

Hyper-detailed development stories ensure:
- Complete context preservation
- No information loss
- Traceable decision-making
- Single source of truth

<!-- section_id: "e8426a35-70fa-49b0-b352-3907b2d6f8ca" -->
### 4. Pull Request Reviews

Quality assurance through:
- Human review of AI-generated content
- AI agent review of implementations
- Automated testing
- Comprehensive validation

<!-- section_id: "af85a287-7f08-45ae-b5f4-0baad3b3a7f2" -->
## Installation

<!-- section_id: "2d07ab60-23d3-4d20-89b4-9a1bfc7362a3" -->
### Prerequisites

- Node.js v20+
- `npx` command available
- Git repository initialized

<!-- section_id: "4037284e-bb90-45fb-a438-f875c1a959dc" -->
### Install BMAD

```bash
npx bmad-method install
```

This command handles:
- New installations
- Upgrades
- Expansion packs

<!-- section_id: "26c108f2-25ec-47c0-9dba-6db3d800c651" -->
### Verify Installation

```bash
# Check if BMAD is installed
ls -la .bmad/

# View available commands
bmad --help
```

<!-- section_id: "c3b126cc-5713-43c5-851c-86297191eaa8" -->
## Getting Started

<!-- section_id: "44b8bb13-08f5-40f1-a152-5e7a0d5b7e29" -->
### Step 1: Set Up the Web UI

1. **Obtain the Full-Stack Team Bundle**
   - Download from https://github.com/bmad-code-org/BMAD-METHOD
   - Extract the bundle files

2. **Create a New AI Agent**
   - Use Gemini Gem or CustomGPT
   - Upload the bundle files

3. **Configure the Agent**
   - Upload instruction: "Your critical operating instructions are attached, do not break character as directed."

<!-- section_id: "234869a3-3d72-4395-850b-6a8aab5b4781" -->
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

<!-- section_id: "a8c8924e-4ac5-4082-9ffc-f6962578d46b" -->
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

<!-- section_id: "fd0e20dd-19c6-48b7-9576-a4072e70b000" -->
## Agent Responsibilities

<!-- section_id: "8dc6177c-186d-46da-829e-5ff30adb0a05" -->
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

<!-- section_id: "55852dcd-fe84-42d4-9908-b20d8a70e3b1" -->
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

<!-- section_id: "e5482910-d7ad-4e53-a66d-bbaf3b781f22" -->
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

<!-- section_id: "d47e31ce-ff04-494c-84f2-121cf33bdde4" -->
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

<!-- section_id: "d4173653-1923-472e-b915-8b9d6afc2de9" -->
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

<!-- section_id: "0726edd4-3f2f-466c-94f8-59bcba78678b" -->
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

<!-- section_id: "f74a5cb6-0c51-4441-9cbd-72c0245807f6" -->
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

<!-- section_id: "141a2857-d232-46d5-821f-ad7c2b48742f" -->
## Workflow Example

<!-- section_id: "1eed4e7f-ba80-4fee-91dd-0bade6216c6f" -->
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

<!-- section_id: "7c3378b0-faf2-4a55-bf73-255ed1beee31" -->
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

<!-- section_id: "5c9736da-138a-44e4-9aa0-4b5e38f26b92" -->
## Best Practices

<!-- section_id: "06fe1393-24f5-4ba0-afc8-924436164699" -->
### Working with Agents

1. **Be Specific**: Provide clear, detailed instructions
2. **Use Proper Commands**: Follow the command syntax
3. **Review Outputs**: Always review agent outputs before proceeding
4. **Iterate**: Don't be afraid to refine and iterate

<!-- section_id: "c9814c30-21ba-44ec-9218-0e97ed7dd98a" -->
### Artifact Management

1. **Version Control**: All artifacts in Git
2. **Documentation**: Keep documentation up-to-date
3. **Sharding**: Break large documents into manageable pieces
4. **Organization**: Maintain clear directory structure

<!-- section_id: "a7b41432-d946-4ed9-b0a1-60c10b60b07d" -->
### Development Process

1. **Follow the Sprint Plan**: Stick to the plan during sprints
2. **Respect Dependencies**: Don't skip dependencies
3. **Test Continuously**: Run tests frequently
4. **Code Reviews**: Review AI-generated code before acceptance

<!-- section_id: "f3a7b7de-1e0f-4da2-92e4-5f865550aade" -->
### Quality Assurance

1. **Test Early**: Write tests alongside code
2. **Automate Testing**: Use automated test suites
3. **Security Testing**: Don't skip security testing
4. **User Testing**: Include real user feedback

<!-- section_id: "df80b565-ba42-4a34-a961-b24fd132baee" -->
## Advanced Features

<!-- section_id: "e9e261d4-880d-4e92-b41a-97faacaefdbe" -->
### Custom Agents

Create custom agents for specific needs:

1. **Define Agent Role**: What is the agent responsible for?
2. **Configure Behavior**: How should the agent behave?
3. **Set Outputs**: What should the agent produce?
4. **Test Agent**: Validate agent behavior

<!-- section_id: "ad666cfe-3d65-4e49-bf7e-06367977052a" -->
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

<!-- section_id: "f51b9d7c-dcd4-4432-849e-f403285571d1" -->
### Integration with Git

Git integration provides:
- Automatic artifact versioning
- Change tracking
- Rollback capabilities
- Collaboration support

<!-- section_id: "e3ea421f-5880-4341-b806-82a658a193f4" -->
### Continuous Integration

Integrate with CI/CD:
- Automated testing
- Deployment pipelines
- Quality checks
- Performance monitoring

<!-- section_id: "d719d9c9-471c-4b6f-8466-4b44f36b279e" -->
## Troubleshooting

<!-- section_id: "77eb0cdf-45da-41c1-b618-083bb15583e3" -->
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

<!-- section_id: "3d33f6e3-f51d-4dc6-8e82-4cf9ab77200c" -->
### Validation

Always validate agent outputs:
- Review for accuracy
- Check for completeness
- Verify alignment with requirements
- Test implementations

<!-- section_id: "f871b2c6-a2e9-4340-b839-1e44d82b6d00" -->
## Resources

<!-- section_id: "9545ce8b-0f1e-4f6e-af11-e18547a6b734" -->
### Official Documentation
- **Documentation**: https://bmadcodes.com/
- **User Guide**: https://deepwiki.com/bmad-code-org/BMAD-METHOD/3-user-guide
- **GitHub**: https://github.com/bmad-code-org/BMAD-METHOD

<!-- section_id: "55828d26-663d-4cec-ae0f-9582b1a0c2b7" -->
### Community
- **Issues**: https://github.com/bmad-code-org/BMAD-METHOD/issues
- **Discussions**: GitHub Discussions

<!-- section_id: "54e9d213-5daf-457d-a272-bb9f187a9b96" -->
### Examples
- **Quick Start**: See `docs/brief.md` in any initialized project
- **Templates**: Check `.bmad/agents/` directory

<!-- section_id: "232dd599-defb-44c1-94c2-2b772583d4a6" -->
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

