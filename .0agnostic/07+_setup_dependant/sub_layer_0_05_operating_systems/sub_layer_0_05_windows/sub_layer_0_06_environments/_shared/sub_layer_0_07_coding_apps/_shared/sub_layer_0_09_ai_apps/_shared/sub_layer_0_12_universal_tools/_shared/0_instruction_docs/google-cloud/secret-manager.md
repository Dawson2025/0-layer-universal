---
resource_id: "505ef538-7ea1-4cf5-9b39-6c555346d5ca"
resource_type: "document"
resource_name: "secret-manager"
---
# Google Secret Manager

Google Secret Manager provides secure storage for API keys, passwords, certificates, and other sensitive data.

<!-- section_id: "c9b5d33b-b41e-42e6-8cdf-2e65699c69be" -->
## Prerequisites

- gcloud CLI installed and authenticated
- Billing enabled on your GCP project
- Secret Manager API enabled

<!-- section_id: "e429c936-28b2-4e13-a25d-1c28a4e4eabc" -->
## Enable the API

```bash
gcloud services enable secretmanager.googleapis.com
```

<!-- section_id: "2388cc94-16ed-4f49-8390-c5a0c5b0b173" -->
## Basic Operations

<!-- section_id: "38260c3b-696c-4a02-9cb4-112385f2132b" -->
### Create a Secret
```bash
# From a value
echo -n "my-secret-value" | gcloud secrets create SECRET_NAME --data-file=-

# From a file
gcloud secrets create SECRET_NAME --data-file=path/to/secret.txt
```

<!-- section_id: "a00cc78f-feed-437e-aa7f-2e8dfa047ca7" -->
### Access a Secret
```bash
# Get the latest version
gcloud secrets versions access latest --secret=SECRET_NAME

# Get a specific version
gcloud secrets versions access VERSION_ID --secret=SECRET_NAME

# Remove trailing newline (important for API keys)
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'
```

<!-- section_id: "5ebf1c15-29f4-41c9-a51b-0acf01e61e8c" -->
### Update a Secret
```bash
# Add a new version
echo -n "new-secret-value" | gcloud secrets versions add SECRET_NAME --data-file=-
```

<!-- section_id: "9bea9d5a-fcce-47c6-9891-66c20637bf1a" -->
### List Secrets
```bash
gcloud secrets list
```

<!-- section_id: "92170cd5-840e-4b96-8163-43b1cad23d04" -->
### Delete a Secret
```bash
gcloud secrets delete SECRET_NAME
```

<!-- section_id: "6bc2634e-5856-4833-862f-3c208151ce30" -->
## Using in Scripts

<!-- section_id: "95c1a6c3-a6d9-4552-ad50-f3edb1f1a4ae" -->
### Bash
```bash
# Store in variable
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Use in API call
curl -H "Authorization: Bearer $CANVAS_API_KEY" https://api.example.com/endpoint
```

<!-- section_id: "153df5fa-ea0c-4695-a9c0-4c2fba123fe7" -->
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

<!-- section_id: "d194c895-b8b0-4e3b-be27-c430e5d7e1c2" -->
### Python
```python
from google.cloud import secretmanager

def access_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```

<!-- section_id: "f952094c-ecf2-4e90-b8f1-cc1af18a6dca" -->
## Common Stored Secrets

| Secret Name | Description |
|-------------|-------------|
| `CANVAS_API_KEY` | Canvas LMS API access token |
| `FIREBASE_API_KEY` | Firebase project API key |
| `OPENAI_API_KEY` | OpenAI API key |

<!-- section_id: "cee93603-1c7e-4734-9587-592e372f6f1c" -->
## Security Best Practices

1. **Least privilege**: Only grant necessary IAM roles
2. **Rotation**: Rotate secrets regularly
3. **Versioning**: Use versions to track changes
4. **Audit logging**: Enable Cloud Audit Logs

<!-- section_id: "e5d794b5-2dea-450d-8ab8-c49280a64eca" -->
## Troubleshooting

<!-- section_id: "583d580f-785a-411c-9bcc-659dc6438757" -->
### Billing Required Error
```
ERROR: This API method requires billing to be enabled.
```
Enable billing at: https://console.cloud.google.com/billing/enable?project=PROJECT_ID

<!-- section_id: "079aa36c-39d7-4e2d-9aa3-3b7714054894" -->
### Permission Denied
Ensure your account has `roles/secretmanager.secretAccessor` role:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL@example.com" \
  --role="roles/secretmanager.secretAccessor"
```

<!-- section_id: "e8e03206-4d13-4578-807b-7e56fdee4a63" -->
## Related
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Canvas API Integration](./canvas-api-integration.md)
