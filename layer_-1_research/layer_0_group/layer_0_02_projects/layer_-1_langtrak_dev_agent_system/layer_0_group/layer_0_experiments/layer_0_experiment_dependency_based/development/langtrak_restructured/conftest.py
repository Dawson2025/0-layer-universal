"""
Pytest configuration and fixtures for Language Tracker project.
Following project constitution standards and Trickle-Down documentation structure.
"""

import pytest
import asyncio
import tempfile
import os
import sqlite3
from pathlib import Path
from typing import Dict, Any, Generator
from unittest.mock import Mock, AsyncMock, patch

# Test configuration
pytest_plugins = ["pytest_asyncio"]

# Global database isolation fixture
@pytest.fixture(autouse=True)
def db_isolation(tmp_path, monkeypatch):
    """
    Automatically isolate the database for every test.
    Creates a unique database file in a temporary directory and patches main.DB_NAME.
    """
    # Create a unique database file for this test
    db_dir = tmp_path / "data"
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / "test_phonemes.db"
    
    # Import modules that use DB_NAME
    import main
    import app
    
    # Save original values (though monkeypatch handles restoration)
    original_db = main.DB_NAME
    
    # Patch DB_NAME in all relevant modules
    monkeypatch.setattr(main, 'DB_NAME', str(db_path))
    monkeypatch.setattr(app.main, 'DB_NAME', str(db_path))
    
    # Initialize the database schema for this test
    # We use a localized migrate_schema to avoid impacting other tests or global state
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Create tables (copied from main.migrate_schema logic but simplified/safer)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            user_id INTEGER,
            syllable_type TEXT,
            position TEXT,
            length_type TEXT,
            group_type TEXT,
            subgroup_type TEXT,
            sub_subgroup_type TEXT,
            phoneme TEXT,
            frequency INTEGER DEFAULT 0
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            project_id INTEGER,
            language TEXT,
            english_words TEXT,
            new_language_word TEXT,
            ipa_phonetics TEXT,
            dictionary_phonetics TEXT,
            syllable_type TEXT,
            onset_phoneme TEXT,
            onset_length_type TEXT,
            nucleus_phoneme TEXT,
            nucleus_length_type TEXT,
            coda_phoneme TEXT,
            coda_length_type TEXT,
            syllables_data TEXT,
            video_path TEXT,
            image_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phoneme_templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            template_data TEXT NOT NULL,
            phoneme_count INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Add auth tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            firebase_uid TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            UNIQUE(name, user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            admin_user_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (admin_user_id) REFERENCES users (id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS group_memberships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            user_id INTEGER,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (group_id) REFERENCES groups (id),
            FOREIGN KEY (user_id) REFERENCES users (id),
            UNIQUE(group_id, user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS group_invites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            invite_token TEXT UNIQUE NOT NULL,
            created_by INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL,
            FOREIGN KEY (group_id) REFERENCES groups (id),
            FOREIGN KEY (created_by) REFERENCES users (id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_shares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            group_id INTEGER NOT NULL,
            shared_by INTEGER NOT NULL,
            shared_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects (id),
            FOREIGN KEY (group_id) REFERENCES groups (id),
            FOREIGN KEY (shared_by) REFERENCES users (id),
            UNIQUE(project_id, group_id)
        )
    """)
    
    conn.commit()
    conn.close()
    
    yield
    
    # Cleanup is handled by tmp_path fixture automatically

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def mock_firebase_project() -> Dict[str, Any]:
    """Mock Firebase project configuration."""
    return {
        "project_id": "test-project",
        "project_number": "123456789",
        "display_name": "Test Project",
        "region": "us-central1",
        "status": "ACTIVE"
    }


@pytest.fixture
def mock_firebase_auth_config() -> Dict[str, Any]:
    """Mock Firebase Auth configuration."""
    return {
        "authorizedDomains": [
            "localhost",
            "127.0.0.1",
            "test-project.web.app",
            "test-project.firebaseapp.com"
        ],
        "signInProviders": [
            {
                "providerId": "google.com",
                "enabled": True,
                "displayName": "Google"
            }
        ]
    }


@pytest.fixture
def mock_google_cloud_credentials() -> Dict[str, Any]:
    """Mock Google Cloud credentials."""
    return {
        "type": "service_account",
        "project_id": "test-project",
        "private_key_id": "test-key-id",
        "private_key": "-----BEGIN PRIVATE KEY-----\nTEST_KEY\n-----END PRIVATE KEY-----\n",
        "client_email": "test@test-project.iam.gserviceaccount.com",
        "client_id": "123456789",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token"
    }


@pytest.fixture
def mock_project_profile() -> Dict[str, Any]:
    """Mock project profile for testing."""
    return {
        "project_type": "web_application",
        "user_scale": "medium",
        "security_level": "standard",
        "budget_range": "medium",
        "timeline": "6_months",
        "team_size": "small",
        "technical_constraints": ["TypeScript", "React"],
        "business_goals": ["User engagement", "Scalability"]
    }


@pytest.fixture
def mock_environment_config() -> Dict[str, Any]:
    """Mock environment configuration."""
    return {
        "development": {
            "project_id": "lang-trak-dev",
            "domains": ["localhost", "127.0.0.1", "lang-trak-dev.web.app"],
            "services": ["auth", "firestore", "functions", "hosting"]
        },
        "staging": {
            "project_id": "lang-trak-staging",
            "domains": ["lang-trak-staging.web.app"],
            "services": ["auth", "firestore", "functions", "hosting", "analytics"]
        },
        "testing": {
            "project_id": "lang-trak-test",
            "domains": ["lang-trak-test.web.app"],
            "services": ["auth", "firestore", "functions", "test_lab"]
        },
        "production": {
            "project_id": "lang-trak-prod",
            "domains": ["lang-trak-prod.web.app"],
            "services": ["auth", "firestore", "functions", "hosting", "analytics", "monitoring"]
        }
    }


@pytest.fixture
def mock_meta_intelligent_config() -> Dict[str, Any]:
    """Mock meta-intelligent configuration."""
    return {
        "learning_sources": [
            "github_trends",
            "stack_overflow_surveys",
            "npm_downloads",
            "pypi_downloads",
            "industry_reports"
        ],
        "recommendation_engines": [
            "technology_selection",
            "architecture_patterns",
            "implementation_strategy",
            "future_proofing"
        ],
        "visualization_types": [
            "timeline",
            "dependency_graph",
            "system_dashboard",
            "integration_flow"
        ]
    }


@pytest.fixture
def mock_browser_automation_tools() -> Dict[str, Any]:
    """Mock browser automation tools configuration."""
    return {
        "browser": {
            "mcp_server": "browser",
            "purpose": "general_purpose",
            "best_for": ["simple_navigation", "form_filling", "basic_interactions"]
        },
        "chrome_devtools": {
            "mcp_server": "chrome-devtools",
            "purpose": "chrome_specific",
            "best_for": ["advanced_debugging", "performance_analysis", "chrome_features"]
        },
        "playwright": {
            "mcp_server": "playwright",
            "purpose": "cross_browser",
            "best_for": ["cross_browser_testing", "complex_interactions", "reliable_automation"]
        }
    }


@pytest.fixture
def mock_visual_orchestration_config() -> Dict[str, Any]:
    """Mock visual orchestration configuration."""
    return {
        "timeline": {
            "orientation": "horizontal",
            "spacing": 50,
            "milestone_size": 20
        },
        "dependency_graph": {
            "layout": "hierarchical",
            "direction": "top_to_bottom",
            "spacing": 100
        },
        "dashboard": {
            "grid_size": 4,
            "widget_size": "medium"
        },
        "export_formats": ["png", "jpeg", "svg", "html", "json"]
    }


@pytest.fixture
def mock_project_analysis_config() -> Dict[str, Any]:
    """Mock project analysis configuration."""
    return {
        "analysis_dimensions": [
            "project_type",
            "user_scale",
            "security_level",
            "budget_range"
        ],
        "recommendation_engines": [
            "technology_selection",
            "architecture_patterns",
            "implementation_strategy",
            "future_proofing"
        ],
        "risk_factors": [
            "technical_complexity",
            "team_expertise",
            "timeline_constraints",
            "budget_limitations"
        ]
    }


@pytest.fixture
def mock_async_function():
    """Mock async function for testing."""
    async def mock_func(*args, **kwargs):
        return {"status": "success", "result": "mock_result"}
    return mock_func


@pytest.fixture
def mock_sync_function():
    """Mock sync function for testing."""
    def mock_func(*args, **kwargs):
        return {"status": "success", "result": "mock_result"}
    return mock_func


@pytest.fixture
def mock_error_response():
    """Mock error response for testing error handling."""
    return {
        "error": "test_error",
        "message": "Test error message",
        "code": 400
    }


@pytest.fixture
def mock_success_response():
    """Mock success response for testing success scenarios."""
    return {
        "status": "success",
        "message": "Operation completed successfully",
        "data": {"result": "test_data"}
    }


# Test markers
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: Unit tests"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests"
    )
    config.addinivalue_line(
        "markers", "e2e: End-to-end tests"
    )
    config.addinivalue_line(
        "markers", "slow: Slow running tests"
    )
    config.addinivalue_line(
        "markers", "firebase: Firebase-specific tests"
    )
    config.addinivalue_line(
        "markers", "auth: Authentication tests"
    )
    config.addinivalue_line(
        "markers", "visual: Visual orchestration tests"
    )
    config.addinivalue_line(
        "markers", "meta: Meta-intelligent orchestration tests"
    )
    config.addinivalue_line(
        "markers", "browser: Browser automation tests"
    )
    config.addinivalue_line(
        "markers", "project_analysis: Project analysis tests"
    )
    config.addinivalue_line(
        "markers", "emulator: Firebase emulator tests"
    )


# Test collection hooks
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names."""
    for item in items:
        # Add markers based on test file location
        if "firebase" in str(item.fspath):
            item.add_marker(pytest.mark.firebase)
        if "auth" in str(item.fspath):
            item.add_marker(pytest.mark.auth)
        if "visual" in str(item.fspath):
            item.add_marker(pytest.mark.visual)
        if "meta" in str(item.fspath):
            item.add_marker(pytest.mark.meta)
        if "browser" in str(item.fspath):
            item.add_marker(pytest.mark.browser)
        if "project_analysis" in str(item.fspath):
            item.add_marker(pytest.mark.project_analysis)
        
        # Add markers based on test function names
        if "test_integration" in item.name:
            item.add_marker(pytest.mark.integration)
        if "test_e2e" in item.name:
            item.add_marker(pytest.mark.e2e)
        if "test_slow" in item.name:
            item.add_marker(pytest.mark.slow)


# Test session hooks
def pytest_sessionstart(session):
    """Called after the Session object has been created."""
    print("\n" + "="*50)
    print("Starting Language Tracker Test Suite")
    print("Following Project Constitution Standards")
    print("="*50)


def pytest_sessionfinish(session, exitstatus):
    """Called after whole test run finished, right before returning the exit status."""
    print("\n" + "="*50)
    print("Language Tracker Test Suite Completed")
    print(f"Exit Status: {exitstatus}")
    print("="*50)


# Test failure hooks
def pytest_runtest_logreport(report):
    """Called when a test report is ready."""
    if report.failed:
        print(f"\n❌ FAILED: {report.nodeid}")
        if hasattr(report, 'longrepr') and report.longrepr:
            print(f"Error: {report.longrepr}")
    elif report.passed:
        print(f"✅ PASSED: {report.nodeid}")
    elif report.skipped:
        print(f"⏭️  SKIPPED: {report.nodeid}")


# Coverage configuration
def pytest_configure(config):
    """Configure pytest with coverage settings."""
    if config.getoption("--cov"):
        config.addinivalue_line(
            "markers", "coverage: Coverage tests"
        )