---
resource_id: "1aa550d5-0ad7-4495-9caa-67335014a211"
resource_type: "document"
resource_name: "small_batch_verification_protocol"
---
# Small Batch Verification Protocol

**Goal:** Minimize wasted effort and debugging time by verifying changes in small, manageable increments before scaling up.

## The Rule

**When implementing new features, fixing bugs, or running data extraction tasks:**
1.  **Start Small:** Execute the task on a single item, a test case, or a small subset (N=1 to 3).
2.  **Verify:** Confirm that the output is exactly as expected for this small batch.
3.  **Scale:** Only *after* verification, proceed to process the full dataset or implement the wider change.

## Applicability
This rule MUST be applied in the following situations:
1.  **First Time:** You are attempting a task or using a tool for the first time.
2.  **Past Failures:** You are retrying a task that failed previously.
3.  **Insufficient Quality:** Previous attempts did not meet the desired level of quality or accuracy.

## Why?
- **Fail Fast:** If the logic is wrong, you find out after 10 seconds, not after waiting for 100 items to process.
- **Isolate Variables:** Debugging a single failure is easier than analyzing a log of 50 mixed failures.
- **Resource Efficiency:** Prevents burning tokens, API calls, or system resources on doomed attempts.

## Examples

### Data Extraction
**Bad:** "Run the scraper on all 100 URLs in the list."
**Good:** "Run the scraper on the first URL. Check the output JSON. If correct, run on the remaining 99."

### Code Refactoring
**Bad:** "Apply this regex replacement to all 50 files in the directory."
**Good:** "Apply the replacement to one file. `diff` the result. If correct, apply to the rest."

### Testing
**Bad:** "Run the full test suite."
**Good:** "Run the specific test case related to the change. If it passes, run the suite."
