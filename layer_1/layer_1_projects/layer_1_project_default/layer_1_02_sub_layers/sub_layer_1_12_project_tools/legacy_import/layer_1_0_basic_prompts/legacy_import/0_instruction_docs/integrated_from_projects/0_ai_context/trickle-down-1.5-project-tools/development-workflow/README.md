---
resource_id: "4d54a7ce-f86a-4f08-949b-6aff33ee89ad"
resource_type: "readme_document"
resource_name: "README"
---
# Development Workflow Tools
*Project Tool: Streamlined Development and Deployment Workflows*

<!-- section_id: "d73a0aab-27e2-4eee-8425-56b5f201b5d9" -->
## Overview

The Development Workflow Tools provide automated scripts and utilities that streamline the development and deployment processes for the Language Tracker project. These tools integrate with the meta-intelligent orchestration system and authentication management to provide seamless development workflows.

<!-- section_id: "01fef4b9-6164-4992-a59c-95b93edadc9d" -->
## Components

<!-- section_id: "34d8e5ab-9062-4340-bda4-1b17ba9d8bda" -->
### 1. Automated Configuration Scripts
**Location**: `scripts/configure_google_auth_automated.py`
**Purpose**: Automated Google Sign-In configuration for all environments

<!-- section_id: "8ef7425d-37bd-45c2-927d-94d15f598638" -->
### 2. Authentication Management Scripts
**Location**: `scripts/simple_auth_setup.py`, `scripts/auth_manager.py`
**Purpose**: One-time authentication setup and management

<!-- section_id: "5ba3de52-c659-453a-a246-871c07dd35a7" -->
### 3. Firebase Management Scripts
**Location**: `scripts/configure-auth-domains.py`
**Purpose**: Firebase domain configuration and management

<!-- section_id: "0527c27e-26e3-42ab-b5b1-1fb4db283884" -->
### 4. Test Automation Scripts
**Location**: `scripts/run_user_stories.py`
**Purpose**: Automated testing and validation

<!-- section_id: "9f0809df-4a06-48c1-9480-60dc3adba5d8" -->
## Key Features

<!-- section_id: "004fad97-f796-4318-b3ce-5e48dca6a453" -->
### 1. One-Time Setup
- **Authentication Setup**: Single credential input for all operations
- **Environment Configuration**: Automated multi-environment setup
- **Service Configuration**: Automated Firebase service configuration
- **Security Setup**: Automated security and domain configuration

<!-- section_id: "d644ce69-35f8-47ea-8de4-f9b1b4cf5a9f" -->
### 2. Automated Operations
- **Google Sign-In Configuration**: Automated configuration across all environments
- **Domain Management**: Automated authorized domain configuration
- **Service Deployment**: Automated Firebase service deployment
- **Health Monitoring**: Automated health checking and validation

<!-- section_id: "761addaa-505f-4556-b191-f0c90e2d25fe" -->
### 3. Development Workflow Integration
- **Pre-commit Hooks**: Automated validation before commits
- **Testing Integration**: Automated testing in development workflow
- **Deployment Automation**: Automated deployment to different environments
- **Monitoring Integration**: Automated monitoring and alerting setup

<!-- section_id: "73768b41-1bab-4dcd-98ec-bda0f19a73c2" -->
### 4. AI Agent Integration
- **Context Loading**: Automated project context loading for AI agents
- **Tool Selection**: Intelligent tool selection based on task requirements
- **Implementation Guidance**: Automated implementation guidance and recommendations

<!-- section_id: "3b062d39-71da-4863-b509-ac39c496272e" -->
## Usage

<!-- section_id: "1ac835cd-d511-4eb4-bb8a-db7044f67ca2" -->
### Initial Project Setup
```bash
# 1. Set up one-time authentication
python3 scripts/simple_auth_setup.py

# 2. Configure Google Sign-In for all environments
python3 scripts/configure_google_auth_automated.py

# 3. Verify configuration
python3 scripts/auto_firebase.py
```

<!-- section_id: "a9e5a228-1227-4c13-afca-a840da075d2b" -->
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

<!-- section_id: "89096c06-1958-4519-9444-db500436ad04" -->
### AI Agent Operations
```bash
# Load project context for AI agents
/init

# Run automated Firebase operations
python3 scripts/auto_firebase.py

# Run specific tool operations
python3 scripts/run_tool.py --tool=firebase-config --action=recommend
```

<!-- section_id: "393c02bb-ec0e-44d8-abc7-283ad4dc3c75" -->
## Script Categories

<!-- section_id: "024ca18f-2540-4aef-8813-969d11f08ca4" -->
### 1. Authentication Scripts
- **`simple_auth_setup.py`**: One-time authentication setup
- **`auth_manager.py`**: Advanced authentication management
- **`configure_google_auth_automated.py`**: Automated Google Sign-In configuration

<!-- section_id: "45b19edf-adf1-4ae0-bebb-c6ced0cf132a" -->
### 2. Firebase Scripts
- **`configure-auth-domains.py`**: Domain configuration utility
- **`firebase_setup_implementation.py`**: Firebase setup implementation
- **`comprehensive-firebase-setup.py`**: Comprehensive Firebase setup

<!-- section_id: "807402c7-af2e-48cd-9dac-e326c9e1314b" -->
### 3. Testing Scripts
- **`run_user_stories.py`**: User story testing
- **`run_tests.py`**: General test runner
- **`mcp-smoke-test.sh`**: MCP server testing

