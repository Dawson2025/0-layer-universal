---
resource_id: "ec03dc29-e737-42bc-9b19-c0c7d12abb6d"
resource_type: "readme_document"
resource_name: "README"
---
# Google Cloud Tools

This directory contains documentation for Google Cloud Platform (GCP) tools and integrations used across AI development workflows.

<!-- section_id: "08995fc5-9e68-488a-bd5b-cec73bd45ae7" -->
## Contents

- [gcloud-cli-setup.md](./gcloud-cli-setup.md) - Installing and configuring the gcloud CLI
- [secret-manager.md](./secret-manager.md) - Using Google Secret Manager for API keys and credentials
- [canvas-api-integration.md](./canvas-api-integration.md) - Canvas LMS API integration with GCP

<!-- section_id: "0ee141db-b025-4b3d-bdfd-311910ad2689" -->
## Quick Reference

<!-- section_id: "ee1def8d-1c95-41e1-945f-62aa07f49670" -->
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

<!-- section_id: "81c11a80-2180-496a-9fb8-97583f62c038" -->
### Secret Manager
```bash
# List secrets
gcloud secrets list

# Access a secret
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'

# Create a secret
echo "secret-value" | gcloud secrets create SECRET_NAME --data-file=-
```

<!-- section_id: "d9eb9dba-c8b2-4775-bab4-e060a6cea549" -->
## Related Documentation

- [Canvas API Integration](./canvas-api-integration.md)
- [Environment Configuration](../scripts/README.md)
