# Context Update Rule

Every AI agent session must keep the knowledge bases in sync:

1. **Project context (`/home/dawson/code/Parallelism and Concurrency/0_context`)** – capture assignment-specific observations, SOPs, and optimizations so the next run inside the same repo inherits the latest state.
2. **Universal context (`/home/dawson/code/0_ai_context`)** – extract any broadly applicable lessons (tooling quirks, workflow rules, environment gotchas) and document them in the appropriate universal section.

### Performance Anchor Policy (applies to all projects)
- Track the “best-performing” commit and its metric snapshot (e.g., run_history_best_*.json) as the **anchor**. Record the commit hash and artifact path in both project and universal contexts.
- Run new experiments off the anchor. If a later milestone beats the anchor’s primary metric (e.g., % of runs meeting the SLA), promote that milestone’s commit to become the new anchor and document the change.
- For submission/hand-off, check out the anchor commit and use its validated artifacts (logs/run histories). Experiments stay on top of a branch; the anchor remains the known-good baseline.

Do not close out a task until both locations reflect the new findings. Reference the updated files in your final response so future chats know where to look.
