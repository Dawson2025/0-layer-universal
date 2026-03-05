---
resource_id: "5cbe0e74-56ce-4c11-8bc4-a6ff4a25de4f"
resource_type: "document"
resource_name: "secret-manager"
---
# Google Secret Manager

Google Secret Manager provides secure storage for API keys, passwords, certificates, and other sensitive data.

## Prerequisites

- gcloud CLI installed and authenticated
- Billing enabled on your GCP project
- Secret Manager API enabled

## Enable the API

```bash
gcloud services enable secretmanager.googleapis.com
```

## Basic Operations

### Create a Secret
```bash
# From a value
echo -n "my-secret-value" | gcloud secrets create SECRET_NAME --data-file=-

# From a file
gcloud secrets create SECRET_NAME --data-file=path/to/secret.txt
```

### Access a Secret
```bash
# Get the latest version
gcloud secrets versions access latest --secret=SECRET_NAME

# Get a specific version
gcloud secrets versions access VERSION_ID --secret=SECRET_NAME

# Remove trailing newline (important for API keys)
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'
```

### Update a Secret
```bash
# Add a new version
echo -n "new-secret-value" | gcloud secrets versions add SECRET_NAME --data-file=-
```

### List Secrets
```bash
gcloud secrets list
```

### Delete a Secret
```bash
gcloud secrets delete SECRET_NAME
```

## Using in Scripts

### Bash
```bash
# Store in variable
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Use in API call
curl -H "Authorization: Bearer $CANVAS_API_KEY" https://api.example.com/endpoint
```

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

### Python
```python
from google.cloud import secretmanager

def access_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```

## Common Stored Secrets

| Secret Name | Description |
|-------------|-------------|
| `CANVAS_API_KEY` | Canvas LMS API access token |
| `FIREBASE_API_KEY` | Firebase project API key |
| `OPENAI_API_KEY` | OpenAI API key |

## Security Best Practices

1. **Least privilege**: Only grant necessary IAM roles
2. **Rotation**: Rotate secrets regularly
3. **Versioning**: Use versions to track changes
4. **Audit logging**: Enable Cloud Audit Logs

## Troubleshooting

### Billing Required Error
```
ERROR: This API method requires billing to be enabled.
```
Enable billing at: https://console.cloud.google.com/billing/enable?project=PROJECT_ID

### Permission Denied
Ensure your account has `roles/secretmanager.secretAccessor` role:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL@example.com" \
  --role="roles/secretmanager.secretAccessor"
```

## Related
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Canvas API Integration](./canvas-api-integration.md)
