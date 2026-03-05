---
resource_id: "89c71582-72a8-42e3-8eba-435ed1ec2e24"
resource_type: "document"
resource_name: "small_batch_verification_protocol"
---
# Small Batch Verification Protocol

**Goal:** Minimize wasted effort and debugging time by verifying changes in small, manageable increments before scaling up.

<!-- section_id: "41b08fa5-5a4b-4ac5-9848-4715655c05f5" -->
## The Rule

**When implementing new features, fixing bugs, or running data extraction tasks:**
1.  **Start Small:** Execute the task on a single item, a test case, or a small subset (N=1 to 3).
2.  **Verify:** Confirm that the output is exactly as expected for this small batch.
3.  **Scale:** Only *after* verification, proceed to process the full dataset or implement the wider change.

<!-- section_id: "38daf219-fefc-48a2-9e07-74d8abd17788" -->
## Applicability
This rule MUST be applied in the following situations:
1.  **First Time:** You are attempting a task or using a tool for the first time.
2.  **Past Failures:** You are retrying a task that failed previously.
3.  **Insufficient Quality:** Previous attempts did not meet the desired level of quality or accuracy.

<!-- section_id: "e611ccfc-11c1-4b58-923f-53887c80d0e4" -->
## Why?
- **Fail Fast:** If the logic is wrong, you find out after 10 seconds, not after waiting for 100 items to process.
- **Isolate Variables:** Debugging a single failure is easier than analyzing a log of 50 mixed failures.
- **Resource Efficiency:** Prevents burning tokens, API calls, or system resources on doomed attempts.

<!-- section_id: "18497f11-c930-49a6-82f2-f62f18b272c9" -->
## Examples

<!-- section_id: "bc30e16d-3417-4ef9-a70f-1b517b1e9647" -->
### Data Extraction
**Bad:** "Run the scraper on all 100 URLs in the list."
**Good:** "Run the scraper on the first URL. Check the output JSON. If correct, run on the remaining 99."

<!-- section_id: "c8db04b4-dd69-4450-b5ea-3b62d282e699" -->
### Code Refactoring
**Bad:** "Apply this regex replacement to all 50 files in the directory."
**Good:** "Apply the replacement to one file. `diff` the result. If correct, apply to the rest."

<!-- section_id: "cdccc589-649d-4712-a8bc-6178defb6f3a" -->
### Testing
**Bad:** "Run the full test suite."
**Good:** "Run the specific test case related to the change. If it passes, run the suite."
