# resource_id: "e333d635-0f13-4bbd-9956-ea617d92d93b"
# resource_type: "document"
# resource_name: "configure-auth-domains"

#!/usr/bin/env python3

"""
configure-auth-domains.py

CLI helper to ensure Firebase/Firebase Identity Platform projects have the required
authorized domains for OAuth sign-in (Google sign-in, etc.).

Usage examples:
  python3 scripts/configure-auth-domains.py --projects lang-trak-dev lang-trak-prod \
      --domains example.com dev.example.com localhost 127.0.0.1

  python3 scripts/configure-auth-domains.py -p lang-trak-dev -d localhost -d 127.0.0.1 --dry-run

This script uses `gcloud auth print-access-token` to get an access token and calls
the Identity Toolkit Admin API endpoint:
  https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT/config

It is safe: use --dry-run to preview changes. You must run this locally (it uses
your gcloud credentials) and you must have adequate IAM permissions for the project.
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from typing import List, Optional


DEFAULT_PROJECTS = ["lang-trak-dev"]
DEFAULT_DOMAINS = ["localhost", "127.0.0.1"]


class Colors:
    BOLD = "\033[1m"
    ENDC = "\033[0m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    WARNING = "\033[93m"
    OKBLUE = "\033[94m"


def print_header(text: str) -> None:
    print(f"\n{Colors.BOLD}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{text}{Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*70}{Colors.ENDC}\n")


def print_step(msg: str) -> None:
    print(f"{Colors.OKBLUE}\u25b6 {msg}{Colors.ENDC}")


def print_success(msg: str) -> None:
    print(f"{Colors.OKGREEN}\u2705 {msg}{Colors.ENDC}")


def print_error(msg: str) -> None:
    print(f"{Colors.FAIL}\u274c {msg}{Colors.ENDC}")


def print_warning(msg: str) -> None:
    print(f"{Colors.WARNING}\u26a0\ufe0f  {msg}{Colors.ENDC}")


def run_command(cmd: str) -> Optional[str]:
    """Run a shell command and return stdout (or None on failure)."""
    try:
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # Return stderr when available to help debugging
        out = e.stdout.strip() if e.stdout else ""
        err = e.stderr.strip() if e.stderr else ""
        print_error(f"Command failed: {cmd}\n{err or out}")
        return None


def get_access_token() -> Optional[str]:
    """Get an access token from gcloud (requires `gcloud auth login`)."""
    print_step("Getting access token using gcloud...")
    token = run_command("gcloud auth print-access-token")
    if token:
        print_success("Got access token from gcloud")
        return token
    print_error("Could not get access token from gcloud")
    print_warning("Please run: gcloud auth login")
    return None


def fetch_project_config(token: str, project: str) -> Optional[dict]:
    print_step(f"Fetching current configuration for project '{project}'...")
    cmd = [
        "curl", "-s",
        "-H", f"Authorization: Bearer {token}",
        "-H", f"X-Goog-User-Project: {project}",
        f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project}/config"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        out = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed: {' '.join(cmd)}\n{e.stderr or e.stdout}")
        return None
    
    if not out:
        print_error("Failed to fetch project configuration")
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        print_error("Failed to parse JSON from project config")
        return None


def patch_project_config(token: str, project: str, body: dict) -> Optional[dict]:
    print_step(f"Patching configuration for project '{project}' (updateMask=authorizedDomains) ...")
    # Write body to a temporary file to avoid shell quoting issues
    body_json = json.dumps(body)
    cmd = [
        "curl", "-s", "-X", "PATCH",
        "-H", f"Authorization: Bearer {token}",
        "-H", f"X-Goog-User-Project: {project}",
        "-H", "Content-Type: application/json",
        f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project}/config?updateMask=authorizedDomains",
        "--data-binary", body_json
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        out = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed: {' '.join(cmd)}\n{e.stderr or e.stdout}")
        return None
    
    if not out:
        print_error("PATCH request failed or returned no output")
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        print_error("Failed to parse JSON from PATCH response")
        return None


def update_authorized_domains(token: str, project: str, domains: List[str], dry_run: bool = False) -> bool:
    """Fetch current config, merge domains, and optionally PATCH to update authorizedDomains."""
    print_step("Verifying current setup...")
    config = fetch_project_config(token, project)
    if config is None:
        print_warning("Cannot read current config; manual configuration may be required")
        return False

    current = config.get("authorizedDomains", []) or []
    print(f"\n   Current authorized domains: {', '.join(current) if current else '(none)'}")

    # Normalize and merge domains
    desired = list({d.strip() for d in current + domains if d and d.strip()})
    missing = [d for d in domains if d not in current]

    if not missing:
        print_success("All required domains are already authorized!")
        return True

    print_warning(f"Missing domains to add: {', '.join(missing)}")

    patch_body = {"authorizedDomains": desired}

    print_step("Patch body preview:")
    print(json.dumps(patch_body, indent=2))

    if dry_run:
        print_warning("Dry-run: not sending PATCH. Use without --dry-run to apply changes.")
        return True

    resp = patch_project_config(token, project, patch_body)
    if resp is None:
        print_error("Failed to apply patch")
        return False

    # Verify response contains the domains
    new_domains = resp.get("authorizedDomains", [])
    if all(d in new_domains for d in domains):
        print_success("Authorized domains updated successfully")
        return True
    else:
        print_error("Patch applied but verification failed; check console for details")
        print(json.dumps(resp, indent=2))
        return False


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Configure Firebase Authentication Authorized Domains for one or more projects")
    p.add_argument("--projects", "-p", nargs="+", default=DEFAULT_PROJECTS,
                   help="One or more Firebase project IDs to update (default: lang-trak-dev)")
    p.add_argument("--domains", "-d", nargs="+", default=DEFAULT_DOMAINS,
                   help="List of domains to add (space separated). Example: example.com dev.example.com localhost")
    p.add_argument("--dry-run", action="store_true", help="Show changes but do not PATCH the API")
    return p.parse_args()


def main() -> bool:
    args = parse_args()
    print_header("FIREBASE AUTH CONFIGURATION - AUTHORIZED DOMAINS")

    print_step(f"Projects: {', '.join(args.projects)}")
    print_step(f"Domains to add: {', '.join(args.domains)}")

    token = get_access_token()
    if not token:
        print_error("Cannot proceed without access token")
        print_warning("To fix:")
        print_warning("  1. Install gcloud CLI: https://cloud.google.com/sdk/docs/install")
        print_warning("  2. Run: gcloud auth login")
        print_warning("  3. Re-run this script")
        return False

    overall_success = True
    for proj in args.projects:
        print_header(f"Project: {proj}")
        success = update_authorized_domains(token, proj, args.domains, dry_run=args.dry_run)
        overall_success = overall_success and success

    print_header("CONFIGURATION SUMMARY")
    if overall_success:
        print_success("All required domains are authorized for the requested projects")
    else:
        print_warning("Some projects may require manual configuration. See logs above.")

    return overall_success


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Configuration cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)

