#!/usr/bin/env python3
# resource_id: "b5766701-8474-4083-97b2-86ba3c648c52"
# resource_type: "knowledge"
# resource_name: "mcp_concurrent_browser"
"""
MCP Concurrent Browser Manager

Enables concurrent Playwright MCP browser instances for multiple AI tools
across different operating systems by creating OS-specific and tool-specific
isolated browser configurations.

Key Features:
- OS-aware configuration (WSL, Linux, macOS, Windows)
- Creates separate Playwright MCP config files per OS + AI tool combination
- Assigns unique browser profile directories (isolated: true)
- Generates tool-specific and OS-specific launch configurations
- Enables simultaneous browser use across different AI CLI tools

Configuration naming: {os}_{tool}
Examples: wsl_codex, wsl_claude, linux_gemini, windows_cursor

Usage:
    # Set up concurrent browser configs for all tools on current OS
    python3 mcp_concurrent_browser.py setup

    # Set up for specific tools only
    python3 mcp_concurrent_browser.py setup --tools codex claude

    # Set up for specific OS
    python3 mcp_concurrent_browser.py setup --os wsl

    # Update Codex CLI config to use OS+tool-specific Playwright config
    python3 mcp_concurrent_browser.py apply-codex

    # Show current configuration status
    python3 mcp_concurrent_browser.py status
"""

from __future__ import annotations

import argparse
import json
import os
import platform
from pathlib import Path
from typing import Dict, List, Optional, Tuple


HOME = Path.home()
CACHE_DIR = HOME / ".cache/ms-playwright"
MCP_CONFIG_DIR = HOME / ".config/mcp"

# Operating system detection and mapping
OS_NAMES = {
    "wsl": "WSL",
    "linux": "Linux",
    "macos": "macOS",
    "windows": "Windows",
}


def detect_os() -> str:
    """
    Detect the current operating system.
    Returns: wsl, linux, macos, or windows
    """
    system = platform.system().lower()

    # Check for WSL
    if system == "linux":
        try:
            with open("/proc/version", "r") as f:
                version_info = f.read().lower()
                if "microsoft" in version_info or "wsl" in version_info:
                    return "wsl"
        except FileNotFoundError:
            pass
        return "linux"

    if system == "darwin":
        return "macos"

    if system == "windows":
        return "windows"

    # Default fallback
    return "linux"


# AI tool configurations (base paths, OS-specific paths added dynamically)
AI_TOOLS = {
    "codex": {
        "name": "Codex CLI",
        "config_dir": HOME / ".codex",
    },
    "claude": {
        "name": "Claude Code CLI",
        "config_dir": MCP_CONFIG_DIR,
    },
    "gemini": {
        "name": "Gemini CLI",
        "config_dir": HOME / ".gemini",
    },
    "cursor": {
        "name": "Cursor Agent",
        "config_dir": MCP_CONFIG_DIR,
    },
}


def get_os_tool_config(os_name: str, tool_id: str) -> Dict:
    """
    Get OS-specific and tool-specific configuration.

    Args:
        os_name: Operating system (wsl, linux, macos, windows)
        tool_id: Tool identifier (codex, claude, gemini, cursor)

    Returns:
        Dictionary with config_file and profile_dir paths
    """
    base_tool = AI_TOOLS[tool_id]
    config_name = f"playwright.{os_name}_{tool_id}.json"
    profile_name = f"mcp-chromium-{os_name}-{tool_id}"

    return {
        "name": base_tool["name"],
        "config_dir": base_tool["config_dir"],
        "config_file": config_name,
        "profile_dir": CACHE_DIR / profile_name,
        "os": os_name,
        "tool": tool_id,
    }


def detect_wslg() -> bool:
    """Detect if running in WSLg environment."""
    wslg_runtime_dir = Path("/mnt/wslg/runtime-dir")
    return Path("/mnt/wslg").exists() and wslg_runtime_dir.exists()


def detect_chromium_executable() -> Optional[str]:
    """
    Find the newest Chromium executable in ms-playwright cache.
    Returns None if not found.
    """
    if not CACHE_DIR.exists():
        return None

    candidates: List[Tuple[int, Path]] = []
    for d in CACHE_DIR.glob("chromium-*"):
        # Skip headless shell variants
        if d.name.startswith("chromium_headless_shell"):
            continue

        chrome = d / "chrome-linux64" / "chrome"
        if not chrome.exists():
            # Try Windows path
            chrome = d / "chrome-win" / "chrome.exe"
            if not chrome.exists():
                # Try macOS path
                chrome = d / "chrome-mac" / "Chromium.app" / "Contents" / "MacOS" / "Chromium"
                if not chrome.exists():
                    continue

        try:
            ver = int(d.name.split("-")[-1])
        except Exception:
            ver = -1

        candidates.append((ver, chrome))

    if not candidates:
        return None

    candidates.sort(reverse=True, key=lambda x: x[0])
    return str(candidates[0][1])


