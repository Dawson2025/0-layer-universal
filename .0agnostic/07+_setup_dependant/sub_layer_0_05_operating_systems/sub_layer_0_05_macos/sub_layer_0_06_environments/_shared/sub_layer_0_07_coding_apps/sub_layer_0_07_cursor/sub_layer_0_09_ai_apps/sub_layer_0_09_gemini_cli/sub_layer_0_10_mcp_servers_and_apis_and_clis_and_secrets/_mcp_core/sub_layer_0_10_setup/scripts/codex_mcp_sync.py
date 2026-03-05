#!/usr/bin/env python3
# resource_id: "503568ae-759f-4a61-8991-ef49dde5aa3d"
# resource_type: "document"
# resource_name: "codex_mcp_sync"
"""
Sync Codex CLI MCP servers from environment presets into ~/.codex/config.toml.

Patterns borrowed from the universal MCP system (dev/test/prod). Generates
~/.codex/environments/<env>.toml and rewrites the [mcp_servers.*] section of
~/.codex/config.toml to match.
"""

from __future__ import annotations

import argparse
import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple


HOME = Path.home()
CODEX_DIR = HOME / ".codex"
CODEX_CONFIG = CODEX_DIR / "config.toml"
ENV_DIR = CODEX_DIR / "environments"

CODEX_ENV_FILE = CODEX_DIR / "mcp.env"


def load_simple_env_file(path: Path) -> Dict[str, str]:
    """
    Load KEY=VALUE lines from an env file (no interpolation).
    Lines starting with '#' are ignored.
    """
    if not path.exists():
        return {}
    result: Dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            result[key] = value
    return result


def pick_secret(key: str, env_file: Dict[str, str]) -> Optional[str]:
    """Prefer ~/.codex/mcp.env, fallback to process env."""
    return env_file.get(key) or os.environ.get(key)

def detect_playwright_chromium_executable() -> Optional[str]:
    """
    On WSLg/Linux, explicitly pinning the Chromium executable can improve reliability.
    Returns the newest ms-playwright chromium binary path if found.
    """
    root = HOME / ".cache/ms-playwright"
    candidates: List[Tuple[int, Path]] = []
    for d in root.glob("chromium-*"):
        if d.name.startswith("chromium_headless_shell"):
            continue
        chrome = d / "chrome-linux64" / "chrome"
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

def write_playwright_mcp_config(
    path: Path,
    *,
    headless: bool,
    isolated: bool,
    executable_path: Optional[str],
    is_wslg: bool,
) -> None:
    """
    Write Playwright MCP JSON config. This lets us control launchOptions (including
    extra Chromium args) in a portable way.
    """
    chromium_args: List[str] = []
    # WSLg: Chromium can crash in headed mode unless Ozone is explicitly set to Wayland.
    if is_wslg and not headless:
        chromium_args += ["--ozone-platform=wayland", "--enable-features=UseOzonePlatform"]

    launch_options: Dict = {
        "headless": headless,
    }
    if executable_path:
        launch_options["executablePath"] = executable_path
    if chromium_args:
        launch_options["args"] = chromium_args

    config = {
        "browser": {
            "browserName": "chromium",
            "isolated": isolated,
            "launchOptions": launch_options,
        }
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config, indent=2) + "\n")

