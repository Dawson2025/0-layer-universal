#!/usr/bin/env python3

"""
Fully Automated Browser Tests for Cloud Features

Uses Playwright to automatically test cloud features in a real browser.
No manual intervention required (except Google OAuth which may need manual sign-in).
"""

import sys
import os
import asyncio
import time
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.firebase import clean_firebase_service, firestore_db

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌ Playwright not installed. Installing...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    from playwright.async_api import async_playwright

APP_URL = os.getenv('APP_BASE_URL', 'http://127.0.0.1:5000')
GOOGLE_EMAIL = os.getenv('GOOGLE_EMAIL', '2025computer2025@gmail.com')
GOOGLE_PASSWORD = os.getenv('GOOGLE_PASSWORD', 'Ca04102003')
TEST_MARKER = f"Auto_Browser_{int(time.time())}"

class Colors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

results = []

def print_test(num, total, name):
    print(f"\n{Colors.OKBLUE}{'='*70}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}📋 TEST {num}/{total}: {name}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'='*70}{Colors.ENDC}")

def print_success(msg):
    print(f"{Colors.OKGREEN}✅ {msg}{Colors.ENDC}")

def print_error(msg):
    print(f"{Colors.FAIL}❌ {msg}{Colors.ENDC}")

def print_info(msg):
    print(f"   {msg}")

async def verify_in_firebase(collection, search_term):
    """Verify data exists in Firebase"""
    try:
        docs = firestore_db._service.get_documents(collection, limit=200)
        matching = [d for d in docs if search_term in str(d.get('name', ''))]
        return matching
    except Exception as e:
        print_error(f"Firebase verification error: {e}")
        return []

