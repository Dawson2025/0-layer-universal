#!/usr/bin/env python3
"""
Create private GitHub repositories for AI context
Uses GitHub REST API
"""
import requests
import json
import sys

# Token from GITHUB_TOKEN_INFO.md
GITHUB_TOKEN = "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"

def create_repo(owner, name, description, is_org=False):
    """Create a private GitHub repository"""
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    if is_org:
        url = f"https://api.github.com/orgs/{owner}/repos"
    else:
        url = "https://api.github.com/user/repos"
    
    data = {
        "name": name,
        "description": description,
        "private": True,
        "auto_init": False
    }
    
    print(f"\nCreating repository: {owner}/{name}")
    print(f"  Description: {description}")
    print(f"  Type: {'Organization' if is_org else 'Personal'}")
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        repo_data = response.json()
        print(f"  ✓ Created successfully!")
        print(f"  URL: {repo_data['html_url']}")
        print(f"  Clone URL: {repo_data['clone_url']}")
        return repo_data
    elif response.status_code == 422:
        # Repository already exists
        print(f"  ⚠ Repository already exists")
        # Try to get the existing repo info
        get_url = f"https://api.github.com/repos/{owner}/{name}"
        get_response = requests.get(get_url, headers=headers)
        if get_response.status_code == 200:
            repo_data = get_response.json()
            print(f"  URL: {repo_data['html_url']}")
            print(f"  Clone URL: {repo_data['clone_url']}")
            return repo_data
        return None
    else:
        print(f"  ✗ Failed with status code: {response.status_code}")
        print(f"  Response: {response.text}")
        return None

def main():
    print("=" * 70)
    print("PHASE 2: CREATE PRIVATE GITHUB REPOSITORIES")
    print("=" * 70)
    
    # Repository 1: Universal Context (Personal)
    print("\n### Repository 1: Universal AI Context ###")
    repo1 = create_repo(
        owner="Dawson2025",
        name="0-universal-context",
        description="Universal AI context documentation for all projects",
        is_org=False
    )
    
    # Repository 2: Project Context (Organization)
    print("\n### Repository 2: Project-Specific AI Context ###")
    repo2 = create_repo(
        owner="byui-math-dept",
        name="1-project-context-pac20026_fall2025",
        description="AI context documentation for pac20026_fall2025 DS250 portfolio",
        is_org=True
    )
    
    print("\n" + "=" * 70)
    if repo1 and repo2:
        print("✓ PHASE 2 COMPLETE!")
        print("=" * 70)
        print("\nRepositories created:")
        print(f"  1. https://github.com/Dawson2025/0-universal-context (private)")
        print(f"  2. https://github.com/byui-math-dept/1-project-context-pac20026_fall2025 (private)")
        print("\nNext: Phase 3 - Initialize Git in context directories")
    else:
        print("⚠ Some repositories may need attention")
        print("=" * 70)

if __name__ == "__main__":
    main()
















