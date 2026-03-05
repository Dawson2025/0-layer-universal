---
resource_id: "34acaf69-c6c4-438d-a5ba-2edaeaedb572"
resource_type: "document"
resource_name: "secret-manager"
---
# Google Secret Manager

Google Secret Manager provides secure storage for API keys, passwords, certificates, and other sensitive data.

<!-- section_id: "82b6187e-7e4d-491d-9d10-a3fb6ab0859b" -->
## Prerequisites

- gcloud CLI installed and authenticated
- Billing enabled on your GCP project
- Secret Manager API enabled

<!-- section_id: "a87db8dc-8b95-4e63-b987-1966d04536c3" -->
## Enable the API

```bash
gcloud services enable secretmanager.googleapis.com
```

<!-- section_id: "1e87920c-b33f-4ac1-899f-33dfb4648d95" -->
## Basic Operations

<!-- section_id: "e5e48b56-c299-4d56-957a-8f13413159d4" -->
### Create a Secret
```bash
# From a value
echo -n "my-secret-value" | gcloud secrets create SECRET_NAME --data-file=-

# From a file
gcloud secrets create SECRET_NAME --data-file=path/to/secret.txt
```

<!-- section_id: "d29c1362-75a7-4ae5-977e-71c3701897ff" -->
### Access a Secret
```bash
# Get the latest version
gcloud secrets versions access latest --secret=SECRET_NAME

# Get a specific version
gcloud secrets versions access VERSION_ID --secret=SECRET_NAME

# Remove trailing newline (important for API keys)
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'
```

<!-- section_id: "459f0052-4f67-44ed-9d99-cdc2e01e74c7" -->
### Update a Secret
```bash
# Add a new version
echo -n "new-secret-value" | gcloud secrets versions add SECRET_NAME --data-file=-
```

<!-- section_id: "62de415e-8187-4628-885f-a36082f85611" -->
### List Secrets
```bash
gcloud secrets list
```

<!-- section_id: "155bb6e3-ee16-41e6-813a-4f58bfeca02a" -->
### Delete a Secret
```bash
gcloud secrets delete SECRET_NAME
```

<!-- section_id: "04602ef5-4463-4c2c-a5e5-b2e640b5c4b0" -->
## Using in Scripts

<!-- section_id: "68e3e708-06f1-497d-844c-2238ffc66c59" -->
### Bash
```bash
# Store in variable
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Use in API call
curl -H "Authorization: Bearer $CANVAS_API_KEY" https://api.example.com/endpoint
```

<!-- section_id: "c60cc9e4-430f-4355-99a4-233a5a6eed04" -->
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

<!-- section_id: "117fa110-88bc-49e0-818f-20a0652db305" -->
### Python
```python
from google.cloud import secretmanager

def access_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```

<!-- section_id: "b07a1f8a-0570-4e98-bf90-76d80788d64c" -->
## Common Stored Secrets

| Secret Name | Description |
|-------------|-------------|
| `CANVAS_API_KEY` | Canvas LMS API access token |
| `FIREBASE_API_KEY` | Firebase project API key |
| `OPENAI_API_KEY` | OpenAI API key |

<!-- section_id: "6ef63833-3080-4371-b81b-9a62471f275b" -->
## Security Best Practices

1. **Least privilege**: Only grant necessary IAM roles
2. **Rotation**: Rotate secrets regularly
3. **Versioning**: Use versions to track changes
4. **Audit logging**: Enable Cloud Audit Logs

<!-- section_id: "ae8d2802-ce22-4181-a750-24bdf9233917" -->
## Troubleshooting

<!-- section_id: "3ab983d5-3697-4d5b-90c5-34e8d958ebb5" -->
### Billing Required Error
```
ERROR: This API method requires billing to be enabled.
```
Enable billing at: https://console.cloud.google.com/billing/enable?project=PROJECT_ID

<!-- section_id: "3e9df94f-31f3-4695-99af-5babb6f06ce9" -->
### Permission Denied
Ensure your account has `roles/secretmanager.secretAccessor` role:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL@example.com" \
  --role="roles/secretmanager.secretAccessor"
```

<!-- section_id: "2ec667d3-6a9a-4b3d-a611-0a50fb8ee33e" -->
## Related
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Canvas API Integration](./canvas-api-integration.md)
