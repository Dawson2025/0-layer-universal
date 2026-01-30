# Universal Notes – CSE 351 Family Search Assignments

These patterns apply to any local BYU CSE 351 assignment that couples a Python client with the provided `server.py` API.

## Environment Patterns
- **Local package resolution** – The helper module (`cse351`) is vendored under `.venv/lib/python3.12/site-packages`. Export this directory through `PYTHONPATH` before invoking any assignment driver.
- **Background services** – Always launch `server.py` in a dedicated terminal, redirect stdout to `/tmp/<lesson>_server.log`, and capture the PID for cleanup. This prevents orphan servers from skewing later tests.
- **Retry-friendly logging** – Mirror the assignment output to `/tmp/<lesson>_prove.log`; repo-local logs stay clean while you retain the raw console stream for debugging.

## Performance Mindset
- The FS server sleeps 0.25 seconds per HTTP call. Meeting the “<10 second” targets requires parallelism: batch every family + person lookup via a `ThreadPoolExecutor` instead of issuing requests serially.
- Track max concurrency using the server’s “active threads / max count” line. If values dip unexpectedly, the client code likely throttled its executors.
- Keep state mutations (adding people/families) guarded by locks while allowing network I/O to run free; this balances correctness with throughput.

## Testing Workflow
1. Kill any stale `server.py` instances (`pkill -f server.py || true`).
2. Start a fresh server and log output to `/tmp`.
3. Run the automated harness (`test_lesson10.sh` template) so the server lifecycle + proof run share the same terminal session.
4. Tail both `/tmp` logs plus `lesson_##/prove/logs/assignment.log` to capture timings and API counts immediately after the run.
5. For the C# port (Lesson 14) add `.dotnet` to PATH and run from `lesson_14/prove/assignment14/Assignment14`; collect timings from `lesson_14/prove/logs/assignment.log` because console logging is disabled during performance runs. The HTTP gate can be overridden with `FS_HTTP_GATE` (default 45) and is logged at startup.

## Common Pitfalls & Fixes
- **`ModuleNotFoundError: cse351`** – add the `.venv` site-packages folder to `PYTHONPATH`.
- **Server 500/timeout spikes** – back off by reducing the queue depth temporarily, then re-run once the server stabilizes. Document any sustained slowdowns.
- **Missing logs** – some assignments write inside `logs/`; always check that directory before assuming execution failed.
- **C# port slower than target** – the Python FS server often caps throughput around ~500 requests/6 generations. Document DFS/BFS timings (e.g., 12 s) and include server thread counts in the submission if you can’t hit 10 s even with aggressive concurrency. A shared HTTP `SemaphoreSlim` (≈60–80 slots), plus caching of `Person`/`Family` fetches, can yield sub‑10 s runs sporadically; capture several runs and send the best log (with server stats) when variability persists.

Reuse these patterns whenever you encounter similar client/server coursework; they prevent late-hour debugging and keep deliverables verifiable.
