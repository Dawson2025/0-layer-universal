#!/usr/bin/env python3
# resource_id: "5541cd75-ba4b-45cc-800e-0a5ca7ce67ad"
# resource_type: "document"
# resource_name: "run_user_stories"
"""
# 🧪 MAIN TESTING SYSTEM: Tests ALL 71 user stories across 18 categories
# Always run with --navigation-mode=both for complete coverage

Parallel runner for MCP-based user story scripts.

Reads a JSON plan describing story commands, launches a dedicated Playwright MCP
server per task, sets MCP_URL automatically, and captures logs/artifacts.
"""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import json
import os
import signal
import sys
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_PORT_BASE = 3334
DEFAULT_CONCURRENCY = 2


def prepare_story_specs(plan: List[Dict[str, Any]], navigation_mode: str) -> List[Dict[str, Any]]:
    prepared: List[Dict[str, Any]] = []

    for raw_spec in plan:
        spec = dict(raw_spec)  # shallow copy
        base_id = spec.get("id", "")
        nav_map = spec.get("navigation")

        if isinstance(nav_map, dict):
            available = {mode: cmd for mode, cmd in nav_map.items() if cmd}
            if not available:
                continue

            if navigation_mode == "both":
                target_modes = sorted(available.keys())
            else:
                if navigation_mode not in available:
                    continue
                target_modes = [navigation_mode]

            for mode_name in target_modes:
                command = available.get(mode_name)
                if not command:
                    continue
                derived = {k: v for k, v in spec.items() if k != "navigation"}
                derived["command"] = command
                derived["navigation_mode"] = mode_name
                if base_id:
                    derived["id"] = f"{base_id}-{mode_name}"
                prepared.append(derived)
        else:
            if navigation_mode == "realistic":
                continue
            derived = dict(spec)
            derived["navigation_mode"] = spec.get("navigation_mode", "direct")
            prepared.append(derived)

    return prepared


class StoryTask:
    def __init__(self, idx: int, spec: Dict[str, Any], port: int, artifacts: Path) -> None:
        self.idx = idx
        self.spec = spec
        self.port = port
        self.navigation_mode = spec.get("navigation_mode", "direct")
        self.id = spec.get("id") or f"story-{idx:03d}"
        self.command = spec.get("command")
        if not self.command:
            raise ValueError(f"Story {self.id} missing 'command'")
        self.env_overrides = dict(spec.get("env", {}))
        self.env_overrides.setdefault("RUN_NAVIGATION_MODE", self.navigation_mode)
        self.artifacts_dir = artifacts / self.id
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        self.mcp_log = self.artifacts_dir / "mcp.log"
        self.story_log = self.artifacts_dir / "story.log"
        self.result_path = self.artifacts_dir / "result.json"
        self.sequential = bool(spec.get("sequential"))
        self.disable_mcp = bool(spec.get("disable_mcp"))


async def wait_for_port(port: int, host: str = "127.0.0.1", retries: int = 30, delay: float = 0.2) -> None:
    for attempt in range(retries):
        try:
            reader, writer = await asyncio.open_connection(host, port)
            writer.close()
            await writer.wait_closed()
            return
        except Exception:
            await asyncio.sleep(delay)
    raise RuntimeError(f"Timed out waiting for MCP server on {host}:{port}")


async def launch_mcp_server(task: StoryTask) -> asyncio.subprocess.Process | None:
    if task.disable_mcp:
        return None
    cmd = [
        "npx",
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chromium",
        "--port",
        str(task.port),
        "--isolated",
    ]
    log_handle = task.mcp_log.open("w")
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=log_handle,
        stderr=asyncio.subprocess.STDOUT,
    )
    setattr(proc, "_log_handle", log_handle)
    await wait_for_port(task.port)
    return proc


@contextlib.asynccontextmanager
async def maybe_acquire(semaphore: asyncio.Semaphore | None):
    if semaphore is None:
        yield
    else:
        async with semaphore:
            yield


