#!/usr/bin/env python3
# resource_id: "d7487c77-dd56-457c-a265-97e73122c58e"
# resource_type: "document"
# resource_name: "test_cloud_templates"
"""
Script to test cloud templates functionality
"""

import subprocess
import sys

def run_cloud_template_tests():
    """Run the cloud template tests"""
    try:
        # Run the specific failing cloud template tests
        result = subprocess.run([
            '.venv/bin/pytest', 
            'tests/integration/test_cloud_templates.py::test_upload_template_to_cloud',
            'tests/integration/test_cloud_templates.py::test_list_public_cloud_templates',
            '-v'
        ], capture_output=True, text=True, timeout=30)
        
        print("=== CLOUD TEMPLATE TESTS ===")
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)
        print(f"Exit Code: {result.returncode}")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("Test timed out after 30 seconds")
        return False
    except Exception as e:
        print(f"Error running tests: {e}")
        return False

if __name__ == "__main__":
    success = run_cloud_template_tests()
    sys.exit(0 if success else 1)
