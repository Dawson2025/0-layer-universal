#!/bin/bash
# resource_id: "04c44e5c-9c79-4da4-bd7a-e957e78efd0f"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 07_testing stage"

# Add custom initialization here
