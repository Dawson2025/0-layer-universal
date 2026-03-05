#!/usr/bin/env python3
# resource_id: "9a28e1e1-03fc-488b-92ce-fc4dc88dc036"
# resource_type: "document"
# resource_name: "mcp_manager"
import json
import os
import sys
import shutil
from pathlib import Path
import platform
import argparse

# --- Configuration Constants (Dynamic) ---
# These will be set by detect_environment()
HOME_DIR = None
MCP_CONFIG_BASE_DIR = None
BROWSER_CACHE_DIR = None
NODE_BIN_DIR = None
NPX_BIN_PATH = None
DISPLAY_VAR = None

# Target AI Tools
TARGET_TOOLS = ["generic", "claude", "gemini", "codex", "cursor"]

# --- Server Definitions (Source of Truth) ---
SERVERS = {
    "playwright": {
        "description": "Playwright MCP Server (Standard)",
        "command": "npx",
        # Headed by default; use config for launchOptions (WSLg stability).
        "args": ["-y", "@playwright/mcp@latest"], 
        "env": {},
        "requires_wrapper": True
    },
    "browser": {
        "description": "Browser automation using @agent-infra/mcp-server-browser",
        "command": "npx",
        "args": ["-y", "@agent-infra/mcp-server-browser"],
        "env": {}, 
        "requires_wrapper": True
    },
    "web-search": {
        "description": "Tavily Web Search",
        "command": "npx",
        "args": ["-y", "tavily-mcp"],
        "env": {
            "TAVILY_API_KEY": "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"
        },
        "requires_wrapper": True
    },
    "chrome-devtools": {
        "description": "Chrome DevTools Protocol",
        "command": "npx",
        "args": [
            "-y", 
            "chrome-devtools-mcp@latest", 
            "--browserUrl", "http://127.0.0.1:9222",
            "--logFile", "/tmp/mcp-chrome.log"
        ],
        "requires_wrapper": True
    },
    "context7": {
        "description": "Context7 Documentation Tool",
        "command": "npx",
        "args": ["-y", "@upstash/context7-mcp"],
        "env": {
            "CONTEXT7_API_KEY": "136116c4-6c35-4ffd-b8fa-cc8f11cb22a4"
        },
        "requires_wrapper": True
    },

}

