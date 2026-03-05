---
resource_id: "ff4f3c93-be10-48d4-a5bd-df83e7c7033c"
resource_type: "document"
resource_name: "small_batch_verification_protocol"
---
# Small Batch Verification Protocol

**Goal:** Minimize wasted effort and debugging time by verifying changes in small, manageable increments before scaling up.

<!-- section_id: "9ed8e548-237e-4537-9698-9851570c504b" -->
## The Rule

**When implementing new features, fixing bugs, or running data extraction tasks:**
1.  **Start Small:** Execute the task on a single item, a test case, or a small subset (N=1 to 3).
2.  **Verify:** Confirm that the output is exactly as expected for this small batch.
3.  **Scale:** Only *after* verification, proceed to process the full dataset or implement the wider change.

<!-- section_id: "a5c2c086-448e-438b-a178-0cb34f24780e" -->
## Applicability
This rule MUST be applied in the following situations:
1.  **First Time:** You are attempting a task or using a tool for the first time.
2.  **Past Failures:** You are retrying a task that failed previously.
3.  **Insufficient Quality:** Previous attempts did not meet the desired level of quality or accuracy.

<!-- section_id: "6c145f59-79ce-411d-b4e6-d368313d673a" -->
## Why?
- **Fail Fast:** If the logic is wrong, you find out after 10 seconds, not after waiting for 100 items to process.
- **Isolate Variables:** Debugging a single failure is easier than analyzing a log of 50 mixed failures.
- **Resource Efficiency:** Prevents burning tokens, API calls, or system resources on doomed attempts.

<!-- section_id: "87f62120-7ee2-4820-b1f7-9720020983e8" -->
## Examples

<!-- section_id: "26a7d9c0-57b8-4052-a870-499450aaae9c" -->
### Data Extraction
**Bad:** "Run the scraper on all 100 URLs in the list."
**Good:** "Run the scraper on the first URL. Check the output JSON. If correct, run on the remaining 99."

<!-- section_id: "d7d63b89-2aa2-4e12-aa8d-c7ff3a16b5da" -->
### Code Refactoring
**Bad:** "Apply this regex replacement to all 50 files in the directory."
**Good:** "Apply the replacement to one file. `diff` the result. If correct, apply to the rest."

<!-- section_id: "8f8839bd-4409-43a0-8720-0eb41ad1b5a7" -->
### Testing
**Bad:** "Run the full test suite."
**Good:** "Run the specific test case related to the change. If it passes, run the suite."
