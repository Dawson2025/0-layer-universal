#!/usr/bin/env python3
# resource_id: "e7b6e549-def2-40b4-b641-ce6c0b353bb7"
# resource_type: "document"
# resource_name: "rename_directories"
"""
Script to rename directories from old naming convention (dots) to new convention (underscores).
"""

import os
import re

BASE_PATH = "/home/dawson/dawson-workspace/code/0_layer_universal"

def find_directories_to_rename(base_path):
    """Find all directories that need renaming, sorted from deepest to shallowest."""
    dirs_to_rename = []

    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            full_path = os.path.join(root, d)

            if re.match(r'^stage_\d+\.\d+_', d):
                new_name = re.sub(r'^(stage_)(\d+)\.(\d+)_', r'\1\2_\3_', d)
                dirs_to_rename.append((full_path, os.path.join(root, new_name)))
            elif re.match(r'^sub_layer_\d+\.\d+', d):
                new_name = re.sub(r'^(sub_layer_)(\d+)\.(\d+)', r'\1\2_\3', d)
                dirs_to_rename.append((full_path, os.path.join(root, new_name)))
            elif re.match(r'^\d+\.\d+_', d):
                new_name = re.sub(r'^(\d+)\.(\d+)_', r'layer_\1_\2_', d)
                dirs_to_rename.append((full_path, os.path.join(root, new_name)))

    dirs_to_rename.sort(key=lambda x: x[0].count('/'), reverse=True)
    return dirs_to_rename

# Auto-execute
dirs_to_rename = find_directories_to_rename(BASE_PATH)
print(f"Found {len(dirs_to_rename)} directories to rename:")
for old_path, new_path in dirs_to_rename[:20]:
    print(f"  {os.path.basename(old_path)} -> {os.path.basename(new_path)}")

# Perform renames
for old_path, new_path in dirs_to_rename:
    try:
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"OK: {os.path.basename(old_path)}")
    except Exception as e:
        print(f"ERR: {old_path}: {e}")

print("Done!")
