---
resource_id: "d8687c66-f763-42c3-8e98-a148e10e716d"
resource_type: "readme
output"
resource_name: "README"
---
# Core System (01-05)

<!-- section_id: "7b7b629d-602a-4c72-b522-36b98a567a07" -->
## What This Contains

The core system is the **unified source of truth** for all context. It contains the five foundational sections from `.0agnostic/`:

- **01_knowledge/**: Domain knowledge, principles, documentation, resources
- **02_rules/**: Static (always-on) and dynamic (trigger-based) constraints
- **03_protocols/**: Step-by-step workflows and procedures
- **04_episodic_memory/**: Session history and accumulated learnings
- **05_handoff_documents/**: Communication across entities and stages

<!-- section_id: "02a98a32-0834-4f12-b910-e41c3e5007ad" -->
## Overview

See `00_core_system_overview/README.md` for detailed explanation of:
- What makes this the source of truth
- Why it's organized this way
- How it gets used by subsequent layers

<!-- section_id: "bb0f61f5-74ed-419d-a973-a8a3a1c72fdd" -->
## Subdirectories

Each numbered subdirectory corresponds to a section of `.0agnostic/`:

- **01_knowledge/** → `.0agnostic/01_knowledge/`
- **02_rules/** → `.0agnostic/02_rules/`
- **03_protocols/** → `.0agnostic/03_protocols/`
- **04_episodic_memory/** → `.0agnostic/04_episodic_memory/`
- **05_handoff_documents/** → `.0agnostic/05_handoff_documents/`

<!-- section_id: "b378c47b-2588-4802-8329-e67c74ba3ba5" -->
## Next Step

After understanding core system, see `02_setup_dependent/` to understand how environment-specific adaptations build on this foundation.
