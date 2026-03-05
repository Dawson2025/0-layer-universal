#!/usr/bin/env python3
# resource_id: "a38ae0f7-796d-4afd-9af7-de1a13778c3a"
# resource_type: "document"
# resource_name: "run_with_visibility"

"""
run_with_visibility.py

Run scripts with better visibility and timeout handling.
"""

import subprocess
import sys
import time
import signal
import threading
from datetime import datetime

class ScriptRunner:
    """Run scripts with better visibility."""
    
    def __init__(self, timeout=60):
        self.timeout = timeout
        self.process = None
        self.start_time = None
        self.completed = False
        
    def signal_handler(self, signum, frame):
        """Handle timeout signal."""
        print(f"\n⏰ Timeout reached ({self.timeout}s). Terminating script...")
        if self.process:
            self.process.terminate()
        sys.exit(1)
    
    def run_script(self, script_path, *args):
        """Run script with timeout and visibility."""
        print(f"🚀 Running: python3 {script_path} {' '.join(args)}")
        print(f"⏱️  Timeout: {self.timeout}s")
        print(f"🕐 Started at: {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 60)
        
        # Set up timeout handler
        signal.signal(signal.SIGALRM, self.signal_handler)
        signal.alarm(self.timeout)
        
        try:
            # Start the process
            cmd = ['python3', script_path] + list(args)
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            self.start_time = time.time()
            
            # Read output in real-time
            while True:
                output = self.process.stdout.readline()
                if output == '' and self.process.poll() is not None:
                    break
                if output:
                    print(f"[{time.time() - self.start_time:6.1f}s] {output.strip()}")
            
            # Wait for process to complete
            return_code = self.process.wait()
            
            # Cancel timeout
            signal.alarm(0)
            
            print("=" * 60)
            elapsed = time.time() - self.start_time
            print(f"⏱️  Completed in {elapsed:.1f}s")
            
            if return_code == 0:
                print("✅ Script completed successfully!")
            else:
                print(f"❌ Script failed with exit code: {return_code}")
            
            return return_code == 0
            
        except Exception as e:
            print(f"❌ Error running script: {e}")
            signal.alarm(0)
            return False

def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python3 run_with_visibility.py <script_path> [timeout] [args...]")
        print("Example: python3 run_with_visibility.py verify_google_provider.py 30")
        sys.exit(1)
    
    script_path = sys.argv[1]
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    args = sys.argv[3:] if len(sys.argv) > 3 else []
    
    runner = ScriptRunner(timeout=timeout)
    success = runner.run_script(script_path, *args)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
