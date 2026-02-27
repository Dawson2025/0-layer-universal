#!/usr/bin/env python3
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
