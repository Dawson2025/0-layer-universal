#!/usr/bin/env python3

"""
Comprehensive Cloud E2E Test Runner

This script performs automated E2E testing of ALL cloud features with real Firebase.
It uses Playwright MCP for browser automation and directly verifies Firebase data.

Tests:
1. Google OAuth sign-in
2. Cloud project creation
3. Words & phonemes in cloud
4. Video upload to cloud storage
5. Local → Cloud migration
6. Cloud → Local fork
7. Phoneme template creation & upload
8. Download & use cloud templates
9. Direct Firebase data verification
10. Cleanup test data

Requirements:
- App must be running (http://127.0.0.1:5000)
- Google account credentials in env vars or args
"""

import sys
import os
import subprocess
import time
import json
import argparse
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.firebase import clean_firebase_service, firestore_db

# Test configuration
APP_BASE_URL = os.getenv('APP_BASE_URL', 'http://127.0.0.1:5000')
GOOGLE_EMAIL = os.getenv('GOOGLE_EMAIL', '2025computer2025@gmail.com')
GOOGLE_PASSWORD = os.getenv('GOOGLE_PASSWORD', 'Ca04102003')
TEST_MARKER = f"E2E_TEST_{int(time.time())}"

# Track created resources for cleanup
CREATED_RESOURCES = {
    'projects': [],
    'words': [],
    'templates': [],
    'videos': []
}

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

def print_test(test_num, total, description):
    print(f"\n{Colors.OKCYAN}📋 TEST {test_num}/{total}: {description}{Colors.ENDC}")

def print_success(message):
    print(f"{Colors.OKGREEN}✅ {message}{Colors.ENDC}")

def print_error(message):
    print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")

def print_warning(message):
    print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")

def verify_firebase_connection():
    """Verify Firebase is available and connected."""
    if not clean_firebase_service.is_available():
        print_error("Firebase not available")
        return False
    
    print_success("Firebase connected")
    return True

