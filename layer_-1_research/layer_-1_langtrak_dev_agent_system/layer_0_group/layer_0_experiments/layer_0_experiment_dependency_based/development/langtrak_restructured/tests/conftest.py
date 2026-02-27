"""Shared pytest configuration and fixtures for the Lang-Trak test suite.

Ensures the repository root is available on ``sys.path`` so tests in
feature packages can import application modules without relying on the
execution context.

Provides common fixtures for authenticated clients, database setup, and mocking.
"""

from __future__ import annotations

import sys
import json
import sqlite3
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Import after path setup
import app as flask_app
import main
import core.database as core_db


def patch_all_db_names(monkeypatch, db_str):
    """Patch DB_NAME in all modules that import it from core.database.

    Python's `from core.database import DB_NAME` creates a local copy in each module.
    Monkeypatching core.database.DB_NAME alone doesn't affect already-imported copies.
    This function patches DB_NAME in all known modules that use it.
    """
    monkeypatch.setattr(main, 'DB_NAME', db_str)
    monkeypatch.setattr(core_db, 'DB_NAME', db_str)

    # Patch all feature modules that import DB_NAME from core.database
    import features.words.creation as words_creation
    import features.words.editing as words_editing
    import features.words.display as words_display
    import features.words.api_operations as word_api
    import features.words.search as words_search
    import features.phonemes.display as phonemes_display
    import features.auth.registration as auth_reg
    import features.auth.login as auth_login
    import features.auth.firebase_auth as auth_firebase
    import features.projects.creation as proj_creation
    import features.projects.storage_ops as proj_storage
    import features.projects.display as proj_display
    import features.projects.editing as proj_editing
    import features.projects.context as proj_context
    import features.admin.template_system as admin_templates
    import features.admin.phoneme_management as admin_phonemes
    import features.admin.database_tools as admin_db_tools

    for mod in [words_creation, words_editing, words_display, word_api, words_search,
                phonemes_display, auth_reg, auth_login, auth_firebase,
                proj_creation, proj_storage, proj_display, proj_editing, proj_context,
                admin_templates, admin_phonemes, admin_db_tools]:
        if hasattr(mod, 'DB_NAME'):
            monkeypatch.setattr(mod, 'DB_NAME', db_str)


@pytest.fixture()
def base_client(tmp_path, monkeypatch):
    """
    Base fixture providing Flask test client with isolated database.
    No authentication or project setup.
    """
    db_path = tmp_path / 'test.db'
    db_str = str(db_path)

    # Point ALL modules to the temporary database
    patch_all_db_names(monkeypatch, db_str)

    # Initialize schema
    main.migrate_schema()
    flask_app.init_users_table()
    
    # Configure Flask
    flask_app.app.config['TESTING'] = True
    flask_app.app.config['SECRET_KEY'] = 'test-secret-key-12345'
    
    # Disable Firebase by default
    mock_firebase = MagicMock()
    mock_firebase.is_available.return_value = False
    
    # Import modules that use Firebase
    import features.words.api_operations as word_api
    import features.admin.template_system as template_module
    
    with patch.object(flask_app, 'clean_firebase_service', mock_firebase):
        with patch.object(word_api, 'clean_firebase_service', mock_firebase):
            with patch.object(template_module, 'clean_firebase_service', mock_firebase):
                with flask_app.app.test_client() as client:
                    yield client, db_str, tmp_path


@pytest.fixture()
def authenticated_client(base_client, monkeypatch):
    """
    Fixture providing authenticated Flask test client with project.
    Use this for most integration tests.
    """
    client, db_str, tmp_path = base_client
    
    # Create user and project
    conn = sqlite3.connect(db_str)
    cursor = conn.cursor()
    
    from werkzeug.security import generate_password_hash
    cursor.execute(
        "INSERT INTO users (username, email, password_hash, is_active) VALUES (?, ?, ?, 1)",
        ('test_user', 'test@example.com', generate_password_hash('Test123!'))
    )
    user_id = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO projects (name, user_id) VALUES (?, ?)",
        ('Test Project', user_id)
    )
    project_id = cursor.lastrowid
    
    # Add baseline phonemes for testing
    phonemes = [
        ('CVC', 'onset', 'single_consonants', '', '', 'm', user_id, project_id),
        ('CVC', 'onset', 'single_consonants', '', '', 'n', user_id, project_id),
        ('CVC', 'onset', 'single_consonants', '', '', 'p', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', '', '', 'a', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', '', '', 'o', user_id, project_id),
        ('CVC', 'coda', 'single_consonants', '', '', 't', user_id, project_id),
        ('CVC', 'coda', 'single_consonants', '', '', 'd', user_id, project_id),
    ]
    cursor.executemany(
        """INSERT INTO phonemes (syllable_type, position, length_type, group_type,
           subgroup_type, phoneme, user_id, project_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        phonemes
    )
    
    conn.commit()
    conn.close()
    
    # Mock user info for authentication decorators
    mock_user_info = {
        'id': user_id,
        'name': 'test_user',
        'email': 'test@example.com',
        'roles': '',
        'is_authenticated': True,
        'current_project': {
            'id': project_id,
            'name': 'Test Project',
            'storage_type': 'local',
            'cloud_project_id': None,
        },
    }
    
    # Import all modules that need user_info mocking
    import features.admin.template_system as template_module
    
    with patch.object(flask_app, 'get_user_info', return_value=mock_user_info):
        with patch.object(template_module, 'get_user_info', return_value=mock_user_info):
            # Set session
            with client.session_transaction() as sess:
                sess['user_id'] = user_id
                sess['username'] = 'test_user'
                sess['current_project_id'] = project_id
                sess['auth_method'] = 'email_password'
            
            yield client, db_str, user_id, project_id


@pytest.fixture()
def admin_client(authenticated_client):
    """
    Fixture providing authenticated admin client.
    Alias for authenticated_client for clarity in admin tests.
    """
    return authenticated_client
