#!/bin/bash
# resource_id: "99987129-8381-4302-905e-6bcd8b5062a4"
# resource_type: "script"
# resource_name: "ai_sudo_helper"
# AI Agent Sudo Helper
# This script provides secure sudo access for AI agents

# Function to run sudo commands securely
run_sudo() {
    local command="$1"
    
    # Try environment variable first
    if [ -n "$SUDO_PASSWORD" ]; then
        echo "$SUDO_PASSWORD" | sudo -S $command
        return $?
    fi
    
    # Try secure file
    if [ -f ~/.ai_sudo_password ]; then
        cat ~/.ai_sudo_password | sudo -S $command
        return $?
    fi
    
    # Fallback: prompt for password
    echo "❌ No sudo password configured. Please run: ./scripts/setup_sudo_password.sh"
    return 1
}

# Function to install packages
install_package() {
    local package="$1"
    echo "📦 Installing package: $package"
    run_sudo "apt update && apt install -y $package"
}

# Function to check if package is installed
is_package_installed() {
    local package="$1"
    dpkg -l | grep -q "^ii  $package "
}

# Main execution
case "$1" in
    "install")
        install_package "$2"
        ;;
    "check")
        is_package_installed "$2"
        ;;
    "run")
        shift
        run_sudo "$@"
        ;;
    *)
        echo "Usage: $0 {install|check|run} [package/command]"
        echo "  install <package>  - Install a package"
        echo "  check <package>    - Check if package is installed"
        echo "  run <command>      - Run a sudo command"
        exit 1
        ;;
esac
