# Reference Format Standard -- Requirements Index

**Need**: [Reference Format Standard](../README.md)

## Overview

These requirements establish a uniform syntax for how files in different tiers reference each other, replacing the ad hoc reference styles that currently make automated validation impossible. They define both the format itself -- script-parseable, relative-path-based, with target file, section, and description -- and the directional rules that govern reference flow. The constraint that references only flow downward (pointers reference knowledge, knowledge references stage outputs) prevents circular coupling and keeps stage outputs self-contained.

## Key Themes

- **Parseable Syntax**: Cross-tier references follow a standard format that scripts can extract and validate, not just human-readable prose
- **Directional Flow**: References flow strictly downward -- 0AGNOSTIC.md references knowledge files, knowledge files reference stage outputs -- and upward references are forbidden to prevent coupling

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Reference Format | Standard syntax for cross-tier links | [REQ-01_reference_format.md](./REQ-01_reference_format.md) |
| REQ-02 | Directional Rules | Rules governing which direction references flow | [REQ-02_directional_rules.md](./REQ-02_directional_rules.md) |
