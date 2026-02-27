#!/usr/bin/env python33

"""
run_tests.py

Test runner for Firebase instance tests following project testing standards.
Provides comprehensive test execution with proper reporting and coverage.
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

def run_unit_tests(verbose=False, coverage=False):
    """Run unit tests for Firebase instance."""
    print("🧪 Running Firebase Instance Unit Tests...")
    print("=" * 50)
    
    cmd = ["python3", "-m", "pytest", "test_firebase_provider.py", "test_firebase_config.py"]
    
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.extend(["--cov=firebase_provider", "--cov=firebase_config", "--cov-report=html", "--cov-report=term"])
    
    cmd.extend([
        "-m", "unit",
        "--tb=short",
        "--strict-markers",
        "--disable-warnings"
    ])
    
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0

def run_integration_tests(verbose=False):
    """Run integration tests for Firebase instance."""
    print("🔗 Running Firebase Instance Integration Tests...")
    print("=" * 50)
    
    cmd = ["python3", "-m", "pytest", "test_firebase_provider.py", "test_firebase_config.py"]
    
    if verbose:
        cmd.append("-v")
    
    cmd.extend([
        "-m", "integration",
        "--tb=short",
        "--strict-markers",
        "--disable-warnings"
    ])
    
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0

def run_all_tests(verbose=False, coverage=False):
    """Run all Firebase instance tests."""
    print("🚀 Running All Firebase Instance Tests...")
    print("=" * 50)
    
    cmd = ["python3", "-m", "pytest", "test_firebase_provider.py", "test_firebase_config.py"]
    
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.extend(["--cov=firebase_provider", "--cov=firebase_config", "--cov-report=html", "--cov-report=term"])
    
    cmd.extend([
        "--tb=short",
        "--strict-markers",
        "--disable-warnings"
    ])
    
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0

def run_specific_test(test_file, verbose=False):
    """Run a specific test file."""
    print(f"🎯 Running Specific Test: {test_file}")
    print("=" * 50)
    
    cmd = ["python3", "-m", "pytest", test_file]
    
    if verbose:
        cmd.append("-v")
    
    cmd.extend([
        "--tb=short",
        "--strict-markers",
        "--disable-warnings"
    ])
    
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0

def check_test_environment():
    """Check if the test environment is properly set up."""
    print("🔍 Checking Test Environment...")
    print("=" * 50)
    
    # Check Python version
    python3_version = sys.version_info
    print(f"Python Version: {python3_version.major}.{python3_version.minor}.{python3_version.micro}")
    
    if python3_version < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    
    # Check required packages
    required_packages = ["pytest", "pytest-cov", "pytest-asyncio"]
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} not installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Install with: pip install " + " ".join(missing_packages))
        return False
    
    # Check test files exist
    test_files = ["test_firebase_provider.py", "test_firebase_config.py", "conftest.py"]
    for test_file in test_files:
        if Path(test_file).exists():
            print(f"✅ {test_file} found")
        else:
            print(f"❌ {test_file} not found")
            return False
    
    print("\n✅ Test environment is ready!")
    return True

def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(description="Firebase Instance Test Runner")
    parser.add_argument("--unit", action="store_true", help="Run unit tests only")
    parser.add_argument("--integration", action="store_true", help="Run integration tests only")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    parser.add_argument("--file", type=str, help="Run specific test file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--coverage", "-c", action="store_true", help="Generate coverage report")
    parser.add_argument("--check", action="store_true", help="Check test environment")
    
    args = parser.parse_args()
    
    # Change to test directory
    os.chdir(Path(__file__).parent)
    
    if args.check:
        success = check_test_environment()
        sys.exit(0 if success else 1)
    
    if args.unit:
        success = run_unit_tests(verbose=args.verbose, coverage=args.coverage)
    elif args.integration:
        success = run_integration_tests(verbose=args.verbose)
    elif args.file:
        success = run_specific_test(args.file, verbose=args.verbose)
    elif args.all:
        success = run_all_tests(verbose=args.verbose, coverage=args.coverage)
    else:
        # Default: run all tests
        success = run_all_tests(verbose=args.verbose, coverage=args.coverage)
    
    if success:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
