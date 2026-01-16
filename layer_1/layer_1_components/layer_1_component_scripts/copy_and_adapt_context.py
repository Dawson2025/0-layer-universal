#!/usr/bin/env python3
"""
Copy 0_context from DS250-Course-Draft to pac20026_fall2025 and adapt content
"""
import os
import shutil
from pathlib import Path

# Source and destination
source_dir = Path("/home/dawson/dawson-workspace/code/DS250-Course-Draft/0_context")
dest_dir = Path("/home/dawson/dawson-workspace/code/pac20026_fall2025/0_context")

# Text replacements to adapt for new project
replacements = {
    "DS250-Course-Draft": "pac20026_fall2025",
    "ds250-course-draft": "pac20026_fall2025",
    "/DS250-Course-Draft/": "/pac20026_fall2025/",
    "DS 250 Course": "DS 250 Portfolio - pac20026_fall2025",
    "DS250 Course": "DS250 Portfolio - pac20026_fall2025",
}

def adapt_content(content, filepath):
    """Replace project-specific references"""
    for old, new in replacements.items():
        content = content.replace(old, new)
    return content

def copy_and_adapt(src, dst):
    """Copy directory and adapt markdown files"""
    # Create destination if it doesn't exist
    dst.parent.mkdir(parents=True, exist_ok=True)
    
    if src.is_file():
        # Read file
        try:
            with open(src, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Adapt content if it's a text file
            if src.suffix in ['.md', '.txt', '.json', '.yaml', '.yml']:
                content = adapt_content(content, src)
            
            # Write to destination
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Copied & adapted: {src.relative_to(source_dir)}")
        except Exception as e:
            print(f"✗ Error with {src}: {e}")
            # Copy without adaptation if there's an error
            shutil.copy2(src, dst)
    else:
        # Create directory
        dst.mkdir(exist_ok=True)

def main():
    print(f"Copying from: {source_dir}")
    print(f"Copying to:   {dest_dir}")
    print(f"Adaptations:  {len(replacements)} text replacements")
    print()
    
    # Walk through source directory
    for root, dirs, files in os.walk(source_dir):
        root_path = Path(root)
        rel_path = root_path.relative_to(source_dir)
        dest_root = dest_dir / rel_path
        
        # Create destination directory
        dest_root.mkdir(parents=True, exist_ok=True)
        
        # Copy files
        for file in files:
            src_file = root_path / file
            dst_file = dest_root / file
            copy_and_adapt(src_file, dst_file)
    
    print()
    print("=" * 60)
    print("✓ COPY AND ADAPTATION COMPLETE!")
    print(f"✓ Created: {dest_dir}")
    print("=" * 60)

if __name__ == "__main__":
    main()

