---
resource_id: "b386b98a-857e-4deb-af19-e4659bde43d0"
resource_type: "readme_document"
resource_name: "README"
---
# Google Cloud Tools

This directory contains documentation for Google Cloud Platform (GCP) tools and integrations used across AI development workflows.

<!-- section_id: "83763d9a-ceea-4177-8aa7-e818fc2ab5c0" -->
## Contents

- [gcloud-cli-setup.md](./gcloud-cli-setup.md) - Installing and configuring the gcloud CLI
- [secret-manager.md](./secret-manager.md) - Using Google Secret Manager for API keys and credentials
- [canvas-api-integration.md](./canvas-api-integration.md) - Canvas LMS API integration with GCP

<!-- section_id: "cb0c3c20-d702-4278-a26e-ab2e04b7ce2b" -->
## Quick Reference

<!-- section_id: "d75eafb1-6ffd-4da6-85c7-f844648674eb" -->
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

<!-- section_id: "b759e54c-62fa-4916-a1b5-ec24f5ac10b3" -->
### Secret Manager
```bash
# List secrets
gcloud secrets list

# Access a secret
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'

# Create a secret
echo "secret-value" | gcloud secrets create SECRET_NAME --data-file=-
```

<!-- section_id: "992209bc-7284-4d71-8ca0-0b6369ba65b8" -->
## Related Documentation

- [Canvas API Integration](./canvas-api-integration.md)
- [Environment Configuration](../scripts/README.md)
