---
resource_id: "b613ff30-2ad1-49a0-9bc7-b4b14583f1a3"
resource_type: "readme_document"
resource_name: "README"
---
# Development Workflow Tools
*Project Tool: Streamlined Development and Deployment Workflows*

<!-- section_id: "c7211844-a46f-455f-a7c4-cf7ea885bd59" -->
## Overview

The Development Workflow Tools provide automated scripts and utilities that streamline the development and deployment processes for the Language Tracker project. These tools integrate with the meta-intelligent orchestration system and authentication management to provide seamless development workflows.

<!-- section_id: "77f9cb48-010e-4d09-8de4-bbf5b4da7c74" -->
## Components

<!-- section_id: "e2eb6dac-4902-4305-add5-66deabed46fb" -->
### 1. Automated Configuration Scripts
**Location**: `scripts/configure_google_auth_automated.py`
**Purpose**: Automated Google Sign-In configuration for all environments

<!-- section_id: "ab29c18c-c6df-4136-b25c-8accdf24f6f2" -->
### 2. Authentication Management Scripts
**Location**: `scripts/simple_auth_setup.py`, `scripts/auth_manager.py`
**Purpose**: One-time authentication setup and management

<!-- section_id: "6d47d6c5-6975-4654-b0e4-4a736c6f0e88" -->
### 3. Firebase Management Scripts
**Location**: `scripts/configure-auth-domains.py`
**Purpose**: Firebase domain configuration and management

<!-- section_id: "2fa0387b-8ea6-474d-ad05-d2381fa1d848" -->
### 4. Test Automation Scripts
**Location**: `scripts/run_user_stories.py`
**Purpose**: Automated testing and validation

<!-- section_id: "3e3f485c-f813-47bb-b989-4b8f13e07ac7" -->
## Key Features

<!-- section_id: "e4bb2be2-f91b-45e4-80ea-7cec26f635f7" -->
### 1. One-Time Setup
- **Authentication Setup**: Single credential input for all operations
- **Environment Configuration**: Automated multi-environment setup
- **Service Configuration**: Automated Firebase service configuration
- **Security Setup**: Automated security and domain configuration

<!-- section_id: "869c6f7a-6938-4b34-b420-875fdab9b201" -->
### 2. Automated Operations
- **Google Sign-In Configuration**: Automated configuration across all environments
- **Domain Management**: Automated authorized domain configuration
- **Service Deployment**: Automated Firebase service deployment
- **Health Monitoring**: Automated health checking and validation

<!-- section_id: "272da2ee-78ba-47e7-8dd7-71c30c703fa1" -->
### 3. Development Workflow Integration
- **Pre-commit Hooks**: Automated validation before commits
- **Testing Integration**: Automated testing in development workflow
- **Deployment Automation**: Automated deployment to different environments
- **Monitoring Integration**: Automated monitoring and alerting setup

<!-- section_id: "8e833f8f-30a5-4a2d-ade3-4d28b437c77a" -->
### 4. AI Agent Integration
- **Context Loading**: Automated project context loading for AI agents
- **Tool Selection**: Intelligent tool selection based on task requirements
- **Implementation Guidance**: Automated implementation guidance and recommendations

<!-- section_id: "6e9e23f8-f5f7-4c33-b106-13f5b5535e14" -->
## Usage

<!-- section_id: "9b5862f0-83a7-4c5d-8308-aa06d4dc216e" -->
### Initial Project Setup
```bash
# 1. Set up one-time authentication
python3 scripts/simple_auth_setup.py

# 2. Configure Google Sign-In for all environments
python3 scripts/configure_google_auth_automated.py

# 3. Verify configuration
python3 scripts/auto_firebase.py
```

<!-- section_id: "14cc8b37-f93b-4727-9950-2ad8e84ddada" -->
### Development Workflow
```bash
# Run tests before making changes
python3 scripts/automation/run_user_stories.py --navigation-mode=both

# Make your changes...

# Run tests after changes
python3 scripts/automation/run_user_stories.py --navigation-mode=both

# Deploy to staging
python3 scripts/deploy_staging.py

# Deploy to production
python3 scripts/deploy_production.py
```