def detect_environment():
    """Detects OS and locates Node.js/NPX binary, and sets global paths."""
    global HOME_DIR, MCP_CONFIG_BASE_DIR, BROWSER_CACHE_DIR, NODE_BIN_DIR, NPX_BIN_PATH, DISPLAY_VAR

    system = platform.system().lower()
    print(f"🔍 Detecting environment on {system}...")
    
    # --- Set HOME_DIR ---
    if system == "windows":
        HOME_DIR = Path(os.environ.get("USERPROFILE", Path.home()))
        MCP_CONFIG_BASE_DIR = HOME_DIR / "AppData/Roaming/.config/mcp"
        BROWSER_CACHE_DIR = HOME_DIR / "AppData/Local/ms-playwright"
        if not BROWSER_CACHE_DIR.exists(): # Fallback for WSL or non-standard
             BROWSER_CACHE_DIR = HOME_DIR / ".cache/ms-playwright" 
    else: # Linux, macOS
        HOME_DIR = Path.home()
        MCP_CONFIG_BASE_DIR = HOME_DIR / ".config/mcp"
        BROWSER_CACHE_DIR = HOME_DIR / ".cache/ms-playwright"

    # --- Find npx binary ---
    npx_found_path = shutil.which("npx")
    
    if not npx_found_path:
        print("   ⚠️ 'npx' not found in system PATH. Checking common locations...")
        if system == "windows":
            node_install_dir = Path(os.environ.get("ProgramFiles", "")) / "nodejs"
            if node_install_dir.exists():
                npx_candidate = node_install_dir / "npx.cmd"
                if npx_candidate.exists():
                    npx_found_path = str(npx_candidate)
                    print(f"   ✅ Found npx in Node.js install dir: {npx_found_path}")
        else: # Linux, macOS - Check NVM
            nvm_versions_dir = HOME_DIR / ".nvm/versions/node"
            if nvm_versions_dir.exists():
                versions = sorted([d for d in nvm_versions_dir.iterdir() if d.is_dir()], reverse=True)
                if versions:
                    npx_candidate = versions[0] / "bin/npx"
                    if npx_candidate.exists():
                        npx_found_path = str(npx_candidate)
                        print(f"   ✅ Found NVM npx: {npx_found_path}")

    if not npx_found_path:
        print("   ❌ Error: Could not find 'npx'.")
        NPX_BIN_PATH = "npx" 
        NODE_BIN_DIR = None
    else:
        NPX_BIN_PATH = npx_found_path
        NODE_BIN_DIR = Path(npx_found_path).parent

    # --- Detect Display ---
    DISPLAY_VAR = os.environ.get("DISPLAY", ":0") # Default to :0 if not set
    print(f"   🖥️  Display detected: {DISPLAY_VAR}")

    # --- WSLg detection (headed browser stability) ---
    has_wslg = Path("/mnt/wslg").exists() and Path("/mnt/wslg/runtime-dir").exists()
    if has_wslg:
        print("   ✅ WSLg detected: enabling Wayland runtime env for headed browsers")

    # Update SERVERS with dynamic paths and display
    # Browser
    SERVERS["browser"]["env"]["PLAYWRIGHT_BROWSERS_PATH"] = str(BROWSER_CACHE_DIR)
    SERVERS["browser"]["env"]["HOME"] = str(HOME_DIR)
    SERVERS["browser"]["env"]["DISPLAY"] = DISPLAY_VAR
    if has_wslg:
        SERVERS["browser"]["env"]["WAYLAND_DISPLAY"] = os.environ.get("WAYLAND_DISPLAY", "wayland-0")
        SERVERS["browser"]["env"]["XDG_RUNTIME_DIR"] = "/mnt/wslg/runtime-dir"
    
    # Playwright
    SERVERS["playwright"]["env"]["PLAYWRIGHT_BROWSERS_PATH"] = str(BROWSER_CACHE_DIR)
    SERVERS["playwright"]["env"]["HOME"] = str(HOME_DIR)
    SERVERS["playwright"]["env"]["DISPLAY"] = DISPLAY_VAR
    if has_wslg:
        SERVERS["playwright"]["env"]["WAYLAND_DISPLAY"] = os.environ.get("WAYLAND_DISPLAY", "wayland-0")
        SERVERS["playwright"]["env"]["XDG_RUNTIME_DIR"] = "/mnt/wslg/runtime-dir"

    # Create a Playwright MCP config file so we can set launchOptions reliably (including WSLg flags).
    configs_dir = MCP_CONFIG_BASE_DIR / "configs"
    configs_dir.mkdir(parents=True, exist_ok=True)
    pw_cfg_path = configs_dir / "playwright.json"

    # Find newest Chromium executable inside ms-playwright cache (best-effort).
    chromium_exec = None
    try:
        candidates = []
        for d in BROWSER_CACHE_DIR.glob("chromium-*"):
            if d.name.startswith("chromium_headless_shell"):
                continue
            chrome = d / "chrome-linux64" / "chrome"
            if chrome.exists():
                try:
                    ver = int(d.name.split("-")[-1])
                except Exception:
                    ver = -1
                candidates.append((ver, chrome))
        candidates.sort(reverse=True, key=lambda x: x[0])
        if candidates:
            chromium_exec = str(candidates[0][1])
    except Exception:
        chromium_exec = None

    launch_args = []
    # WSLg headed Chromium: prevent immediate crash by forcing Wayland/Ozone.
    if has_wslg:
        launch_args += ["--ozone-platform=wayland", "--enable-features=UseOzonePlatform"]

    pw_cfg = {
        "browser": {
            "browserName": "chromium",
            "isolated": True,
            "launchOptions": {
                "headless": False,
                **({"executablePath": chromium_exec} if chromium_exec else {}),
                **({"args": launch_args} if launch_args else {}),
            },
        }
    }
    pw_cfg_path.write_text(json.dumps(pw_cfg, indent=2) + "\n")

    # Point Playwright MCP to the config file.
    SERVERS["playwright"]["args"] = ["-y", "@playwright/mcp@latest", "--config", str(pw_cfg_path)]

    print(f"   HOME_DIR: {HOME_DIR}")
    print(f"   MCP_CONFIG_BASE_DIR: {MCP_CONFIG_BASE_DIR}")
    
    return {"os": system, "npx_path_found": npx_found_path, "node_dir_found": NODE_BIN_DIR} 

def get_scope_paths(scope):
    """Determines paths based on installation scope."""
    if scope == "user":
        config_root = MCP_CONFIG_BASE_DIR
        wrapper_root = config_root / "servers"
        json_path = config_root / "mcp.json"
    elif scope == "project":
        config_root = Path.cwd() / ".cursor" 
        wrapper_root = config_root / "mcp-servers"
        json_path = config_root / "mcp.json"
    elif scope == "system":
        if platform.system().lower() == "windows":
            config_root = Path("C:/ProgramData/.config/mcp")
            wrapper_root = Path("C:/Program Files/MCP/servers")
        else:
            config_root = Path("/etc/mcp")
            wrapper_root = Path("/usr/local/share/mcp/servers")
        json_path = config_root / "mcp.json"
    elif scope == "local":
        config_root = Path.cwd() / ".mcp"
        wrapper_root = config_root / "servers"
        json_path = config_root / "mcp.json"
    else:
        raise ValueError(f"Unknown scope: {scope}")

    return config_root, wrapper_root, json_path

def setup_directories(config_root, wrapper_root):
    """Ensure config directories exist."""
    try:
        config_root.mkdir(parents=True, exist_ok=True)
        wrapper_root.mkdir(parents=True, exist_ok=True)
        print(f"✅ Directories checked for config root: {config_root}")
    except PermissionError:
        print(f"❌ Permission denied creating directories in {config_root}.")
        raise

