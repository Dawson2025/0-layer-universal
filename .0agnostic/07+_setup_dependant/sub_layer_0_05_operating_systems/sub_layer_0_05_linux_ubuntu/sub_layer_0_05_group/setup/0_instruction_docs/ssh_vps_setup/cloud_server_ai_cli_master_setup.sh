#!/bin/bash
# resource_id: "e4aa7148-7e19-40d0-aabc-2a91e5fc76da"
# resource_type: "script"
# resource_name: "cloud_server_ai_cli_master_setup"
# =============================================================================
# CLOUD SERVER AI CLI MASTER SETUP
# Layer: 0 (Universal)
# Stage: 0.05 Setup
# Purpose: Set up Gemini CLI, Claude Code CLI, and Codex CLI on cloud server
# =============================================================================
#
# USAGE:
#   chmod +x cloud_server_ai_cli_master_setup.sh
#   ./cloud_server_ai_cli_master_setup.sh [stage]
#
# STAGES:
#   0 or no arg - Run all stages
#   1 - Prerequisites (Node.js, npm)
#   2 - Gemini CLI setup
#   3 - Claude Code CLI setup
#   4 - Codex CLI setup
#   5 - Verification
#
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# API Keys - UPDATE THESE
GOOGLE_API_KEY="AIzaSyCoGDYmISEIK4PI-mQno4EhShL0Jp6RY2I"
# ANTHROPIC_API_KEY=""  # Set this if you have one, or use browser login
# OPENAI_API_KEY=""     # Set this for Codex

log_stage() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}STAGE $1: $2${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

log_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

log_error() {
    echo -e "${RED}✗ $1${NC}"
}

# =============================================================================
# STAGE 1: Prerequisites
# =============================================================================
stage_1_prerequisites() {
    log_stage "1" "Installing Prerequisites"

    # Check if Node.js is installed
    if command -v node &> /dev/null; then
        NODE_VERSION=$(node --version)
        log_success "Node.js already installed: $NODE_VERSION"
    else
        log_warning "Node.js not found. Installing..."

        # Install nvm
        if [ ! -d "$HOME/.nvm" ]; then
            curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
            export NVM_DIR="$HOME/.nvm"
            [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        fi

        # Install latest LTS
        nvm install --lts
        nvm use --lts
        log_success "Node.js installed: $(node --version)"
    fi

    # Check npm
    if command -v npm &> /dev/null; then
        log_success "npm available: $(npm --version)"
    else
        log_error "npm not found. Please install Node.js properly."
        exit 1
    fi
}

# =============================================================================
# STAGE 2: Gemini CLI Setup
# =============================================================================
stage_2_gemini() {
    log_stage "2" "Setting up Gemini CLI"

    # Set environment variable
    export GOOGLE_API_KEY="$GOOGLE_API_KEY"

    # Add to bashrc if not already there
    if ! grep -q "GOOGLE_API_KEY" ~/.bashrc 2>/dev/null; then
        echo "export GOOGLE_API_KEY=\"$GOOGLE_API_KEY\"" >> ~/.bashrc
        log_success "Added GOOGLE_API_KEY to ~/.bashrc"
    else
        log_success "GOOGLE_API_KEY already in ~/.bashrc"
    fi

    # Install Gemini CLI
    echo "Installing Gemini CLI..."
    npm install -g @google/gemini-cli

    # Verify
    if command -v gemini &> /dev/null; then
        log_success "Gemini CLI installed: $(gemini --version)"
    else
        log_error "Gemini CLI installation failed"
        return 1
    fi

    # Test
    echo "Testing Gemini CLI..."
    gemini "Say 'Gemini CLI working' in 5 words or less" && log_success "Gemini CLI working!"
}

# =============================================================================
# STAGE 3: Claude Code CLI Setup
# =============================================================================
stage_3_claude() {
    log_stage "3" "Setting up Claude Code CLI"

    # Install Claude Code CLI
    echo "Installing Claude Code CLI..."
    npm install -g @anthropic-ai/claude-code

    # Verify installation
    if command -v claude &> /dev/null; then
        log_success "Claude Code CLI installed: $(claude --version 2>/dev/null || echo 'version check requires auth')"
    else
        log_error "Claude Code CLI installation failed"
        return 1
    fi

    # Note about authentication
    echo ""
    log_warning "Claude Code requires authentication on first run."
    echo "Run 'claude' and follow the browser login prompts."
    echo "Or set ANTHROPIC_API_KEY environment variable."
}

# =============================================================================
# STAGE 4: Codex CLI Setup
# =============================================================================
stage_4_codex() {
    log_stage "4" "Setting up Codex CLI"

    # Install Codex CLI
    echo "Installing OpenAI Codex CLI..."
    npm install -g @openai/codex

    # Verify
    if command -v codex &> /dev/null; then
        log_success "Codex CLI installed: $(codex --version 2>/dev/null || echo 'installed')"
    else
        log_warning "Codex CLI may need different package name or manual setup"
    fi

    # Note about API key
    echo ""
    log_warning "Codex requires OPENAI_API_KEY environment variable."
    echo "Get your key from: https://platform.openai.com/api-keys"
    echo "Then run: export OPENAI_API_KEY='your-key-here'"
}

# =============================================================================
# STAGE 5: Verification
# =============================================================================
stage_5_verify() {
    log_stage "5" "Verification"

    echo "Checking installed CLIs:"
    echo ""

    # Gemini
    if command -v gemini &> /dev/null; then
        log_success "Gemini CLI: $(gemini --version 2>/dev/null || echo 'installed')"
    else
        log_error "Gemini CLI: NOT FOUND"
    fi

    # Claude
    if command -v claude &> /dev/null; then
        log_success "Claude Code CLI: installed"
    else
        log_error "Claude Code CLI: NOT FOUND"
    fi

    # Codex
    if command -v codex &> /dev/null; then
        log_success "Codex CLI: installed"
    else
        log_warning "Codex CLI: NOT FOUND (may need different setup)"
    fi

    echo ""
    echo "Environment variables:"
    [ -n "$GOOGLE_API_KEY" ] && log_success "GOOGLE_API_KEY: set" || log_warning "GOOGLE_API_KEY: not set"
    [ -n "$ANTHROPIC_API_KEY" ] && log_success "ANTHROPIC_API_KEY: set" || log_warning "ANTHROPIC_API_KEY: not set (use browser login)"
    [ -n "$OPENAI_API_KEY" ] && log_success "OPENAI_API_KEY: set" || log_warning "OPENAI_API_KEY: not set"

    echo ""
    echo "============================================"
    echo "Setup complete! Reload your shell:"
    echo "  source ~/.bashrc"
    echo ""
    echo "Then use:"
    echo "  gemini \"your prompt\""
    echo "  claude"
    echo "  codex \"your prompt\""
    echo "============================================"
}

# =============================================================================
# MAIN
# =============================================================================
main() {
    STAGE="${1:-0}"

    echo "============================================"
    echo "CLOUD SERVER AI CLI SETUP"
    echo "============================================"
    echo "Stage: $STAGE"
    echo ""

    case $STAGE in
        0)
            stage_1_prerequisites
            stage_2_gemini
            stage_3_claude
            stage_4_codex
            stage_5_verify
            ;;
        1) stage_1_prerequisites ;;
        2) stage_2_gemini ;;
        3) stage_3_claude ;;
        4) stage_4_codex ;;
        5) stage_5_verify ;;
        *)
            echo "Unknown stage: $STAGE"
            echo "Usage: $0 [0-5]"
            exit 1
            ;;
    esac
}

main "$@"
