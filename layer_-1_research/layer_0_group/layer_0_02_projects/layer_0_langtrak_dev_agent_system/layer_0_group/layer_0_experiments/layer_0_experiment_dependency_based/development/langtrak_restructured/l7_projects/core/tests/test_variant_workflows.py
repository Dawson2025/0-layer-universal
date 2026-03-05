# resource_id: "94f10f53-554a-46ef-8715-6ccdb9ef2534"
# resource_type: "document"
# resource_name: "test_variant_workflows"
from typing import Iterator, Tuple
import sqlite3
from datetime import datetime

import pytest

import main
import app
import core.database as core_database
import src.storage_manager as storage_manager_module
from src.storage_manager import storage_manager
from flask import Flask


@pytest.fixture
def temp_app(tmp_path, monkeypatch) -> Iterator[Tuple[Flask, sqlite3.Connection, sqlite3.Cursor]]:
    """Set up an isolated app context with a temporary SQLite database."""
    temp_db_path = tmp_path / "data/test_phonemes.db"
    original_db = main.DB_NAME
    original_core_db = core_database.DB_NAME

    main.DB_NAME = str(temp_db_path)
    core_database.DB_NAME = str(temp_db_path) # Ensure core_database uses the temp_db_path

    # Ensure the directory exists
    temp_db_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Delete the temporary database file if it exists to ensure a clean slate
    if temp_db_path.exists():
        temp_db_path.unlink()

    # Initialise database schema BEFORE creating app
    core_database.init_database(db_path=str(temp_db_path))
    main.migrate_schema()

    test_app = app.create_app()
    assert test_app is not None

    # Create connection for test use (each test gets its own connection)
    conn = core_database.get_db_connection(temp_db_path)
    cursor = conn.cursor()

    # Refresh cached column metadata against the new database
    for attr in ('_words_columns', '_phoneme_columns', '_project_columns'):
        if hasattr(storage_manager, attr):
            delattr(storage_manager, attr)
    storage_manager._ensure_column_cache()

    yield test_app, conn, cursor # Yield app, connection, and cursor

    # Teardown: Commit any pending changes and close connection from fixture
    try:
        conn.commit()
        conn.close()
    except sqlite3.ProgrammingError:
        pass  # Connection may already be closed

    # Restore global configuration
    monkeypatch.setattr(main, 'DB_NAME', original_db)
    monkeypatch.setattr(core_database, 'DB_NAME', original_core_db)
    # The app module's main.DB_NAME is implicitly covered by main.DB_NAME monkeypatch
    # storage_manager_module's main.DB_NAME is implicitly covered by main.DB_NAME monkeypatch
    
    # Remove the temporary monkeypatch on sqlite3.connect and storage_manager._connect
    monkeypatch.undo()

    for attr in ('_words_columns', '_phoneme_columns', '_project_columns'):
        if hasattr(storage_manager, attr):
            delattr(storage_manager, attr)
    storage_manager._ensure_column_cache()


def _create_user(conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash, is_active) VALUES (?, ?, ?, 1)",
            ('tester', 'tester@example.com', 'hash')
        )
        user_id = cursor.lastrowid
        conn.commit()
        return user_id
    except Exception as e:
        print(f"ERROR Test Helper: _create_user in test_variant_workflows failed: {e}")
        raise e


def _create_local_project(conn: sqlite3.Connection, cursor: sqlite3.Cursor, user_id, name):
    project_id = storage_manager._create_project_sqlite({
        'name': name,
        'user_id': user_id,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    })

    # After creating the project, ensure the user is added to the corresponding group
    # The group is implicitly created/retrieved by storage_manager.get_projects
    # We need to call get_projects to trigger the group creation and get the group_id
    # associated with this new project's root variant.
    projects_groups = storage_manager.get_projects(user_id)
    
    # Find the group ID for the newly created project
    group_id_for_new_project = None
    for group_item in projects_groups:
        for variant in group_item.get('variants', []):
            if variant.get('id') == str(project_id) and variant.get('type') == 'local':
                group_id_for_new_project = group_item['group_id']
                break
        if group_id_for_new_project:
            break

    if group_id_for_new_project:
        pass # Membership is now handled by storage_manager._ensure_group_metadata

    return project_id


def test_project_variant_menu_route_shows_variants(temp_app):
    flask_app, conn, cursor = temp_app
    user_id = _create_user(conn, cursor)
    project_id = _create_local_project(conn, cursor, user_id, 'Alpha Project')

    # Seed a word so the variant appears populated
    try:
        cursor.execute(
            "INSERT INTO words (language, english_words, project_id, user_id) VALUES (?, ?, ?, ?)",
            ('en', 'alpha', project_id, user_id)
        )
        conn.commit()
    except Exception as e:
        print(f"ERROR: Failed to seed word in test: {e}")
        raise

    projects = storage_manager.get_projects(user_id)
    group_id = projects[0]['group_id']

    client = flask_app.test_client()
    with client.session_transaction() as session:
        session['user_id'] = user_id
        session['auth_method'] = 'email_password'
    
    response = client.get(f'/projects/group/{group_id}')
    assert response.status_code == 200
    assert b'Variant Menu' in response.data
    assert b'Alpha Project' in response.data



def test_merge_endpoint_overwrites_target_variant(temp_app):
    flask_app, conn, cursor = temp_app
    user_id = _create_user(conn, cursor)
    
    main_project_id = _create_local_project(conn, cursor, user_id, 'Main Variant')
    # Seed base project data
    try:
        cursor.execute(
            "INSERT INTO words (language, english_words, project_id, user_id) VALUES (?, ?, ?, ?)",
            ('en', 'base-word', main_project_id, user_id)
        )
        conn.commit()
    except Exception as e:
        print(f"ERROR: Failed to seed word in test: {e}")
        raise

    # Create a branch variant and modify its contents
    success, info = storage_manager.branch_variant(user_id, f'local:{main_project_id}', 'feature')
    assert success, info
    branch_identifier = info['variant_identifier']
    branch_project_id = int(branch_identifier.split(':', 1)[1])

    try:
        cursor.execute(
            "UPDATE words SET english_words = ? WHERE project_id = ?",
            ('feature-word', branch_project_id)
        )
        cursor.execute(
            "INSERT INTO words (language, english_words, project_id, user_id) VALUES (?, ?, ?, ?)",
            ('en', 'new-branch-word', branch_project_id, user_id)
        )
        conn.commit()
    except Exception as e:
        print(f"ERROR: Failed to update/insert word in test: {e}")
        raise

    client = flask_app.test_client()
    with client.session_transaction() as session:
        session['user_id'] = user_id
        session['auth_method'] = 'email_password'

    response = client.post(
        f'/api/projects/{branch_identifier}/merge',
        json={'target_variant': f'local:{main_project_id}'}
    )
    assert response.status_code == 200
    payload = response.get_json()
    assert payload['success']

    try:
        cursor.execute(
            "SELECT english_words FROM words WHERE project_id = ? ORDER BY english_words",
            (main_project_id,)
        )
        merged_words = [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"ERROR: Failed to select words in test: {e}")
        raise

    assert merged_words == ['feature-word', 'new-branch-word']