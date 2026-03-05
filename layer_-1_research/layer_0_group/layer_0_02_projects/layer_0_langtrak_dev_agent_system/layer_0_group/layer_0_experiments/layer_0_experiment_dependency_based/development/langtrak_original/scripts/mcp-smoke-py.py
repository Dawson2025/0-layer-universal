#!/usr/bin/env python3
# resource_id: "533763ff-1d04-4dd8-a6ae-554a8b588c7f"
# resource_type: "document"
# resource_name: "mcp-smoke-py"
"""Simple Python smoke test for Playwright MCP server
Starts the helper, waits for the port, GETs /mcp and checks for expected response.
"""
import os
import subprocess
import sys
import time
import signal
import socket
import urllib.request

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 9234
HOST = sys.argv[2] if len(sys.argv) > 2 else '127.0.0.1'


def start_helper(port):
    # Start helper in its own process group so we can kill the group later
    proc = subprocess.Popen(['bash', 'scripts/mcp-start.sh', '--port', str(port)],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                            preexec_fn=os.setsid)
    return proc


def wait_for_port(host, port, timeout=20):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except Exception:
            time.sleep(0.25)
    return False


def smoke(host, port):
    try:
        with urllib.request.urlopen(f'http://{host}:{port}/mcp', timeout=5) as r:
            body = r.read().decode('utf-8', errors='ignore')
            print(body[:200])
            return 'invalid request' in body.lower()
    except urllib.error.HTTPError as e:
        # HTTPError has a response body we can read
        try:
            body = e.read().decode('utf-8', errors='ignore')
            print('HTTPError body:', body[:200])
            return 'invalid request' in body.lower()
        except Exception:
            print('HTTPError without readable body:', e)
            return False
    except Exception as e:
        print('Error during request:', e)
        return False


def main():
    p = start_helper(PORT)
    try:
        if not wait_for_port(HOST, PORT, timeout=20):
            print('Timed out waiting for server to listen', file=sys.stderr)
            try:
                os.killpg(os.getpgid(p.pid), signal.SIGTERM)
            except Exception:
                p.terminate()
            p.wait()
            sys.exit(2)

        ok = smoke(HOST, PORT)
        print('✅ Python smoke test passed' if ok else '❌ Python smoke test failed')
        sys.exit(0 if ok else 3)
    finally:
        try:
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
            p.wait(timeout=5)
        except Exception:
            try:
                p.kill()
            except Exception:
                pass


if __name__ == '__main__':
    main()
