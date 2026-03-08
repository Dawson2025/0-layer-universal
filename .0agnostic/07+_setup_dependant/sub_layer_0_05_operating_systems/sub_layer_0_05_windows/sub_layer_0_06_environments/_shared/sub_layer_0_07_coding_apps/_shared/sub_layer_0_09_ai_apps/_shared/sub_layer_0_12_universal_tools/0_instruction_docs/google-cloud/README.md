---
resource_id: "17888105-ce55-4629-8129-f2d7430ec4b7"
resource_type: "readme_document"
resource_name: "README"
---
# Google Cloud Tools

This directory contains documentation for Google Cloud Platform (GCP) tools and integrations used across AI development workflows.

<!-- section_id: "dec3256a-9722-4964-bb46-6ecfbd8c3df0" -->
## Contents

- [gcloud-cli-setup.md](./gcloud-cli-setup.md) - Installing and configuring the gcloud CLI
- [secret-manager.md](./secret-manager.md) - Using Google Secret Manager for API keys and credentials
- [canvas-api-integration.md](./canvas-api-integration.md) - Canvas LMS API integration with GCP

<!-- section_id: "1a6126da-1ccb-40dd-8e5d-a52f67edd5c8" -->
## Quick Reference

<!-- section_id: "8e93867f-3c66-449f-a051-fd360b971170" -->
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

<!-- section_id: "bf440a2d-12a9-41f4-b015-4ad5f703c2d5" -->
### Secret Manager
```bash
# List secrets
gcloud secrets list

# Access a secret
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'

# Create a secret
echo "secret-value" | gcloud secrets create SECRET_NAME --data-file=-
```

<!-- section_id: "62ee4153-17da-495c-a897-47a8ed47f0db" -->
## Related Documentation

- [Canvas API Integration](./canvas-api-integration.md)
- [Environment Configuration](../scripts/README.md)
