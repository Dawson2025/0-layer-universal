# resource_id: "30e2d706-bf14-4153-97b1-32c955f05133"
# resource_type: "document"
# resource_name: "api"
"""API endpoints for the groups feature."""

from __future__ import annotations

import sqlite3
from typing import Any, Dict

from flask import jsonify, request

import main
from features.auth import get_user_info, require_auth

from . import groups_bp


def _user_is_group_admin(cursor: sqlite3.Cursor, group_id: int, user_id: int) -> bool:
    cursor.execute(
        "SELECT user_id FROM project_groups WHERE id = ?", # Query project_groups.id and user_id
        (group_id,),
    )
    group_data = cursor.fetchone()
    return bool(group_data and group_data[0] == user_id)


@groups_bp.route("/api/groups/<int:group_id>/regenerate-invite", methods=["POST"])
@require_auth
def api_regenerate_invite_link(group_id: int):
    """Regenerate invite link for group (admin only)."""

    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        if not _user_is_group_admin(cursor, group_id, user["id"]):
            return jsonify({"success": False, "error": "Access denied"})

        try:
            import secrets

            invite_token = secrets.token_urlsafe(32)
            cursor.execute(
                """
                UPDATE project_groups
                SET invite_code = ?, created_at = CURRENT_TIMESTAMP
                WHERE id = ? AND user_id = ?
                """,
                (invite_token, group_id, user["id"]),
            )

            conn.commit()

            invite_url = f"{request.host_url}groups/join/{invite_token}"
            return jsonify(
                {
                    "success": True,
                    "invite_link": {"token": invite_token, "url": invite_url},
                    "message": "New invite link generated successfully!",
                }
            )

        except Exception as exc:  # pragma: no cover - defensive logging aid
            conn.rollback()
            return jsonify({"success": False, "error": str(exc)})

    finally:
        conn.close()


def _user_is_group_member(cursor: sqlite3.Cursor, group_id: int, user_id: int) -> bool:
    cursor.execute(
        """
        SELECT id FROM group_memberships
        WHERE group_id = ? AND user_id = ?
        """,
        (group_id, user_id),
    )
    return cursor.fetchone() is not None


def _create_project(
    cursor: sqlite3.Cursor, user_id: int, project_name: str, project_description: str
) -> int: # Changed return type to int
    try:
        cursor.execute(
            """
            INSERT INTO projects (name, user_id, created_at, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """,
            (project_name, user_id),
        )
        project_id = cursor.lastrowid
        if project_id is None:
            print(f"ERROR: _create_project failed to get lastrowid after inserting project {project_name}")
            raise Exception("Failed to retrieve project ID after insert")
        print(f"DEBUG: _create_project generated project_id: {project_id} for project '{project_name}'")
        return project_id # Return the integer directly
    except Exception as e:
        print(f"ERROR: _create_project failed for project '{project_name}': {e}")
        raise e


@groups_bp.route("/api/groups/<int:group_id>/projects", methods=["POST"])
@require_auth
def api_create_group_project(group_id: int):
    """Create a new project for the group."""

    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        if not _user_is_group_member(cursor, group_id, user["id"]):
            return jsonify({"success": False, "error": "Access denied"})

        data: Dict[str, Any] = request.get_json(silent=True) or {}
        project_name = data.get("name", "").strip()
        project_description = data.get("description", "").strip()

        if not project_name:
            return jsonify({"success": False, "error": "Project name is required"})

        try:
            # Call _create_project which now returns an integer project_id
            project_id = _create_project(cursor, user["id"], project_name, project_description)
            project_identifier = f"local:{project_id}"
            print(f"DEBUG: api_create_group_project project_identifier: {project_identifier}, project_id (int): {project_id}")

            cursor.execute(
                """
                INSERT INTO project_shares (project_identifier, project_id, storage_type, group_id, shared_by)
                VALUES (?, ?, ?, ?, ?)
                """,
                (project_identifier, project_id, 'local', group_id, user["id"]), # Corrected parameter order and count
            )

        except Exception as exc:  # pragma: no cover - defensive logging aid
            conn.rollback()
            print(f"ERROR in api_create_group_project: {str(exc)}") # Debug print the actual exception
            return jsonify({"success": False, "error": str(exc)})

    finally:
        conn.close()