def env_presets() -> Dict[str, Dict]:
    """Return MCP server presets for dev/test/prod-lite."""
    env_file = load_simple_env_file(CODEX_ENV_FILE)

    wslg_runtime_dir = "/mnt/wslg/runtime-dir"
    has_wslg = Path("/mnt/wslg").exists() and Path(wslg_runtime_dir).exists()

    # Defaults (can be overridden in main() for headless mode).
    playwright_config_path = CODEX_DIR / "playwright.development.json"

    base_env = {
        "PLAYWRIGHT_BROWSERS_PATH": str(HOME / ".cache/ms-playwright"),
        "HOME": str(HOME),
        "DISPLAY": os.environ.get("DISPLAY", ":0"),
        "WAYLAND_DISPLAY": os.environ.get("WAYLAND_DISPLAY", "wayland-0"),
        "XDG_RUNTIME_DIR": wslg_runtime_dir if has_wslg else os.environ.get("XDG_RUNTIME_DIR", str(HOME / ".run")),
    }

    chromium_executable = detect_playwright_chromium_executable()
    # Use config file to control headless/headed and extra WSLg launch args.
    write_playwright_mcp_config(
        playwright_config_path,
        headless=False,
        isolated=True,
        executable_path=chromium_executable,
        is_wslg=has_wslg,
    )
    playwright_base_args = ["-y", "@playwright/mcp@latest", "--config", str(playwright_config_path)]

    tavily_key = pick_secret("TAVILY_API_KEY", env_file)
    context7_key = pick_secret("CONTEXT7_API_KEY", env_file)
    context7_url = pick_secret("CONTEXT7_API_URL", env_file)

    return {
        "development": {
            "chrome-devtools": {
                "command": "npx",
                "args": ["-y", "chrome-devtools-mcp@latest"],
                "env": {},
            },
            "playwright": {
                "command": "npx",
                # Headed by default; add --headless only when requested.
                "args": playwright_base_args,
                "env": base_env,
            },
            "browser": {
                "command": "npx",
                "args": ["-y", "@agent-infra/mcp-server-browser"],
                "env": base_env,
            },
            "web-search": {
                "command": "npx",
                "args": ["-y", "tavily-mcp"],
                "env": {"TAVILY_API_KEY": tavily_key} if tavily_key else {},
            },
            "context7": {
                "command": "npx",
                "args": ["-y", "@upstash/context7-mcp"],
                "env": {
                    **({"CONTEXT7_API_KEY": context7_key} if context7_key else {}),
                    **({"CONTEXT7_API_URL": context7_url} if context7_url else {}),
                },
            },
            "filesystem": {
                "command": "npx",
                "args": ["-y", "mcp-filesystem-server"],
                "env": {},
            },
        },
        "testing": {
            "playwright": {
                "command": "npx",
                "args": playwright_base_args,
                "env": base_env,
            },
            "browser": {
                "command": "npx",
                "args": ["-y", "@agent-infra/mcp-server-browser"],
                "env": base_env,
            },
            "filesystem": {
                "command": "npx",
                "args": ["-y", "mcp-filesystem-server"],
                "env": {},
            },
        },
        "production-lite": {
            "web-search": {
                "command": "npx",
                "args": ["-y", "tavily-mcp"],
                "env": {"TAVILY_API_KEY": tavily_key} if tavily_key else {},
            },
            "context7": {
                "command": "npx",
                "args": ["-y", "@upstash/context7-mcp"],
                "env": {
                    **({"CONTEXT7_API_KEY": context7_key} if context7_key else {}),
                    **({"CONTEXT7_API_URL": context7_url} if context7_url else {}),
                },
            },
            "filesystem": {
                "command": "npx",
                "args": ["-y", "mcp-filesystem-server"],
                "env": {},
            },
        },
    }


def render_env_block(env_name: str, servers: Dict[str, Dict]) -> str:
    """Render a TOML block for [mcp_servers.*]."""
    lines: List[str] = []
    lines.append(f"# Generated for Codex CLI MCP ({env_name})")
    for name, cfg in servers.items():
        lines.append(f'[mcp_servers.{name}]')
        lines.append(f'command = "{cfg["command"]}"')
        args_str = ", ".join(f'"{a}"' for a in cfg["args"])
        lines.append(f'args = [{args_str}]')
        if cfg.get("env"):
            lines.append(f"[mcp_servers.{name}.env]")
            for k, v in cfg["env"].items():
                lines.append(f'{k} = "{v}"')
        lines.append("")  # spacer
    return "\n".join(lines).strip() + "\n"


