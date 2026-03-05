---
resource_id: "7cb15a5c-0a63-4774-8f67-2ffce3c104de"
resource_type: "rule"
resource_name: "TERMINAL_HANGING_SOLUTION"
---
# Terminal Hanging Solution

<!-- section_id: "002053cf-262c-4108-b3e7-d9b4806cd9a9" -->
## Problem
The terminal tool (`run_terminal_cmd`) was getting stuck waiting for output from Python scripts that had already completed and displayed their output in the terminal. This caused the AI to hang indefinitely while the user could see the output was already there.

<!-- section_id: "8b042b7a-d4ca-471b-843a-42bf3e102348" -->
## Root Cause
The issue occurs because:
1. **Output Buffering**: Python scripts buffer their output, causing delays in when output appears
2. **Process Completion Detection**: The terminal tool wasn't properly detecting when processes completed
3. **Stream Reading**: The tool was waiting for output streams that had already been consumed

<!-- section_id: "bf0a2076-19a7-494f-a410-1454e88f6b20" -->
## Solution

<!-- section_id: "4ba30835-eea5-4a7a-9540-58db63ec2c5a" -->
### 1. Robust Script Runner (`robust_script_runner.py`)
A comprehensive script runner that handles:
- **Real-time Output**: Displays output as it's generated
- **Timeout Protection**: Prevents infinite hanging
- **Proper Stream Handling**: Uses threading to read stdout/stderr
- **Process Management**: Properly terminates stuck processes

<!-- section_id: "7d36d0c9-5efd-40cf-897f-a93cb6f411f4" -->
### 2. Terminal Wrapper (`terminal_wrapper.py`)
A drop-in replacement for the terminal tool that:
- **Non-blocking Execution**: Uses threading for output reading
- **Timeout Management**: Automatically terminates long-running processes
- **Real-time Feedback**: Shows output as it's generated
- **Error Handling**: Captures and reports errors properly

<!-- section_id: "5b26401f-884a-4706-a7b4-64e853a3c68f" -->
### 3. Key Features

#### Real-time Output Display
```python
def _read_output(self, stream, output_list):
    for line in iter(stream.readline, ''):
        if line:
            line = line.strip()
            output_list.append(line)
            print(f"[SCRIPT] {line}")  # Real-time output
```

#### Timeout Protection
```python
while self.process.poll() is None:
    if time.time() - start_time > self.timeout:
        print(f"\n[RUNNER] Timeout after {self.timeout}s, terminating...")
        self.process.terminate()
        # ... proper cleanup
```

#### Proper Process Management
```python
# Start process with proper buffering
self.process = subprocess.Popen(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1,  # Line buffered
    universal_newlines=True
)
```

<!-- section_id: "0d293450-406b-477f-8158-8ca52332ac04" -->
## Usage

<!-- section_id: "18c4716d-f964-47a6-b118-b8542c90c3a6" -->
### For Python Scripts
```python
from terminal_wrapper import run_python_script

result = run_python_script("scripts/quick_verify.py", timeout=30)
print(f"Success: {result['success']}")
print(f"Output: {result['output']}")
```

<!-- section_id: "0ad92819-402a-4bf0-885b-de43abce637c" -->
### For Shell Commands
```python
from terminal_wrapper import run_command_robust

result = run_command_robust("python3 scripts/quick_verify.py", timeout=30)
print(f"Success: {result['success']}")
```

<!-- section_id: "6ee6d1c6-90b3-48e0-b8e2-8a36675b8cd5" -->
### Direct Command Line Usage
```bash
# Run a Python script
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py

# Run a shell command
python3 scripts/terminal_wrapper.py "python3 scripts/quick_verify.py"
```

<!-- section_id: "f9843ef5-8666-4c65-9d8c-ec1a2985deab" -->
## Benefits

1. **No More Hanging**: Scripts complete properly without infinite waiting
2. **Real-time Feedback**: See output as it's generated
3. **Timeout Protection**: Long-running scripts are automatically terminated
4. **Error Handling**: Proper capture and reporting of errors
5. **Drop-in Replacement**: Can replace the terminal tool in most cases

<!-- section_id: "f3ac21f5-f31c-4d86-93a7-796ad0974b78" -->
## Testing

The solution has been tested with:
- ✅ Basic commands (`echo`, `ls`)
- ✅ Python scripts (`simple_test.py`)
- ✅ Complex scripts (`quick_verify.py`)
- ✅ Timeout scenarios
- ✅ Error handling

<!-- section_id: "4dbaf98d-79ea-4a34-a8eb-ad9f8af630e9" -->
## Implementation Notes

<!-- section_id: "9ca23ba1-5cb0-4b2e-8004-96a0b06cf19b" -->
### Why This Works
1. **Threading**: Output reading happens in separate threads
2. **Line Buffering**: Uses `bufsize=1` for immediate output
3. **Process Polling**: Checks `process.poll()` instead of waiting for streams
4. **Timeout Management**: Prevents infinite waiting
5. **Proper Cleanup**: Terminates and kills processes as needed

<!-- section_id: "80e93eb5-aff2-4dad-8404-4df590089cfd" -->
### Best Practices
1. **Always set timeouts**: Prevent infinite hanging
2. **Use real-time output**: Show progress to users
3. **Handle errors gracefully**: Capture and report errors
4. **Clean up resources**: Properly terminate processes

<!-- section_id: "3f9248d9-c84d-43aa-b396-675f9973883a" -->
## Future Improvements

1. **Progress Indicators**: Show progress for long-running scripts
2. **Output Filtering**: Filter sensitive information from output
3. **Logging**: Better logging for debugging
4. **Configuration**: Configurable timeouts and behavior
5. **Integration**: Better integration with the existing terminal tool

<!-- section_id: "d7064143-e1b6-4714-865d-9ba809476183" -->
## Conclusion

This solution completely eliminates the terminal hanging issue by:
- Using proper process management
- Implementing real-time output display
- Adding timeout protection
- Handling errors gracefully

The result is a robust system that never hangs and provides clear feedback to users.
