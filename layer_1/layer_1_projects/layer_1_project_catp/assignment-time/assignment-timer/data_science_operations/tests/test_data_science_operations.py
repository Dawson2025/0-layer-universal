# resource_id: "08b6b343-8ca4-4149-a390-d6b1a680e1ad"
# resource_type: "document"
# resource_name: "test_data_science_operations"
﻿"""Quick smoke tests for data_science_operations using bundled sample data."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parent
SAMPLE_MODULE_PATH = PROJECT_ROOT / "sample_data" / "same_as_google_firebase" / "sample_data.py"

# We load the fixture module dynamically so the smoke test mirrors a Firestore response
# without forcing the fixtures to live on sys.path.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import data_science_operations as ops


def _load_sample_module():
    """Import the sample_data module (without requiring package installs)."""
    spec = importlib.util.spec_from_file_location("data_science_operations_sample", SAMPLE_MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError("Could not load sample data module")
    spec.loader.exec_module(module)
    return module


def main() -> None:
    """Execute a light-weight smoke test against the bundled sample data."""
    sample_module = _load_sample_module()
    records = ops.normalise_records(sample_module.SAMPLE_TIMINGS)
    print(f"Loaded {len(records)} timing records from in-memory sample fixtures")

    print("\n=== Summary by assignmentId ===")
    by_assignment = ops.group_timings(records, "assignmentId")  # mirror CLI default
    ops.print_summary(by_assignment)

    print("\n=== Summary by course+assignment ===")
    by_course_assignment = ops.group_timings(records, "courseAssignment")  # alternate grouping example
    ops.print_summary(by_course_assignment)

    export_path = PROJECT_ROOT / "sample_data" / "json" / "analysis_output.json"
    # Exercise JSON export to ensure structure matches expectations
    project_id = getattr(sample_module, "SAMPLE_PROJECT_ID", "sample-data")
    ops.export_json(records, by_assignment, project_id=project_id, output_path=export_path)
    print(f"Exported aggregated data to {export_path}")


def test_firestore_guidance_message_when_dependency_missing(monkeypatch, capsys):
    """Ensure actionable guidance is provided when firebase-admin is unavailable."""
    # Simulate missing firebase_admin for both get_firestore_client and interactive mode.
    monkeypatch.setattr(ops, "firebase_admin", None)
    monkeypatch.setattr(ops, "firestore", None)

    with pytest.raises(RuntimeError) as excinfo:
        ops.get_firestore_client()

    guidance_text = ops.MISSING_FIRESTORE_GUIDANCE
    assert guidance_text in str(excinfo.value)
    assert ops._INSTALL_FIREBASE_COMMAND in guidance_text
    assert ops._VERIFY_FIREBASE_COMMAND in guidance_text

    responses = iter(["1", ""])  # Request Firestore mode, then accept defaults.
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    mode, payload = ops._choose_runtime_mode(SimpleNamespace(input_json=None, project=None))
    captured = capsys.readouterr()
    assert guidance_text in captured.out
    assert mode == "sample"
    assert payload is None

def test_firestore_credentials_guidance_when_adc_missing(monkeypatch, capsys):
    """Warn users when firebase-admin is installed but ADC are unavailable."""

    class StubCredentials:
        @staticmethod
        def ApplicationDefault():
            raise ops.DefaultCredentialsError('ADC unavailable for tests')

    def _raise_get_app(name='[DEFAULT]'):
        raise ValueError('App has not been initialised')

    def _init_app(options=None, name='[DEFAULT]'):
        return {'name': name, 'options': options}

    stub_admin = SimpleNamespace(
        credentials=StubCredentials(),
        get_app=_raise_get_app,
        initialize_app=_init_app,
    )
    stub_firestore = SimpleNamespace(client=lambda app: SimpleNamespace(app=app))

    monkeypatch.setattr(ops, 'firebase_admin', stub_admin)
    monkeypatch.setattr(ops, 'firestore', stub_firestore)
    monkeypatch.setattr(ops, 'credentials', StubCredentials)

    with pytest.raises(RuntimeError) as excinfo:
        ops.get_firestore_client()

    guidance_text = ops.MISSING_FIRESTORE_CREDENTIALS_GUIDANCE
    assert guidance_text in str(excinfo.value)

    responses = iter(['1', ''])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(responses))

    mode, payload = ops._choose_runtime_mode(SimpleNamespace(input_json=None, project=None))
    captured = capsys.readouterr()
    assert guidance_text in captured.out
    assert mode == 'sample'
    assert payload is None



if __name__ == "__main__":
    # Allow `python tests/test_data_science_operations.py` for quick verification.
    main()