def get_os_specific_launch_args(os_name: str, headless: bool) -> List[str]:
    """
    Get OS-specific Chromium launch arguments.

    Args:
        os_name: Operating system (wsl, linux, macos, windows)
        headless: Whether running in headless mode

    Returns:
        List of Chromium launch arguments
    """
    args: List[str] = []

    # WSL-specific: Force Wayland/Ozone for headed browser stability
    if os_name == "wsl" and not headless:
        if detect_wslg():
            args += [
                "--ozone-platform=wayland",
                "--enable-features=UseOzonePlatform"
            ]

    # Linux-specific args (if needed)
    elif os_name == "linux" and not headless:
        # Add Linux-specific args here if needed
        pass

    # macOS-specific args (if needed)
    elif os_name == "macos":
        # Add macOS-specific args here if needed
        pass

    # Windows-specific args (if needed)
    elif os_name == "windows":
        # Add Windows-specific args here if needed
        pass

    return args


def create_playwright_config(
    os_name: str,
    tool_id: str,
    config_path: Path,
    *,
    headless: bool = False,
) -> None:
    """
    Create an OS-specific and tool-specific Playwright MCP config file.

    Args:
        os_name: Operating system (wsl, linux, macos, windows)
        tool_id: Tool identifier (codex, claude, gemini, cursor)
        config_path: Path where config JSON should be written
        headless: Whether to run in headless mode (default: False)
    """
    chromium_exec = detect_chromium_executable()
    chromium_args = get_os_specific_launch_args(os_name, headless)

    # Prepare launch options
    launch_options: Dict = {
        "headless": headless,
    }

    if chromium_exec:
        launch_options["executablePath"] = chromium_exec

    if chromium_args:
        launch_options["args"] = chromium_args

    # Create config structure
    config = {
        "browser": {
            "browserName": "chromium",
            "isolated": True,  # Critical: enables concurrent instances
            "launchOptions": launch_options,
        },
        "_metadata": {
            "os": os_name,
            "tool": tool_id,
            "config_name": f"{os_name}_{tool_id}",
        }
    }

    # Write config file
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(config, indent=2) + "\n")

    print(f"   ✅ Created config: {config_path}")


def setup_concurrent_configs(
    os_name: str,
    tool_ids: List[str],
    headless: bool = False
) -> None:
    """
    Set up concurrent browser configurations for specified OS and AI tools.

    Args:
        os_name: Operating system (wsl, linux, macos, windows)
        tool_ids: List of tool IDs to set up (e.g., ['codex', 'claude'])
        headless: Whether to configure headless mode
    """
    print(f"🔧 Setting up concurrent Playwright MCP browser configurations...")
    print(f"   OS: {OS_NAMES[os_name]}")
    print(f"   Tools: {', '.join([AI_TOOLS[tid]['name'] for tid in tool_ids])}")
    print(f"   Headless: {headless}")

    if os_name == "wsl":
        print(f"   WSLg detected: {detect_wslg()}")

    print()

    for tool_id in tool_ids:
        tool_config = get_os_tool_config(os_name, tool_id)
        config_path = tool_config["config_dir"] / tool_config["config_file"]

        print(f"📦 {tool_config['name']} ({os_name}_{tool_id})")
        print(f"   Config file: {config_path}")
        print(f"   Profile dir: {tool_config['profile_dir']}")

        # Create the config
        create_playwright_config(os_name, tool_id, config_path, headless=headless)

        # Create profile directory
        tool_config["profile_dir"].mkdir(parents=True, exist_ok=True)
        print(f"   ✅ Created profile directory")
        print()


def update_codex_config(os_name: str) -> None:
    """
    Update Codex CLI config.toml to use the OS+tool-specific Playwright config.

    Args:
        os_name: Operating system (wsl, linux, macos, windows)
    """
    codex_config = HOME / ".codex/config.toml"
    if not codex_config.exists():
        print(f"❌ Codex config not found: {codex_config}")
        return

    codex_playwright_config = HOME / f".codex/playwright.{os_name}_codex.json"

    # Read current config
    config_text = codex_config.read_text()
    lines = config_text.splitlines()

    # Find and update the playwright MCP server args line
    updated_lines = []
    in_playwright_section = False

    for line in lines:
        stripped = line.strip()

        # Detect playwright section
        if stripped.startswith('[mcp_servers.playwright]'):
            in_playwright_section = True
            updated_lines.append(line)
            continue

        # Exit playwright section on new section
        if in_playwright_section and stripped.startswith('[') and 'playwright' not in stripped:
            in_playwright_section = False

        # Update args line in playwright section
        if in_playwright_section and stripped.startswith('args = '):
            # Replace with new config path
            updated_lines.append(f'args = ["-y", "@playwright/mcp@latest", "--config", "{codex_playwright_config}"]')
        else:
            updated_lines.append(line)

    # Write back
    backup = codex_config.with_suffix('.toml.bak')
    backup.write_text(config_text)
    codex_config.write_text('\n'.join(updated_lines) + '\n')

    print(f"✅ Updated Codex CLI config to use: {codex_playwright_config}")
    print(f"📦 Backup saved: {backup}")
    print("🔁 Restart Codex CLI to apply changes")


