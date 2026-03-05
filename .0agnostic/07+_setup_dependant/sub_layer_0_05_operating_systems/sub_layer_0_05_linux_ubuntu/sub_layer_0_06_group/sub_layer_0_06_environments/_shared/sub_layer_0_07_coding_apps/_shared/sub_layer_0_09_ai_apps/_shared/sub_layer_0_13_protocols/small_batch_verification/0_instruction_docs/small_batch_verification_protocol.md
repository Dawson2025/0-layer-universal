---
resource_id: "5327e258-019a-42ca-8700-80d08b3fc9c6"
resource_type: "document"
resource_name: "small_batch_verification_protocol"
---
# Small Batch Verification Protocol

**Goal:** Minimize wasted effort and debugging time by verifying changes in small, manageable increments before scaling up.

<!-- section_id: "220201c6-002f-4efa-acbe-267e659afebf" -->
## The Rule

**When implementing new features, fixing bugs, or running data extraction tasks:**
1.  **Start Small:** Execute the task on a single item, a test case, or a small subset (N=1 to 3).
2.  **Verify:** Confirm that the output is exactly as expected for this small batch.
3.  **Scale:** Only *after* verification, proceed to process the full dataset or implement the wider change.

<!-- section_id: "0c9b43a9-749b-4211-8bfe-1370febfd4f1" -->
## Applicability
This rule MUST be applied in the following situations:
1.  **First Time:** You are attempting a task or using a tool for the first time.
2.  **Past Failures:** You are retrying a task that failed previously.
3.  **Insufficient Quality:** Previous attempts did not meet the desired level of quality or accuracy.

<!-- section_id: "adbe7d01-a07b-408d-b749-728c971fc96a" -->
## Why?
- **Fail Fast:** If the logic is wrong, you find out after 10 seconds, not after waiting for 100 items to process.
- **Isolate Variables:** Debugging a single failure is easier than analyzing a log of 50 mixed failures.
- **Resource Efficiency:** Prevents burning tokens, API calls, or system resources on doomed attempts.

<!-- section_id: "e5ac2326-5ee9-48b4-bc80-1ec72957587c" -->
## Examples

<!-- section_id: "2f185f31-dec6-41c2-a6a6-ee5620ddba84" -->
### Data Extraction
**Bad:** "Run the scraper on all 100 URLs in the list."
**Good:** "Run the scraper on the first URL. Check the output JSON. If correct, run on the remaining 99."

<!-- section_id: "7aa03d2c-bd4c-43d6-9d12-c163e23efe6a" -->
### Code Refactoring
**Bad:** "Apply this regex replacement to all 50 files in the directory."
**Good:** "Apply the replacement to one file. `diff` the result. If correct, apply to the rest."

<!-- section_id: "be67608e-66ea-4917-9966-eee61c38b886" -->
### Testing
**Bad:** "Run the full test suite."
**Good:** "Run the specific test case related to the change. If it passes, run the suite."
