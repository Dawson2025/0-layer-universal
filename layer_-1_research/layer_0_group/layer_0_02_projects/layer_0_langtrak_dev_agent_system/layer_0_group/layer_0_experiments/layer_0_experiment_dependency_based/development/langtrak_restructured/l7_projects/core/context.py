# resource_id: "a9149918-70c7-4448-8a53-982802778fa0"
# resource_type: "document"
# resource_name: "context"
"""
Projects Context Module

Handles entering and exiting project contexts.
Agents can work on context management without affecting other sub-modules.
"""

from flask import redirect, url_for, flash, session
import sqlite3

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from services.firebase import clean_firebase_service
from services.firebase import firestore_db
import main
from . import projects_bp


@projects_bp.route('/projects/<project_id>/enter')
@require_auth
def enter_project(project_id):
    """
    Enter a specific project context.

    Sets the current project in session, allowing project-scoped operations.
    Supports both Firebase (string ID) and SQLite (integer ID) projects.

    Args:
        project_id: ID of project to enter (can be string or int)

    Returns:
        Redirect to main menu on success, dashboard on failure
    """
    user = get_user_info()

    # Check if project exists in either storage type
    project = None
    project_name = None

    # First check if it's a Firebase project (string ID)
    if clean_firebase_service.is_available():
        try:
            firebase_project = firestore_db.get_project(project_id)
            if firebase_project:
                owner_id = firebase_project.get('user_id')
                if owner_id is None:
                    owner_id = firebase_project.get('user_id_str')
                if owner_id is not None and str(owner_id) == str(user['id']):
                    project = firebase_project
                    project_name = firebase_project.get('name')
        except Exception as e:
            print(f"Error checking Firebase project: {e}")

    # If not found in Firebase, check SQLite (integer ID)
    if not project:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            # Try to convert to int for SQLite lookup
            int_project_id = int(project_id)

            cursor.execute("""
                SELECT p.name, p.user_id FROM projects p
                WHERE p.id = ? AND (
                    p.user_id = ? OR
                    EXISTS (
                        SELECT 1 FROM project_shares ps
                        JOIN group_memberships gm ON ps.group_id = gm.group_id
                        WHERE gm.user_id = ?
                          AND ps.project_identifier IN ('local:' || p.id, 'cloud:' || p.cloud_project_id)
                    )
                )
            """, (int_project_id, user['id'], user['id']))
            sqlite_project = cursor.fetchone()

            if sqlite_project:
                project = {'name': sqlite_project[0], 'user_id': sqlite_project[1]}
                project_name = sqlite_project[0]

            conn.close()
        except (ValueError, TypeError):
            # project_id is not a valid integer, skip SQLite check
            pass
        except Exception as e:
            print(f"Error checking SQLite project: {e}")

    if project:
        session['current_project_id'] = project_id
        flash(f'Entered project: {project_name}', 'success')
        return redirect(url_for('main_menu'))
    else:
        flash('Project not found or access denied', 'error')
        return redirect(url_for('dashboard.dashboard'))


@projects_bp.route('/projects/exit')
@require_auth
def exit_project():
    """
    Exit current project context.

    Removes current_project_id from session.

    Returns:
        Redirect to dashboard
    """
    if 'current_project_id' in session:
        del session['current_project_id']
        flash('Exited project', 'success')

    return redirect(url_for('dashboard.dashboard'))


__all__ = ['enter_project', 'exit_project']