def show_status(os_name: Optional[str] = None) -> None:
    """
    Display current status of concurrent browser configurations.

    Args:
        os_name: Optional OS filter (wsl, linux, macos, windows). Shows all if None.
    """
    detected_os = detect_os()

    print("📊 Concurrent Browser Configuration Status")
    print("=" * 70)
    print()

    print(f"Environment:")
    print(f"   Detected OS: {OS_NAMES.get(detected_os, detected_os)}")

    if detected_os == "wsl":
        wslg = detect_wslg()
        print(f"   WSLg detected: {'✅ Yes' if wslg else '❌ No'}")

    chromium = detect_chromium_executable()
    print(f"   Chromium executable: {chromium or '❌ Not found'}")
    print()

    # Determine which OSes to show
    os_list = [os_name] if os_name else list(OS_NAMES.keys())

    for check_os in os_list:
        print(f"Configuration for {OS_NAMES[check_os]}:")
        print()

        for tool_id, tool in AI_TOOLS.items():
            tool_config = get_os_tool_config(check_os, tool_id)
            config_path = tool_config["config_dir"] / tool_config["config_file"]
            profile_dir = tool_config["profile_dir"]

            config_exists = config_path.exists()
            profile_exists = profile_dir.exists()

            status_emoji = "✅" if (config_exists and profile_exists) else "⚠️" if config_exists else "❌"

            print(f"  {status_emoji} {tool['name']} ({check_os}_{tool_id})")
            print(f"     Config: {config_path}")
            print(f"             {'✅ Exists' if config_exists else '❌ Missing'}")

            if config_exists:
                try:
                    config_data = json.loads(config_path.read_text())
                    isolated = config_data.get("browser", {}).get("isolated", False)
                    headless = config_data.get("browser", {}).get("launchOptions", {}).get("headless", True)
                    metadata = config_data.get("_metadata", {})
                    print(f"             isolated={isolated}, headless={headless}")
                    if metadata:
                        print(f"             OS: {metadata.get('os')}, Tool: {metadata.get('tool')}")
                except Exception as e:
                    print(f"             ⚠️  Error reading config: {e}")

            print(f"     Profile: {profile_dir}")
            print(f"              {'✅ Exists' if profile_exists else '❌ Missing'}")
            print()

        print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="MCP Concurrent Browser Manager - Enable simultaneous browser use across AI tools with OS-specific configs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Set up concurrent configs for all tools on current OS
  python3 mcp_concurrent_browser.py setup

  # Set up for specific tools only
  python3 mcp_concurrent_browser.py setup --tools codex claude

  # Set up for specific OS
  python3 mcp_concurrent_browser.py setup --os wsl

  # Set up in headless mode
  python3 mcp_concurrent_browser.py setup --headless

  # Update Codex CLI config (auto-detects OS)
  python3 mcp_concurrent_browser.py apply-codex

  # Show current status for all OSes
  python3 mcp_concurrent_browser.py status

  # Show status for specific OS
  python3 mcp_concurrent_browser.py status --os wsl
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Setup command
    setup_parser = subparsers.add_parser("setup", help="Set up concurrent browser configs")
    setup_parser.add_argument(
        "--os",
        choices=list(OS_NAMES.keys()),
        default=None,
        help="Target OS (default: auto-detect current OS)",
    )
    setup_parser.add_argument(
        "--tools",
        nargs="+",
        choices=list(AI_TOOLS.keys()),
        default=list(AI_TOOLS.keys()),
        help="AI tools to configure (default: all)",
    )
    setup_parser.add_argument(
        "--headless",
        action="store_true",
        help="Configure headless mode (default: headed)",
    )

    # Apply-codex command
    apply_parser = subparsers.add_parser("apply-codex", help="Update Codex CLI config to use OS+tool-specific Playwright config")
    apply_parser.add_argument(
        "--os",
        choices=list(OS_NAMES.keys()),
        default=None,
        help="Target OS (default: auto-detect current OS)",
    )

    # Status command
    status_parser = subparsers.add_parser("status", help="Show current configuration status")
    status_parser.add_argument(
        "--os",
        choices=list(OS_NAMES.keys()),
        default=None,
        help="Show status for specific OS only (default: all OSes)",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Auto-detect OS if not specified
    detected_os = detect_os()

    if args.command == "setup":
        target_os = args.os or detected_os
        setup_concurrent_configs(target_os, args.tools, headless=args.headless)
        print("✅ Concurrent browser setup complete!")
        print("⚠️  Next steps:")
        print(f"   1. Run: python3 mcp_concurrent_browser.py apply-codex --os {target_os}")
        print("   2. Restart all AI CLI tools to apply changes")
        print("   3. Each tool will now use its own isolated browser instance")
        return 0

    elif args.command == "apply-codex":
        target_os = args.os or detected_os
        update_codex_config(target_os)
        return 0

    elif args.command == "status":
        show_status(args.os)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
