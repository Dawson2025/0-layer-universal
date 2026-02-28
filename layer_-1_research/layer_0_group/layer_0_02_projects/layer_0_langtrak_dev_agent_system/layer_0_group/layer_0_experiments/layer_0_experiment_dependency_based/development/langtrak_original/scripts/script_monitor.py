#!/usr/bin/env python3

"""
script_monitor.py

A monitoring system to track script execution and detect when scripts are stuck.
"""

import subprocess
import time
import signal
import sys
import threading
from datetime import datetime
from pathlib import Path

class ScriptMonitor:
    """Monitor script execution and detect stuck processes."""
    
    def __init__(self, timeout=30, check_interval=2):
        self.timeout = timeout
        self.check_interval = check_interval
        self.is_running = False
        self.start_time = None
        self.last_output_time = None
        self.output_buffer = []
        
    def monitor_output(self, process):
        """Monitor process output in real-time."""
        self.is_running = True
        self.start_time = datetime.now()
        self.last_output_time = self.start_time
        
        try:
            while True:
                # Read output line by line
                line = process.stdout.readline()
                if line:
                    output = line.decode('utf-8').strip()
                    if output:
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] {output}")
                        self.output_buffer.append(output)
                        self.last_output_time = datetime.now()
                elif process.poll() is not None:
                    # Process has finished
                    break
                    
                time.sleep(0.1)
                
        except Exception as e:
            print(f"❌ Error monitoring output: {e}")
        finally:
            self.is_running = False
    
    def check_if_stuck(self):
        """Check if the process appears to be stuck."""
        if not self.is_running:
            return False
            
        now = datetime.now()
        elapsed = (now - self.start_time).total_seconds()
        time_since_output = (now - self.last_output_time).total_seconds()
        
        # Consider stuck if:
        # 1. Running longer than timeout
        # 2. No output for more than 10 seconds
        if elapsed > self.timeout:
            print(f"⚠️  Script running for {elapsed:.1f}s (timeout: {self.timeout}s)")
            return True
            
        if time_since_output > 10:
            print(f"⚠️  No output for {time_since_output:.1f}s")
            return True
            
        return False
    
    def run_script(self, script_path, *args):
        """Run a script with monitoring."""
        print(f"🚀 Starting script: {script_path}")
        print(f"⏱️  Timeout: {self.timeout}s, Check interval: {self.check_interval}s")
        print("=" * 60)
        
        try:
            # Start the process
            cmd = ['python3', str(script_path)] + list(args)
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Start monitoring thread
            monitor_thread = threading.Thread(target=self.monitor_output, args=(process,))
            monitor_thread.daemon = True
            monitor_thread.start()
            
            # Main monitoring loop
            while self.is_running:
                if self.check_if_stuck():
                    print("🛑 Script appears to be stuck. Terminating...")
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                    return False
                
                time.sleep(self.check_interval)
            
            # Wait for process to complete
            return_code = process.wait()
            
            print("=" * 60)
            if return_code == 0:
                print("✅ Script completed successfully!")
            else:
                print(f"❌ Script failed with exit code: {return_code}")
            
            return return_code == 0
            
        except Exception as e:
            print(f"❌ Error running script: {e}")
            return False

def run_with_monitoring(script_path, timeout=30, *args):
    """Run a script with monitoring."""
    monitor = ScriptMonitor(timeout=timeout)
    return monitor.run_script(script_path, *args)

def quick_test(script_path, *args):
    """Quick test with shorter timeout."""
    monitor = ScriptMonitor(timeout=10, check_interval=1)
    return monitor.run_script(script_path, *args)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script_monitor.py <script_path> [timeout] [args...]")
        sys.exit(1)
    
    script_path = sys.argv[1]
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    args = sys.argv[3:] if len(sys.argv) > 3 else []
    
    success = run_with_monitoring(script_path, timeout, *args)
    sys.exit(0 if success else 1)
