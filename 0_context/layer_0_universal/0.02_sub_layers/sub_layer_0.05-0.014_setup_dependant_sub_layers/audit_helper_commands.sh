#!/bin/bash
# Helper commands for auditing missing content
# Use these commands to investigate what content existed before consolidation

echo "=== Missing Content Audit Helper Commands ==="
echo ""
echo "Run these commands to investigate missing content:"
echo ""

echo "1. Find the last commit before old sublayers were deleted:"
echo "   git log --all --oneline --grep='Remove old sublayer' | head -1"
echo ""

echo "2. List all files in old sublayers at commit d64c065 (after revert):"
echo "   git ls-tree -r d64c065 --name-only | grep -E 'sub_layer_0\.(0[6-9]|1[0-4])' | wc -l"
echo ""

echo "3. Get detailed file listing of each old sublayer:"
echo "   for i in 06 07 08 09 10 11 12 13 14; do"
echo "     echo \"=== sub_layer_0.\${i} ===\";"
echo "     git ls-tree -r d64c065 --name-only | grep \"sub_layer_0.\${i}_\" | head -10;"
echo "   done"
echo ""

echo "4. Count files in current hierarchical structure:"
echo "   find 0.01_universal_setup_file_tree_0 -type f -name '*.md' | wc -l"
echo ""

echo "5. See what was in legacy_content before it was removed:"
echo "   git show 3dda597:0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.05-0.014_setup/legacy_content/"
echo ""

echo "6. Compare file counts by sublayer:"
echo "   # At commit d64c065 (original content restored)"
echo "   git ls-tree -r d64c065 --name-only | grep 'sub_layer_0.10_mcp' | wc -l"
echo "   # Current in hierarchy at level 5"
echo "   find 0.01_universal_setup_file_tree_0 -path '*0.06_mcp_servers/_shared/*' -type f | wc -l"
echo ""

echo "7. See full content of a specific old sublayer:"
echo "   git show d64c065:0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.10_mcp_servers_and_tools_setup/"
echo ""

echo "8. Check if specific files exist in current structure:"
echo "   # Example: Check for MCP configuration guide"
echo "   find 0.01_universal_setup_file_tree_0 -name 'MCP_CONFIGURATION_GUIDE.md'"
echo ""

echo "9. Get list of all markdown files from old sublayers:"
echo "   git ls-tree -r d64c065 --name-only | grep -E 'sub_layer_0\.(0[6-9]|1[0-4]).*\.md$' > /tmp/old_files.txt"
echo "   echo \"Total old files: \$(wc -l < /tmp/old_files.txt)\""
echo ""

echo "10. Get list of all markdown files in new structure:"
echo "   find 0.01_universal_setup_file_tree_0 -name '*.md' > /tmp/new_files.txt"
echo "   echo \"Total new files: \$(wc -l < /tmp/new_files.txt)\""
echo ""

echo "11. Compare file basenames to find missing files:"
echo "   comm -23 <(git ls-tree -r d64c065 --name-only | grep -E 'sub_layer_0\.(0[6-9]|1[0-4]).*\.md$' | xargs -n1 basename | sort) <(find 0.01_universal_setup_file_tree_0 -name '*.md' | xargs -n1 basename | sort)"
echo ""

echo "12. Detailed comparison for specific sublayer (example: 0.10 MCP):"
echo "   echo '=== Files in old sub_layer_0.10 ==='"
echo "   git ls-tree -r d64c065 --name-only | grep 'sub_layer_0.10_mcp_servers_and_tools_setup'"
echo "   echo ''"
echo "   echo '=== Files in new Level 5 (MCP) ==='"
echo "   find 0.01_universal_setup_file_tree_0 -path '*0.06_mcp_servers/*' -type f"
echo ""

echo "=== Quick Start: Run Essential Commands ==="
echo ""
echo "# Get total counts:"
echo "git ls-tree -r d64c065 --name-only | grep -E 'sub_layer_0\.(0[6-9]|1[0-4])' | wc -l"
echo "find 0.01_universal_setup_file_tree_0 -type f | wc -l"
echo ""
echo "# Find potentially missing basenames:"
echo "comm -23 \\"
echo "  <(git ls-tree -r d64c065 --name-only | grep -E 'sub_layer_0\.(0[6-9]|1[0-4])' | xargs -n1 basename | sort | uniq) \\"
echo "  <(find 0.01_universal_setup_file_tree_0 -type f | xargs -n1 basename | sort | uniq)"
