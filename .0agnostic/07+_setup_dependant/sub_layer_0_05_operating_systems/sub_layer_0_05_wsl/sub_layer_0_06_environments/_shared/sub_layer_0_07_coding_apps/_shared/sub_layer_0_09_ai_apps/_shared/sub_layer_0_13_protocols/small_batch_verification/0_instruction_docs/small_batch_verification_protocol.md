---
resource_id: "ae21c67c-c5f0-43b3-b35c-24649d447e6c"
resource_type: "document"
resource_name: "small_batch_verification_protocol"
---
# Small Batch Verification Protocol

**Goal:** Minimize wasted effort and debugging time by verifying changes in small, manageable increments before scaling up.

<!-- section_id: "ed8d7136-8eac-408f-a0a2-39612a223c1a" -->
## The Rule

**When implementing new features, fixing bugs, or running data extraction tasks:**
1.  **Start Small:** Execute the task on a single item, a test case, or a small subset (N=1 to 3).
2.  **Verify:** Confirm that the output is exactly as expected for this small batch.
3.  **Scale:** Only *after* verification, proceed to process the full dataset or implement the wider change.

<!-- section_id: "7e0e64b2-9f1b-4c1b-9599-a69a3a234205" -->
## Applicability
This rule MUST be applied in the following situations:
1.  **First Time:** You are attempting a task or using a tool for the first time.
2.  **Past Failures:** You are retrying a task that failed previously.
3.  **Insufficient Quality:** Previous attempts did not meet the desired level of quality or accuracy.

<!-- section_id: "36981186-b2b5-4ff0-af12-2671f0de9b4a" -->
## Why?
- **Fail Fast:** If the logic is wrong, you find out after 10 seconds, not after waiting for 100 items to process.
- **Isolate Variables:** Debugging a single failure is easier than analyzing a log of 50 mixed failures.
- **Resource Efficiency:** Prevents burning tokens, API calls, or system resources on doomed attempts.

<!-- section_id: "7a999d22-d2a6-44c3-878e-786f5b4e083c" -->
## Examples

<!-- section_id: "9f7bcad4-4e4d-4428-8d53-8db7af95d799" -->
### Data Extraction
**Bad:** "Run the scraper on all 100 URLs in the list."
**Good:** "Run the scraper on the first URL. Check the output JSON. If correct, run on the remaining 99."

<!-- section_id: "0f9e4364-32eb-4085-96fe-7b933df53af1" -->
### Code Refactoring
**Bad:** "Apply this regex replacement to all 50 files in the directory."
**Good:** "Apply the replacement to one file. `diff` the result. If correct, apply to the rest."

<!-- section_id: "75605965-a4e2-4ad9-a186-9fa541802a3e" -->
### Testing
**Bad:** "Run the full test suite."
**Good:** "Run the specific test case related to the change. If it passes, run the suite."