<!-- section_id: "68ec8f66-838c-4f7a-93b6-46a2448d3500" -->
### 4. Deployment Scripts
- **`deploy_staging.py`**: Staging deployment
- **`deploy_production.py`**: Production deployment
- **`deploy_all.py`**: Multi-environment deployment

<!-- section_id: "8e65e06d-6e3a-4b8a-95b9-64ddfa30495d" -->
## Environment Management

<!-- section_id: "9c205d09-d798-4869-8286-16ededbf105e" -->
### Development Environment
```bash
# Switch to development
firebase use lang-trak-dev

# Run development tests
python3 scripts/run_user_stories.py --environment=dev

# Deploy to development
python3 scripts/deploy_development.py
```

<!-- section_id: "5ba1aff0-9d2a-45bd-84e8-09931245c612" -->
### Staging Environment
```bash
# Switch to staging
firebase use lang-trak-staging

# Run staging tests
python3 scripts/run_user_stories.py --environment=staging

# Deploy to staging
python3 scripts/deploy_staging.py
```

<!-- section_id: "bff9c07c-c1cf-4f17-b8f5-cad56e695d6f" -->
### Production Environment
```bash
# Switch to production
firebase use lang-trak-prod

# Run production tests
python3 scripts/run_user_stories.py --environment=production

# Deploy to production
python3 scripts/deploy_production.py
```

<!-- section_id: "a1a5fa7f-555f-4f7a-8f15-8b1d2c31465c" -->
## Integration with Project

<!-- section_id: "f5bb2a16-716e-4bd9-959b-ae3a6651bad9" -->
### Trickle-Down Integration
- **Level 0.5**: Universal orchestration system (setup)
- **Level 1.5**: Project-specific tools and implementations ← **This Tool**
- **Level 2**: Feature specifications and implementations
- **Level 3**: Component implementations
- **Level 4**: Detailed implementation tasks

<!-- section_id: "455f6ae7-2d5c-486f-8b87-7db7c3c6143d" -->
### Project Constitution Compliance
- **Golden Rule Testing**: Always start with user story testing
- **Dual-Mode Testing**: Both direct and realistic navigation testing
- **Test-Driven Development**: Tests before implementation
- **Clean Architecture**: Modular, reusable workflow components

<!-- section_id: "8e2c0474-9a36-44a1-88bd-9a5a0d1642ce" -->
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

<!-- section_id: "b48abd28-529f-4c7a-8f11-9bbc9651dc56" -->
## Testing Integration

<!-- section_id: "9e937002-f024-4f1a-b706-49f25ba2abd2" -->
### Pre-commit Testing
```bash
# Run before every commit
python3 scripts/automation/run_user_stories.py --navigation-mode=both
```

<!-- section_id: "00ba8139-e33c-4022-a7fc-53dc07cd7901" -->
### Continuous Integration
```bash
# Run in CI pipeline
python3 scripts/automation/run_user_stories.py --navigation-mode=direct
python3 scripts/run_tests.py --all --coverage
```

<!-- section_id: "a5fb5351-1cfe-4883-b418-89fd6bbb1586" -->
### Manual Testing
```bash
# Run realistic user testing
python3 scripts/automation/run_user_stories.py --navigation-mode=realistic
```

<!-- section_id: "bde6caee-0b2b-4203-8559-8417abbc79ee" -->
## Monitoring and Logging

<!-- section_id: "746058f0-7a83-4578-8fe5-69247df187c2" -->
### Development Monitoring
- **Console Logging**: Detailed console output for development
- **Debug Mode**: Enhanced debugging information
- **Performance Monitoring**: Development performance tracking

<!-- section_id: "07876ad2-09e2-4c92-837c-8a26bc9a39c3" -->
### Production Monitoring
- **Firebase Monitoring**: Firebase service monitoring
- **Error Tracking**: Error logging and tracking
- **Performance Analytics**: Production performance analytics

<!-- section_id: "d930b491-9bc0-4166-9d30-6fa0beab8c51" -->
## Troubleshooting

<!-- section_id: "30b58c5e-e7c9-402e-bbd9-5079fb084ca5" -->
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

<!-- section_id: "b92cbf68-2183-412d-808b-5f90d27feb5d" -->
### Debug Mode
```bash
# Enable debug output
export DEBUG=1
export FIREBASE_DEBUG=1
python3 scripts/configure_google_auth_automated.py
```

<!-- section_id: "6d34dad2-367c-4def-9871-1f3059a6c264" -->
## Future Enhancements

<!-- section_id: "39857b6a-bccf-4ca5-b1bc-eb5fc90f0890" -->
### Planned Features
- **Advanced CI/CD**: Enhanced continuous integration and deployment
- **Automated Rollbacks**: Automatic rollback on deployment failures
- **Performance Optimization**: Automated performance optimization
- **Security Scanning**: Automated security vulnerability scanning

<!-- section_id: "b4a82dea-8fae-4ef3-a231-7c198047edab" -->
### Extensibility
- **Custom Workflows**: Support for custom development workflows
- **Third-Party Integration**: Integration with external development tools
- **Advanced Monitoring**: Enhanced monitoring and alerting
- **Machine Learning**: ML-powered workflow optimization

<!-- section_id: "0d685560-470f-434b-9833-08cee20116a1" -->
## Documentation

- [Meta-Intelligent Orchestration System](./meta-intelligent-orchestration/README.md)
- [Firebase Instance Tools](./firebase-instance/README.md)
- [Authentication Management System](./authentication-management/README.md)
- [Project Constitution](../trickle-down-1-project/constitution.md)

---
*This tool is part of the Language Tracker project's Trickle-Down documentation structure.*