<!-- section_id: "6c0f8e49-82eb-4313-b72f-a6e35e1cea0f" -->
### AI Agent Operations
```bash
# Load project context for AI agents
/init

# Run automated Firebase operations
python3 scripts/auto_firebase.py

# Run specific tool operations
python3 scripts/run_tool.py --tool=firebase-config --action=recommend
```

<!-- section_id: "73014a00-be58-4c5e-92cb-c8b6eb623e5c" -->
## Script Categories

<!-- section_id: "899c5fd7-a2e1-4c52-883c-4ee25992bfdc" -->
### 1. Authentication Scripts
- **`simple_auth_setup.py`**: One-time authentication setup
- **`auth_manager.py`**: Advanced authentication management
- **`configure_google_auth_automated.py`**: Automated Google Sign-In configuration

<!-- section_id: "ad7171b5-6a9d-455e-880d-fb83f3ef6c91" -->
### 2. Firebase Scripts
- **`configure-auth-domains.py`**: Domain configuration utility
- **`firebase_setup_implementation.py`**: Firebase setup implementation
- **`comprehensive-firebase-setup.py`**: Comprehensive Firebase setup

<!-- section_id: "96a6b05c-01ce-471a-b5ab-df1d5918487c" -->
### 3. Testing Scripts
- **`run_user_stories.py`**: User story testing
- **`run_tests.py`**: General test runner
- **`mcp-smoke-test.sh`**: MCP server testing

<!-- section_id: "e84fa801-8bd0-42cc-9cab-b8eba46e4b24" -->
### 4. Deployment Scripts
- **`deploy_staging.py`**: Staging deployment
- **`deploy_production.py`**: Production deployment
- **`deploy_all.py`**: Multi-environment deployment

<!-- section_id: "75998860-c7ec-45ce-8253-3ae2866dd4bf" -->
## Environment Management

<!-- section_id: "fce53c44-c325-4e82-81ea-975daf3f8149" -->
### Development Environment
```bash
# Switch to development
firebase use lang-trak-dev

# Run development tests
python3 scripts/run_user_stories.py --environment=dev

# Deploy to development
python3 scripts/deploy_development.py
```

<!-- section_id: "8f8ebf44-ee50-4d45-b341-84035ed140e3" -->
### Staging Environment
```bash
# Switch to staging
firebase use lang-trak-staging

# Run staging tests
python3 scripts/run_user_stories.py --environment=staging

# Deploy to staging
python3 scripts/deploy_staging.py
```

<!-- section_id: "5e3d20a2-57d6-4500-9219-a5adad03dd95" -->
### Production Environment
```bash
# Switch to production
firebase use lang-trak-prod

# Run production tests
python3 scripts/run_user_stories.py --environment=production

# Deploy to production
python3 scripts/deploy_production.py
```

<!-- section_id: "e134d7b2-b9f2-4228-bef0-5fd0dec8a4b4" -->
## Integration with Project

<!-- section_id: "aed673b7-e910-4e2b-83d6-f5f4dfa7adba" -->
### Trickle-Down Integration
- **Level 0.5**: Universal orchestration system (setup)
- **Level 1.5**: Project-specific tools and implementations ← **This Tool**
- **Level 2**: Feature specifications and implementations
- **Level 3**: Component implementations
- **Level 4**: Detailed implementation tasks

<!-- section_id: "faf05169-6595-4d4c-a031-d75d67a55c30" -->
### Project Constitution Compliance
- **Golden Rule Testing**: Always start with user story testing
- **Dual-Mode Testing**: Both direct and realistic navigation testing
- **Test-Driven Development**: Tests before implementation
- **Clean Architecture**: Modular, reusable workflow components

<!-- section_id: "227629eb-7799-4b9e-92d6-5dfb2cb94b4a" -->
## File Structure

```
scripts/
├── auth_manager.py                    # Advanced authentication manager
├── simple_auth_setup.py              # Simple one-time setup
├── configure_google_auth_automated.py # Automated configuration
├── auto_firebase.py                  # Automated Firebase operations
├── configure-auth-domains.py         # Domain configuration utility
├── automation/
│   ├── run_user_stories.py          # User story testing
│   └── mcp-smoke-test.sh            # MCP testing
├── deployment/
│   ├── deploy_staging.py            # Staging deployment
│   ├── deploy_production.py         # Production deployment
│   └── deploy_all.py                # Multi-environment deployment
└── tools/
    ├── run_tool.py                  # Tool runner
    └── context_loader.py            # Context loading utility
```

