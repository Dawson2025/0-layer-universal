---
resource_id: "780207d9-c6c1-4c07-8e0e-b95ab72c66b5"
resource_type: "rule"
resource_name: "canvas_submission_protocol"
---
# Canvas Submission Protocol for Programming Assignments

<!-- section_id: "86c8ab00-864b-4732-8962-367c7bad3ea0" -->
## Purpose
Ensure every submission to Canvas includes the correct auto-generated evidence files and avoids common upload errors.

<!-- section_id: "9733aa45-963f-4857-86f0-7e383c3333e7" -->
## Required Files
1. Assignment source file (for example `assignment06.py`).
2. Auto-generated log files from the `Log` class (for example `1101-184337.log`, `1101-182543.log`).
   - **Only submit logs that were created by running the program.**
   - Never hand-edit or rewrite log contents; re-run the program instead.
   - Keep the original filenames so timestamps remain trustworthy.

<!-- section_id: "7ce11b91-0baf-4a30-9893-29ed387b3058" -->
## Upload Steps in Canvas
1. Click **"Choose a file to upload"** and attach the code file.
2. Click **"+ Add Another File"** and attach each required log file.
3. Verify each file shows a non-zero size before clicking **Submit Assignment**.
4. If Canvas shows `Attached files must be greater than 0 bytes`, no file was selected—repeat steps 1–3.

<!-- section_id: "7ffcdf66-92c1-433a-8ecd-2f5cc8d9b4c1" -->
## Regenerating Logs Legitimately
- If the baseline (original) log is missing, check out the original code (`git checkout -- assignmentXX.py`), run it, and let the `Log` class create the file automatically. Then restore your working version (`git checkout -`).
- If the optimized log is missing, re-run the optimized code.
- Do **not** edit timestamps or contents manually. Re-running is the only allowed fix.

<!-- section_id: "d1999df4-0b33-487d-a572-b19a773c1781" -->
## Maintaining Log Integrity
- Keep the `logs/` folder limited to auto-generated files. Delete any hand-written logs.
- If logs appear gray in the IDE, it is because `logs/` is ignored by `.gitignore`; this is expected and does not prevent submission.
- If the original run happens after the optimized run, add a note in your submission explaining the order (e.g., “Reverted to the baseline via git to capture an accurate comparison”).

<!-- section_id: "1907797c-a9e5-4529-a714-63c3e40bdc54" -->
## Troubleshooting Upload Issues
- Large folders such as `faces/` and `step3_edges/` are kept out of git by design; you still submit the compiled results when Canvas requires them.
- Ensure each required file is attached once; duplicate uploads or missing attachments are common causes of Canvas errors.
- If Canvas continues to reject files, refresh the page and reattach the files one at a time.
