#!/usr/bin/env python3
# resource_id: "a952b595-b614-4ae6-b576-b1a68461446f"
# resource_type: "document"
# resource_name: "conftest"

"""
conftest.py

Pytest configuration and shared fixtures for Firebase instance tests.
Follows project testing standards and provides common test utilities.
"""

import pytest
import tempfile
import json
import os
from pathlib import Path
from unittest.mock import Mock, patch

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
import sys
sys.path.insert(0, str(project_root))

@pytest.fixture(scope="session")
def project_root_path():
    """Get the project root path for testing."""
    return project_root

@pytest.fixture
def temp_config_file():
    """Create a temporary configuration file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        config = {
            "default_region": "us-central1",
            "firebase_cli_path": "firebase",
            "gcloud_cli_path": "gcloud",
            "project_configs": {},
            "max_concurrent_tasks": 5,
            "task_timeout_minutes": 30,
            "health_check_interval_minutes": 5,
            "retry_attempts": 3
        }
        json.dump(config, f)
        config_file = f.name
    
    yield config_file
    
    # Cleanup
    if os.path.exists(config_file):
        os.unlink(config_file)

@pytest.fixture
def mock_firebase_cli():
    """Mock Firebase CLI for testing."""
    with patch('subprocess.run') as mock_run:
        # Default successful response
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "Firebase CLI 12.0.0"
        mock_run.return_value.stderr = ""
        yield mock_run

@pytest.fixture
def mock_gcloud_cli():
    """Mock Google Cloud CLI for testing."""
    with patch('subprocess.run') as mock_run:
        # Default successful response
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "Google Cloud SDK 400.0.0"
        mock_run.return_value.stderr = ""
        yield mock_run

@pytest.fixture
def sample_firebase_project_config():
    """Sample Firebase project configuration for testing."""
    return {
        "project_id": "test-project-12345",
        "project_number": "123456789012",
        "display_name": "Test Project",
        "region": "us-central1",
        "environments": {
            "development": {
                "status": "active",
                "created_at": "2024-01-01T00:00:00Z"
            },
            "staging": {
                "status": "active", 
                "created_at": "2024-01-02T00:00:00Z"
            },
            "production": {
                "status": "active",
                "created_at": "2024-01-03T00:00:00Z"
            }
        },
        "services": {
            "authentication": {
                "enabled": True,
                "providers": ["google", "email"]
            },
            "firestore": {
                "enabled": True,
                "database_id": "(default)"
            },
            "storage": {
                "enabled": True,
                "bucket": "test-project-12345.appspot.com"
            },
            "functions": {
                "enabled": True,
                "region": "us-central1"
            },
            "hosting": {
                "enabled": True,
                "site": "test-project-12345"
            }
        }
    }

@pytest.fixture
def sample_firebase_environment():
    """Sample Firebase environment for testing."""
    from features.meta_intelligent_orchestration.core.orchestration.universal_orchestration_system import Environment, EnvironmentType
    from datetime import datetime
    
    return Environment(
        name="test-environment",
        type=EnvironmentType.DEVELOPMENT,
        project_id="test-project-12345",
        region="us-central1",
        status="active",
        created_at=datetime.now(),
        last_updated=datetime.now(),
        metadata={
            "firebase_config": "test-config.json",
            "deployment_id": "deploy-123"
        }
    )

@pytest.fixture
def sample_firebase_integration():
    """Sample Firebase integration for testing."""
    from features.meta_intelligent_orchestration.core.orchestration.universal_orchestration_system import Integration
    from datetime import datetime
    
    return Integration(
        id="test-integration-001",
        name="Test Firebase Auth",
        type="authentication",
        version="latest",
        status="active",
        environment="test-environment",
        dependencies=[],
        configuration={
            "providers": ["google", "email"],
            "settings": {
                "allow_new_users": True,
                "email_verification": True
            }
        },
        health_status="healthy",
        last_checked=datetime.now()
    )

@pytest.fixture
def mock_firebase_api_responses():
    """Mock Firebase API responses for testing."""
    return {
        "projects_list": {
            "projects": [
                {
                    "projectId": "test-project-12345",
                    "displayName": "Test Project",
                    "projectNumber": "123456789012"
                }
            ]
        },
        "auth_config": {
            "signIn": {
                "email": {"enabled": True},
                "google": {"enabled": True}
            }
        },
        "firestore_databases": {
            "databases": [
                {
                    "name": "projects/test-project-12345/databases/(default)",
                    "type": "FIRESTORE_NATIVE"
                }
            ]
        },
        "storage_buckets": {
            "buckets": [
                {
                    "name": "test-project-12345.appspot.com",
                    "location": "US"
                }
            ]
        },
        "functions_list": {
            "functions": [
                {
                    "name": "projects/test-project-12345/locations/us-central1/functions/testFunction",
                    "status": "ACTIVE"
                }
            ]
        },
        "hosting_sites": {
            "sites": [
                {
                    "name": "test-project-12345",
                    "defaultUrl": "https://test-project-12345.web.app"
                }
            ]
        }
    }

@pytest.fixture(autouse=True)
def cleanup_temp_files():
    """Cleanup temporary files after each test."""
    temp_files = []
    
    def track_temp_file(filepath):
        temp_files.append(filepath)
    
    yield track_temp_file
    
    # Cleanup all tracked temporary files
    for filepath in temp_files:
        if os.path.exists(filepath):
            try:
                os.unlink(filepath)
            except OSError:
                pass  # File might already be deleted

@pytest.fixture
def mock_async_sleep():
    """Mock asyncio.sleep for faster testing."""
    with patch('asyncio.sleep') as mock_sleep:
        mock_sleep.return_value = None
        yield mock_sleep

@pytest.fixture
def mock_datetime_now():
    """Mock datetime.now for consistent testing."""
    from datetime import datetime
    fixed_time = datetime(2024, 1, 1, 12, 0, 0)
    
    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = fixed_time
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)
        yield fixed_time

# Pytest configuration
def pytest_configure(config):
    """Configure pytest with project-specific settings."""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )

def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names."""
    for item in items:
        # Add integration marker to integration tests
        if "integration" in item.name.lower():
            item.add_marker(pytest.mark.integration)
        
        # Add unit marker to unit tests
        if "test_" in item.name and "integration" not in item.name.lower():
            item.add_marker(pytest.mark.unit)
        
        # Add slow marker to tests that might be slow
        if any(keyword in item.name.lower() for keyword in ["full", "complete", "end_to_end"]):
            item.add_marker(pytest.mark.slow)
