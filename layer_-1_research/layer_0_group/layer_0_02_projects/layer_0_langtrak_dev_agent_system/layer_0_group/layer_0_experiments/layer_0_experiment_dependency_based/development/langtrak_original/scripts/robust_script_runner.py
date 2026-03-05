#!/usr/bin/env python3
# resource_id: "944ca71f-c7d0-4273-b1a1-fb40e5ec68d9"
# resource_type: "document"
# resource_name: "robust_script_runner"
"""
Robust Script Runner - Solves the terminal tool hanging issue
"""

import subprocess
import threading
import time
import sys
import os
from pathlib import Path

class RobustScriptRunner:
    """
    A robust script runner that handles the terminal tool hanging issue
    by using proper output buffering and timeout mechanisms.
    """
    
    def __init__(self, timeout=30, buffer_size=1024):
        self.timeout = timeout
        self.buffer_size = buffer_size
        self.output_lines = []
        self.error_lines = []
        self.process = None
        self.completed = False
        self.exit_code = None
        
    def _read_output(self, stream, output_list):
        """Read output from a stream and store it in a list."""
        try:
            for line in iter(stream.readline, ''):
                if line:
                    line = line.strip()
                    output_list.append(line)
                    print(f"[SCRIPT] {line}")  # Real-time output
            stream.close()
        except Exception as e:
            print(f"[ERROR] Error reading output: {e}")
    
    def run_script(self, script_path, *args):
        """
        Run a Python script with proper output handling.
        Returns (success, output_lines, error_lines, exit_code)
        """
        if not os.path.exists(script_path):
            return False, [], [f"Script not found: {script_path}"], -1
            
        # Build command
        cmd = [sys.executable, script_path] + list(args)
        cmd_str = " ".join(cmd)
        
        print(f"[RUNNER] Executing: {cmd_str}")
        print(f"[RUNNER] Timeout: {self.timeout}s")
        print("=" * 60)
        
        try:
            # Start process with proper buffering
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,  # Line buffered
                universal_newlines=True
            )
            
            # Start output reading threads
            stdout_thread = threading.Thread(
                target=self._read_output, 
                args=(self.process.stdout, self.output_lines)
            )
            stderr_thread = threading.Thread(
                target=self._read_output, 
                args=(self.process.stderr, self.error_lines)
            )
            
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            
            stdout_thread.start()
            stderr_thread.start()
            
            # Wait for completion with timeout
            start_time = time.time()
            while self.process.poll() is None:
                if time.time() - start_time > self.timeout:
                    print(f"\n[RUNNER] Timeout after {self.timeout}s, terminating...")
                    self.process.terminate()
                    time.sleep(1)
                    if self.process.poll() is None:
                        self.process.kill()
                    return False, self.output_lines, self.error_lines + ["Process timed out"], -1
                time.sleep(0.1)
            
            # Wait for output threads to finish
            stdout_thread.join(timeout=2)
            stderr_thread.join(timeout=2)
            
            self.exit_code = self.process.returncode
            self.completed = True
            
            print("=" * 60)
            print(f"[RUNNER] Script completed with exit code: {self.exit_code}")
            
            return self.exit_code == 0, self.output_lines, self.error_lines, self.exit_code
            
        except Exception as e:
            print(f"[RUNNER] Error running script: {e}")
            return False, self.output_lines, self.error_lines + [str(e)], -1
    
    def run_command(self, command, shell=True):
        """
        Run a shell command with proper output handling.
        Returns (success, output_lines, error_lines, exit_code)
        """
        print(f"[RUNNER] Executing: {command}")
        print(f"[RUNNER] Timeout: {self.timeout}s")
        print("=" * 60)
        
        try:
            # Start process
            self.process = subprocess.Popen(
                command,
                shell=shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Start output reading threads
            stdout_thread = threading.Thread(
                target=self._read_output, 
                args=(self.process.stdout, self.output_lines)
            )
            stderr_thread = threading.Thread(
                target=self._read_output, 
                args=(self.process.stderr, self.error_lines)
            )
            
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            
            stdout_thread.start()
            stderr_thread.start()
            
            # Wait for completion with timeout
            start_time = time.time()
            while self.process.poll() is None:
                if time.time() - start_time > self.timeout:
                    print(f"\n[RUNNER] Timeout after {self.timeout}s, terminating...")
                    self.process.terminate()
                    time.sleep(1)
                    if self.process.poll() is None:
                        self.process.kill()
                    return False, self.output_lines, self.error_lines + ["Process timed out"], -1
                time.sleep(0.1)
            
            # Wait for output threads to finish
            stdout_thread.join(timeout=2)
            stderr_thread.join(timeout=2)
            
            self.exit_code = self.process.returncode
            self.completed = True
            
            print("=" * 60)
            print(f"[RUNNER] Command completed with exit code: {self.exit_code}")
            
            return self.exit_code == 0, self.output_lines, self.error_lines, self.exit_code
            
        except Exception as e:
            print(f"[RUNNER] Error running command: {e}")
            return False, self.output_lines, self.error_lines + [str(e)], -1

def main():
    """Test the robust script runner."""
    if len(sys.argv) < 2:
        print("Usage: python3 robust_script_runner.py <script_path> [args...]")
        print("   or: python3 robust_script_runner.py --command '<shell_command>'")
        sys.exit(1)
    
    runner = RobustScriptRunner(timeout=30)
    
    if sys.argv[1] == "--command":
        if len(sys.argv) < 3:
            print("Error: --command requires a shell command")
            sys.exit(1)
        command = " ".join(sys.argv[2:])
        success, output, errors, exit_code = runner.run_command(command)
    else:
        script_path = sys.argv[1]
        args = sys.argv[2:] if len(sys.argv) > 2 else []
        success, output, errors, exit_code = runner.run_script(script_path, *args)
    
    print(f"\n[FINAL] Success: {success}")
    print(f"[FINAL] Exit Code: {exit_code}")
    print(f"[FINAL] Output Lines: {len(output)}")
    print(f"[FINAL] Error Lines: {len(errors)}")
    
    if errors:
        print("\n[ERRORS]")
        for error in errors:
            print(f"  {error}")

if __name__ == "__main__":
    main()
