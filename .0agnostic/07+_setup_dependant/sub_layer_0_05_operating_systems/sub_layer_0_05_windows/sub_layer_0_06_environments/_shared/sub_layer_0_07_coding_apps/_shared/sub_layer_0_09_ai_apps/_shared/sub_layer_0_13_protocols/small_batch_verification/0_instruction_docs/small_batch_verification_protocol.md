---
resource_id: "1aa550d5-0ad7-4495-9caa-67335014a211"
resource_type: "document"
resource_name: "small_batch_verification_protocol"
---
# Small Batch Verification Protocol

**Goal:** Minimize wasted effort and debugging time by verifying changes in small, manageable increments before scaling up.

<!-- section_id: "6edb6ddf-44b0-4188-822a-d27937426643" -->
## The Rule

**When implementing new features, fixing bugs, or running data extraction tasks:**
1.  **Start Small:** Execute the task on a single item, a test case, or a small subset (N=1 to 3).
2.  **Verify:** Confirm that the output is exactly as expected for this small batch.
3.  **Scale:** Only *after* verification, proceed to process the full dataset or implement the wider change.

<!-- section_id: "538b07fc-35d0-4c47-85de-0dce62521f1c" -->
## Applicability
This rule MUST be applied in the following situations:
1.  **First Time:** You are attempting a task or using a tool for the first time.
2.  **Past Failures:** You are retrying a task that failed previously.
3.  **Insufficient Quality:** Previous attempts did not meet the desired level of quality or accuracy.

<!-- section_id: "f6c38e4b-8c6a-4c7d-b5ab-334c34a59687" -->
## Why?
- **Fail Fast:** If the logic is wrong, you find out after 10 seconds, not after waiting for 100 items to process.
- **Isolate Variables:** Debugging a single failure is easier than analyzing a log of 50 mixed failures.
- **Resource Efficiency:** Prevents burning tokens, API calls, or system resources on doomed attempts.

<!-- section_id: "8a9a966b-6244-45e6-849b-f4e33a26f9d5" -->
## Examples

<!-- section_id: "325b4c09-f1ac-4945-b851-63759ee04391" -->
### Data Extraction
**Bad:** "Run the scraper on all 100 URLs in the list."
**Good:** "Run the scraper on the first URL. Check the output JSON. If correct, run on the remaining 99."

<!-- section_id: "0a69969d-5df4-4b08-b9bd-ed88c589794f" -->
### Code Refactoring
**Bad:** "Apply this regex replacement to all 50 files in the directory."
**Good:** "Apply the replacement to one file. `diff` the result. If correct, apply to the rest."

<!-- section_id: "6936079a-2439-4ba6-8d0d-af9a435400aa" -->
### Testing
**Bad:** "Run the full test suite."
**Good:** "Run the specific test case related to the change. If it passes, run the suite."
