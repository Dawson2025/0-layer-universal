---
resource_id: "10a91f28-b8be-476f-8a1e-2ab1cfd2a27b"
resource_type: "document"
resource_name: "canvas-api-integration"
---
# Canvas LMS API Integration

This guide covers integrating with the Canvas LMS API using credentials stored in Google Secret Manager.

<!-- section_id: "d235c022-299a-4507-9a75-3295911c5a45" -->
## Overview

Canvas LMS provides a REST API for accessing course data, assignments, grades, and more. API keys should be stored securely in Google Secret Manager.

<!-- section_id: "fb1bd2d0-dce4-40dc-aa7e-848c8b372117" -->
## Prerequisites

- Canvas LMS account with API access
- Google Cloud project with Secret Manager enabled
- gcloud CLI installed and authenticated

<!-- section_id: "cccda575-332a-4a92-a79c-bdd28bbd09a6" -->
## Generating a Canvas API Token

1. Log into Canvas at your institution's URL
2. Go to **Account** > **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Provide a purpose description and optional expiry
6. Copy the generated token (it won't be shown again)

<!-- section_id: "2910f035-4a13-4d29-b1b5-f850d1760179" -->
## Storing the Token in Secret Manager

```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Create the secret
echo -n "YOUR_CANVAS_TOKEN" | gcloud secrets create CANVAS_API_KEY --data-file=-
```

<!-- section_id: "54d45bba-6fa6-4bb3-9984-40b135dced1e" -->
## Using the API

<!-- section_id: "10910094-b415-491f-b63b-b8df7465755b" -->
### Quick Test
```bash
# Get the API key
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Test with user profile endpoint
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "https://YOUR_INSTITUTION.instructure.com/api/v1/users/self"
```

<!-- section_id: "eb8dc122-15ef-4e34-baa4-4889bcf47c7e" -->
### Common Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/v1/users/self` | Current user profile |
| `/api/v1/courses` | List enrolled courses |
| `/api/v1/courses/:id/assignments` | Course assignments |
| `/api/v1/courses/:id/students` | Course students |

<!-- section_id: "f4bb9a81-458f-4679-83be-5cddb4091cbe" -->
### Example: List Courses

```bash
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')
BASE_URL="https://byui.instructure.com/api/v1"

wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses?enrollment_state=active" | jq '.[].name'
```

<!-- section_id: "5f8cc279-7453-4521-856c-b3e2f11b403b" -->
### Example: Get Assignments

```bash
COURSE_ID="12345"
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses/$COURSE_ID/assignments" | jq '.[] | {name, due_at}'
```

<!-- section_id: "5c91435c-ea5e-468f-8705-220712c61af1" -->
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

<!-- section_id: "c3358f9a-5d8e-4efe-b854-6c677330c2b4" -->
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

<!-- section_id: "4b581ee7-6fab-4c81-92ee-7711d54a6d68" -->
## Rate Limiting

Canvas API has rate limits. Check response headers:
- `X-Rate-Limit-Remaining`: Requests remaining
- `X-Request-Cost`: Cost of the request

<!-- section_id: "2fc7326d-43d2-454e-bac4-5713760700a7" -->
## Institution-Specific URLs

| Institution | Base URL |
|-------------|----------|
| BYU-Idaho | `https://byui.instructure.com/api/v1` |
| Generic | `https://YOUR_SCHOOL.instructure.com/api/v1` |

<!-- section_id: "5bf3aae4-eb65-4e55-ab18-fc443a6f59f4" -->
## Troubleshooting

<!-- section_id: "20c6b48c-0333-4d29-8226-3450e3d36c0c" -->
### 401 Unauthorized
- Check if token is valid and not expired
- Ensure token has necessary permissions

<!-- section_id: "54140923-6a87-4c47-8d22-a086cee57ee2" -->
### 403 Forbidden
- User may not have access to the requested resource
- Check course enrollment status

<!-- section_id: "201e2342-4d9e-4c88-ac6d-7e0f76f6772a" -->
### curl vs wget
If `curl` fails with exit code 43, use `wget`:
```bash
# Instead of curl
wget -qO- --header="Authorization: Bearer $TOKEN" "URL"
```

<!-- section_id: "f460a56f-e89e-4cd2-adc5-b2b92d1d9bde" -->
## Related Projects

- **catp (Canvas Assignment Time Predictor)**: `/home/dawson/dawson-workspace/code/catp/`
  - Reference implementation using Canvas API with Firebase

<!-- section_id: "31a01868-68c4-4941-a9f4-c058856b4f27" -->
## Related Documentation
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Secret Manager](./secret-manager.md)
- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
