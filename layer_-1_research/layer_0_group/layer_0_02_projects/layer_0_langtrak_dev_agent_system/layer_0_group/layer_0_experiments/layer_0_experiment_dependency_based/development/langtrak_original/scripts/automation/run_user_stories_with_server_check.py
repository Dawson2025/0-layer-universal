#!/usr/bin/env python3
# resource_id: "e8ede493-eff8-4004-83a9-2440511892bc"
# resource_type: "document"
# resource_name: "run_user_stories_with_server_check"
"""
# 🧪 IMPROVED TESTING SYSTEM: Tests ALL 71 user stories across 18 categories
# WITH SERVER CONNECTIVITY VERIFICATION
# Always run with --navigation-mode=both for complete coverage

Parallel runner for MCP-based user story scripts with server connectivity checks.

Reads a JSON plan describing story commands, verifies server connectivity,
launches a dedicated Playwright MCP server per task, sets MCP_URL automatically, 
and captures logs/artifacts.
"""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import json
import os
import signal
import sys
import time
import socket
import requests
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_PORT_BASE = 3334
DEFAULT_CONCURRENCY = 2
DEFAULT_SERVER_URL = os.environ.get("APP_BASE_URL", "http://127.0.0.1:5000")
DEFAULT_TIMEOUT = 30


def find_free_port(start_port: int, used: set[int], host: str = "127.0.0.1") -> int:
    """
    Find an available TCP port at/above start_port that is not already reserved in `used`.
    Uses a bind test to avoid races with already-running servers.
    """
    port = start_port
    while True:
        if port in used:
            port += 1
            continue
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
            except OSError:
                port += 1
                continue
        used.add(port)
        return port


def check_server_connectivity(server_url: str = DEFAULT_SERVER_URL, timeout: int = DEFAULT_TIMEOUT) -> bool:
    """
    Check if the development server is running and accessible.
    
    Args:
        server_url: URL of the server to check
        timeout: Timeout in seconds for the request
        
    Returns:
        True if server is accessible, False otherwise
    """
    try:
        print(f"🔍 Checking server connectivity to {server_url}...")
        response = requests.get(f"{server_url}/login", timeout=timeout)
        if response.status_code in [200, 302]:  # 200 for success, 302 for redirect
            print(f"✅ Server is accessible (status: {response.status_code})")
            return True
        else:
            print(f"❌ Server returned unexpected status: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection refused - server is not running at {server_url}")
        return False
    except requests.exceptions.Timeout:
        print(f"❌ Connection timeout after {timeout} seconds")
        return False
    except Exception as e:
        print(f"❌ Unexpected error checking server: {e}")
        return False


def wait_for_server(server_url: str = DEFAULT_SERVER_URL, max_attempts: int = 10, delay: int = 5) -> bool:
    """
    Wait for the server to become available.
    
    Args:
        server_url: URL of the server to check
        max_attempts: Maximum number of attempts
        delay: Delay between attempts in seconds
        
    Returns:
        True if server becomes available, False otherwise
    """
    print(f"⏳ Waiting for server to become available at {server_url}...")
    
    for attempt in range(1, max_attempts + 1):
        print(f"   Attempt {attempt}/{max_attempts}...")
        
        if check_server_connectivity(server_url, timeout=5):
            print(f"✅ Server is now available after {attempt} attempts")
            return True
        
        if attempt < max_attempts:
            print(f"   Waiting {delay} seconds before next attempt...")
            time.sleep(delay)
    
    print(f"❌ Server did not become available after {max_attempts} attempts")
    return False


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

                prepared_spec = dict(spec)
                prepared_spec["id"] = f"{base_id}-{mode_name}"
                prepared_spec["command"] = command
                prepared_spec["navigation_mode"] = mode_name
                prepared_spec["sequential"] = spec.get("sequential", False)
                prepared.append(prepared_spec)

    return prepared