<!-- section_id: "b4dd375f-fb6d-42f1-afa4-b126c45e94d5" -->
## Testing Integration

<!-- section_id: "fa941f98-cb27-4783-a6a2-ec4a18a7ed7b" -->
### Pre-commit Testing
```bash
# Run before every commit
python3 scripts/automation/run_user_stories.py --navigation-mode=both
```

<!-- section_id: "8fff754a-7062-4355-bba0-0b73bb0f3733" -->
### Continuous Integration
```bash
# Run in CI pipeline
python3 scripts/automation/run_user_stories.py --navigation-mode=direct
python3 scripts/run_tests.py --all --coverage
```

<!-- section_id: "057d2f71-72c4-4403-8228-1e1f79872d14" -->
### Manual Testing
```bash
# Run realistic user testing
python3 scripts/automation/run_user_stories.py --navigation-mode=realistic
```

<!-- section_id: "50709d76-bfcb-401c-a1a4-71f3975c19d4" -->
## Monitoring and Logging

<!-- section_id: "c8cac2d6-a834-4ead-880a-aad0dd6417d6" -->
### Development Monitoring
- **Console Logging**: Detailed console output for development
- **Debug Mode**: Enhanced debugging information
- **Performance Monitoring**: Development performance tracking

<!-- section_id: "219b3663-a60f-4bcc-bad0-c9d969107592" -->
### Production Monitoring
- **Firebase Monitoring**: Firebase service monitoring
- **Error Tracking**: Error logging and tracking
- **Performance Analytics**: Production performance analytics

<!-- section_id: "5493c06b-228e-470c-9d47-412e2d40fc14" -->
## Troubleshooting

<!-- section_id: "1193fa5c-769e-451a-9bfd-e8accf19e464" -->
### Common Issues

#### Authentication Failures
```bash
# Re-authenticate
python3 scripts/simple_auth_setup.py

# Clear credentials
gcloud auth revoke --all
gcloud auth login
```

#### Test Failures
```bash
# Run tests with debug output
DEBUG=1 python3 scripts/automation/run_user_stories.py --navigation-mode=both

# Check test logs
tail -f logs/test.log
```

#### Deployment Failures
```bash
# Check deployment status
firebase hosting:channel:list

# View deployment logs
firebase functions:log
```

<!-- section_id: "fb1b0fb6-4d11-41e9-b1cb-34f1054f7753" -->
### Debug Mode
```bash
# Enable debug output
export DEBUG=1
export FIREBASE_DEBUG=1
python3 scripts/configure_google_auth_automated.py
```

<!-- section_id: "dc437e5d-bdc1-40ca-8bf7-e6add6b8923d" -->
## Future Enhancements

<!-- section_id: "48a9b8d6-2cf6-4c0e-aa4d-9024be008339" -->
### Planned Features
- **Advanced CI/CD**: Enhanced continuous integration and deployment
- **Automated Rollbacks**: Automatic rollback on deployment failures
- **Performance Optimization**: Automated performance optimization
- **Security Scanning**: Automated security vulnerability scanning

<!-- section_id: "1cfc3b7b-5169-4175-9bd9-623e55c03975" -->
### Extensibility
- **Custom Workflows**: Support for custom development workflows
- **Third-Party Integration**: Integration with external development tools
- **Advanced Monitoring**: Enhanced monitoring and alerting
- **Machine Learning**: ML-powered workflow optimization

<!-- section_id: "3b28da40-7fef-44b1-9d52-530a48f6c0e4" -->
## Documentation

- [Meta-Intelligent Orchestration System](./meta-intelligent-orchestration/README.md)
- [Firebase Instance Tools](./firebase-instance/README.md)
- [Authentication Management System](./authentication-management/README.md)
- [Project Constitution](../trickle-down-1-project/constitution.md)

---
*This tool is part of the Language Tracker project's Trickle-Down documentation structure.*