def create_wrapper(server_name, config, env_info, tool_context, wrapper_root):
    """Creates a bash wrapper."""
    wrapper_extension = ".sh"
    if env_info["os"] == "windows":
        wrapper_extension = ".cmd"
        
    filename = f"mcp-{server_name}-{tool_context}{wrapper_extension}"
    wrapper_path = wrapper_root / filename
    
    if env_info["os"] == "windows":
        env_exports = ""
        if "env" in config:
            for k, v in config["env"].items():
                env_exports += f'SET "{k}={v}"\n'
    else: # Unix-like
        env_exports = ""
        if "env" in config:
            for k, v in config["env"].items():
                env_exports += f'export {k}="{v}"\n'

    cmd = config["command"]
    args = " ".join(config["args"])
    
    path_export_cmd = ""
    if env_info["os"] == "windows":
        if NODE_BIN_DIR:
            path_export_cmd = f'SET "PATH={NODE_BIN_DIR};%PATH%"\n'
    else: # Unix-like
        if NODE_BIN_DIR:
            path_export_cmd = f'export PATH="{NODE_BIN_DIR}:$HOME/.local/bin:/usr/local/bin:$PATH"'
        else:
            path_export_cmd = 'export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"'

    exec_cmd = cmd
    if cmd == "npx":
        exec_cmd = NPX_BIN_PATH

    script_content = ""
    if env_info["os"] == "windows":
        script_content = f"""@echo off
REM Wrapper for Server: {server_name} ({tool_context})
REM Generated by mcp_manager.py

{path_export_cmd}
{env_exports}
{exec_cmd} {args} %* 
"""
    else: # Unix-like
        script_content = f"""#!/bin/bash
# Wrapper for Server: {server_name} ({tool_context})
# Generated by mcp_manager.py

{path_export_cmd}
{env_exports}

exec {exec_cmd} {args} \"$@\"
"""
    
    try:
        wrapper_path.write_text(script_content)
        if env_info["os"] != "windows": 
            wrapper_path.chmod(0o755)
        print(f"   🔨 Created wrapper: {wrapper_path}")
        return str(wrapper_path)
    except PermissionError:
        print(f"   ❌ Permission denied writing to {wrapper_path}")
        return None

def generate_config(scope, env_info):
    """Generates the mcp.json file."""
    config_root, wrapper_root, json_path = get_scope_paths(scope)
    
    print(f"⚙️ Generating MCP Configuration for SCOPE: {scope.upper()}")
    print(f"   📂 Config Root:  {config_root}")
    print(f"   📂 Wrapper Root: {wrapper_root}")
    print(f"   📄 JSON Path:    {json_path}")

    setup_directories(config_root, wrapper_root)

    mcp_config = {"mcpServers": {}}
    
    for name, server_data in SERVERS.items():
        
        server_entry = {}
        wrapper_path = None

        if server_data.get("requires_wrapper"):
            for tool in TARGET_TOOLS:
                path = create_wrapper(name, server_data, env_info, tool, wrapper_root)
                if tool == "generic":
                    wrapper_path = path
            
            if wrapper_path:
                server_entry["command"] = wrapper_path
                server_entry["args"] = []
                server_entry["env"] = {} 
            else:
                continue
        else:
            server_entry["command"] = server_data["command"]
            server_entry["args"] = server_data["args"]
            server_entry["env"] = server_data.get("env", {})
            
        mcp_config["mcpServers"][name] = server_entry
        print(f"   ➕ Configured: {name}")

    try:
        with open(json_path, 'w') as f:
            json.dump(mcp_config, f, indent=2)
        print(f"✅ Wrote config to: {json_path}")
    except PermissionError:
        print(f"❌ Permission denied writing {json_path}")

def main():
    parser = argparse.ArgumentParser(description="MCP Automation Manager v3.0")
    parser.add_argument("--scope", choices=["user", "project", "system", "local"], default="user", help="Installation scope")
    args = parser.parse_args()

    print("🚀 Starting MCP Automation Manager")
    env_info = detect_environment()
    
    if env_info["npx_path_found"] == "npx": 
        print("⚠️ Warning: 'npx' not found in system PATH.")
    if env_info["os"] == "windows":
        print("💡 Note: Running on Windows. Wrappers will be .cmd files.")

    if args.scope == "system":
        print("\nAttempting SYSTEM-level installation...")
        try:
            generate_config("system", env_info)
            print("\n✅ SYSTEM-level Setup Complete!")
        except Exception as e:
            print(f"❌ SYSTEM-level installation failed: {e}. Attempting USER-level fallback...")
            try:
                generate_config("user", env_info)
                print("\n✅ USER-level Setup Complete!")
            except Exception as e_user:
                print(f"❌ USER-level fallback also failed: {e_user}.")
    else:
        generate_config(args.scope, env_info)
        print("\n✅ Setup Complete! Restart your Agent/IDE to apply changes.")

if __name__ == "__main__":
    main()
