---
resource_id: "e2ca5a6c-3c4c-41f1-a1e7-990d012aef67"
resource_type: "document"
resource_name: "canvas_submission_protocol"
---
# Canvas Submission Protocol for Programming Assignments

<!-- section_id: "8559f663-d131-4920-a744-fa49e8718da1" -->
## Purpose
Ensure every submission to Canvas includes the correct auto-generated evidence files and avoids common upload errors.

<!-- section_id: "ddbb8d2a-41d4-40bb-b775-e62ce04c2dd3" -->
## Required Files
1. Assignment source file (for example `assignment06.py`).
2. Auto-generated log files from the `Log` class (for example `1101-184337.log`, `1101-182543.log`).
   - **Only submit logs that were created by running the program.**
   - Never hand-edit or rewrite log contents; re-run the program instead.
   - Keep the original filenames so timestamps remain trustworthy.

<!-- section_id: "025688c6-a7ed-4ce2-bc86-42eb0021293f" -->
## Upload Steps in Canvas
1. Click **"Choose a file to upload"** and attach the code file.
2. Click **"+ Add Another File"** and attach each required log file.
3. Verify each file shows a non-zero size before clicking **Submit Assignment**.
4. If Canvas shows `Attached files must be greater than 0 bytes`, no file was selected—repeat steps 1–3.

<!-- section_id: "e4fbb855-ad37-4ca2-92fe-139bf5a0dd08" -->
## Regenerating Logs Legitimately
- If the baseline (original) log is missing, check out the original code (`git checkout -- assignmentXX.py`), run it, and let the `Log` class create the file automatically. Then restore your working version (`git checkout -`).
- If the optimized log is missing, re-run the optimized code.
- Do **not** edit timestamps or contents manually. Re-running is the only allowed fix.

<!-- section_id: "d86b5f78-e613-41c1-bd59-e36feae0d379" -->
## Maintaining Log Integrity
- Keep the `logs/` folder limited to auto-generated files. Delete any hand-written logs.
- If logs appear gray in the IDE, it is because `logs/` is ignored by `.gitignore`; this is expected and does not prevent submission.
- If the original run happens after the optimized run, add a note in your submission explaining the order (e.g., “Reverted to the baseline via git to capture an accurate comparison”).

<!-- section_id: "00efbd51-6285-4544-88ea-1245b51d6ca1" -->
## Troubleshooting Upload Issues
- Large folders such as `faces/` and `step3_edges/` are kept out of git by design; you still submit the compiled results when Canvas requires them.
- Ensure each required file is attached once; duplicate uploads or missing attachments are common causes of Canvas errors.
- If Canvas continues to reject files, refresh the page and reattach the files one at a time.
