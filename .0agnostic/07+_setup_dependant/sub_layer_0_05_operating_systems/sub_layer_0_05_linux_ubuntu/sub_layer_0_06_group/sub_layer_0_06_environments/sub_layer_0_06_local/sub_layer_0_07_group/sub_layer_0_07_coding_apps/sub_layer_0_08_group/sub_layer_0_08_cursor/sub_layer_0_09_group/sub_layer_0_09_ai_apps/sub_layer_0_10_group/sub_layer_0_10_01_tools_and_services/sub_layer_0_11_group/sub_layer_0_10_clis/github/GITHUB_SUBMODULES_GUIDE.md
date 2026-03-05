---
resource_id: "fefc5164-69c5-4194-a1b9-68668f4d5c96"
resource_type: "document"
resource_name: "GITHUB_SUBMODULES_GUIDE"
---
# GitHub Repositories and Submodules Guide

## Overview

This guide documents how to create GitHub repositories and set up git submodules for a nested project structure using the `gh` CLI and git commands.

## Prerequisites

- `gh` CLI installed and authenticated (see GH_CLI_SETUP.md)
- Git configured with gh credential helper: `gh auth setup-git`

## Creating GitHub Repositories

### Create a Private Repository

```bash
gh repo create username/repo-name --private --description "Repository description"
```

### Create a Public Repository

```bash
gh repo create username/repo-name --public --description "Repository description"
```

### Verify Creation

```bash
gh repo view username/repo-name
```

## Setting Up Submodules

### Adding a Submodule

```bash
cd /path/to/parent-repo
git submodule add https://github.com/username/child-repo.git path/to/submodule
```

### Initialize and Update Submodules

```bash
# Initialize submodules after cloning
git submodule update --init

# Initialize nested submodules recursively
git submodule update --init --recursive
```

### Cloning a Repo with Submodules

```bash
git clone --recurse-submodules https://github.com/username/repo.git
```

## Working with Nested Submodules

### Project Structure Example

```
parent-repo/
├── .gitmodules
├── sub_projects/
│   ├── project_a/          → github.com/user/project-a.git
│   │   ├── .gitmodules
│   │   └── nested_projects/
│   │       ├── component_1/ → github.com/user/component-1.git
│   │       └── component_2/ → github.com/user/component-2.git
│   └── project_b/          → github.com/user/project-b.git
```

### Creating Nested Structure

1. **Create all repos first:**
```bash
gh repo create user/parent-repo --private
gh repo create user/project-a --private
gh repo create user/project-b --private
gh repo create user/component-1 --private
gh repo create user/component-2 --private
```

2. **Initialize parent and add first-level submodules:**
```bash
cd parent-repo
git submodule add https://github.com/user/project-a.git sub_projects/project_a
git submodule add https://github.com/user/project-b.git sub_projects/project_b
```

3. **Add nested submodules inside project_a:**
```bash
cd sub_projects/project_a
git submodule add https://github.com/user/component-1.git nested_projects/component_1
git submodule add https://github.com/user/component-2.git nested_projects/component_2
git add -A && git commit -m "Add nested submodules"
git push
```

4. **Update parent to track new commits:**
```bash
cd ../..  # back to parent-repo
git add sub_projects/project_a
git commit -m "Update project_a submodule"
git push
```

## Common Issues and Fixes

### "Already exists in the index" Error

```bash
# Remove from index first
git rm --cached path/to/submodule

# Then add as submodule
git submodule add https://github.com/user/repo.git path/to/submodule
```

### "Git directory found locally" Error

```bash
# Clean up stale module references
rm -rf .git/modules/path/to/submodule

# Then add submodule
git submodule add https://github.com/user/repo.git path/to/submodule
```

### Empty Submodule After Clone

```bash
git submodule update --init --recursive
```

### Submodule Points to Wrong Commit

```bash
cd path/to/submodule
git checkout main
git pull
cd ..
git add path/to/submodule
git commit -m "Update submodule to latest"
```

## Moving/Renaming Submodules

When restructuring projects that are already submodules:

1. **Deinit the submodule:**
```bash
git submodule deinit -f path/to/old/location
```

2. **Remove from git:**
```bash
git rm --cached path/to/old/location
```

3. **Remove module data:**
```bash
rm -rf .git/modules/path/to/old/location
```

4. **Update .gitmodules manually** (remove old entry)

5. **Add at new location:**
```bash
git submodule add https://github.com/user/repo.git path/to/new/location
```

## Committing Changes

Always commit changes in this order:
1. Commit and push changes in the innermost submodule first
2. Work outward to parent repos
3. Each parent needs to commit the updated submodule reference

```bash
# In submodule
cd path/to/submodule
git add -A && git commit -m "Changes in submodule"
git push

# In parent
cd ..
git add path/to/submodule
git commit -m "Update submodule reference"
git push
```

## Best Practices

1. **Always use `--recursive`** when cloning repos with nested submodules
2. **Commit from inside out** - innermost submodule changes first
3. **Keep submodule URLs consistent** - use HTTPS for portability
4. **Document your structure** - maintain a README showing the submodule hierarchy
5. **Use meaningful commit messages** when updating submodule references

## Real-World Example: School Project Structure

This structure was created on 2026-01-14:

```
1_school/                              → github.com/Dawson2025/1-school.git
├── layer_2_sub_projects/
│   ├── layer_2_sub_project_classes/   → github.com/Dawson2025/school-classes.git
│   │   └── layer_3_subx2_projects/
│   │       ├── layer_3_subx2_project_computer_science/
│   │       │                          → github.com/Dawson2025/school-computer-science.git
│   │       └── layer_3_subx2_project_math/
│   │                                  → github.com/Dawson2025/school-math.git
│   └── layer_2_sub_project_planning_and_scheduling/
│                                      → github.com/Dawson2025/school-planning-and-scheduling.git
```

Commands used:
```bash
# Create repos
gh repo create Dawson2025/school-classes --private
gh repo create Dawson2025/school-planning-and-scheduling --private

# Add as submodules
cd 1_school
git submodule add https://github.com/Dawson2025/school-classes.git \
    layer_2_sub_projects/layer_2_sub_project_classes
git submodule add https://github.com/Dawson2025/school-planning-and-scheduling.git \
    layer_2_sub_projects/layer_2_sub_project_planning_and_scheduling

# Initialize nested submodules
git submodule update --init --recursive
```
