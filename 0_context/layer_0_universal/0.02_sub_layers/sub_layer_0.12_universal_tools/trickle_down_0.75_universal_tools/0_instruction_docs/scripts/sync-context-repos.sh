#!/bin/bash
# Sync workflow for universal-context and setup-hub repositories
# This script helps keep both context repositories in sync

set -e

REPO1="/home/dawson/dawson-workspace/code/0-universal-context"
REPO2="/home/dawson/dawson-workspace/code/setup-hub"

echo "🔄 Syncing context repositories..."
echo ""

# Function to sync a repository
sync_repo() {
    local repo_path=$1
    local repo_name=$2
    
    echo "📦 Syncing $repo_name..."
    cd "$repo_path" || exit 1
    
    # Check for uncommitted changes
    if ! git diff-index --quiet HEAD --; then
        echo "  ⚠️  Warning: Uncommitted changes detected in $repo_name"
        echo "  📝 Status:"
        git status --short
        echo ""
    fi
    
    # Pull latest changes
    echo "  ⬇️  Pulling latest changes..."
    git pull origin main || git pull origin master
    
    echo "  ✅ $repo_name synced"
    echo ""
}

# Sync both repositories
sync_repo "$REPO1" "0-universal-context"
sync_repo "$REPO2" "setup-hub"

echo "✨ Sync complete!"
echo ""
echo "📊 Repository status:"
cd "$REPO1" && echo "  0-universal-context: $(git log -1 --oneline)"
cd "$REPO2" && echo "  setup-hub: $(git log -1 --oneline)"

