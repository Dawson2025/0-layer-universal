#!/usr/bin/env python3
"""
Create the full nested specific/ structure for AI manager systems.

The nested specificity pattern is:
specific/
└── os/
    └── {wsl|linux_ubuntu|macos|windows}/
        └── environment/
            └── {local|cloud/aws|cloud/gcp|cloud/azure}/
                └── coding_app/
                    └── {cursor_ide|vscode|jetbrains|rstudio|terminal}/
                        └── ai_app/
                            └── {claude_code_cli|codex_cli|gemini_cli|cursor_agent}/

Usage: python3 create_specific_structure.py [target_dir]
"""

import os
from pathlib import Path
import sys

# Configuration
OPERATING_SYSTEMS = ['wsl', 'linux_ubuntu', 'macos', 'windows']
ENVIRONMENTS = ['local', 'cloud/aws', 'cloud/gcp', 'cloud/azure']
CODING_APPS = ['cursor_ide', 'vscode', 'jetbrains', 'rstudio', 'terminal']
AI_APPS = ['claude_code_cli', 'codex_cli', 'gemini_cli', 'cursor_agent']

def create_specific_structure(base_dir):
    """Create the full nested specific/ structure."""
    base_path = Path(base_dir) / 'specific' / 'os'

    created_count = 0

    for os_name in OPERATING_SYSTEMS:
        for env in ENVIRONMENTS:
            for app in CODING_APPS:
                for ai in AI_APPS:
                    # Build the full path
                    full_path = base_path / os_name / 'environment' / env / 'coding_app' / app / 'ai_app' / ai

                    # Create the directory
                    full_path.mkdir(parents=True, exist_ok=True)

                    # Create a .gitkeep file
                    gitkeep = full_path / '.gitkeep'
                    if not gitkeep.exists():
                        gitkeep.touch()
                        created_count += 1

    return created_count

def main():
    # Default target directory
    default_target = "/home/dawson/dawson-workspace/code/0_layer_universal/layer_0/layer_0_00_ai_manager_system"

    # Get target from command line or use default
    target_dir = sys.argv[1] if len(sys.argv) > 1 else default_target

    print(f"Creating specific/ structure in: {target_dir}")
    print()

    # Calculate expected count
    total = len(OPERATING_SYSTEMS) * len(ENVIRONMENTS) * len(CODING_APPS) * len(AI_APPS)
    print(f"Expected directories: {total}")
    print(f"  Operating Systems: {len(OPERATING_SYSTEMS)} ({', '.join(OPERATING_SYSTEMS)})")
    print(f"  Environments: {len(ENVIRONMENTS)} ({', '.join(ENVIRONMENTS)})")
    print(f"  Coding Apps: {len(CODING_APPS)} ({', '.join(CODING_APPS)})")
    print(f"  AI Apps: {len(AI_APPS)} ({', '.join(AI_APPS)})")
    print()

    created = create_specific_structure(target_dir)

    print(f"Created {created} new .gitkeep files")
    print("Done!")

if __name__ == "__main__":
    main()
