#!/usr/bin/env python3
# resource_id: "d320ff54-0a81-4165-a129-3239614273a8"
# resource_type: "document"
# resource_name: "terminal_wrapper"
"""
Terminal Wrapper - A replacement for the terminal tool that doesn't hang
"""

import subprocess
import threading
import time
import sys
import os
from pathlib import Path

def run_command_robust(command, timeout=30, capture_output=True):
    """
    Run a command robustly without hanging.
    
    Args:
        command: Command to run (string or list)
        timeout: Timeout in seconds
        capture_output: Whether to capture output
    
    Returns:
        dict with keys: success, output, errors, exit_code, duration
    """
    start_time = time.time()
    
    print(f"[TERMINAL] Running: {command}")
    print(f"[TERMINAL] Timeout: {timeout}s")
    print("=" * 50)
    
    output_lines = []
    error_lines = []
    process = None
    
    try:
        # Start process
        if isinstance(command, str):
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
        else:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
        
        if capture_output:
            # Read output in real-time
            def read_stream(stream, output_list):
                try:
                    for line in iter(stream.readline, ''):
                        if line:
                            line = line.strip()
                            output_list.append(line)
                            print(f"[OUTPUT] {line}")
                    stream.close()
                except Exception as e:
                    print(f"[ERROR] Stream read error: {e}")
            
            # Start output reading threads
            stdout_thread = threading.Thread(
                target=read_stream, 
                args=(process.stdout, output_lines)
            )
            stderr_thread = threading.Thread(
                target=read_stream, 
                args=(process.stderr, error_lines)
            )
            
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            
            stdout_thread.start()
            stderr_thread.start()
        
        # Wait for completion with timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                print(f"\n[TERMINAL] Timeout after {timeout}s, terminating...")
                process.terminate()
                time.sleep(1)
                if process.poll() is None:
                    process.kill()
                return {
                    'success': False,
                    'output': output_lines,
                    'errors': error_lines + ["Process timed out"],
                    'exit_code': -1,
                    'duration': time.time() - start_time
                }
            time.sleep(0.1)
        
        # Wait for output threads to finish
        if capture_output:
            stdout_thread.join(timeout=2)
            stderr_thread.join(timeout=2)
        
        exit_code = process.returncode
        duration = time.time() - start_time
        
        print("=" * 50)
        print(f"[TERMINAL] Completed in {duration:.2f}s with exit code: {exit_code}")
        
        return {
            'success': exit_code == 0,
            'output': output_lines,
            'errors': error_lines,
            'exit_code': exit_code,
            'duration': duration
        }
        
    except Exception as e:
        duration = time.time() - start_time
        print(f"[TERMINAL] Error: {e}")
        return {
            'success': False,
            'output': output_lines,
            'errors': error_lines + [str(e)],
            'exit_code': -1,
            'duration': duration
        }

def run_python_script(script_path, *args, timeout=30):
    """
    Run a Python script with robust output handling.
    """
    if not os.path.exists(script_path):
        return {
            'success': False,
            'output': [],
            'errors': [f"Script not found: {script_path}"],
            'exit_code': -1,
            'duration': 0
        }
    
    # Build command
    cmd = [sys.executable, script_path] + list(args)
    return run_command_robust(cmd, timeout=timeout)

def main():
    """Test the terminal wrapper."""
    if len(sys.argv) < 2:
        print("Usage: python3 terminal_wrapper.py <command>")
        print("   or: python3 terminal_wrapper.py --script <script_path> [args...]")
        sys.exit(1)
    
    if sys.argv[1] == "--script":
        if len(sys.argv) < 3:
            print("Error: --script requires a script path")
            sys.exit(1)
        script_path = sys.argv[2]
        args = sys.argv[3:] if len(sys.argv) > 3 else []
        result = run_python_script(script_path, *args)
    else:
        command = " ".join(sys.argv[1:])
        result = run_command_robust(command)
    
    print(f"\n[RESULT] Success: {result['success']}")
    print(f"[RESULT] Exit Code: {result['exit_code']}")
    print(f"[RESULT] Duration: {result['duration']:.2f}s")
    print(f"[RESULT] Output Lines: {len(result['output'])}")
    print(f"[RESULT] Error Lines: {len(result['errors'])}")
    
    if result['errors']:
        print("\n[ERRORS]")
        for error in result['errors']:
            print(f"  {error}")

if __name__ == "__main__":
    main()
