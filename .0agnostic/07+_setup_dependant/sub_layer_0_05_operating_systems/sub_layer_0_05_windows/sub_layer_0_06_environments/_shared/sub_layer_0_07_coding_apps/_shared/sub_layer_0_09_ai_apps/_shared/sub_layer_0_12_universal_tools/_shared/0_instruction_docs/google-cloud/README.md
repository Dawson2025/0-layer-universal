---
resource_id: "5267c21c-7b60-4afe-83db-2e970f4d3c12"
resource_type: "readme_document"
resource_name: "README"
---
# Google Cloud Tools

This directory contains documentation for Google Cloud Platform (GCP) tools and integrations used across AI development workflows.

<!-- section_id: "a4183877-658a-432f-be65-5f8039ed9d85" -->
## Contents

- [gcloud-cli-setup.md](./gcloud-cli-setup.md) - Installing and configuring the gcloud CLI
- [secret-manager.md](./secret-manager.md) - Using Google Secret Manager for API keys and credentials
- [canvas-api-integration.md](./canvas-api-integration.md) - Canvas LMS API integration with GCP

<!-- section_id: "c67be701-fa12-47cb-af76-a0c4438628c8" -->
## Quick Reference

<!-- section_id: "ab28a866-47cc-417b-9b1f-cce9d6884101" -->
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

<!-- section_id: "ef3f7785-c2e7-4b47-b68f-816232e5250a" -->
### Secret Manager
```bash
# List secrets
gcloud secrets list

# Access a secret
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'

# Create a secret
echo "secret-value" | gcloud secrets create SECRET_NAME --data-file=-
```

<!-- section_id: "a4da9098-0d83-4cd6-9c36-a23a18256e65" -->
## Related Documentation

- [Canvas API Integration](./canvas-api-integration.md)
- [Environment Configuration](../scripts/README.md)
