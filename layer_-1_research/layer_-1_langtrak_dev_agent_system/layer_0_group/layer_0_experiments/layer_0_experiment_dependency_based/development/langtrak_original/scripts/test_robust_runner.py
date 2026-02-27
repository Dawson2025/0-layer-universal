#!/usr/bin/env python3
"""
Test script to demonstrate the robust runner solution
"""

import sys
import os
from pathlib import Path

# Add the scripts directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from terminal_wrapper import run_command_robust, run_python_script

def test_basic_command():
    """Test basic command execution."""
    print("=== Testing Basic Command ===")
    result = run_command_robust("echo 'Hello from robust runner!'", timeout=10)
    print(f"Success: {result['success']}")
    print(f"Output: {result['output']}")
    print(f"Errors: {result['errors']}")
    print()

def test_python_script():
    """Test Python script execution."""
    print("=== Testing Python Script ===")
    script_path = Path(__file__).parent / "simple_test.py"
    result = run_python_script(str(script_path), timeout=10)
    print(f"Success: {result['success']}")
    print(f"Output: {result['output']}")
    print(f"Errors: {result['errors']}")
    print()

def test_quick_verify():
    """Test the quick verify script."""
    print("=== Testing Quick Verify Script ===")
    script_path = Path(__file__).parent / "quick_verify.py"
    result = run_python_script(str(script_path), timeout=30)
    print(f"Success: {result['success']}")
    print(f"Output: {result['output']}")
    print(f"Errors: {result['errors']}")
    print()

def test_timeout():
    """Test timeout handling."""
    print("=== Testing Timeout Handling ===")
    result = run_command_robust("sleep 5 && echo 'This should timeout'", timeout=2)
    print(f"Success: {result['success']}")
    print(f"Output: {result['output']}")
    print(f"Errors: {result['errors']}")
    print()

if __name__ == "__main__":
    print("Testing Robust Script Runner Solution")
    print("=" * 50)
    
    test_basic_command()
    test_python_script()
    test_quick_verify()
    test_timeout()
    
    print("All tests completed!")