class StoryTask:
    def __init__(self, idx: int, spec: Dict[str, Any], port: int, artifacts_dir: Path, headed: bool = False, mcp_start_timeout: float = 0):
        self.idx = idx
        self.spec = spec
        self.port = port
        self.artifacts_dir = artifacts_dir
        self.story_id = spec["id"]
        self.command = spec["command"]
        self.navigation_mode = spec.get("navigation_mode", "unknown")
        self.sequential = spec.get("sequential", False)
        self.disable_mcp = spec.get("disable_mcp", False)
        self.env_overrides = spec.get("env", {})
        self.headed = headed
        self.mcp_start_timeout = mcp_start_timeout

        # Create story-specific directories
        self.story_dir = artifacts_dir / self.story_id
        self.story_dir.mkdir(parents=True, exist_ok=True)
        
        # Artifact paths
        self.story_log = self.story_dir / "story.log"
        self.result_path = self.story_dir / "result.json"
        self.mcp_log = self.story_dir / "mcp.log"
        self.traces_dir = self.story_dir / "traces"
        self.screenshots_dir = self.story_dir / "screenshots"
        self.videos_dir = self.story_dir / "videos"
        
        # Create artifact subdirectories
        self.traces_dir.mkdir(exist_ok=True)
        self.screenshots_dir.mkdir(exist_ok=True)
        self.videos_dir.mkdir(exist_ok=True)

