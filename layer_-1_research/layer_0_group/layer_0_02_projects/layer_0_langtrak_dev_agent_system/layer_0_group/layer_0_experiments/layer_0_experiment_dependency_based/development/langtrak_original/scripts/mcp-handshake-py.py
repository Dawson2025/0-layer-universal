#!/usr/bin/env python3
# resource_id: "ae13fa21-3848-4e67-8695-a5261d271f26"
# resource_type: "document"
# resource_name: "mcp-handshake-py"
"""Run the Node MCP handshake script and print output. This is a pragmatic Python-side handshake
by delegating to the Node client implemented in scripts/mcp-handshake-node-full.cjs.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NODE_SCRIPT = ROOT / 'mcp-handshake-node-full.cjs'

def main():
    cmd = ['node', str(NODE_SCRIPT)]
    print('Running:', ' '.join(cmd))
    proc = subprocess.Popen(cmd)
    proc.wait()
    return proc.returncode

if __name__ == '__main__':
    rc = main()
    sys.exit(rc)
