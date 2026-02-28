# Dependency Diagram Reference

Visual representations of request dependencies for the better_ai_system project.

## Current Project Dependencies

```
                         ┌─────────────────────────┐
                         │       REQ-01            │
                         │  Layer-Stage System     │
                         │     (Foundation)        │
                         └───────────┬─────────────┘
                                     │
            ┌────────────────────────┼────────────────────────┐
            │                        │                        │
            ▼                        ▼                        ▼
   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
   │     REQ-05      │    │     REQ-06      │    │     REQ-07      │
   │  Documentation  │    │  Context System │    │  Rules System   │
   └────────┬────────┘    └────────┬────────┘    └────────┬────────┘
            │                      │                      │
            └──────────────────────┼──────────────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │       REQ-08        │
                         │  Automation System  │
                         │   (Enforcement)     │
                         └───────────┬─────────┘
                                     │
            ┌────────────────────────┼────────────────────────┐
            │                        │                        │
            ▼                        ▼                        ▼
   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
   │     REQ-02      │    │     REQ-03      │    │     REQ-04      │
   │  Setup System   │    │ Manager Hierarchy│   │  Memory System  │
   └─────────────────┘    └─────────────────┘    │   (Research)    │
                                                 └─────────────────┘
```

## Simplified View

```
Foundation:     REQ-01
                   │
                   ▼
Parallel:       REQ-05, REQ-06, REQ-07
                   │
                   ▼
Enforcement:    REQ-08
                   │
                   ▼
End Features:   REQ-02, REQ-03, REQ-04
```

## Critical Path

```
REQ-01 ──► REQ-06 ──► REQ-08 ──► REQ-03 ──► REQ-04
   │                     │
   │                     └──► REQ-02
   │
   └──► REQ-05, REQ-07 (parallel, feed into REQ-08)
```

## Legend

```
┌─────────┐
│ REQ-XX  │  = Request box
└────┬────┘
     │
     ▼         = Dependency arrow (points to dependent)

(Foundation)  = Role annotation
```

## Diagram Conventions

1. **Top-down flow**: Dependencies flow downward
2. **Parallel items**: Items on same horizontal level can be done in parallel
3. **Critical path**: Longest chain of dependencies
4. **Foundation**: Requests with no dependencies
5. **End features**: Requests that don't block others

## How to Update This Diagram

When adding a new request:

1. Identify what it depends on
2. Identify what depends on it
3. Place it at the appropriate level
4. Draw arrows to/from related requests
5. Update the critical path if it changes

## ASCII Diagram Building Blocks

```
Boxes:
┌─────────┐
│  Text   │
└─────────┘

Arrows:
    │
    ▼

    ──►

Branching:
    ┌───────┬───────┐
    │       │       │
    ▼       ▼       ▼

Merging:
    │       │       │
    └───────┼───────┘
            │
            ▼
```
