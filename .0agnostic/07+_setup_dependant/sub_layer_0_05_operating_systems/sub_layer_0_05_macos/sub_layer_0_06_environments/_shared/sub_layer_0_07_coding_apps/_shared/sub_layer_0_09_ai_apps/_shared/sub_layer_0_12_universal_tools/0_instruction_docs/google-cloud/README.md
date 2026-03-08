---
resource_id: "ecd7dbd8-d288-46d2-b617-8bb89e6f3d7f"
resource_type: "readme_document"
resource_name: "README"
---
# Google Cloud Tools

This directory contains documentation for Google Cloud Platform (GCP) tools and integrations used across AI development workflows.

<!-- section_id: "584a3cad-8b62-4eff-a5d5-92aa9bcfa929" -->
## Contents

- [gcloud-cli-setup.md](./gcloud-cli-setup.md) - Installing and configuring the gcloud CLI
- [secret-manager.md](./secret-manager.md) - Using Google Secret Manager for API keys and credentials
- [canvas-api-integration.md](./canvas-api-integration.md) - Canvas LMS API integration with GCP

<!-- section_id: "9db2fcbe-b05d-45ed-9832-1d0bfe5df5a9" -->
## Quick Reference

<!-- section_id: "a6711a9e-d857-4454-9623-fae27d03eeb9" -->
### Authentication
```bash
# Login with browser-based auth
gcloud auth login

# Login without browser (for remote/headless systems)
gcloud auth login --no-launch-browser

# Check current auth
gcloud auth list

# Set project
gcloud config set project PROJECT_ID
```

<!-- section_id: "0632983f-cd64-4480-b688-9a3a8c5d1d54" -->
### Secret Manager
```bash
# List secrets
gcloud secrets list

# Access a secret
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'

# Create a secret
echo "secret-value" | gcloud secrets create SECRET_NAME --data-file=-
```

<!-- section_id: "b1eab7fe-305d-433f-a67f-426677a4f735" -->
## Related Documentation

- [Canvas API Integration](./canvas-api-integration.md)
- [Environment Configuration](../scripts/README.md)
