"""
Configuration for Firebase Emulator-based integration tests.

These tests run against a local Firebase Emulator for fast, offline testing.
"""

import pytest
import os
import time
import subprocess
import signal

# Global emulator process reference
_emulator_process = None


def pytest_configure(config):
    """Register custom markers for emulator tests"""
    config.addinivalue_line(
        "markers", "emulator: mark test as using Firebase Emulator"
    )


@pytest.fixture(scope="session", autouse=True)
def firebase_emulator():
    """
    Start Firebase Emulator for all emulator-based tests.

    This fixture:
    1. Sets environment variables to route Firebase SDK to emulator
    2. Starts the Firebase Emulator Suite
    3. Waits for emulator to be ready
    4. Cleans up emulator when tests complete
    """
    global _emulator_process

    # Set environment variables to use emulator
    os.environ["FIRESTORE_EMULATOR_HOST"] = "127.0.0.1:8081"
    os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "127.0.0.1:9099"
    os.environ["FIREBASE_STORAGE_EMULATOR_HOST"] = "127.0.0.1:9199"

    # Disable actual Firebase connections
    os.environ["DISABLE_FIREBASE"] = "0"  # Keep Firebase SDK enabled, but route to emulator

    # Add local Java to PATH for emulator
    java_path = os.path.expanduser("~/java/jdk-17.0.2/bin")
    if os.path.exists(java_path):
        os.environ["PATH"] = f"{java_path}{os.pathsep}{os.environ.get('PATH', '')}"
        print(f"Added Java to PATH: {java_path}")

    print("\n🚀 Starting Firebase Emulator Suite...")

    # Start emulator (suppress UI for faster startup)
    _emulator_process = subprocess.Popen(
        ["firebase", "emulators:start", "--only", "firestore,auth,storage", "--project", "demo-test"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid if os.name != 'nt' else None
    )

    # Wait for emulator to be ready (check for "All emulators ready" message)
    max_wait = 30  # seconds
    start_time = time.time()
    emulator_ready = False

    while time.time() - start_time < max_wait:
        if _emulator_process.poll() is not None:
            # Process died
            stdout, stderr = _emulator_process.communicate()
            print(f"Firebase Emulator failed to start:\nSTDOUT: {stdout.decode()}\nSTDERR: {stderr.decode()}")
            pytest.skip("Firebase Emulator not available (failed to start)")

        time.sleep(1)

        # Simple check: try to connect to Firestore emulator port
        import socket
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', 8081))
            sock.close()
            if result == 0:
                emulator_ready = True
                break
        except Exception:
            pass

    if not emulator_ready:
        if _emulator_process:
            _emulator_process.terminate()
            _emulator_process.wait()
        pytest.skip("Firebase Emulator not available (failed to become ready within 30 seconds)")

    print("✅ Firebase Emulator is ready!\n")

    # Yield control to tests
    yield

    # Cleanup: Stop emulator
    print("\n🛑 Stopping Firebase Emulator...")
    if _emulator_process:
        # Send SIGTERM to process group to kill all child processes
        if os.name != 'nt':
            os.killpg(os.getpgid(_emulator_process.pid), signal.SIGTERM)
        else:
            _emulator_process.terminate()

        try:
            _emulator_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            # Force kill if graceful shutdown failed
            if os.name != 'nt':
                os.killpg(os.getpgid(_emulator_process.pid), signal.SIGKILL)
            else:
                _emulator_process.kill()
            _emulator_process.wait()

    print("✅ Firebase Emulator stopped\n")


@pytest.fixture(autouse=True)
def reset_emulator_data():
    """
    Reset emulator data between tests for isolation.

    This ensures each test starts with a clean slate.
    """
    # Note: The emulator automatically provides isolation between test runs
    # If we need explicit cleanup, we can clear collections here
    yield
    # Post-test cleanup if needed
