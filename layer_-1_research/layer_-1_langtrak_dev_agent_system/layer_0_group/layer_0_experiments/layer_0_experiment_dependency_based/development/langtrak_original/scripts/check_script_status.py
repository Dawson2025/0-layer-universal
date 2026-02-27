#!/usr/bin/env python3

"""
check_script_status.py

Check if a script is running, stuck, or completed.
"""

import subprocess
import psutil
import time
import sys
from datetime import datetime

def find_python_processes():
    """Find all running Python processes."""
    python_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'create_time']):
        try:
            if proc.info['name'] and 'python' in proc.info['name'].lower():
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
                python_processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cmdline': cmdline,
                    'create_time': proc.info['create_time'],
                    'running_time': time.time() - proc.info['create_time']
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return python_processes

def check_script_status(script_name=None):
    """Check status of running scripts."""
    print(f"🔍 Checking script status at {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 60)
    
    processes = find_python_processes()
    
    if not processes:
        print("❌ No Python processes found")
        return
    
    print(f"📊 Found {len(processes)} Python process(es):")
    print()
    
    for proc in processes:
        status = "🟢 Running"
        if proc['running_time'] > 60:
            status = "⚠️  Long running"
        if proc['running_time'] > 300:
            status = "🔴 Potentially stuck"
            
        print(f"PID: {proc['pid']}")
        print(f"Name: {proc['name']}")
        print(f"Command: {proc['cmdline']}")
        print(f"Running for: {proc['running_time']:.1f}s")
        print(f"Status: {status}")
        
        if script_name and script_name in proc['cmdline']:
            print("🎯 This matches your target script!")
        
        print("-" * 40)

def kill_stuck_scripts():
    """Kill potentially stuck Python scripts."""
    processes = find_python_processes()
    killed = 0
    
    for proc in processes:
        # Kill scripts running longer than 5 minutes
        if proc['running_time'] > 300:
            try:
                psutil.Process(proc['pid']).kill()
                print(f"🛑 Killed stuck process PID {proc['pid']}: {proc['cmdline']}")
                killed += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    
    if killed == 0:
        print("✅ No stuck processes found")
    else:
        print(f"🛑 Killed {killed} stuck process(es)")

def main():
    """Main function."""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--kill-stuck":
            kill_stuck_scripts()
        else:
            check_script_status(sys.argv[1])
    else:
        check_script_status()

if __name__ == "__main__":
    main()
