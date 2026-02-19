#!/usr/bin/env bash
# create-tree-of-needs.sh — Create tree_of_needs scaffold in a stage_01 outputs directory
# Usage: bash tools/create-tree-of-needs.sh <stage_01_outputs_dir> <root_need_name>
#
# Creates:
#   outputs/requests/tree_of_needs/
#   ├── _meta/
#   │   ├── VERSION.md
#   │   ├── CHANGELOG.md
#   │   └── DEPENDENCIES.md
#   └── 00_<root_need>/
#       └── README.md
#
# After running, manually add branches (01_*, 02_*, ...) with leaf needs.
# Each leaf need gets: README.md, requirements/ (with REQ-NN files), user_stories/ (with US-NN files)
# Reference: @imports/entity_structure.md

set -euo pipefail

OUTPUTS_DIR="${1:?Usage: create-tree-of-needs.sh <stage_01_outputs_dir> <root_need_name>}"
ROOT_NEED="${2:?Usage: create-tree-of-needs.sh <stage_01_outputs_dir> <root_need_name>}"
OUTPUTS_DIR="${OUTPUTS_DIR%/}"

TON="$OUTPUTS_DIR/requests/tree_of_needs"

echo "=== Create Tree of Needs ==="
echo "Location: $TON"
echo "Root need: $ROOT_NEED"
echo ""

# Verify outputs dir exists
if [ ! -d "$OUTPUTS_DIR" ]; then
  echo "  [ERROR] Outputs directory does not exist: $OUTPUTS_DIR"
  exit 1
fi

# Create structure
mkdir -p "$TON/_meta"
mkdir -p "$TON/00_$ROOT_NEED"

# _meta/VERSION.md
cat > "$TON/_meta/VERSION.md" << 'VEOF'
# Tree of Needs — Version

**Version**: 1.0
**Status**: Initial scaffold
**Created**: $(date +%Y-%m-%d)

## History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Initial | Scaffold created |
VEOF

# _meta/CHANGELOG.md
cat > "$TON/_meta/CHANGELOG.md" << 'CEOF'
# Tree of Needs — Changelog

## [1.0] - Initial

- Created tree_of_needs scaffold
- Root need established
CEOF

# _meta/DEPENDENCIES.md
cat > "$TON/_meta/DEPENDENCIES.md" << 'DEOF'
# Tree of Needs — Dependencies

## Upstream Dependencies

(None yet — this is the root requirements document)

## Downstream Consumers

| Consumer | How They Use This |
|----------|-------------------|
| stage_02_research | Research each need |
| stage_04_planning | Plan implementation |
| stage_05_design | Design solutions |
DEOF

# Root need README.md
cat > "$TON/00_$ROOT_NEED/README.md" << EOF
# Root Need: $ROOT_NEED

## Description

(Describe the root need here)

## Branches

| Branch | Name | Description |
|--------|------|-------------|
| 01_* | (TBD) | (Add branches as needed) |

## Success Criteria

- (Define what success looks like for this root need)
EOF

echo "  [OK] Created tree_of_needs scaffold"
echo ""
echo "Next steps:"
echo "  1. Edit 00_$ROOT_NEED/README.md with root need description"
echo "  2. Create branch directories: 01_<branch_name>/, 02_<branch_name>/, ..."
echo "  3. Add leaf needs in each branch: 01_<need>/, 02_<need>/, ..."
echo "  4. Add README.md, requirements/, and user_stories/ to each leaf need"
echo "     (requirements/ gets REQ-NN_name.md files; user_stories/ gets US-NN_name.md files)"
EOF