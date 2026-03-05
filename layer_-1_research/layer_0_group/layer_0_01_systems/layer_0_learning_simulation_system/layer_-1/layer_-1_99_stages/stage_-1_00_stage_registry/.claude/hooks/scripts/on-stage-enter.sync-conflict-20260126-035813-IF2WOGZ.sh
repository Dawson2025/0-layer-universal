#!/bin/bash
# resource_id: "fa607884-393c-45af-a86f-02245695c87b"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-035813-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 00_stage_registry stage"

# Add custom initialization here