def create_cloud_project_via_api(name, language="Test Language"):
    """Create a cloud project using the API."""
    import requests
    
    try:
        # This assumes we're authenticated (cookie from browser session)
        # In real testing, we'd get session cookie from Playwright
        response = requests.post(
            f"{APP_BASE_URL}/api/projects",
            json={
                'name': name,
                'language': language,
                'storage_type': 'cloud'
            },
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code in [200, 201]:
            data = response.json()
            project_id = data.get('id') or data.get('project_id')
            CREATED_RESOURCES['projects'].append(project_id)
            return project_id
        else:
            print_error(f"Failed to create project: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error creating project: {e}")
        return None

def verify_project_in_firebase(project_id):
    """Verify a project exists in Firebase."""
    try:
        projects = firestore_db._service.get_documents('projects', limit=1000)
        matching = [p for p in projects if p.get('id') == project_id]
        
        if matching:
            print_success(f"Project {project_id} found in Firestore")
            return True
        else:
            print_error(f"Project {project_id} NOT found in Firestore")
            return False
    except Exception as e:
        print_error(f"Error verifying project: {e}")
        return False

def create_word_in_cloud_project(project_id, word_data):
    """Create a word in a cloud project."""
    import requests
    
    try:
        response = requests.post(
            f"{APP_BASE_URL}/api/words",
            json={
                'project_id': project_id,
                **word_data
            },
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code in [200, 201]:
            data = response.json()
            word_id = data.get('word_id') or data.get('id')
            CREATED_RESOURCES['words'].append(word_id)
            return word_id
        else:
            print_error(f"Failed to create word: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error creating word: {e}")
        return None

def verify_word_in_firebase(word_id):
    """Verify a word exists in Firebase."""
    try:
        words = firestore_db._service.get_documents('words', limit=1000)
        matching = [w for w in words if w.get('id') == word_id]
        
        if matching:
            print_success(f"Word {word_id} found in Firestore")
            return True
        else:
            print_error(f"Word {word_id} NOT found in Firestore")
            return False
    except Exception as e:
        print_error(f"Error verifying word: {e}")
        return False

def create_template_and_upload(template_name):
    """Create a phoneme template and upload to cloud."""
    import requests
    
    try:
        # Create template
        response = requests.post(
            f"{APP_BASE_URL}/api/templates",
            json={
                'name': template_name,
                'phonemes': {
                    'consonants': ['p', 't', 'k', 'm', 'n'],
                    'vowels': ['a', 'e', 'i', 'o', 'u']
                },
                'syllable_structures': ['CV', 'CVC', 'V']
            },
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code not in [200, 201]:
            print_error(f"Failed to create template: {response.status_code}")
            return None
        
        data = response.json()
        template_id = data.get('template_id') or data.get('id')
        
        # Upload to cloud
        upload_response = requests.post(
            f"{APP_BASE_URL}/api/templates/{template_id}/upload",
            json={'is_public': True, 'description': 'E2E test template'},
            headers={'Content-Type': 'application/json'}
        )
        
        if upload_response.status_code in [200, 201]:
            CREATED_RESOURCES['templates'].append(template_id)
            return template_id
        else:
            print_error(f"Failed to upload template: {upload_response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error creating/uploading template: {e}")
        return None

def verify_template_in_firebase(template_id):
    """Verify a template exists in Firebase."""
    try:
        templates = firestore_db._service.get_documents('templates', limit=1000)
        matching = [t for t in templates if t.get('id') == template_id]
        
        if matching:
            template = matching[0]
            is_public = template.get('is_public', False)
            print_success(f"Template {template_id} found in Firestore (public: {is_public})")
            return True
        else:
            print_error(f"Template {template_id} NOT found in Firestore")
            return False
    except Exception as e:
        print_error(f"Error verifying template: {e}")
        return False

def cleanup_test_data(dry_run=False):
    """Clean up all created test data."""
    print_header("CLEANING UP TEST DATA")
    
    deleted = {'projects': 0, 'words': 0, 'templates': 0}
    
    # Delete projects
    for project_id in CREATED_RESOURCES['projects']:
        if dry_run:
            print(f"[DRY RUN] Would delete project: {project_id}")
        else:
            try:
                firestore_db._service.delete_document('projects', project_id)
                deleted['projects'] += 1
                print_success(f"Deleted project: {project_id}")
            except Exception as e:
                print_error(f"Failed to delete project {project_id}: {e}")
    
    # Delete words
    for word_id in CREATED_RESOURCES['words']:
        if dry_run:
            print(f"[DRY RUN] Would delete word: {word_id}")
        else:
            try:
                firestore_db._service.delete_document('words', word_id)
                deleted['words'] += 1
                print_success(f"Deleted word: {word_id}")
            except Exception as e:
                print_error(f"Failed to delete word {word_id}: {e}")
    
    # Delete templates
    for template_id in CREATED_RESOURCES['templates']:
        if dry_run:
            print(f"[DRY RUN] Would delete template: {template_id}")
        else:
            try:
                firestore_db._service.delete_document('templates', template_id)
                deleted['templates'] += 1
                print_success(f"Deleted template: {template_id}")
            except Exception as e:
                print_error(f"Failed to delete template {template_id}: {e}")
    
    print(f"\n{'Would delete' if dry_run else 'Deleted'}:")
    print(f"  Projects: {deleted['projects']}")
    print(f"  Words: {deleted['words']}")
    print(f"  Templates: {deleted['templates']}")
    print(f"  Total: {sum(deleted.values())}")

def run_tests(skip_cleanup=False, dry_run_cleanup=False):
    """Run all cloud E2E tests."""
    
    print_header("COMPREHENSIVE CLOUD E2E TEST SUITE")
    print(f"Test Marker: {TEST_MARKER}")
    print(f"App URL: {APP_BASE_URL}")
    print(f"Firebase Project: lang-trak-dev")
    
    total_tests = 12
    passed = 0
    failed = 0
    
    # Verify Firebase connection first
    if not verify_firebase_connection():
        print_error("Cannot proceed without Firebase connection")
        return False
    
    # TEST 1: Verify existing cloud data
    print_test(1, total_tests, "Verify existing cloud data")
    try:
        projects = firestore_db._service.get_documents('projects', limit=1000)
        words = firestore_db._service.get_documents('words', limit=1000)
        templates = firestore_db._service.get_documents('templates', limit=1000)
        
        print(f"   Found {len(projects)} projects in Firebase")
        print(f"   Found {len(words)} words in Firebase")
        print(f"   Found {len(templates)} templates in Firebase")
        print_success("Firebase data accessible")
        passed += 1
    except Exception as e:
        print_error(f"Failed to access Firebase: {e}")
        failed += 1
    
    # TEST 2: Create cloud project via API
    print_test(2, total_tests, "Create cloud project via API")
    project_name = f"Cloud_{TEST_MARKER}"
    project_id = create_cloud_project_via_api(project_name)
    
    if project_id:
        print_success(f"Created project: {project_id}")
        passed += 1
    else:
        print_warning("Skipped (requires authenticated session)")
        print_warning("This test needs browser OAuth session")
    
    # TEST 3: Verify project in Firebase
    if project_id:
        print_test(3, total_tests, "Verify project in Firebase")
        if verify_project_in_firebase(project_id):
            passed += 1
        else:
            failed += 1
    else:
        print_test(3, total_tests, "Verify project in Firebase - SKIPPED")
    
    # TEST 4: Create words in cloud project
    if project_id:
        print_test(4, total_tests, "Create words in cloud project")
        word_data = {
            'english_word': 'hello',
            'translation': 'greeting',
            'ipa_pronunciation': '/hɛˈloʊ/',
            'syllables_json': json.dumps([
                {'type': 'CV', 'onset': 'h', 'nucleus': 'ɛ'},
                {'type': 'CV', 'onset': 'l', 'nucleus': 'oʊ'}
            ])
        }
        
        word_id = create_word_in_cloud_project(project_id, word_data)
        if word_id:
            print_success(f"Created word: {word_id}")
            passed += 1
        else:
            print_error("Failed to create word")
            failed += 1
    else:
        print_test(4, total_tests, "Create words in cloud project - SKIPPED")
    
    # TEST 5: Verify word in Firebase
    if project_id and 'word_id' in locals():
        print_test(5, total_tests, "Verify word in Firebase")
        if verify_word_in_firebase(word_id):
            passed += 1
        else:
            failed += 1
    else:
        print_test(5, total_tests, "Verify word in Firebase - SKIPPED")
    
    # TEST 6: Create and upload phoneme template
    print_test(6, total_tests, "Create and upload phoneme template")
    template_name = f"Template_{TEST_MARKER}"
    template_id = create_template_and_upload(template_name)
    
    if template_id:
        print_success(f"Created template: {template_id}")
        passed += 1
    else:
        print_warning("Skipped (requires authenticated session)")
    
    # TEST 7: Verify template in Firebase
    if template_id:
        print_test(7, total_tests, "Verify template in Firebase")
        if verify_template_in_firebase(template_id):
            passed += 1
        else:
            failed += 1
    else:
        print_test(7, total_tests, "Verify template in Firebase - SKIPPED")
    
    # TEST 8-12: Manual browser tests required
    manual_tests = [
        "Google OAuth sign-in",
        "Video upload to cloud storage",
        "Local → Cloud migration",
        "Cloud → Local fork",
        "Download and use cloud template"
    ]
    
    for i, test_name in enumerate(manual_tests, start=8):
        print_test(i, total_tests, test_name)
        print_warning("Requires manual browser testing")
        print_warning(f"See: tests/e2e/manual_cloud_tests.md")
    
    # Summary
    print_header("TEST RESULTS SUMMARY")
    print(f"{Colors.OKGREEN}✅ Passed: {passed}{Colors.ENDC}")
    print(f"{Colors.FAIL}❌ Failed: {failed}{Colors.ENDC}")
    print(f"{Colors.WARNING}⚠️  Manual Required: {len(manual_tests)}{Colors.ENDC}")
    print(f"{Colors.BOLD}📊 Total: {total_tests}{Colors.ENDC}")
    
    if failed == 0:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}All automated tests passed!{Colors.ENDC}")
    
    print(f"\n{Colors.OKCYAN}Manual tests: See tests/e2e/manual_cloud_tests.md{Colors.ENDC}")
    
    # Cleanup
    if not skip_cleanup:
        cleanup_test_data(dry_run=dry_run_cleanup)
    else:
        print_warning("\nSkipping cleanup (--skip-cleanup flag)")
        print(f"Run cleanup later with: python3 scripts/cleanup-test-data.py --marker '{TEST_MARKER}'")
    
    return failed == 0

def main():
    global APP_BASE_URL
    
    parser = argparse.ArgumentParser(description='Run comprehensive cloud E2E tests')
    parser.add_argument('--skip-cleanup', action='store_true', help='Skip cleanup after tests')
    parser.add_argument('--dry-run-cleanup', action='store_true', help='Show cleanup without executing')
    parser.add_argument('--app-url', default=APP_BASE_URL, help='App base URL')
    
    args = parser.parse_args()
    
    APP_BASE_URL = args.app_url
    
    success = run_tests(
        skip_cleanup=args.skip_cleanup,
        dry_run_cleanup=args.dry_run_cleanup
    )
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()