def strip_existing_mcp(config_text: str) -> str:
    """Remove existing [mcp_servers.*] blocks from config.toml."""
    lines = config_text.splitlines()
    out: List[str] = []
    in_mcp = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# Generated for Codex CLI MCP"):
            continue
        if stripped.startswith("[mcp_servers."):
            in_mcp = True
            continue
        if in_mcp and stripped.startswith("[") and not stripped.startswith("[mcp_servers."):
            in_mcp = False
        if not in_mcp:
            out.append(line)
    # tidy extra blank lines
    while len(out) >= 2 and out[-1] == "" and out[-2] == "":
        out.pop()
    if out and out[-1] != "":
        out.append("")  # ensure newline separation
    return "\n".join(out) + "\n"


def write_env_file(env_name: str, content: str) -> Path:
    ENV_DIR.mkdir(parents=True, exist_ok=True)
    path = ENV_DIR / f"{env_name}.toml"
    path.write_text(content)
    return path


def backup_config(config_path: Path) -> Path:
    backup = config_path.with_suffix(config_path.suffix + ".bak")
    backup.write_text(config_path.read_text())
    return backup


def merge_config(env_block: str, config_path: Path) -> None:
    text = config_path.read_text()
    text_wo_mcp = strip_existing_mcp(text)
    new_text = text_wo_mcp + env_block
    config_path.write_text(new_text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Codex MCP servers from presets.")
    parser.add_argument("--env", choices=["development", "testing", "production-lite"], default="development")
    parser.add_argument("--config", type=Path, default=CODEX_CONFIG, help="Path to Codex config.toml")
    parser.add_argument(
        "--disable",
        nargs="*",
        default=[],
        help="Server names to remove from the selected environment (e.g., --disable chrome-devtools web-search)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Force Playwright MCP to run headless (adds --headless). Default is headed.",
    )
    args = parser.parse_args()

    # If headless is requested, rewrite the Playwright config to headless=true.
    if args.headless:
        wslg_runtime_dir = "/mnt/wslg/runtime-dir"
        has_wslg = Path("/mnt/wslg").exists() and Path(wslg_runtime_dir).exists()
        chromium_executable = detect_playwright_chromium_executable()
        env_name_for_config = args.env
        config_path = CODEX_DIR / f"playwright.{env_name_for_config}.json"
        write_playwright_mcp_config(
            config_path,
            headless=True,
            isolated=True,
            executable_path=chromium_executable,
            is_wslg=has_wslg,
        )

    presets = env_presets()
    servers_full = dict(presets[args.env])  # baseline

    if args.headless and "playwright" in servers_full:
        # Point Playwright server to the headless config path written above.
        config_path = CODEX_DIR / f"playwright.{args.env}.json"
        servers_full["playwright"] = dict(servers_full["playwright"])
        servers_full["playwright"]["args"] = ["-y", "@playwright/mcp@latest", "--config", str(config_path)]

    servers_active = dict(servers_full)
    disabled_servers = {}
    for name in list(servers_active.keys()):
        if name in args.disable:
            disabled_servers[name] = servers_active.pop(name)

    env_block = render_env_block(args.env, servers_active)
    env_full_block = render_env_block(f"{args.env}-full", servers_full)
    disabled_block = render_env_block(f"{args.env}-disabled", disabled_servers) if disabled_servers else "# No disabled servers for this env.\n"

    if not args.config.exists():
        raise SystemExit(f"Config not found: {args.config}")

    backup = backup_config(args.config)
    merge_config(env_block, args.config)
    env_file = write_env_file(args.env, env_block)
    env_full_file = write_env_file(f"{args.env}.full", env_full_block)
    env_disabled_file = write_env_file(f"{args.env}.disabled", disabled_block)

    print(f"✅ Updated {args.config} with MCP servers for '{args.env}'.")
    print(f"📦 Backup: {backup}")
    print(f"🗂️  Env snippet (active) saved to: {env_file}")
    print(f"🗂️  Env snippet (full) saved to:   {env_full_file}")
    print(f"🗂️  Disabled servers saved to:    {env_disabled_file}")
    print("🔁 Restart Codex CLI to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
