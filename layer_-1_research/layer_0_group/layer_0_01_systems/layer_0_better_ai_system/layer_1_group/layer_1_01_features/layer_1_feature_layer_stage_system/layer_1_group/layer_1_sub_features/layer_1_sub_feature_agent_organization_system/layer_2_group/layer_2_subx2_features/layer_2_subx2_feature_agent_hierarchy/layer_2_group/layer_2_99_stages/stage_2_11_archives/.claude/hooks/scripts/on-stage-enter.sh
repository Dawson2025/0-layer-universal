#!/bin/bash
# resource_id: "9622d152-69be-4481-8945-9702fa63ba04"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 11_archives stage"

# Add custom initialization here
