#!/usr/bin/env python3
# resource_id: "2e26c048-b2f5-490b-b8cd-48a32e108359"
# resource_type: "document"
# resource_name: "restructure_docs"
"""
Script to restructure trickle-down documentation directories
to include 2_testing_docs as the third category
"""

import os
import sys

def restructure_directories():
    """Restructure all trickle_down directories to have 4 categories"""
    base_path = "docs/0_context"
    
    # Find all trickle_down directories
    trickle_dirs = []
    for item in os.listdir(base_path):
        if item.startswith("trickle_down_"):
            trickle_dirs.append(os.path.join(base_path, item))
    
    print(f"Found {len(trickle_dirs)} trickle_down directories")
    
    for dir_path in trickle_dirs:
        print(f"Processing {dir_path}")
        
        # Check if 2_archive_docs exists and rename to 3_archive_docs
        archive_path = os.path.join(dir_path, "2_archive_docs")
        if os.path.exists(archive_path):
            new_archive_path = os.path.join(dir_path, "3_archive_docs")
            os.rename(archive_path, new_archive_path)
            print(f"  Renamed 2_archive_docs to 3_archive_docs")
        
        # Create 2_testing_docs directory
        testing_path = os.path.join(dir_path, "2_testing_docs")
        if not os.path.exists(testing_path):
            os.makedirs(testing_path)
            print(f"  Created 2_testing_docs")
        else:
            print(f"  2_testing_docs already exists")
    
    print("Restructuring complete!")

if __name__ == "__main__":
    restructure_directories()
