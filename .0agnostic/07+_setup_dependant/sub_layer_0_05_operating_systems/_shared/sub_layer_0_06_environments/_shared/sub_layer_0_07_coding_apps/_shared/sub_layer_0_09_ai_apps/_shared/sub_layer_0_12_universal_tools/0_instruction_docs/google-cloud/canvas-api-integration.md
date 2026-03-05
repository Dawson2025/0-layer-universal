---
resource_id: "81349c3d-66ee-4857-8553-2a610ba60253"
resource_type: "document"
resource_name: "canvas-api-integration"
---
# Canvas LMS API Integration

This guide covers integrating with the Canvas LMS API using credentials stored in Google Secret Manager.

<!-- section_id: "633d05c2-b7dc-4469-85df-08427d7db13f" -->
## Overview

Canvas LMS provides a REST API for accessing course data, assignments, grades, and more. API keys should be stored securely in Google Secret Manager.

<!-- section_id: "56163cb6-a322-46b2-87b8-1b77cc17a9b7" -->
## Prerequisites

- Canvas LMS account with API access
- Google Cloud project with Secret Manager enabled
- gcloud CLI installed and authenticated

<!-- section_id: "4cef0af6-f704-41b9-8bcd-679c7af8da33" -->
## Generating a Canvas API Token

1. Log into Canvas at your institution's URL
2. Go to **Account** > **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Provide a purpose description and optional expiry
6. Copy the generated token (it won't be shown again)

<!-- section_id: "ce02b1a8-fb41-4c04-a68b-dd5927eb7cff" -->
## Storing the Token in Secret Manager

```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Create the secret
echo -n "YOUR_CANVAS_TOKEN" | gcloud secrets create CANVAS_API_KEY --data-file=-
```

<!-- section_id: "b37589db-0420-461f-be0b-46d5d08f56fd" -->
## Using the API

<!-- section_id: "85b6d8c4-bc28-42bb-ac4d-9d70df5f6e1d" -->
### Quick Test
```bash
# Get the API key
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Test with user profile endpoint
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "https://YOUR_INSTITUTION.instructure.com/api/v1/users/self"
```

<!-- section_id: "409bb3d2-b29a-4bec-b3cd-afdaac0f2146" -->
### Common Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/v1/users/self` | Current user profile |
| `/api/v1/courses` | List enrolled courses |
| `/api/v1/courses/:id/assignments` | Course assignments |
| `/api/v1/courses/:id/students` | Course students |

<!-- section_id: "fb05e7fb-bb0b-4052-a1ca-02442369496d" -->
### Example: List Courses

```bash
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')
BASE_URL="https://byui.instructure.com/api/v1"

wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses?enrollment_state=active" | jq '.[].name'
```

<!-- section_id: "9eb20b8e-9306-48f8-a4aa-031cfd6bae85" -->
### Example: Get Assignments

```bash
COURSE_ID="12345"
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses/$COURSE_ID/assignments" | jq '.[] | {name, due_at}'
```

<!-- section_id: "f85bedb4-607f-448b-a72b-646f425f94a0" -->
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

<!-- section_id: "6648485d-0378-4c79-a196-fa3784972df4" -->
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

<!-- section_id: "5d695344-8b07-4d44-98ea-1e6fbdda9a4a" -->
## Rate Limiting

Canvas API has rate limits. Check response headers:
- `X-Rate-Limit-Remaining`: Requests remaining
- `X-Request-Cost`: Cost of the request

<!-- section_id: "b4eaf07d-d573-465b-b6fb-0c847cdd3eb5" -->
## Institution-Specific URLs

| Institution | Base URL |
|-------------|----------|
| BYU-Idaho | `https://byui.instructure.com/api/v1` |
| Generic | `https://YOUR_SCHOOL.instructure.com/api/v1` |

<!-- section_id: "3fb6c7a1-4304-4b46-b9cc-91e7618dbea2" -->
## Troubleshooting

<!-- section_id: "690c5ce7-77d0-475b-8f59-c4c67b532cb2" -->
### 401 Unauthorized
- Check if token is valid and not expired
- Ensure token has necessary permissions

<!-- section_id: "dbc3748f-101f-47ab-8e0f-bb813ba4dc38" -->
### 403 Forbidden
- User may not have access to the requested resource
- Check course enrollment status

<!-- section_id: "26e16c2c-b4e0-45b7-9ab0-5f5c29ac9378" -->
### curl vs wget
If `curl` fails with exit code 43, use `wget`:
```bash
# Instead of curl
wget -qO- --header="Authorization: Bearer $TOKEN" "URL"
```

<!-- section_id: "983ac7a0-b220-45e4-89e5-fc3a2944ab45" -->
## Related Projects

- **catp (Canvas Assignment Time Predictor)**: `/home/dawson/dawson-workspace/code/catp/`
  - Reference implementation using Canvas API with Firebase

<!-- section_id: "141f01d6-663f-4c70-9fa9-d3775324fd05" -->
## Related Documentation
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Secret Manager](./secret-manager.md)
- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
