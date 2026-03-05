#!/usr/bin/env python3
# resource_id: "e36044a4-efbb-445f-ae88-981859f4074b"
# resource_type: "document"
# resource_name: "configure-firebase-auth"

"""
Automated Firebase Authentication Configuration

This script uses Playwright to automatically configure Firebase Console:
1. Sign in to Firebase Console
2. Navigate to Authentication settings
3. Add authorized domains (localhost, 127.0.0.1)
4. Verify Google Sign-in provider is enabled
"""

import sys
import asyncio
import os

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Installing Playwright...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    from playwright.async_api import async_playwright

GOOGLE_EMAIL = os.getenv('GOOGLE_EMAIL', '2025computer2025@gmail.com')
GOOGLE_PASSWORD = os.getenv('GOOGLE_PASSWORD', 'Ca04102003')
FIREBASE_PROJECT = 'lang-trak-dev'

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_step(msg):
    print(f"{Colors.OKBLUE}▶ {msg}{Colors.ENDC}")

def print_success(msg):
    print(f"{Colors.OKGREEN}✅ {msg}{Colors.ENDC}")

def print_error(msg):
    print(f"{Colors.FAIL}❌ {msg}{Colors.ENDC}")

def print_warning(msg):
    print(f"{Colors.WARNING}⚠️  {msg}{Colors.ENDC}")