async def run_story(task: StoryTask, semaphore: asyncio.Semaphore | None) -> Dict[str, Any]:
    async with maybe_acquire(semaphore):

        result: Dict[str, Any] = {
            "id": task.id,
            "status": "pending",
            "port": task.port,
            "command": task.command,
            "artifacts": str(task.artifacts_dir),
            "navigation_mode": task.navigation_mode,
        }

        mcp_proc = None
        story_proc = None
        try:
            mcp_proc = await launch_mcp_server(task)
            env = os.environ.copy()
            env.update(task.env_overrides)
            if not task.disable_mcp:
                env["MCP_URL"] = f"http://localhost:{task.port}/mcp"
                env["MCP_SERVER_PORT"] = str(task.port)

            story_log_handle = task.story_log.open("w")
            try:
                story_proc = await asyncio.create_subprocess_exec(
                    *task.command,
                    cwd=os.environ.get("PROJECT_CWD") or str(Path(__file__).resolve().parents[2]),
                    env=env,
                    stdout=story_log_handle,
                    stderr=asyncio.subprocess.STDOUT,
                )
                exit_code = await story_proc.wait()
            finally:
                story_log_handle.close()
            result["exit_code"] = exit_code
            result["status"] = "passed" if exit_code == 0 else "failed"
        except Exception as exc:
            result["status"] = "error"
            result["error"] = str(exc)
        finally:
            if story_proc and story_proc.returncode is None:
                story_proc.terminate()
                with contextlib.suppress(ProcessLookupError):
                    await story_proc.wait()
            if mcp_proc:
                if mcp_proc.returncode is None:
                    mcp_proc.send_signal(signal.SIGTERM)
                    try:
                        await asyncio.wait_for(mcp_proc.wait(), timeout=5)
                    except asyncio.TimeoutError:
                        mcp_proc.kill()
                        await mcp_proc.wait()
                log_handle = getattr(mcp_proc, "_log_handle", None)
                if log_handle:
                    log_handle.close()
            with task.result_path.open("w") as fp:
                json.dump(result, fp, indent=2)
        return result


async def main_async(args: argparse.Namespace) -> int:
    plan_path = Path(args.plan).resolve()
    if not plan_path.exists():
        print(f"Plan file not found: {plan_path}", file=sys.stderr)
        return 1

    plan: List[Dict[str, Any]] = json.loads(plan_path.read_text())
    if not isinstance(plan, list):
        print("Plan file must contain a JSON list of story definitions", file=sys.stderr)
        return 1

    expanded_plan = prepare_story_specs(plan, args.navigation_mode)
    if not expanded_plan:
        print("No stories match the requested navigation mode.", file=sys.stderr)
        return 1

    artifacts_dir = Path(args.artifacts).resolve()
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    semaphore = asyncio.Semaphore(args.concurrency)
    tasks = []
    sequential_tasks = []
    for idx, spec in enumerate(expanded_plan):
        port = args.port_base + idx
        story = StoryTask(idx, spec, port, artifacts_dir)
        if story.sequential:
            sequential_tasks.append(story)
        else:
            tasks.append(run_story(story, semaphore))

    results = []
    if tasks:
        results.extend(await asyncio.gather(*tasks, return_exceptions=False))

    for story in sequential_tasks:
        results.append(await run_story(story, None))

    failures = [r for r in results if r["status"] != "passed"]
    summary = {
        "total": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "results": results,
        "navigation_mode": args.navigation_mode,
    }
    summary_path = artifacts_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))

    print(json.dumps(summary, indent=2))
    return 0 if not failures else 2


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run user story scripts in parallel via MCP.")
    parser.add_argument(
        "--plan",
        default="scripts/automation/story_plan.sample.json",
        help="Path to JSON plan file (default: %(default)s)",
    )
    parser.add_argument(
        "--artifacts",
        default="artifacts/story_runs",
        help="Directory to store logs/results (default: %(default)s)",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help="Maximum concurrent stories (default: %(default)s)",
    )
    parser.add_argument(
        "--port-base",
        type=int,
        default=DEFAULT_PORT_BASE,
        help="Base TCP port for MCP servers (default: %(default)s)",
    )
    parser.add_argument(
        "--navigation-mode",
        choices=["direct", "realistic", "both"],
        default="direct",
        help="Select which navigation variants to run (default: %(default)s)",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        return asyncio.run(main_async(args))
    except KeyboardInterrupt:
        print("Interrupted by user", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
