# Layer 0.01 to Specific Handoff

## Purpose
This directory contains handoff documents for transitioning context from Layer 0 universal config to environment-specific configurations.

## When to Use
- When universal settings need environment-specific overrides
- When new environments are being configured
- When platform-specific adaptations are required

## Handoff Protocol
1. Identify the universal setting being overridden
2. Document the specific override and rationale
3. Create the specific config in the appropriate path
4. Update this handoff with the mapping

## Environment Path Structure
```
specific/
  +-- os/
        +-- wsl/
        +-- linux_ubuntu/
        +-- macos/
        +-- windows/
              +-- environment/
                    +-- local/
                    +-- cloud/
                    +-- ci_cd/
```

## Current Handoffs
- (Add active handoff documents here)

## Completed Handoffs
- (Move completed handoffs to archives)
