#!/usr/bin/env python3

"""
Interactive Manual Browser Tests for Cloud Features

This script opens a browser and guides you through manual testing of cloud features
that require browser interaction (Google OAuth, file uploads, etc.).

It will:
1. Open a browser to the app
2. Guide you through each test with instructions
3. Verify results in Firebase after each test
4. Mark tests as pass/fail
"""

import sys
import os
import subprocess
import time
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.firebase import clean_firebase_service, firestore_db

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}\n")

def print_test(num, total, description):
    print(f"\n{Colors.OKCYAN}{'='*70}{Colors.ENDC}")
    print(f"{Colors.OKCYAN}📋 MANUAL TEST {num}/{total}: {description}{Colors.ENDC}")
    print(f"{Colors.OKCYAN}{'='*70}{Colors.ENDC}\n")

def print_instruction(text):
    print(f"{Colors.OKBLUE}ℹ️  {text}{Colors.ENDC}")

def print_success(text):
    print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")

def wait_for_user(prompt="Press Enter when ready to continue..."):
    input(f"\n{Colors.WARNING}⏸️  {prompt}{Colors.ENDC}\n")

def ask_pass_fail(test_name):
    while True:
        response = input(f"\n{Colors.BOLD}Did '{test_name}' pass? (y/n): {Colors.ENDC}").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")

def verify_firebase_recent_data():
    """Check for recently created data in Firebase"""
    try:
        projects = firestore_db._service.get_documents('projects', limit=10, order_by=[('created_at', 'desc')])
        if projects:
            latest = projects[0]
            print_success(f"Latest project: {latest.get('name')} (created: {latest.get('created_at')})")
            return True
        return False
    except Exception as e:
        print_error(f"Firebase verification failed: {e}")
        return False

APP_URL = os.environ.get("APP_BASE_URL", "http://127.0.0.1:5000")
TEST_MARKER = f"Manual_Browser_{int(time.time())}"

print_header("INTERACTIVE MANUAL BROWSER TESTS")
print(f"App URL: {APP_URL}")
print(f"Test Marker: {TEST_MARKER}")
print(f"\nThis script will guide you through manual browser tests.")
print(f"A browser will open, and you'll follow instructions for each test.")

wait_for_user("Press Enter to begin...")

