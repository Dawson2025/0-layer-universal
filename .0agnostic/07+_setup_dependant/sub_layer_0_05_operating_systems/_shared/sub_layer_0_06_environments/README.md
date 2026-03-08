---
resource_id: "6c71ea22-619b-402c-810a-5247b2bd90ae"
resource_type: "readme_document"
resource_name: "README"
---
# Environments

This level organizes setup documentation by development environment type.

<!-- section_id: "b67d1f14-9e4f-40b8-a7fa-c7f8b11c2193" -->
## Available Environments

- **_shared/** - Setup that works across all environments
- **development/** - Local development environment setup
- **production/** - Production environment setup
- **testing/** - Testing/staging environment setup

<!-- section_id: "8cc55394-e0af-476a-a955-dbb1f15199bb" -->
## How to Navigate

1. Choose your environment directory
2. Navigate down to `0.07_coding_apps/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all environments

<!-- section_id: "3b7be872-be96-4237-a1dc-1630f9e76a2c" -->
## Environment-Specific Considerations

<!-- section_id: "e051b0ff-3955-437c-8ba5-1f94b5af227c" -->
### Development
- Hot reload and debugging tools
- Development-specific dependencies
- Local testing servers
- More verbose logging

<!-- section_id: "f8adb533-de6c-4c08-bbc4-8471c6eeeb56" -->
### Production
- Optimized builds
- Security hardening
- Performance monitoring
- Production-grade error handling

<!-- section_id: "b6483884-8cdb-4529-8243-ed80b6545b59" -->
### Testing
- Test frameworks and runners
- CI/CD integration
- Mock services and test data
- Code coverage tools

<!-- section_id: "0ba11ab7-15c8-41be-b330-61e99d863a11" -->
## Links to Detailed Documentation

For detailed environment setup, see:
- **sub_layer_0_06_environment_setup/** (if exists)
- **sub_layer_0_07_coding_app_setup/** for coding app-specific environment configuration
