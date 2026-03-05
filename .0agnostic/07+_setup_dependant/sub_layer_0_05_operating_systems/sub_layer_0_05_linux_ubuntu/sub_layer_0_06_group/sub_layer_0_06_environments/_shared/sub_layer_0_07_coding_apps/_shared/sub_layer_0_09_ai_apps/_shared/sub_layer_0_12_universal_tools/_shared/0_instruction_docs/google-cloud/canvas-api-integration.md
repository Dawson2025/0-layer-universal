---
resource_id: "8513835b-784f-473f-883f-98a01697b653"
resource_type: "document"
resource_name: "canvas-api-integration"
---
# Canvas LMS API Integration

This guide covers integrating with the Canvas LMS API using credentials stored in Google Secret Manager.

<!-- section_id: "ad208f48-8ba0-43d7-97b7-d959e6886c78" -->
## Overview

Canvas LMS provides a REST API for accessing course data, assignments, grades, and more. API keys should be stored securely in Google Secret Manager.

<!-- section_id: "959a14f1-a6eb-4409-a24e-2b9a3019202c" -->
## Prerequisites

- Canvas LMS account with API access
- Google Cloud project with Secret Manager enabled
- gcloud CLI installed and authenticated

<!-- section_id: "c76a7f8b-b06f-42ad-96ab-5894a4517d7b" -->
## Generating a Canvas API Token

1. Log into Canvas at your institution's URL
2. Go to **Account** > **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Provide a purpose description and optional expiry
6. Copy the generated token (it won't be shown again)

<!-- section_id: "76945e05-7c40-4f22-aaac-4bb98cc958ac" -->
## Storing the Token in Secret Manager

```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Create the secret
echo -n "YOUR_CANVAS_TOKEN" | gcloud secrets create CANVAS_API_KEY --data-file=-
```

<!-- section_id: "f72d9b8f-8e84-4a75-896d-47264c5145de" -->
## Using the API

<!-- section_id: "f644754c-8f9d-4ede-a6a6-7cca97d762a5" -->
### Quick Test
```bash
# Get the API key
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Test with user profile endpoint
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "https://YOUR_INSTITUTION.instructure.com/api/v1/users/self"
```

<!-- section_id: "9f37992d-79e1-4679-a640-cc097f92420e" -->
### Common Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/v1/users/self` | Current user profile |
| `/api/v1/courses` | List enrolled courses |
| `/api/v1/courses/:id/assignments` | Course assignments |
| `/api/v1/courses/:id/students` | Course students |

<!-- section_id: "c6c551b5-9184-4700-9108-e1c8f77f9ce6" -->
### Example: List Courses

```bash
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')
BASE_URL="https://byui.instructure.com/api/v1"

wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses?enrollment_state=active" | jq '.[].name'
```

<!-- section_id: "aed1c889-e02d-4fa5-bd21-7e1cf17a7ac1" -->
### Example: Get Assignments

```bash
COURSE_ID="12345"
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses/$COURSE_ID/assignments" | jq '.[] | {name, due_at}'
```

<!-- section_id: "49e00069-94a3-4220-9d15-6e3a8bffa74d" -->
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

<!-- section_id: "7a62ef55-607c-47de-ab84-1ac45762e9fa" -->
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

<!-- section_id: "b214c349-4829-427c-a523-617becea179a" -->
## Rate Limiting

Canvas API has rate limits. Check response headers:
- `X-Rate-Limit-Remaining`: Requests remaining
- `X-Request-Cost`: Cost of the request

<!-- section_id: "5edc1c62-85a0-48d1-8fb1-f709b40bc0a5" -->
## Institution-Specific URLs

| Institution | Base URL |
|-------------|----------|
| BYU-Idaho | `https://byui.instructure.com/api/v1` |
| Generic | `https://YOUR_SCHOOL.instructure.com/api/v1` |

<!-- section_id: "00c24dc1-bf5f-41f9-969c-cb64d5b9362e" -->
## Troubleshooting

<!-- section_id: "51f17614-6966-4a1c-9460-9ce335e6f8db" -->
### 401 Unauthorized
- Check if token is valid and not expired
- Ensure token has necessary permissions

<!-- section_id: "6f52d4ca-bfca-4aba-8bf1-c78ed2ed5e84" -->
### 403 Forbidden
- User may not have access to the requested resource
- Check course enrollment status

<!-- section_id: "30fde040-0ad7-41d7-b0df-2c865904e04e" -->
### curl vs wget
If `curl` fails with exit code 43, use `wget`:
```bash
# Instead of curl
wget -qO- --header="Authorization: Bearer $TOKEN" "URL"
```

<!-- section_id: "67873e14-359e-4c3b-ac0a-7ad7261194bb" -->
## Related Projects

- **catp (Canvas Assignment Time Predictor)**: `/home/dawson/dawson-workspace/code/catp/`
  - Reference implementation using Canvas API with Firebase

<!-- section_id: "d45d3247-d7d9-4738-84c0-9f4c7c25ddb5" -->
## Related Documentation
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Secret Manager](./secret-manager.md)
- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