# Open browser
print("\n🌐 Opening browser...")
try:
    subprocess.Popen(['xdg-open', APP_URL], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    print_success("Browser opened")
except Exception as e:
    print_error(f"Failed to open browser: {e}")
    print_instruction(f"Please manually open: {APP_URL}")

results = []

# ==============================================================================
# TEST 1: Google OAuth Sign-In
# ==============================================================================
print_test(1, 5, "Google OAuth Sign-In")

print_instruction("STEPS:")
print_instruction("1. In the browser, navigate to the login page if not there")
print_instruction("2. Click 'Sign in with Google' button")
print_instruction("3. Complete the Google OAuth flow")
print_instruction("   - Email: 2025computer2025@gmail.com")
print_instruction("   - Password: Ca04102003")
print_instruction("4. Verify you're redirected to the dashboard")
print_instruction("5. Check that your name/email is displayed")

wait_for_user("Press Enter when you've completed the sign-in...")

passed = ask_pass_fail("Google OAuth Sign-In")
results.append(("Google OAuth Sign-In", passed))

if passed:
    print_success("✓ Google OAuth working!")
else:
    print_error("✗ Google OAuth failed")
    print_instruction("Note: This may require manual debugging")

# ==============================================================================
# TEST 2: Create Cloud Project and Add Words
# ==============================================================================
print_test(2, 5, "Create Cloud Project with Words")

print_instruction("STEPS:")
print_instruction(f"1. Click 'Create New Project' or similar button")
print_instruction(f"2. Project name: Cloud_{TEST_MARKER}")
print_instruction("3. Language: Test Language")
print_instruction("4. Storage type: Select 'Cloud' (if option available)")
print_instruction("5. Click 'Create' or 'Save'")
print_instruction("6. Once created, click 'Add Word' in the project")
print_instruction("7. Add a word:")
print_instruction("   - English: test")
print_instruction("   - Translation: example")
print_instruction("   - IPA: /tɛst/")
print_instruction("   - Add syllables if multi-syllable UI available")
print_instruction("8. Save the word")

wait_for_user("Press Enter when you've created the project and word...")

# Verify in Firebase
print("\n🔍 Verifying in Firebase...")
try:
    projects = firestore_db._service.get_documents('projects', limit=100)
    matching = [p for p in projects if TEST_MARKER in p.get('name', '')]
    
    if matching:
        print_success(f"Found project in Firebase: {matching[0].get('name')}")
        print_success(f"Project ID: {matching[0].get('id')}")
        
        # Check for words
        words = firestore_db._service.get_documents('words', limit=100)
        project_words = [w for w in words if w.get('project_id') == matching[0].get('id')]
        
        if project_words:
            print_success(f"Found {len(project_words)} word(s) in project")
            for word in project_words:
                print(f"   • {word.get('english_word')} → {word.get('translation')}")
        else:
            print_error("No words found in project")
    else:
        print_error(f"Project not found in Firebase")
except Exception as e:
    print_error(f"Firebase verification error: {e}")

passed = ask_pass_fail("Create Cloud Project with Words")
results.append(("Create Cloud Project with Words", passed))

# ==============================================================================
# TEST 3: Create and Upload Phoneme Template
# ==============================================================================
print_test(3, 5, "Create and Upload Phoneme Template")

print_instruction("STEPS:")
print_instruction("1. Navigate to Templates section (if available)")
print_instruction(f"2. Click 'Create New Template'")
print_instruction(f"3. Template name: Template_{TEST_MARKER}")
print_instruction("4. Add some consonants: p, t, k")
print_instruction("5. Add some vowels: a, e, i")
print_instruction("6. Add syllable structures: CV, CVC")
print_instruction("7. Save the template")
print_instruction("8. If 'Upload to Cloud' or 'Make Public' option exists, use it")
print_instruction("9. Set visibility to Public if possible")

wait_for_user("Press Enter when you've created the template...")

# Verify in Firebase
print("\n🔍 Verifying in Firebase...")
try:
    templates = firestore_db._service.get_documents('templates', limit=100)
    matching = [t for t in templates if TEST_MARKER in t.get('name', '')]
    
    if matching:
        template = matching[0]
        print_success(f"Found template in Firebase: {template.get('name')}")
        print_success(f"Public: {template.get('is_public', False)}")
        print_success(f"Template ID: {template.get('id')}")
    else:
        print_error("Template not found in Firebase")
except Exception as e:
    print_error(f"Firebase verification error: {e}")

passed = ask_pass_fail("Create and Upload Phoneme Template")
results.append(("Create and Upload Phoneme Template", passed))

# ==============================================================================
# TEST 4: Local → Cloud Migration (Optional)
# ==============================================================================
print_test(4, 5, "Local → Cloud Migration (Optional)")

print_instruction("STEPS (if migration UI exists):")
print_instruction("1. Create a LOCAL project with 1-2 words")
print_instruction("2. Look for 'Migrate to Cloud' or similar option")
print_instruction("3. Click it and confirm migration")
print_instruction("4. Wait for migration to complete")
print_instruction("5. Verify project now shows as 'Cloud' type")
print_instruction("6. Verify words are still present")

print_instruction("\nNOTE: If migration UI doesn't exist, mark as N/A")

wait_for_user("Press Enter when done or to skip...")

passed = ask_pass_fail("Local → Cloud Migration (or N/A)")
results.append(("Local → Cloud Migration", passed))

# ==============================================================================
# TEST 5: Video Upload (Optional)
# ==============================================================================
print_test(5, 5, "Video Upload to Cloud Storage (Optional)")

print_instruction("STEPS (if video upload exists):")
print_instruction("1. Open a cloud project")
print_instruction("2. Select a word")
print_instruction("3. Look for 'Upload Video' or video section")
print_instruction("4. Click upload and select a small video file")
print_instruction("5. Wait for upload to complete")
print_instruction("6. Verify video appears/plays in the UI")

print_instruction("\nNOTE: If video upload UI doesn't exist, mark as N/A")
print_instruction("Check Firebase Storage console:")
print_instruction("https://console.firebase.google.com/project/lang-trak-dev/storage")

wait_for_user("Press Enter when done or to skip...")

passed = ask_pass_fail("Video Upload (or N/A)")
results.append(("Video Upload", passed))

# ==============================================================================
# SUMMARY
# ==============================================================================
print_header("MANUAL BROWSER TEST RESULTS")

passed_count = sum(1 for _, p in results if p)
total_count = len(results)

print(f"{Colors.BOLD}Results:{Colors.ENDC}\n")
for test_name, passed in results:
    status = f"{Colors.OKGREEN}✅ PASS{Colors.ENDC}" if passed else f"{Colors.FAIL}❌ FAIL{Colors.ENDC}"
    print(f"{status}  {test_name}")

print(f"\n{Colors.BOLD}Summary:{Colors.ENDC}")
print(f"Passed: {passed_count}/{total_count}")
print(f"Pass Rate: {(passed_count/total_count)*100:.0f}%")

if passed_count == total_count:
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}🎉 ALL MANUAL TESTS PASSED! 🎉{Colors.ENDC}")
else:
    print(f"\n{Colors.WARNING}⚠️  Some tests did not pass. Review failures above.{Colors.ENDC}")

# Final Firebase check
print_header("FINAL FIREBASE VERIFICATION")
print("\n🔍 Checking all test data in Firebase...\n")

try:
    projects = firestore_db._service.get_documents('projects', limit=200)
    words = firestore_db._service.get_documents('words', limit=200)
    templates = firestore_db._service.get_documents('templates', limit=200)
    
    test_projects = [p for p in projects if TEST_MARKER in p.get('name', '')]
    test_templates = [t for t in templates if TEST_MARKER in t.get('name', '')]
    
    print(f"📊 Total cloud documents: {len(projects) + len(words) + len(templates)}")
    print(f"   • Projects: {len(projects)}")
    print(f"   • Words: {len(words)}")
    print(f"   • Templates: {len(templates)}")
    
    print(f"\n📊 Test data created:")
    print(f"   • Test Projects: {len(test_projects)}")
    print(f"   • Test Templates: {len(test_templates)}")
    
    if test_projects:
        print(f"\n   Test Project IDs:")
        for proj in test_projects:
            print(f"      • {proj.get('id')} - {proj.get('name')}")
    
    if test_templates:
        print(f"\n   Test Template IDs:")
        for tmpl in test_templates:
            print(f"      • {tmpl.get('id')} - {tmpl.get('name')}")
    
    print_success("✓ Firebase verification complete")
    
except Exception as e:
    print_error(f"Firebase verification failed: {e}")

# Cleanup option
print(f"\n{Colors.OKCYAN}{'='*70}{Colors.ENDC}")
print(f"{Colors.OKCYAN}CLEANUP{Colors.ENDC}")
print(f"{Colors.OKCYAN}{'='*70}{Colors.ENDC}\n")

print(f"To clean up test data from Firebase:")
print(f"  python3 scripts/cleanup-test-data.py --marker '{TEST_MARKER}'")

print(f"\nTo view data in Firebase Console:")
print(f"  https://console.firebase.google.com/project/lang-trak-dev/firestore")

print_header("MANUAL BROWSER TESTS COMPLETE!")

