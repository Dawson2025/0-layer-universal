# resource_id: "15c77399-e63b-46aa-a35d-300ab4de172d"
# resource_type: "document"
# resource_name: "membership"
"""Group membership and invitation management."""

from __future__ import annotations

import sqlite3

from flask import flash, redirect, session, url_for

import main
from features.auth import get_user_info

from . import groups_bp


@groups_bp.route("/groups/join/<invite_token>")
def join_group_via_invite(invite_token: str):
    """Join group via invite link."""

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT gi.group_id, g.name, gi.expires_at
            FROM group_invites gi
            JOIN groups g ON gi.group_id = g.id
            WHERE gi.invite_token = ? AND gi.expires_at > datetime('now')
            """,
            (invite_token,),
        )

        invite_data = cursor.fetchone()
        if not invite_data:
            flash("Invalid or expired invite link", "error")
            return redirect(url_for("index"))

        group_id, group_name, _expires_at = invite_data

        user = get_user_info()
        if not user["is_authenticated"]:
            session["pending_group_invite"] = invite_token
            flash(f'Please create an account or sign in to join "{group_name}"', "info")
            return redirect(url_for("auth.register"))

        cursor.execute(
            """
            SELECT id FROM group_memberships
            WHERE group_id = ? AND user_id = ?
            """,
            (group_id, user["id"]),
        )

        if cursor.fetchone():
            flash(f'You are already a member of "{group_name}"', "info")
            return redirect(url_for("groups.group_detail", group_id=group_id))

        try:
            cursor.execute(
                """
                INSERT INTO group_memberships (group_id, user_id)
                VALUES (?, ?)
                """,
                (group_id, user["id"]),
            )
            conn.commit()
            flash(f'Successfully joined "{group_name}"!', "success")
            return redirect(url_for("groups.group_detail", group_id=group_id))
        except Exception as exc:  # pragma: no cover - defensive logging aid
            flash(f"Error joining group: {exc}", "error")
            return redirect(url_for("groups.groups_menu"))

    finally:
        conn.close()

    # Fallback redirect - should not be reached during normal flow.
    return redirect(url_for("index"))
