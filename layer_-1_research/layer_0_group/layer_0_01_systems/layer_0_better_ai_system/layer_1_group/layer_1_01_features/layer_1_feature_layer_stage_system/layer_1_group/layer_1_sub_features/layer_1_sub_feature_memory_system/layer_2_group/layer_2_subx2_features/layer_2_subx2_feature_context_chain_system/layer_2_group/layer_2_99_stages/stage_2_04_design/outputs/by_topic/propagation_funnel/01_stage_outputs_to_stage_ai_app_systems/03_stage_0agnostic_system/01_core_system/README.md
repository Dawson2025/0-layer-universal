---
resource_id: "d8687c66-f763-42c3-8e98-a148e10e716d"
resource_type: "readme
output"
resource_name: "README"
---
# Core System (01-05)

## What This Contains

The core system is the **unified source of truth** for all context. It contains the five foundational sections from `.0agnostic/`:

- **01_knowledge/**: Domain knowledge, principles, documentation, resources
- **02_rules/**: Static (always-on) and dynamic (trigger-based) constraints
- **03_protocols/**: Step-by-step workflows and procedures
- **04_episodic_memory/**: Session history and accumulated learnings
- **05_handoff_documents/**: Communication across entities and stages

## Overview

See `00_core_system_overview/README.md` for detailed explanation of:
- What makes this the source of truth
- Why it's organized this way
- How it gets used by subsequent layers

## Subdirectories

Each numbered subdirectory corresponds to a section of `.0agnostic/`:

- **01_knowledge/** → `.0agnostic/01_knowledge/`
- **02_rules/** → `.0agnostic/02_rules/`
- **03_protocols/** → `.0agnostic/03_protocols/`
- **04_episodic_memory/** → `.0agnostic/04_episodic_memory/`
- **05_handoff_documents/** → `.0agnostic/05_handoff_documents/`

## Next Step

After understanding core system, see `02_setup_dependent/` to understand how environment-specific adaptations build on this foundation.
