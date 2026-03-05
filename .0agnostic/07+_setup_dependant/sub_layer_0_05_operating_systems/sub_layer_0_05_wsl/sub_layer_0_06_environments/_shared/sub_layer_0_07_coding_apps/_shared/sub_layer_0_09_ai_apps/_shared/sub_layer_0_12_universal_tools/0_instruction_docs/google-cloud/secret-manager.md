---
resource_id: "fc235d77-09f5-4a50-8b38-030f3f84ed16"
resource_type: "document"
resource_name: "secret-manager"
---
# Google Secret Manager

Google Secret Manager provides secure storage for API keys, passwords, certificates, and other sensitive data.

<!-- section_id: "524e23b9-6c5c-4914-b4c0-8ead84270aa2" -->
## Prerequisites

- gcloud CLI installed and authenticated
- Billing enabled on your GCP project
- Secret Manager API enabled

<!-- section_id: "a73cf78e-c964-41f3-97c3-797fe2b51aa1" -->
## Enable the API

```bash
gcloud services enable secretmanager.googleapis.com
```

<!-- section_id: "aa86c9d2-e63d-4281-9d83-837d1b4425a2" -->
## Basic Operations

<!-- section_id: "2ac9773e-1dbc-45b5-9237-fb8bc07b6e46" -->
### Create a Secret
```bash
# From a value
echo -n "my-secret-value" | gcloud secrets create SECRET_NAME --data-file=-

# From a file
gcloud secrets create SECRET_NAME --data-file=path/to/secret.txt
```

<!-- section_id: "62b8c7f7-2849-4792-87d8-6775c45db501" -->
### Access a Secret
```bash
# Get the latest version
gcloud secrets versions access latest --secret=SECRET_NAME

# Get a specific version
gcloud secrets versions access VERSION_ID --secret=SECRET_NAME

# Remove trailing newline (important for API keys)
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'
```

<!-- section_id: "a28e6513-bf4b-489d-993a-95185377418f" -->
### Update a Secret
```bash
# Add a new version
echo -n "new-secret-value" | gcloud secrets versions add SECRET_NAME --data-file=-
```

<!-- section_id: "cabc0bb8-3f32-42d6-b8ad-8f74c3e5f610" -->
### List Secrets
```bash
gcloud secrets list
```

<!-- section_id: "b7c1c5f1-8bef-4ea7-937b-2608ba07a314" -->
### Delete a Secret
```bash
gcloud secrets delete SECRET_NAME
```

<!-- section_id: "57373e46-24ef-4857-bbfe-1991b5bbff0e" -->
## Using in Scripts

<!-- section_id: "8a1a4cf6-c220-4836-89ec-e4159c5f43be" -->
### Bash
```bash
# Store in variable
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Use in API call
curl -H "Authorization: Bearer $CANVAS_API_KEY" https://api.example.com/endpoint
```

<!-- section_id: "0346e29d-9c09-4da5-9c69-900de1feaa35" -->
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

<!-- section_id: "308f6bdc-b615-4750-b8b4-2804c3c57f5d" -->
### Python
```python
from google.cloud import secretmanager

def access_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```

<!-- section_id: "ab386eb4-1115-4f47-8e2b-6d3b4f90327f" -->
## Common Stored Secrets

| Secret Name | Description |
|-------------|-------------|
| `CANVAS_API_KEY` | Canvas LMS API access token |
| `FIREBASE_API_KEY` | Firebase project API key |
| `OPENAI_API_KEY` | OpenAI API key |

<!-- section_id: "7d87cf45-7dcf-4483-bae3-c2a12d183ddf" -->
## Security Best Practices

1. **Least privilege**: Only grant necessary IAM roles
2. **Rotation**: Rotate secrets regularly
3. **Versioning**: Use versions to track changes
4. **Audit logging**: Enable Cloud Audit Logs

<!-- section_id: "b2a8265a-2278-4763-a57e-da81e2e772e6" -->
## Troubleshooting

<!-- section_id: "8c1d4ec6-2398-4c26-926b-22c98068dbe7" -->
### Billing Required Error
```
ERROR: This API method requires billing to be enabled.
```
Enable billing at: https://console.cloud.google.com/billing/enable?project=PROJECT_ID

<!-- section_id: "744ae1a5-98e2-4a5f-8ab0-76c13f71d174" -->
### Permission Denied
Ensure your account has `roles/secretmanager.secretAccessor` role:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL@example.com" \
  --role="roles/secretmanager.secretAccessor"
```

<!-- section_id: "794a86fc-1567-455b-a3bc-c53e3de5a750" -->
## Related
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Canvas API Integration](./canvas-api-integration.md)
