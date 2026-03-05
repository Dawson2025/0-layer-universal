---
resource_id: "d0a61515-9f45-4d03-8e00-197a1306a995"
resource_type: "readme
document"
resource_name: "README"
---
# assignment-time

## Local Development
- Install deps: `npm install` inside `functions/` and `assignment-timer/`.
- Populate secrets for emulators: either export `CANVAS_API_KEY` locally or place it in `functions/.env.local` (git-ignored). If you need the real key, pull it with `gcloud secrets versions access CANVAS_API_KEY`.
- Start emulators from `functions/`: `firebase emulators:start --only functions,firestore`.
- Seed test data and call the new endpoint in another terminal: `node test-student-course-details.js`.

## Testing
- The `functions/test-student-course-details.js` script seeds the Firestore emulator and asserts the `getStudentCourseDetails` response structure. Run it while emulators are active.
- For integration against staging Canvas, provide a staging `CANVAS_API_KEY` via env var or `.env.test` and invoke `fetchCanvasCourses` / `syncAllAssignments` through the emulator.

## Deployment
- Ensure production secrets live in Secret Manager; the Cloud Functions service account must have `Secret Manager Secret Accessor`.
- Deploy from `functions/`: `firebase deploy --only functions`.
- After deployment, trigger `fetchCanvasCourses` and `syncAllAssignments`, then verify `getStudentCourseDetails` through the deployed URL.
## Additional Documentation
- [Cloud Integration & Credential Plan](docs/integration-plan.md)