async def wait_for_tcp_listen(host: str, port: int, timeout: float = 10.0) -> bool:
    """Wait until a TCP port is accepting connections."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.25)
            try:
                sock.connect((host, port))
                return True
            except OSError:
                pass
        await asyncio.sleep(0.25)
    return False


async def launch_mcp_server(task: StoryTask):
    """Launch MCP server for the task."""
    if task.disable_mcp:
        return None

    mcp_log_handle = task.mcp_log.open("w")
    args = ["bash", "scripts/mcp-start.sh"]
    if task.headed:
        args.append("--headed")
    args.extend(["--port", str(task.port)])
    mcp_proc = await asyncio.create_subprocess_exec(
        *args,
        cwd=os.environ.get("PROJECT_CWD") or str(Path(__file__).resolve().parents[2]),
        stdout=mcp_log_handle,
        stderr=asyncio.subprocess.STDOUT,
        start_new_session=True,
    )
    mcp_proc._log_handle = mcp_log_handle

    # Wait for MCP server to start accepting connections.
    if task.mcp_start_timeout > 0:
        startup_timeout = task.mcp_start_timeout
    else:
        # Headed mode can take longer (browser launch + WSL UI startup), so allow extra time.
        startup_timeout = 120.0 if task.headed else 60.0
        
    ready = await wait_for_tcp_listen("127.0.0.1", task.port, timeout=startup_timeout)
    if not ready:
        with contextlib.suppress(ProcessLookupError):
            os.killpg(mcp_proc.pid, signal.SIGTERM)
        with contextlib.suppress(asyncio.TimeoutError, ProcessLookupError):
            await asyncio.wait_for(mcp_proc.wait(), timeout=5)
        if mcp_proc.returncode is None:
            with contextlib.suppress(ProcessLookupError):
                os.killpg(mcp_proc.pid, signal.SIGKILL)
            with contextlib.suppress(ProcessLookupError):
                await mcp_proc.wait()
        mcp_log_handle.close()
        raise RuntimeError(f"MCP server did not start listening on 127.0.0.1:{task.port}")
    return mcp_proc


async def run_story(task: StoryTask, semaphore: asyncio.Semaphore | None, stagger: float = 0.0) -> Dict[str, Any]:
    """Run a single story task."""
    if stagger > 0 and semaphore:
        # Stagger start times to avoid thundering herd on MCP startup
        await asyncio.sleep(task.idx * stagger)
        
    if semaphore:
        async with semaphore:
            return await _run_story_impl(task)
    else:
        return await _run_story_impl(task)


async def _run_story_impl(task: StoryTask) -> Dict[str, Any]:
    """Implementation of story execution."""
    result = {
        "story_id": task.story_id,
        "navigation_mode": task.navigation_mode,
        "status": "pending",
        "start_time": time.time(),
        "failure_category": None,  # For better error classification
        "artifacts": {
            "logs": str(task.story_log.relative_to(task.artifacts_dir.parent)),
            "mcp_log": str(task.mcp_log.relative_to(task.artifacts_dir.parent)),
            "traces": str(task.traces_dir.relative_to(task.artifacts_dir.parent)),
            "screenshots": str(task.screenshots_dir.relative_to(task.artifacts_dir.parent)),
            "videos": str(task.videos_dir.relative_to(task.artifacts_dir.parent)),
        }
    }
    
    mcp_proc = None
    story_proc = None
    
    try:
        print(f"🚀 Starting story: {task.story_id} ({task.navigation_mode})")
        
        # Launch MCP server
        try:
            mcp_proc = await launch_mcp_server(task)
        except RuntimeError as exc:
            result["status"] = "error"
            result["failure_category"] = "mcp_bootstrap_failure"
            result["error"] = str(exc)
            print(f"❌ MCP bootstrap failed for {task.story_id}: {exc}")
            return result
        
        # Set up environment for story script
        env = os.environ.copy()
        env.update(task.env_overrides)
        if not task.disable_mcp:
            env["MCP_URL"] = f"http://127.0.0.1:{task.port}/mcp"
            env["MCP_SERVER_PORT"] = str(task.port)
        
        # Enable Playwright trace/video/screenshot collection
        env["PLAYWRIGHT_TRACE_DIR"] = str(task.traces_dir)
        env["PLAYWRIGHT_SCREENSHOTS_DIR"] = str(task.screenshots_dir)
        env["PLAYWRIGHT_VIDEOS_DIR"] = str(task.videos_dir)

        # Run the story script
        story_log_handle = task.story_log.open("w")
        try:
            story_proc = await asyncio.create_subprocess_exec(
                *task.command,
                cwd=os.environ.get("PROJECT_CWD") or str(Path(__file__).resolve().parents[2]),
                env=env,
                stdout=story_log_handle,
                stderr=asyncio.subprocess.STDOUT,
                start_new_session=True,
            )
            exit_code = await story_proc.wait()
        finally:
            story_log_handle.close()
        
        result["exit_code"] = exit_code
        
        # Categorize failure if test didn't pass
        if exit_code != 0:
            result["status"] = "failed"
            # Analyze log to categorize failure
            log_content = task.story_log.read_text()
            if "ERR_CONNECTION_REFUSED" in log_content or "ECONNREFUSED" in log_content:
                result["failure_category"] = "server_not_running"
            elif "timeout" in log_content.lower() or "timed out" in log_content.lower():
                result["failure_category"] = "timeout"
            else:
                result["failure_category"] = "test_failure"
        else:
            result["status"] = "passed"
        
        status_emoji = "✅" if result["status"] == "passed" else "❌"
        print(f"{status_emoji} Completed story: {task.story_id} (status: {result['status']}, category: {result.get('failure_category', 'N/A')})")
        
    except Exception as exc:
        result["status"] = "error"
        result["failure_category"] = "unknown_error"
        result["error"] = str(exc)
        print(f"❌ Unexpected error in story: {task.story_id} - {exc}")
    finally:
        if story_proc and story_proc.returncode is None:
            with contextlib.suppress(ProcessLookupError):
                os.killpg(story_proc.pid, signal.SIGTERM)
            with contextlib.suppress(asyncio.TimeoutError, ProcessLookupError):
                await asyncio.wait_for(story_proc.wait(), timeout=5)
            if story_proc.returncode is None:
                with contextlib.suppress(ProcessLookupError):
                    os.killpg(story_proc.pid, signal.SIGKILL)
                with contextlib.suppress(ProcessLookupError):
                    await story_proc.wait()
        if mcp_proc:
            if mcp_proc.returncode is None:
                with contextlib.suppress(ProcessLookupError):
                    os.killpg(mcp_proc.pid, signal.SIGTERM)
                try:
                    await asyncio.wait_for(mcp_proc.wait(), timeout=5)
                except asyncio.TimeoutError:
                    with contextlib.suppress(ProcessLookupError):
                        os.killpg(mcp_proc.pid, signal.SIGKILL)
                    await mcp_proc.wait()
            log_handle = getattr(mcp_proc, "_log_handle", None)
            if log_handle:
                log_handle.close()
        with task.result_path.open("w") as fp:
            json.dump(result, fp, indent=2)
    return result


async def main_async(args: argparse.Namespace) -> int:
    """Main async function with server connectivity check."""
    # Check server connectivity first
    if not check_server_connectivity(args.server_url, args.timeout):
        print(f"\n❌ Server is not accessible at {args.server_url}")
        print("💡 Please ensure the development server is running:")
        print("   python3 scripts/terminal_wrapper.py --script scripts/start_dev.sh")
        print("\n🔄 Attempting to wait for server...")
        
        if not wait_for_server(args.server_url, args.max_attempts, args.delay):
            print("\n❌ Cannot proceed without server connectivity")
            return 1
    
    print(f"\n✅ Server connectivity verified - proceeding with user story tests")
    
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

    print(f"📋 Running {len(expanded_plan)} user story tests...")

    artifacts_dir = Path(args.artifacts).resolve()
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    semaphore = asyncio.Semaphore(args.concurrency)
    tasks = []
    sequential_tasks = []
    used_ports: set[int] = set()
    for idx, spec in enumerate(expanded_plan):
        port = find_free_port(args.port_base + idx, used_ports)
        story = StoryTask(idx, spec, port, artifacts_dir, headed=args.headed, mcp_start_timeout=args.mcp_start_timeout)
        if story.sequential:
            sequential_tasks.append(story)
        else:
            tasks.append(run_story(story, semaphore, stagger=args.stagger))

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
        "server_url": args.server_url,
        "server_connectivity_verified": True,
    }
    summary_path = artifacts_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))

    print(f"\n📊 Test Results Summary:")
    print(f"   Total: {summary['total']}")
    print(f"   Passed: {summary['passed']}")
    print(f"   Failed: {summary['failed']}")
    print(f"   Success Rate: {(summary['passed'] / summary['total'] * 100):.1f}%")

    return 0 if not failures else 2


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run user story scripts in parallel via MCP with server connectivity checks.",
        epilog="""
