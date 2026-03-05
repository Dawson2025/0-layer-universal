#!/bin/bash
# resource_id: "a6050f06-f286-4a62-a330-7653fa25f73b"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 11_archives stage"

# Add custom initialization here
