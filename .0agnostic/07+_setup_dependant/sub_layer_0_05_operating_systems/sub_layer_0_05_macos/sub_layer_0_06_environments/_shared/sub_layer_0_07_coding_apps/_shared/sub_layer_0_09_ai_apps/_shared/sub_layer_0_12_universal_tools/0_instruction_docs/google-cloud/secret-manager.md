---
resource_id: "0cd62809-6503-48aa-8c9c-2713f7090565"
resource_type: "document"
resource_name: "secret-manager"
---
# Google Secret Manager

Google Secret Manager provides secure storage for API keys, passwords, certificates, and other sensitive data.

<!-- section_id: "e23b5858-c679-4135-b35b-c2f2e6053415" -->
## Prerequisites

- gcloud CLI installed and authenticated
- Billing enabled on your GCP project
- Secret Manager API enabled

<!-- section_id: "b19bb1bb-cea4-42d8-9101-71dab5f2e827" -->
## Enable the API

```bash
gcloud services enable secretmanager.googleapis.com
```

<!-- section_id: "1718f04b-6f2d-4b0e-bd10-10db2d3907f2" -->
## Basic Operations

<!-- section_id: "570b06b2-26b3-4758-9f4c-b05949f77c40" -->
### Create a Secret
```bash
# From a value
echo -n "my-secret-value" | gcloud secrets create SECRET_NAME --data-file=-

# From a file
gcloud secrets create SECRET_NAME --data-file=path/to/secret.txt
```

<!-- section_id: "5fd6a1f9-2c8a-4f86-a01c-720a7e59a5ce" -->
### Access a Secret
```bash
# Get the latest version
gcloud secrets versions access latest --secret=SECRET_NAME

# Get a specific version
gcloud secrets versions access VERSION_ID --secret=SECRET_NAME

# Remove trailing newline (important for API keys)
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'
```

<!-- section_id: "39e88f49-b4f9-482b-a523-9b09f27bad67" -->
### Update a Secret
```bash
# Add a new version
echo -n "new-secret-value" | gcloud secrets versions add SECRET_NAME --data-file=-
```

<!-- section_id: "10221f5e-6a84-47e5-b329-6950eb28b703" -->
### List Secrets
```bash
gcloud secrets list
```

<!-- section_id: "d3d7dfc5-0700-4a15-afaf-7019534a0d00" -->
### Delete a Secret
```bash
gcloud secrets delete SECRET_NAME
```

<!-- section_id: "8a800e95-994f-4ada-a851-09a73b967a5e" -->
## Using in Scripts

<!-- section_id: "0b21f880-07d1-4516-af99-bee04581f9ce" -->
### Bash
```bash
# Store in variable
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Use in API call
curl -H "Authorization: Bearer $CANVAS_API_KEY" https://api.example.com/endpoint
```

<!-- section_id: "67eebe50-3cb2-499b-adfb-0dd66d1aabfa" -->
### Node.js
```javascript
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');
const client = new SecretManagerServiceClient();

async function accessSecret(secretName) {
  const [version] = await client.accessSecretVersion({
    name: `projects/PROJECT_ID/secrets/${secretName}/versions/latest`,
  });
  return version.payload.data.toString();
}
```

<!-- section_id: "0b0a1c64-1d25-4eff-9130-f75e7d3ad686" -->
### Python
```python
from google.cloud import secretmanager

def access_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```

<!-- section_id: "ca982b4f-3c61-4e38-9666-b3e3cf2a2bc0" -->
## Common Stored Secrets

| Secret Name | Description |
|-------------|-------------|
| `CANVAS_API_KEY` | Canvas LMS API access token |
| `FIREBASE_API_KEY` | Firebase project API key |
| `OPENAI_API_KEY` | OpenAI API key |

<!-- section_id: "715c26a5-cf00-400a-83ae-685d1cb8e401" -->
## Security Best Practices

1. **Least privilege**: Only grant necessary IAM roles
2. **Rotation**: Rotate secrets regularly
3. **Versioning**: Use versions to track changes
4. **Audit logging**: Enable Cloud Audit Logs

<!-- section_id: "8bbbd6cb-44b5-4eb2-b2a3-44a3e3608923" -->
## Troubleshooting

<!-- section_id: "47087bc2-5868-4e00-89ae-b3e5de1515f4" -->
### Billing Required Error
```
ERROR: This API method requires billing to be enabled.
```
Enable billing at: https://console.cloud.google.com/billing/enable?project=PROJECT_ID

<!-- section_id: "25cf1de5-a418-4595-a477-e21f5d79c9cc" -->
### Permission Denied
Ensure your account has `roles/secretmanager.secretAccessor` role:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL@example.com" \
  --role="roles/secretmanager.secretAccessor"
```

<!-- section_id: "73a92238-7479-495d-9431-3d734c9f8b00" -->
## Related
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Canvas API Integration](./canvas-api-integration.md)
