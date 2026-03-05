#!/usr/bin/env python3
# resource_id: "abb7f96d-1e0d-497a-bd5d-ea861e8aacaa"
# resource_type: "document"
# resource_name: "rename_old_directories"
"""
Rename directories from old naming convention (dots) to new convention (underscores).
Run this script from the 0_layer_universal directory.

Usage: python3 rename_old_directories.py
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("/home/dawson/dawson-workspace/code/0_layer_universal")

# Patterns to match and their replacements
PATTERNS = [
    # Stage directories: stage_0_01_* -> stage_0_01_*
    (r'^stage_(\d+)\.(\d+)_(.*)$', r'stage_\1_\2_\3'),

    # Sub-layer directories: sub_layer_0_01_* -> sub_layer_0_01_*
    (r'^sub_layer_(\d+)\.(\d+)(.*)$', r'sub_layer_\1_\2\3'),

    # Handoff subdirectories: 0.00_to_* -> layer_0_00_to_*
    (r'^(\d+)\.(\d+)_to_(.*)$', r'layer_\1_\2_to_\3'),

    # Layer directories: 0.00_* -> layer_0_00_*
    (r'^(\d+)\.(\d+)_(.*)$', r'layer_\1_\2_\3'),
]

def get_new_name(dirname):
    """Get new directory name if it matches any pattern."""
    for pattern, replacement in PATTERNS:
        if re.match(pattern, dirname):
            return re.sub(pattern, replacement, dirname)
    return None

def find_directories_to_rename(base_dir):
    """Find all directories that need renaming, sorted deepest first."""
    to_rename = []

    for root, dirs, files in os.walk(base_dir):
        for dirname in dirs:
            new_name = get_new_name(dirname)
            if new_name and new_name != dirname:
                old_path = Path(root) / dirname
                new_path = Path(root) / new_name
                # Calculate depth for sorting (deeper first)
                depth = len(old_path.parts)
                to_rename.append((depth, old_path, new_path))

    # Sort by depth descending (deepest first)
    to_rename.sort(key=lambda x: -x[0])
    return to_rename

def main():
    print(f"Scanning {BASE_DIR} for directories to rename...")
    print()

    to_rename = find_directories_to_rename(BASE_DIR)

    if not to_rename:
        print("No directories found matching old naming convention.")
        return

    print(f"Found {len(to_rename)} directories to rename:")
    print("-" * 80)

    renamed_count = 0
    error_count = 0

    for depth, old_path, new_path in to_rename:
        print(f"Renaming: {old_path.name}")
        print(f"      to: {new_path.name}")
        print(f"    path: {old_path.parent}")

        try:
            if old_path.exists():
                if new_path.exists():
                    print(f"  SKIPPED: Target already exists")
                else:
                    old_path.rename(new_path)
                    print(f"  SUCCESS")
                    renamed_count += 1
            else:
                print(f"  SKIPPED: Source no longer exists (may have been renamed as part of parent)")
        except Exception as e:
            print(f"  ERROR: {e}")
            error_count += 1
        print()

    print("-" * 80)
    print(f"Summary: {renamed_count} renamed, {error_count} errors, {len(to_rename) - renamed_count - error_count} skipped")

if __name__ == "__main__":
    main()
