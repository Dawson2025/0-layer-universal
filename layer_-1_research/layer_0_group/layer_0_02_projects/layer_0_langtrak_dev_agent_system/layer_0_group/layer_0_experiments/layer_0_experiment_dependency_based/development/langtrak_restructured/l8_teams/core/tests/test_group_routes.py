# resource_id: "a4ed259f-4c30-4c0a-85d9-5b72bcf67268"
# resource_type: "document"
# resource_name: "test_group_routes"
"""Integration tests for the groups blueprint routes and APIs."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from typing import Iterator, Tuple

import pytest

import app
import main
import core.database as core_database
from features.auth import helpers as auth_helpers
from features.groups import display as group_display
from flask import Flask


@pytest.fixture
def temp_app(tmp_path, monkeypatch) -> Iterator[Tuple[Flask, sqlite3.Connection, sqlite3.Cursor]]:
    """Provide an isolated Flask app instance backed by a temporary database, returning the app, connection, and cursor."""

    temp_db_path = tmp_path / "groups_test.db"
    original_db = main.DB_NAME

    main.DB_NAME = str(temp_db_path)
    app.main.DB_NAME = str(temp_db_path)
    core_database.DB_NAME = str(temp_db_path)

    # Disable remote dependencies during tests
    for module in (app, auth_helpers, group_display):
        if hasattr(module, "clean_firebase_service"):
            monkeypatch.setattr(module.clean_firebase_service, "is_available", lambda: False, raising=False)
        if hasattr(module, "firestore_db"):
            monkeypatch.setattr(module.firestore_db, "count_project_words", lambda *args, **kwargs: 0, raising=False)
            monkeypatch.setattr(module.firestore_db, "get_user_projects", lambda *args, **kwargs: [], raising=False)
            monkeypatch.setattr(module.firestore_db, "get_project", lambda *args, **kwargs: None, raising=False)

    # Ensure schema exists for the new database
    core_database.init_database()
    main.migrate_schema()
    # app.init_users_table() # Removed - this contains conflicting schema definitions

    # Get a connection and cursor for the fixture
    conn = core_database.get_db_connection(temp_db_path)
    cursor = conn.cursor()

    # Debug print schema of project_shares
    cursor.execute("PRAGMA table_info(project_shares)")
    print(f"DEBUG: project_shares schema: {cursor.fetchall()}")

    test_app = app.app
    assert test_app is not None
    yield test_app, conn, cursor # Yield app, connection, and cursor

    # Commit any pending changes and close connection from fixture
    conn.commit()
    conn.close()

    # Restore globals after test execution
    main.DB_NAME = original_db
    app.main.DB_NAME = original_db
    core_database.DB_NAME = original_db


def _create_user(conn: sqlite3.Connection, cursor: sqlite3.Cursor, username: str = "tester", email: str | None = None) -> int:
    email = email or f"{username}@example.com"
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash, is_active, created_at) VALUES (?, ?, 'hash', 1, ?)",
            (username, email, datetime.now(timezone.utc).isoformat()),
        )
        user_id = cursor.lastrowid
        conn.commit() # Commit changes made by helper functions
        print(f"DEBUG Test Helper: _create_user generated user_id={user_id} for username='{username}'")
        return user_id
    except Exception as e:
        print(f"ERROR Test Helper: _create_user failed for username='{username}': {e}")
        raise e


def _user_is_group_admin(cursor: sqlite3.Cursor, group_id: int, user_id: int) -> bool:
    cursor.execute(
        "SELECT user_id FROM project_groups WHERE id = ?",
        (group_id,),
    )
    group_data = cursor.fetchone()
    return bool(group_data and group_data[0] == user_id)


def _create_group(conn: sqlite3.Connection, cursor: sqlite3.Cursor, admin_user_id: int, name: str = "Team Alpha") -> int:
    try:
        cursor.execute(
            "INSERT INTO project_groups (name, description, user_id, group_identifier, invite_code) VALUES (?, ?, ?, ?, ?)",
            (name, "Test group", admin_user_id, f"local:group_{name.replace(' ', '_')}", "token")
        )
        group_id = cursor.lastrowid
        if group_id is None:
            raise Exception("Failed to create group or retrieve group_id")

        cursor.execute(
            "INSERT INTO group_memberships (group_id, user_id) VALUES (?, ?)",
            (group_id, admin_user_id),
        )
        conn.commit() # Commit changes made by helper functions
        print(f"DEBUG Test Helper: _create_group generated group_id={group_id} for name='{name}', admin_user_id={admin_user_id}")
        return group_id
    except Exception as e:
        print(f"ERROR Test Helper: _create_group failed for name='{name}', admin_user_id={admin_user_id}: {e}")
        raise e


def _add_member(conn: sqlite3.Connection, cursor: sqlite3.Cursor, group_id: int, user_id: int) -> None:
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO group_memberships (group_id, user_id) VALUES (?, ?)",
            (group_id, user_id),
        )
        conn.commit() # Commit changes made by helper functions
    except Exception as e:
        print(f"ERROR Test Helper: _add_member failed for group_id={group_id}, user_id={user_id}: {e}")
        raise e


def test_groups_menu_lists_members_groups(temp_app):
    flask_app, conn, cursor = temp_app
    user_id = _create_user(conn, cursor)
    _create_group(conn, cursor, user_id, "Writers Guild")
    # conn.commit() # Removed - commit happens in helpers

    client = flask_app.test_client()
    with client.session_transaction() as session:
        session["user_id"] = user_id
        session["username"] = "tester"
        session["auth_method"] = "email_password"

    response = client.get("/groups")

    assert response.status_code == 200
    assert b"Writers Guild" in response.data


def test_group_project_creation_shares_project(temp_app):
    flask_app, conn, cursor = temp_app
    user_id = _create_user(conn, cursor, "admin")
    group_id = _create_group(conn, cursor, user_id, "Builders")
    # conn.commit() # Removed - commit happens in helpers

    client = flask_app.test_client()
    with client.session_transaction() as session:
        session["user_id"] = user_id
        session["username"] = "admin"
        session["auth_method"] = "email_password"

    response = client.post(
        f"/api/groups/{group_id}/projects",
        json={"name": "Shared Variant", "description": "New collaborative variant"},
    )

    assert response.status_code == 200
    payload = response.get_json()
    if not payload["success"]:
        print(f"DEBUG: Project creation failed: {payload}")
    assert payload["success"]

    # Verify project shares after API call
    cursor.execute(
        "SELECT p.name, ps.project_identifier FROM project_shares ps JOIN projects p ON ps.project_id = p.id WHERE ps.group_id = ?",
        (group_id,),
    )
    row = cursor.fetchone()
    assert row is not None
    project_name, project_identifier = row
    assert project_name == "Shared Variant"
    assert project_identifier.startswith("local:")


def test_regenerate_invite_requires_admin(temp_app):
    flask_app, conn, cursor = temp_app
    admin_id = _create_user(conn, cursor, "owner")
    member_id = _create_user(conn, cursor, "member")
    group_id = _create_group(conn, cursor, admin_id, "Explorers")
    _add_member(conn, cursor, group_id, member_id)
    # conn.commit() # Removed - commit happens in helpers

    client = flask_app.test_client()
    with client.session_transaction() as session:
        session["user_id"] = member_id
        session["username"] = "member"
        session["auth_method"] = "email_password"

    response = client.post(f"/api/groups/{group_id}/regenerate-invite")
    assert response.status_code == 200
    assert not response.get_json()["success"]

    with client.session_transaction() as session:
        session["user_id"] = admin_id
        session["username"] = "owner"
        session["auth_method"] = "email_password"

    response = client.post(f"/api/groups/{group_id}/regenerate-invite")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["success"]
    assert "invite_link" in payload