async def run_tests():
    print(f"""
{Colors.HEADER}{Colors.BOLD}{'='*70}
AUTOMATED BROWSER CLOUD TESTS
{'='*70}{Colors.ENDC}

App URL: {APP_URL}
Test Marker: {TEST_MARKER}
Browser: Chromium (headed mode)

This will automatically test cloud features in a real browser!
{'='*70}
""")

    async with async_playwright() as p:
        # Launch browser (headed so you can watch)
        browser = await p.chromium.launch(
            headless=False,  # Show browser
            slow_mo=1000     # Slow down so you can see
        )
        
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        
        page = await context.new_page()
        
        try:
            # ============================================================
            # TEST 1: Navigate to App
            # ============================================================
            print_test(1, 6, "Navigate to Application")
            
            await page.goto(APP_URL, wait_until='networkidle', timeout=30000)
            await page.wait_for_timeout(2000)
            
            title = await page.title()
            print_info(f"Page title: {title}")
            print_success("App loaded successfully")
            results.append(("Navigate to App", True))
            
            # ============================================================
            # TEST 2: Check if Logged In / Navigate to Dashboard
            # ============================================================
            print_test(2, 6, "Check Authentication State")
            
            current_url = page.url
            print_info(f"Current URL: {current_url}")
            
            if '/login' in current_url or '/register' in current_url:
                print_info("Not logged in - on login/register page")
                print_info("⚠️  Google OAuth requires manual sign-in")
                print_info("   The browser will stay open for you to sign in manually")
                print_info("   Email: 2025computer2025@gmail.com")
                print_info("   Password: Ca04102003")
                
                # Try to find and click Google sign-in button
                try:
                    google_btn = page.locator('button:has-text("Google"), a:has-text("Google"), [class*="google"]').first
                    if await google_btn.is_visible(timeout=5000):
                        print_info("Found Google sign-in button")
                        await google_btn.click()
                        await page.wait_for_timeout(5000)
                        
                        # Wait for OAuth completion (up to 60 seconds)
                        print_info("Waiting for OAuth completion...")
                        try:
                            await page.wait_for_url('**/dashboard**', timeout=60000)
                            print_success("OAuth completed - logged in!")
                            results.append(("Google OAuth Sign-In", True))
                        except:
                            print_error("OAuth timeout - may need manual sign-in")
                            print_info("Browser will stay open - please sign in manually")
                            await page.wait_for_timeout(30000)  # Wait 30s for manual sign-in
                            results.append(("Google OAuth Sign-In", False))
                except Exception as e:
                    print_error(f"Could not find Google sign-in button: {e}")
                    results.append(("Google OAuth Sign-In", False))
            else:
                print_success("Already logged in!")
                results.append(("Check Authentication", True))
            
            # ============================================================
            # TEST 3: Create Cloud Project
            # ============================================================
            print_test(3, 6, "Create Cloud Project")
            
            try:
                # Navigate to main page
                await page.goto(f"{APP_URL}/", wait_until='networkidle')
                await page.wait_for_timeout(2000)
                
                # Look for create project button/link
                create_selectors = [
                    'button:has-text("Create")',
                    'a:has-text("Create")',
                    'button:has-text("New Project")',
                    'a:has-text("New Project")',
                    '[class*="create"]',
                    '[id*="create"]'
                ]
                
                clicked = False
                for selector in create_selectors:
                    try:
                        btn = page.locator(selector).first
                        if await btn.is_visible(timeout=2000):
                            print_info(f"Found create button: {selector}")
                            await btn.click()
                            clicked = True
                            break
                    except:
                        continue
                
                if clicked:
                    await page.wait_for_timeout(2000)
                    
                    # Fill project form
                    project_name = f"Cloud_{TEST_MARKER}"
                    
                    # Try to fill name field
                    name_selectors = ['input[name="name"]', 'input[name="project_name"]', 'input[id*="name"]']
                    for selector in name_selectors:
                        try:
                            await page.fill(selector, project_name, timeout=2000)
                            print_info(f"Filled project name: {project_name}")
                            break
                        except:
                            continue
                    
                    # Try to fill language field
                    try:
                        await page.fill('input[name="language"]', 'Test Language', timeout=2000)
                    except:
                        pass
                    
                    # Try to select cloud storage
                    try:
                        cloud_radio = page.locator('input[type="radio"][value="cloud"]')
                        if await cloud_radio.is_visible(timeout=2000):
                            await cloud_radio.click()
                            print_info("Selected cloud storage")
                    except:
                        pass
                    
                    # Submit form
                    await page.click('button[type="submit"]:has-text("Create"), button:has-text("Save")', timeout=5000)
                    await page.wait_for_timeout(5000)
                    
                    # Verify in Firebase
                    matching = await verify_in_firebase('projects', TEST_MARKER)
                    if matching:
                        print_success(f"Project created and verified in Firebase!")
                        print_info(f"Project ID: {matching[0].get('id')}")
                        results.append(("Create Cloud Project", True))
                    else:
                        print_error("Project not found in Firebase")
                        results.append(("Create Cloud Project", False))
                else:
                    print_error("Could not find create project button")
                    results.append(("Create Cloud Project", False))
                    
            except Exception as e:
                print_error(f"Project creation failed: {e}")
                results.append(("Create Cloud Project", False))
            
            # ============================================================
            # TEST 4: Add Word to Project
            # ============================================================
            print_test(4, 6, "Add Word to Cloud Project")
            
            try:
                # Look for Add Word button
                add_word_selectors = [
                    'button:has-text("Add Word")',
                    'a:has-text("Add Word")',
                    'button:has-text("New Word")',
                    '[class*="add-word"]'
                ]
                
                clicked = False
                for selector in add_word_selectors:
                    try:
                        btn = page.locator(selector).first
                        if await btn.is_visible(timeout=2000):
                            await btn.click()
                            clicked = True
                            print_info("Clicked Add Word button")
                            break
                    except:
                        continue
                
                if clicked:
                    await page.wait_for_timeout(2000)
                    
                    # Fill word form
                    try:
                        await page.fill('input[name="english_word"]', 'test', timeout=3000)
                        await page.fill('input[name="translation"]', 'example', timeout=3000)
                        await page.fill('input[name="ipa_pronunciation"]', '/tɛst/', timeout=3000)
                        print_info("Filled word form")
                    except Exception as e:
                        print_error(f"Could not fill word form: {e}")
                    
                    # Submit
                    await page.click('button[type="submit"]:has-text("Save"), button:has-text("Add")', timeout=5000)
                    await page.wait_for_timeout(5000)
                    
                    # Verify in Firebase
                    words = firestore_db._service.get_documents('words', limit=200)
                    recent_words = [w for w in words if w.get('english_word') == 'test']
                    
                    if recent_words:
                        print_success(f"Word created and verified in Firebase!")
                        results.append(("Add Word to Project", True))
                    else:
                        print_error("Word not found in Firebase")
                        results.append(("Add Word to Project", False))
                else:
                    print_error("Could not find Add Word button")
                    results.append(("Add Word to Project", False))
                    
            except Exception as e:
                print_error(f"Word creation failed: {e}")
                results.append(("Add Word to Project", False))
            
            # ============================================================
            # TEST 5: Navigate to Templates (if exists)
            # ============================================================
            print_test(5, 6, "Navigate to Templates Section")
            
            try:
                await page.goto(f"{APP_URL}/templates", wait_until='networkidle', timeout=10000)
                await page.wait_for_timeout(2000)
                
                content = await page.content()
                if 'template' in content.lower():
                    print_success("Templates section accessible")
                    results.append(("Navigate to Templates", True))
                else:
                    print_error("Templates section not found")
                    results.append(("Navigate to Templates", False))
                    
            except Exception as e:
                print_error(f"Templates navigation failed: {e}")
                results.append(("Navigate to Templates", False))
            
            # ============================================================
            # TEST 6: Keep Browser Open for Inspection
            # ============================================================
            print_test(6, 6, "Browser Inspection")
            
            print_info("Browser will remain open for 30 seconds for manual inspection")
            print_info("You can:")
            print_info("  • View the current state")
            print_info("  • Test additional features manually")
            print_info("  • Take screenshots if needed")
            
            await page.wait_for_timeout(30000)
            print_success("Inspection period complete")
            results.append(("Browser Inspection", True))
            
        except Exception as e:
            print_error(f"Test suite error: {e}")
        finally:
            await browser.close()
    
    # ================================================================
    # SUMMARY
    # ================================================================
    print(f"""
{Colors.HEADER}{Colors.BOLD}{'='*70}
TEST RESULTS SUMMARY
{'='*70}{Colors.ENDC}
""")
    
    passed = sum(1 for _, p in results if p)
    failed = sum(1 for _, p in results if not p)
    
    for test_name, success in results:
        status = f"{Colors.OKGREEN}✅ PASS{Colors.ENDC}" if success else f"{Colors.FAIL}❌ FAIL{Colors.ENDC}"
        print(f"{status}  {test_name}")
    
    print(f"""
{Colors.BOLD}Summary:{Colors.ENDC}
  Passed: {passed}
  Failed: {failed}
  Total:  {len(results)}
  Pass Rate: {(passed/len(results)*100) if results else 0:.0f}%
""")
    
    # Firebase verification
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}")
    print("FIREBASE VERIFICATION")
    print(f"{'='*70}{Colors.ENDC}\n")
    
    try:
        projects = firestore_db._service.get_documents('projects', limit=200)
        words = firestore_db._service.get_documents('words', limit=200)
        templates = firestore_db._service.get_documents('templates', limit=200)
        
        test_projects = [p for p in projects if TEST_MARKER in p.get('name', '')]
        
        print(f"📊 Total cloud documents: {len(projects) + len(words) + len(templates)}")
        print(f"   • Projects: {len(projects)}")
        print(f"   • Words: {len(words)}")
        print(f"   • Templates: {len(templates)}")
        
        if test_projects:
            print(f"\n✅ Test project(s) created:")
            for proj in test_projects:
                print(f"   • {proj.get('name')} (ID: {proj.get('id')})")
        
        print_success("Firebase verification complete")
        
    except Exception as e:
        print_error(f"Firebase verification failed: {e}")
    
    # Cleanup instructions
    print(f"""
{Colors.OKBLUE}{'='*70}
CLEANUP
{'='*70}{Colors.ENDC}

To clean up test data:
  python3 scripts/cleanup-test-data.py --marker '{TEST_MARKER}'

To view in Firebase Console:
  https://console.firebase.google.com/project/lang-trak-dev/firestore
""")
    
    return passed == len(results)

if __name__ == '__main__':
    try:
        success = asyncio.run(run_tests())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Test execution error: {e}")
        sys.exit(1)

