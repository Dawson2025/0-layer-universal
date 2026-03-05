---
resource_id: "13e86bca-6a1c-47fb-ab1c-c960ac6a4a02"
resource_type: "document"
resource_name: "canvas-api-integration"
---
# Canvas LMS API Integration

This guide covers integrating with the Canvas LMS API using credentials stored in Google Secret Manager.

<!-- section_id: "96839891-7ff4-4ca5-b032-48af551e41c1" -->
## Overview

Canvas LMS provides a REST API for accessing course data, assignments, grades, and more. API keys should be stored securely in Google Secret Manager.

<!-- section_id: "ccf1190d-27a9-4cef-8bcb-5bc3ece35cc0" -->
## Prerequisites

- Canvas LMS account with API access
- Google Cloud project with Secret Manager enabled
- gcloud CLI installed and authenticated

<!-- section_id: "92f30753-f383-4837-8d7c-652466f49260" -->
## Generating a Canvas API Token

1. Log into Canvas at your institution's URL
2. Go to **Account** > **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Provide a purpose description and optional expiry
6. Copy the generated token (it won't be shown again)

<!-- section_id: "76a269f6-b21d-4491-bc4e-2b33799ac0bc" -->
## Storing the Token in Secret Manager

```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Create the secret
echo -n "YOUR_CANVAS_TOKEN" | gcloud secrets create CANVAS_API_KEY --data-file=-
```

<!-- section_id: "94727a9e-6e9b-462f-add6-a99d9b7ab9f0" -->
## Using the API

<!-- section_id: "a4d307ba-edc5-4ead-a637-2ff6de61660c" -->
### Quick Test
```bash
# Get the API key
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Test with user profile endpoint
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "https://YOUR_INSTITUTION.instructure.com/api/v1/users/self"
```

<!-- section_id: "7cbb6f46-0728-4faf-8f0c-36ce6ddfada2" -->
### Common Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/v1/users/self` | Current user profile |
| `/api/v1/courses` | List enrolled courses |
| `/api/v1/courses/:id/assignments` | Course assignments |
| `/api/v1/courses/:id/students` | Course students |

<!-- section_id: "d954505c-b3a5-477b-a497-170ad270c823" -->
### Example: List Courses

```bash
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')
BASE_URL="https://byui.instructure.com/api/v1"

wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses?enrollment_state=active" | jq '.[].name'
```

<!-- section_id: "792574f1-f731-42e1-b793-adddbf441025" -->
### Example: Get Assignments

```bash
COURSE_ID="12345"
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses/$COURSE_ID/assignments" | jq '.[] | {name, due_at}'
```

<!-- section_id: "7ee81077-b405-482c-bd8d-29e6058bda67" -->
## Node.js Integration

```javascript
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');

async function getCanvasApiKey() {
  const client = new SecretManagerServiceClient();
  const [version] = await client.accessSecretVersion({
    name: 'projects/PROJECT_ID/secrets/CANVAS_API_KEY/versions/latest',
  });
  return version.payload.data.toString();
}

async function fetchCanvasCourses(apiKey, baseUrl) {
  const response = await fetch(`${baseUrl}/courses`, {
    headers: {
      'Authorization': `Bearer ${apiKey}`,
    },
  });
  return response.json();
}

// Usage
const apiKey = await getCanvasApiKey();
const courses = await fetchCanvasCourses(apiKey, 'https://byui.instructure.com/api/v1');
```

<!-- section_id: "531d2786-3deb-46d9-9623-ade1299f150b" -->
## Python Integration

```python
from google.cloud import secretmanager
import requests

def get_canvas_api_key(project_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/CANVAS_API_KEY/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def fetch_courses(api_key, base_url):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(f"{base_url}/courses", headers=headers)
    return response.json()

# Usage
api_key = get_canvas_api_key("assignment-time")
courses = fetch_courses(api_key, "https://byui.instructure.com/api/v1")
```

<!-- section_id: "bf335bd2-e041-475b-969f-9b06ffd452cc" -->
## Rate Limiting

Canvas API has rate limits. Check response headers:
- `X-Rate-Limit-Remaining`: Requests remaining
- `X-Request-Cost`: Cost of the request

<!-- section_id: "291642d1-4ad1-4b21-ad79-891e46d73495" -->
## Institution-Specific URLs

| Institution | Base URL |
|-------------|----------|
| BYU-Idaho | `https://byui.instructure.com/api/v1` |
| Generic | `https://YOUR_SCHOOL.instructure.com/api/v1` |

<!-- section_id: "b000a316-5b4c-4390-98ed-341e817299f9" -->
## Troubleshooting

<!-- section_id: "cba26c7a-a895-4b20-8ddc-990b06e9e50b" -->
### 401 Unauthorized
- Check if token is valid and not expired
- Ensure token has necessary permissions

<!-- section_id: "64cb2cac-0a43-4ee6-9d8a-cf9c75e9ca2a" -->
### 403 Forbidden
- User may not have access to the requested resource
- Check course enrollment status

<!-- section_id: "6fbcc61e-2b44-4aaa-a41f-c97d4e362a1f" -->
### curl vs wget
If `curl` fails with exit code 43, use `wget`:
```bash
# Instead of curl
wget -qO- --header="Authorization: Bearer $TOKEN" "URL"
```

<!-- section_id: "4fb30c54-c990-43af-b252-244070da65fa" -->
## Related Projects

- **catp (Canvas Assignment Time Predictor)**: `/home/dawson/dawson-workspace/code/catp/`
  - Reference implementation using Canvas API with Firebase

<!-- section_id: "e3ff3676-6728-4c81-912a-d92eadb2e56a" -->
## Related Documentation
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Secret Manager](./secret-manager.md)
- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
