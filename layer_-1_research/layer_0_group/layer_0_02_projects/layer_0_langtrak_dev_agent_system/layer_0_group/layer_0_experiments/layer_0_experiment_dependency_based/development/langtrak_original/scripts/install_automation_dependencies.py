#!/usr/bin/env python3
# resource_id: "d41d5736-cd53-4579-b359-2fcd8d847e43"
# resource_type: "document"
# resource_name: "install_automation_dependencies"

"""
install_automation_dependencies.py

Install required dependencies for automated Google Sign-In setup.
This script installs all necessary packages for browser automation.
"""

import sys
import subprocess
import os
from pathlib import Path

def run_command(command: list, description: str) -> bool:
    """Run a command and return success status."""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def install_python_packages():
    """Install required Python packages."""
    packages = [
        "playwright",
        "pyautogui",
        "keyring",
        "asyncio",
        "aiohttp",
        "selenium",
        "beautifulsoup4",
        "requests"
    ]
    
    print("🐍 Installing Python packages...")
    
    # Try pip install first
    for package in packages:
        if not run_command([sys.executable, "-m", "pip", "install", package], f"Installing {package}"):
            # Try with --break-system-packages if in externally managed environment
            if not run_command([sys.executable, "-m", "pip", "install", package, "--break-system-packages"], f"Installing {package} (with --break-system-packages)"):
                print(f"⚠️  Failed to install {package}, please install manually")
    
    # Install Playwright browsers
    print("🎭 Installing Playwright browsers...")
    run_command([sys.executable, "-m", "playwright", "install"], "Installing Playwright browsers")
    run_command([sys.executable, "-m", "playwright", "install", "chromium"], "Installing Chromium browser")

def install_system_dependencies():
    """Install system dependencies."""
    print("🖥️  Installing system dependencies...")
    
    # Check if we're on Ubuntu/Debian
    if os.path.exists("/etc/debian_version"):
        system_packages = [
            "python3-tk",  # For PyAutoGUI
            "xclip",       # For clipboard operations
            "xdotool",     # For X11 automation
            "scrot",       # For screenshots
            "imagemagick", # For image processing
        ]
        
        for package in system_packages:
            run_command(["sudo", "apt", "update"], "Updating package list")
            run_command(["sudo", "apt", "install", "-y", package], f"Installing {package}")
    
    # Check if we're on macOS
    elif sys.platform == "darwin":
        run_command(["brew", "install", "python-tk"], "Installing python-tk via Homebrew")
    
    # Check if we're on Windows
    elif sys.platform == "win32":
        print("Windows detected - system dependencies should be handled automatically")

def setup_environment():
    """Setup environment variables and configuration."""
    print("🔧 Setting up environment...")
    
    # Set up PyAutoGUI settings
    try:
        import pyautogui
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        print("✅ PyAutoGUI configured")
    except ImportError:
        print("⚠️  PyAutoGUI not available")
    
    # Set up Playwright environment
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = str(Path.home() / ".playwright")
    print("✅ Playwright environment configured")

def verify_installation():
    """Verify that all dependencies are properly installed."""
    print("🔍 Verifying installation...")
    
    # Check Python packages
    packages_to_check = [
        ("playwright", "Playwright"),
        ("pyautogui", "PyAutoGUI"),
        ("keyring", "Keyring"),
        ("selenium", "Selenium"),
        ("bs4", "BeautifulSoup4"),
        ("requests", "Requests")
    ]
    
    all_installed = True
    for package, name in packages_to_check:
        try:
            __import__(package)
            print(f"✅ {name} is available")
        except ImportError:
            print(f"❌ {name} is not available")
            all_installed = False
    
    # Check Playwright browsers
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            browser.close()
        print("✅ Playwright Chromium is working")
    except Exception as e:
        print(f"❌ Playwright Chromium test failed: {e}")
        all_installed = False
    
    return all_installed

def create_requirements_file():
    """Create a requirements.txt file for the automation dependencies."""
    requirements = """# Browser Automation Dependencies
playwright>=1.40.0
pyautogui>=0.9.54
keyring>=24.0.0
selenium>=4.15.0
beautifulsoup4>=4.12.0
requests>=2.31.0
aiohttp>=3.9.0

# Optional dependencies for enhanced functionality
pillow>=10.0.0
opencv-python>=4.8.0
pytesseract>=0.3.10
"""
    
    with open("requirements-automation.txt", "w") as f:
        f.write(requirements)
    
    print("✅ Created requirements-automation.txt")

def main():
    """Main installation function."""
    print("🚀 Installing Browser Automation Dependencies")
    print("=" * 60)
    
    # Install Python packages
    install_python_packages()
    
    # Install system dependencies
    install_system_dependencies()
    
    # Setup environment
    setup_environment()
    
    # Create requirements file
    create_requirements_file()
    
    # Verify installation
    if verify_installation():
        print("\n🎉 All dependencies installed successfully!")
        print("\n📋 Next steps:")
        print("1. Run: python3 scripts/automated_google_setup.py")
        print("2. Or run individual setup scripts as needed")
        print("3. Check the logs for any issues")
    else:
        print("\n⚠️  Some dependencies failed to install")
        print("Please check the error messages above and install manually if needed")
        sys.exit(1)

if __name__ == "__main__":
    main()
