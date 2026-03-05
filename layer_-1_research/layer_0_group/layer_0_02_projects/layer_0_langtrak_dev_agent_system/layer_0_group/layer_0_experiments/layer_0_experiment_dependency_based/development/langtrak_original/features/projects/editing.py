# resource_id: "f9821543-7fae-4e8b-85ad-48aaeef0757e"
# resource_type: "document"
# resource_name: "editing"
"""
Projects Editing Module

Handles editing project metadata (name, etc.).
Agents can work on editing improvements without affecting other sub-modules.
"""

from flask import render_template, request, redirect, url_for, flash
import sqlite3

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from services.firebase import clean_firebase_service
from services.firebase import firestore_db
from .metadata import fetch_project_metadata, normalize_project_identifier
from . import projects_bp


@projects_bp.route('/projects/<project_id>/edit', methods=['GET', 'POST'])
@require_auth
def edit_project(project_id):
    """
    Edit project name and metadata.

    Supports both local (SQLite) and cloud (Firestore) projects.

    Args:
        project_id: ID of project to edit

    Returns:
        Rendered edit form or redirect on success
    """
    user = get_user_info()

    storage_type, identifier, project_identifier = normalize_project_identifier(project_id)
    if not storage_type:
        flash('Invalid project identifier', 'error')
        return redirect(url_for('projects.projects_menu'))

    # Handle local project editing
    if storage_type == 'local':
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.name FROM projects p
            WHERE p.id = ? AND p.user_id = ?
        """, (identifier, user['id']))
        project = cursor.fetchone()

        if not project:
            cursor.close()
            conn.close()
            flash('Project not found or access denied', 'error')
            return redirect(url_for('projects.projects_menu'))

        current_name = project[0]

        if request.method == 'POST':
            new_name = request.form.get('name', '').strip()

            if not new_name:
                flash('Project name is required', 'error')
                cursor.close()
                conn.close()
                return render_template('edit_project.html',
                                     project={'id': project_id, 'name': current_name},
                                     user=user)

            try:
                cursor.execute("""
                    UPDATE projects
                    SET name = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ? AND user_id = ?
                """, (new_name, identifier, user['id']))

                # Update language for all words in this project
                cursor.execute("""
                    UPDATE words
                    SET language = ?
                    WHERE project_id = ?
                """, (new_name, identifier))

                conn.commit()
                flash(f'Project renamed to "{new_name}" successfully!', 'success')
                return redirect(url_for('projects.projects_menu'))

            except sqlite3.IntegrityError:
                flash('A project with this name already exists', 'error')
            finally:
                cursor.close()
                conn.close()

        cursor.close()
        conn.close()
        return render_template('edit_project.html',
                             project={'id': project_id, 'name': current_name},
                             user=user)

    # Handle cloud project editing
    if not clean_firebase_service.is_available():
        flash('Cloud storage features are currently unavailable.', 'error')
        return redirect(url_for('projects.projects_menu'))

    project_meta = fetch_project_metadata('cloud', identifier, owner_id=user['id'])
    if not project_meta:
        flash('Project not found or access denied', 'error')
        return redirect(url_for('projects.projects_menu'))

    current_name = project_meta.get('name') or 'Cloud Project'

    if request.method == 'POST':
        new_name = request.form.get('name', '').strip()
        if not new_name:
            flash('Project name is required', 'error')
            return render_template('edit_project.html',
                                 project={'id': project_id, 'name': current_name},
                                 user=user)

        try:
            firestore_db.update_project(identifier, {'name': new_name})

            # Update language for all associated words for consistency
            words = firestore_db.get_project_words(identifier)
            for word in words:
                word_id = word.get('id')
                if word_id:
                    firestore_db.update_word(word_id, {'language': new_name})

            flash(f'Cloud project renamed to "{new_name}" successfully!', 'success')
            return redirect(url_for('projects.projects_menu'))
        except Exception as exc:
            flash(f'Unable to update project: {exc}', 'error')
            return render_template('edit_project.html',
                                 project={'id': project_id, 'name': current_name},
                                 user=user)

    return render_template('edit_project.html',
                         project={'id': project_id, 'name': current_name},
                         user=user)


__all__ = ['edit_project']