Examples:
  # Run smoke tests (PR-blocking subset)
  %(prog)s --plan scripts/automation/story_plan_smoke.json
  
  # Run full suite (nightly)
  %(prog)s --plan scripts/automation/story_plan_full.json
  
  # Run with headed browser for debugging
  %(prog)s --plan scripts/automation/story_plan_smoke.json --headed
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--plan",
        default="scripts/automation/story_plan_full.json",
        help="Path to JSON plan file (smoke: 5 critical stories, full: all 18 categories)",
    )
    parser.add_argument(
        "--artifacts",
        default="artifacts/story_runs/current-run",
        help="Directory for test artifacts",
    )
    parser.add_argument(
        "--navigation-mode",
        choices=["direct", "realistic", "both"],
        default="both",
        help="Navigation mode to test",
    )
    parser.add_argument(
        "--headed",
        action="store_true",
        help="Run Playwright MCP in headed mode (visible browser windows).",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help="Maximum concurrent tasks",
    )
    parser.add_argument(
        "--port-base",
        type=int,
        default=DEFAULT_PORT_BASE,
        help="Base port for MCP servers",
    )
    parser.add_argument(
        "--server-url",
        default=DEFAULT_SERVER_URL,
        help="URL of the development server to check",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help="Timeout for server connectivity check",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=10,
        help="Maximum attempts to wait for server",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=5,
        help="Delay between server connectivity attempts",
    )
    parser.add_argument(
        "--mcp-start-timeout",
        type=float,
        default=0,
        help="Timeout in seconds for MCP server startup (0 = auto: 60s headless, 120s headed)",
    )
    parser.add_argument(
        "--stagger",
        type=float,
        default=0.0,
        help="Delay in seconds between starting parallel tasks to reduce CPU load spikes",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    args = parse_args(argv)
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    sys.exit(main())
