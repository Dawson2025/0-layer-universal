#!/usr/bin/env python3
# resource_id: "ad88bda5-94e8-4d8b-bcda-162784324558"
# resource_type: "document"
# resource_name: "migrate_content"
"""
Migrate content from old directory structure to new structure.

This script:
1. Moves content from layer_0/ to layer_0/
2. Moves content from layer_1/layer_1_features/layer_1_feature_layer_stage_system/ and layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/
   to layer_1/layer_1_features/layer_1_feature_layer_stage_system/

Usage: python3 migrate_content.py
"""

import os
import shutil
from pathlib import Path

BASE_DIR = Path("/home/dawson/dawson-workspace/code/0_layer_universal")

def copy_tree_contents(src, dst, dry_run=False):
    """Copy contents of src into dst, merging directories."""
    src = Path(src)
    dst = Path(dst)

    if not src.exists():
        print(f"  Source does not exist: {src}")
        return 0

    copied = 0
    for item in src.iterdir():
        src_item = item
        dst_item = dst / item.name

        if dry_run:
            if item.is_dir():
                print(f"  [DRY RUN] Would copy dir: {src_item.name} -> {dst_item}")
            else:
                print(f"  [DRY RUN] Would copy file: {src_item.name} -> {dst_item}")
            copied += 1
        else:
            if item.is_dir():
                if dst_item.exists():
                    # Recursively merge
                    copied += copy_tree_contents(src_item, dst_item, dry_run)
                else:
                    shutil.copytree(src_item, dst_item)
                    print(f"  Copied dir: {src_item.name}")
                    copied += 1
            else:
                if not dst_item.exists():
                    dst_item.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_item, dst_item)
                    print(f"  Copied file: {src_item.name}")
                    copied += 1
                else:
                    print(f"  Skipped (exists): {src_item.name}")

    return copied

def migrate_layer_0(dry_run=False):
    """Migrate layer_0/ contents to layer_0/"""
    print("\n" + "=" * 80)
    print("MIGRATION 1: layer_0/ -> layer_0/")
    print("=" * 80)

    src = BASE_DIR / "layer_0"
    dst = BASE_DIR / "layer_0"

    # Mapping of old names to new names
    mappings = [
        ("0.00_ai_manager_system", "layer_0_00_ai_manager_system"),
        ("0.01_manager_handoff_documents", "layer_0_01_manager_handoff_documents"),
        ("0.02_sub_layers", "layer_0_02_sub_layers"),
        ("0.99_stages", "layer_0_99_stages"),
    ]

    total = 0
    for old_name, new_name in mappings:
        old_path = src / old_name
        new_path = dst / new_name

        print(f"\nMigrating: {old_name} -> {new_name}")

        if old_path.exists():
            if not dry_run:
                new_path.mkdir(parents=True, exist_ok=True)
            total += copy_tree_contents(old_path, new_path, dry_run)
        else:
            print(f"  Source not found: {old_path}")

    return total

def migrate_framework_docs(dry_run=False):
    """Migrate framework documentation to the layer_stage_system feature."""
    print("\n" + "=" * 80)
    print("MIGRATION 2: Framework docs -> layer_1_feature_layer_stage_system")
    print("=" * 80)

    # Source: layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers (or layer_0_01_layer_stage_framework if renamed)
    old_src = BASE_DIR / "layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers"
    new_src = BASE_DIR / "layer_0_01_layer_stage_framework"
    src = old_src if old_src.exists() else new_src

    # Destination
    dst = BASE_DIR / "layer_1" / "layer_1_features" / "layer_1_feature_layer_stage_system" / "layer_1" / "layer_1_02_sub_layers" / "sub_layer_1_05+_setup_dependant"

    if not src.exists():
        print(f"Source not found: {src}")
        return 0

    print(f"Source: {src}")
    print(f"Destination: {dst}")

    # Map framework content
    mappings = [
        # Framework docs go to sub_layer_1_05_framework_docs
        (["FLEXIBLE_LAYERING_SYSTEM.md", "EXTENDING_THE_FRAMEWORK.md",
          "WORKFLOW_FEATURE_PATTERN.md", "FEATURE_TYPE_DECISION_GUIDE.md",
          "UNIVERSAL_SYSTEM_EVALUATION.md", "README.md"],
         "sub_layer_1_05_framework_docs"),

        # Templates go to sub_layer_1_06_templates
        (["0_universal_template", "1_project_template", "2_feature_template",
          "2_sub_project_template", "3_component_template"],
         "sub_layer_1_06_templates"),
    ]

    total = 0
    for items, dst_folder in mappings:
        dst_path = dst / dst_folder
        if not dry_run:
            dst_path.mkdir(parents=True, exist_ok=True)

        for item_name in items:
            item_src = src / item_name
            item_dst = dst_path / item_name

            if item_src.exists():
                if dry_run:
                    print(f"  [DRY RUN] Would copy: {item_name} -> {dst_folder}/")
                    total += 1
                else:
                    if item_src.is_dir():
                        if not item_dst.exists():
                            shutil.copytree(item_src, item_dst)
                            print(f"  Copied dir: {item_name}")
                            total += 1
                    else:
                        if not item_dst.exists():
                            shutil.copy2(item_src, item_dst)
                            print(f"  Copied file: {item_name}")
                            total += 1
                        else:
                            print(f"  Skipped (exists): {item_name}")

    return total

def migrate_stage_system_content(dry_run=False):
    """Migrate layer_1/layer_1_features/layer_1_feature_layer_stage_system content to the feature."""
    print("\n" + "=" * 80)
    print("MIGRATION 3: Stage system content -> layer_1_feature_layer_stage_system")
    print("=" * 80)

    # Source
    old_src = BASE_DIR / "layer_1/layer_1_features/layer_1_feature_layer_stage_system"
    new_src = BASE_DIR / "layer_0_00_layer_stage_system"
    src = old_src if old_src.exists() else new_src

    if not src.exists():
        print(f"Source not found: {src}")
        return 0

    # The stages content should go into the feature's layer_1_99_stages
    dst = BASE_DIR / "layer_1" / "layer_1_features" / "layer_1_feature_layer_stage_system" / "layer_1" / "layer_1_99_stages"

    print(f"Source: {src}/stages")
    print(f"Destination: {dst}")

    stages_src = src / "stages"
    if stages_src.exists():
        return copy_tree_contents(stages_src, dst, dry_run)
    else:
        print(f"  Stages directory not found: {stages_src}")
        return 0

def main():
    import sys
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=" * 80)
        print("DRY RUN MODE - No changes will be made")
        print("=" * 80)

    print(f"Base directory: {BASE_DIR}")

    total = 0
    total += migrate_layer_0(dry_run)
    total += migrate_framework_docs(dry_run)
    total += migrate_stage_system_content(dry_run)

    print("\n" + "=" * 80)
    print(f"TOTAL: {total} items processed")
    print("=" * 80)

    if dry_run:
        print("\nRun without --dry-run to perform the actual migration.")

if __name__ == "__main__":
    main()
