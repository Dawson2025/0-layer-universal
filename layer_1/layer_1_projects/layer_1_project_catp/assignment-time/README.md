---
resource_id: "d0a61515-9f45-4d03-8e00-197a1306a995"
resource_type: "readme
document"
resource_name: "README"
---
# assignment-time

<!-- section_id: "d2e668c2-0795-49b7-ba50-93cb7947d4e6" -->
## Local Development
- Install deps: `npm install` inside `functions/` and `assignment-timer/`.
- Populate secrets for emulators: either export `CANVAS_API_KEY` locally or place it in `functions/.env.local` (git-ignored). If you need the real key, pull it with `gcloud secrets versions access CANVAS_API_KEY`.
- Start emulators from `functions/`: `firebase emulators:start --only functions,firestore`.
- Seed test data and call the new endpoint in another terminal: `node test-student-course-details.js`.

<!-- section_id: "4d03dfe8-b83c-48c3-a79b-b1ed4dd32b64" -->
## Testing
- The `functions/test-student-course-details.js` script seeds the Firestore emulator and asserts the `getStudentCourseDetails` response structure. Run it while emulators are active.
- For integration against staging Canvas, provide a staging `CANVAS_API_KEY` via env var or `.env.test` and invoke `fetchCanvasCourses` / `syncAllAssignments` through the emulator.

<!-- section_id: "f48d312d-8db2-43fa-b7d8-c4ec5f20a056" -->
## Deployment
- Ensure production secrets live in Secret Manager; the Cloud Functions service account must have `Secret Manager Secret Accessor`.
- Deploy from `functions/`: `firebase deploy --only functions`.
- After deployment, trigger `fetchCanvasCourses` and `syncAllAssignments`, then verify `getStudentCourseDetails` through the deployed URL.
<!-- section_id: "fc682a34-f033-406c-9dae-a6d96750c19f" -->
## Additional Documentation
- [Cloud Integration & Credential Plan](docs/integration-plan.md)