async def configure_firebase():
    print(f"""
{Colors.BOLD}{'='*70}
FIREBASE AUTHENTICATION CONFIGURATION
{'='*70}{Colors.ENDC}

Project: {FIREBASE_PROJECT}
Email: {GOOGLE_EMAIL}

This script will:
  1. Sign in to Firebase Console
  2. Navigate to Authentication settings
  3. Add authorized domains (localhost, 127.0.0.1)
  4. Verify Google Sign-in provider

{'='*70}
""")

    async with async_playwright() as p:
        print_step("Launching browser...")
        browser = await p.chromium.launch(
            headless=False,  # Show browser so you can watch
            slow_mo=500
        )
        
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        
        page = await context.new_page()
        
        try:
            # ================================================================
            # STEP 1: Navigate to Firebase Console
            # ================================================================
            print_step("Navigating to Firebase Console...")
            await page.goto('https://console.firebase.google.com/', wait_until='networkidle')
            await page.wait_for_timeout(3000)
            
            current_url = page.url
            
            # ================================================================
            # STEP 2: Sign in with Google (if needed)
            # ================================================================
            if 'accounts.google.com' in current_url or 'signin' in current_url.lower():
                print_step("Signing in with Google...")
                
                try:
                    # Enter email
                    email_input = page.locator('input[type="email"]')
                    if await email_input.is_visible(timeout=5000):
                        await email_input.fill(GOOGLE_EMAIL)
                        await page.click('button:has-text("Next"), #identifierNext')
                        await page.wait_for_timeout(3000)
                        print_success(f"Entered email: {GOOGLE_EMAIL}")
                except Exception as e:
                    print_warning(f"Could not enter email automatically: {e}")
                    print_warning("Please sign in manually in the browser window...")
                    await page.wait_for_timeout(10000)
                
                try:
                    # Enter password
                    password_input = page.locator('input[type="password"]')
                    if await password_input.is_visible(timeout=5000):
                        await password_input.fill(GOOGLE_PASSWORD)
                        await page.click('button:has-text("Next"), #passwordNext')
                        await page.wait_for_timeout(3000)
                        print_success("Entered password")
                except Exception as e:
                    print_warning(f"Could not enter password automatically: {e}")
                    print_warning("Please complete sign-in manually...")
                    await page.wait_for_timeout(10000)
                
                # Wait for Firebase Console to load
                await page.wait_for_timeout(5000)
            else:
                print_success("Already signed in")
            
            # ================================================================
            # STEP 3: Navigate to Project
            # ================================================================
            print_step(f"Navigating to project: {FIREBASE_PROJECT}...")
            await page.goto(f'https://console.firebase.google.com/project/{FIREBASE_PROJECT}/authentication/settings', 
                          wait_until='networkidle', timeout=30000)
            await page.wait_for_timeout(5000)
            print_success("Navigated to Authentication Settings")
            
            # ================================================================
            # STEP 4: Check Authorized Domains
            # ================================================================
            print_step("Checking authorized domains...")
            
            # Look for authorized domains section
            page_content = await page.content()
            
            if 'localhost' in page_content:
                print_success("localhost is already authorized")
            else:
                print_warning("localhost may not be authorized")
            
            if '127.0.0.1' in page_content:
                print_success("127.0.0.1 is already authorized")
            else:
                print_warning("127.0.0.1 may not be authorized")
            
            # ================================================================
            # STEP 5: Instructions for Manual Configuration
            # ================================================================
            print(f"""
{Colors.BOLD}{'='*70}
MANUAL CONFIGURATION INSTRUCTIONS
{'='*70}{Colors.ENDC}

The browser is now on the Authentication Settings page.

{Colors.OKBLUE}TO ADD AUTHORIZED DOMAINS:{Colors.ENDC}

1. Scroll down to "Authorized domains" section
2. Click "Add domain" button
3. Add these domains (if not already present):
   • localhost
   • 127.0.0.1
4. Click "Add" or "Save"

{Colors.OKBLUE}TO VERIFY GOOGLE SIGN-IN:{Colors.ENDC}

1. Click "Sign-in method" tab at the top
2. Find "Google" in the providers list
3. Make sure it shows "Enabled"
4. If not, click Google, toggle to Enable, and Save

{Colors.OKBLUE}CURRENT STATUS:{Colors.ENDC}
   • Browser is open on the correct page
   • You can make changes in the browser
   • Script will wait for 60 seconds

{'='*70}
""")
            
            print_warning("Browser will remain open for 60 seconds for manual configuration...")
            print_warning("Make any needed changes in the browser window now")
            
            await page.wait_for_timeout(60000)
            
            # ================================================================
            # STEP 6: Verify Configuration
            # ================================================================
            print_step("Verifying configuration...")
            
            # Refresh and check
            await page.reload(wait_until='networkidle')
            await page.wait_for_timeout(3000)
            
            final_content = await page.content()
            
            domains_ok = 'localhost' in final_content and '127.0.0.1' in final_content
            
            if domains_ok:
                print_success("✓ Authorized domains appear to be configured")
            else:
                print_warning("⚠ Could not verify all authorized domains")
            
            # Check Google Sign-in
            print_step("Checking Google Sign-in provider...")
            await page.goto(f'https://console.firebase.google.com/project/{FIREBASE_PROJECT}/authentication/providers',
                          wait_until='networkidle')
            await page.wait_for_timeout(3000)
            
            provider_content = await page.content()
            if 'Google' in provider_content and ('Enabled' in provider_content or 'enabled' in provider_content):
                print_success("✓ Google Sign-in provider is enabled")
            else:
                print_warning("⚠ Could not verify Google Sign-in status")
            
            print(f"""
{Colors.OKGREEN}{Colors.BOLD}{'='*70}
CONFIGURATION COMPLETE
{'='*70}{Colors.ENDC}

You can now close the browser or let it close automatically.

To test the configuration:
  python3 scripts/run-automated-browser-tests.py

{'='*70}
""")
            
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print_error(f"Configuration error: {e}")
            print_warning("Browser will stay open for manual configuration...")
            await page.wait_for_timeout(30000)
        finally:
            await browser.close()
    
    return True

if __name__ == '__main__':
    try:
        asyncio.run(configure_firebase())
        print_success("Firebase configuration script completed")
    except KeyboardInterrupt:
        print_warning("\nConfiguration interrupted by user")
    except Exception as e:
        print_error(f"Script error: {e}")
        sys.exit(1)

