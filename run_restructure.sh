#!/bin/bash
# Master script to complete the Layer-Stage System restructure
# Run from: /home/dawson/dawson-workspace/code/0_layer_universal/

set -e  # Exit on error

echo "========================================"
echo "Layer-Stage System Restructure Scripts"
echo "========================================"
echo ""
echo "This will run three scripts in sequence:"
echo "1. rename_old_directories.py - Rename 0.XX_ -> layer_N_XX_"
echo "2. create_specific_structure.py - Create nested specific/ structure"
echo "3. migrate_content.py - Move content to new locations"
echo ""

cd /home/dawson/dawson-workspace/code/0_layer_universal

# Check if Python3 is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 not found"
    exit 1
fi

echo "========================================"
echo "STEP 1: Rename directories"
echo "========================================"
python3 rename_old_directories.py

echo ""
echo "========================================"
echo "STEP 2: Create specific/ structure"
echo "========================================"
python3 create_specific_structure.py

echo ""
echo "========================================"
echo "STEP 3: Migrate content"
echo "========================================"
echo "Running in dry-run mode first..."
python3 migrate_content.py --dry-run

echo ""
echo "To perform actual migration, run:"
echo "  python3 migrate_content.py"
echo ""
echo "========================================"
echo "RESTRUCTURE COMPLETE"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Review the changes"
echo "2. Run: python3 migrate_content.py  (without --dry-run)"
echo "3. Delete old directories after verifying migration"
echo "4. Commit the changes to git"
