# stage_-1_00_registry

**Data Only** - This is a registry, not a manager.

## Purpose

Contains stage definitions, metadata, and schema for this project's stages.

## Contents

- `outputs/` - Stage registry data files
- `hand_off_documents/` - Legacy (registry doesn't process handoffs)

## Manager Location

The Stages Manager is at the parent level:
- **Manager CLAUDE.md**: `../CLAUDE.md`
- **Manager .claude/**: `../.claude/`

## Why Registry Pattern?

Position 00 in any container is reserved for registry data only.
The container itself (parent folder) acts as the manager.
This separation ensures:
- Clear distinction between data and behavior
- Manager has full visibility of all children
- No special status for position 00
