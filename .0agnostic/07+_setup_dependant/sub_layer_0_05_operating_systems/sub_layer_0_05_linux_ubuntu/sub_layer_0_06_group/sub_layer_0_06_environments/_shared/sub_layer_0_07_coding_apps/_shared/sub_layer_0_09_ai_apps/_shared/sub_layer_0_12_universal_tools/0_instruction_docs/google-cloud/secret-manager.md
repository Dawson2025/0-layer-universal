---
resource_id: "5cbe0e74-56ce-4c11-8bc4-a6ff4a25de4f"
resource_type: "document"
resource_name: "secret-manager"
---
# Google Secret Manager

Google Secret Manager provides secure storage for API keys, passwords, certificates, and other sensitive data.

<!-- section_id: "a0796cb9-2424-471a-ae93-625a55f511c7" -->
## Prerequisites

- gcloud CLI installed and authenticated
- Billing enabled on your GCP project
- Secret Manager API enabled

<!-- section_id: "89e53ad9-08f1-42ee-90c8-6828107958cb" -->
## Enable the API

```bash
gcloud services enable secretmanager.googleapis.com
```

<!-- section_id: "819fbdbd-c03d-4c5b-bc86-3fc9bd34c8fd" -->
## Basic Operations

<!-- section_id: "b4a18220-fbc9-45ec-b4bc-7d038212fc06" -->
### Create a Secret
```bash
# From a value
echo -n "my-secret-value" | gcloud secrets create SECRET_NAME --data-file=-

# From a file
gcloud secrets create SECRET_NAME --data-file=path/to/secret.txt
```

<!-- section_id: "44a72eaf-d996-4de4-9067-95bde504c119" -->
### Access a Secret
```bash
# Get the latest version
gcloud secrets versions access latest --secret=SECRET_NAME

# Get a specific version
gcloud secrets versions access VERSION_ID --secret=SECRET_NAME

# Remove trailing newline (important for API keys)
gcloud secrets versions access latest --secret=SECRET_NAME | tr -d '\n'
```

<!-- section_id: "9705a75f-4483-4d4e-b3d8-c081544e9448" -->
### Update a Secret
```bash
# Add a new version
echo -n "new-secret-value" | gcloud secrets versions add SECRET_NAME --data-file=-
```

<!-- section_id: "9766307f-3d3b-451b-944a-cd5edbb823e5" -->
### List Secrets
```bash
gcloud secrets list
```

<!-- section_id: "42af7ff5-91bd-46b5-98d7-9bacc36b91be" -->
### Delete a Secret
```bash
gcloud secrets delete SECRET_NAME
```

<!-- section_id: "7829dff9-638d-4236-bf75-b226d184c1e5" -->
## Using in Scripts

<!-- section_id: "3373e599-b09c-40b2-bb30-00016525ddfa" -->
### Bash
```bash
# Store in variable
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Use in API call
curl -H "Authorization: Bearer $CANVAS_API_KEY" https://api.example.com/endpoint
```

<!-- section_id: "5037ef2f-ee8a-4c69-a660-98158d6a2ad4" -->
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

<!-- section_id: "9824d3e5-587c-421a-ac1b-d868c5e687e9" -->
### Python
```python
from google.cloud import secretmanager

def access_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```

<!-- section_id: "83cc5c24-693f-4fe9-a28d-4a7e2725f5bd" -->
## Common Stored Secrets

| Secret Name | Description |
|-------------|-------------|
| `CANVAS_API_KEY` | Canvas LMS API access token |
| `FIREBASE_API_KEY` | Firebase project API key |
| `OPENAI_API_KEY` | OpenAI API key |

<!-- section_id: "4350e03c-f50a-44fc-840d-ff51aa151557" -->
## Security Best Practices

1. **Least privilege**: Only grant necessary IAM roles
2. **Rotation**: Rotate secrets regularly
3. **Versioning**: Use versions to track changes
4. **Audit logging**: Enable Cloud Audit Logs

<!-- section_id: "697c3d1d-dd15-470f-af75-32c77f18cda1" -->
## Troubleshooting

<!-- section_id: "a1426fc4-4662-46e8-bb48-5a202c966d66" -->
### Billing Required Error
```
ERROR: This API method requires billing to be enabled.
```
Enable billing at: https://console.cloud.google.com/billing/enable?project=PROJECT_ID

<!-- section_id: "d445dc7c-9787-4db2-8cfb-84563f1b817f" -->
### Permission Denied
Ensure your account has `roles/secretmanager.secretAccessor` role:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL@example.com" \
  --role="roles/secretmanager.secretAccessor"
```

<!-- section_id: "a9641467-c1f3-4b01-b906-c57c0399c0a9" -->
## Related
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Canvas API Integration](./canvas-api-integration.md)
