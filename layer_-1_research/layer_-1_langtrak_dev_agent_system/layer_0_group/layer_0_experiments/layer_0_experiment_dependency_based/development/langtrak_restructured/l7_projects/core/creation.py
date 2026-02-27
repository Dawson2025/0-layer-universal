"""
Projects Creation Module

Handles creating new projects with cloud or local storage.
Agents can work on creation improvements without affecting other sub-modules.
"""

from flask import render_template, request, redirect, url_for, flash, session, get_flashed_messages
import sqlite3

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from services.firebase import clean_firebase_service, firestore_db
from src.storage_manager import storage_manager, StorageType
from . import projects_bp


@projects_bp.route('/projects/create', methods=['GET', 'POST'])
@require_auth
def create_project():
    """
    Create a new project with cloud or local storage.

    GET: Display creation form
    POST: Process form and create project

    Returns:
        Rendered creation form or redirect to new project
    """
    user = get_user_info()

    # Get user's groups for sharing functionality
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT g.id, g.name
        FROM groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ?
        ORDER BY g.name
    """, (user['id'],))

    user_groups = []
    for group in cursor.fetchall():
        user_groups.append({
            'id': group[0],
            'name': group[1]
        })
    conn.close()

    if request.method == 'POST':
        print("DEBUG: POST request received for project creation")
        project_name = request.form.get('name', '').strip()
        storage_type = request.form.get('storage_type', 'cloud')  # Default to cloud
        print(f"DEBUG: Extracted project_name='{project_name}', storage_type='{storage_type}'")

        if not project_name:
            flash('Project name is required', 'error')
            return render_template('create_project.html',
                                 user=user,
                                 user_groups=user_groups,
                                 firebase_available=clean_firebase_service.is_available())

        # Convert storage type string to enum
        storage_enum = StorageType.CLOUD if storage_type == 'cloud' else StorageType.LOCAL

        try:
            # Use storage manager to create project with selected storage type
            project_data = {
                'name': project_name,
                'user_id': user['id'],
                'firebase_uid': user.get('firebase_uid')
            }

            # Debug logging
            print(f"DEBUG: Creating project '{project_name}' for user {user['id']}")
            print(f"DEBUG: Storage type requested: {storage_type}")
            print(f"DEBUG: Storage enum: {storage_enum}")
            print(f"DEBUG: Clean Firebase available: {clean_firebase_service.is_available()}")

            # Try cloud storage first, fallback to local if Firebase fails
            if storage_enum == StorageType.CLOUD:
                try:
                    # Check if Firebase is actually available before attempting
                    if not clean_firebase_service.is_available():
                        raise Exception("Firebase not available")
                    print("DEBUG: Attempting cloud storage creation...")
                    project_id = storage_manager.create_project_with_storage(project_data, storage_enum)
                    print(f"DEBUG: Cloud storage result: {project_id}")
                    # Confirm Firestore write before treating as success
                    if not project_id or not firestore_db.get_project(project_id):
                        raise Exception("Cloud project write not confirmed")
                except Exception as cloud_error:
                    print(f"Cloud storage failed: {cloud_error}")
                    # Fallback to local storage
                    storage_enum = StorageType.LOCAL
                    project_id = storage_manager.create_project_with_storage(project_data, storage_enum)
                    flash(f'Cloud storage unavailable - created "{project_name}" with local storage. You can migrate to cloud later.', 'warning')
            else:
                project_id = storage_manager.create_project_with_storage(project_data, storage_enum)

            print(f"DEBUG: Final project_id check: {project_id}")

            if project_id:
                # Seed project with default phoneme template (hard-coded English baseline)
                try:
                    from src.phoneme_seed import seed_project_phonemes
                    # Determine storage label and normalized project id for seeding
                    storage_label = "cloud" if storage_enum == StorageType.CLOUD else "local"
                    seed_project_phonemes(str(project_id), user.get('id'), storage_label)
                except Exception as seed_exc:
                    print(f"Warning: failed to seed default phonemes: {seed_exc}")

                # Automatically switch to the new project and enter it
                session['current_project_id'] = project_id

                storage_label = "cloud (Firebase)" if storage_enum == StorageType.CLOUD else "local (SQLite)"
                if 'warning' not in [msg[0] for msg in get_flashed_messages(with_categories=True)]:
                    flash(f'Project "{project_name}" created successfully using {storage_label} storage!', 'success')

                print(f"DEBUG: Redirecting to project {project_id}")
                # Automatically enter the new project instead of going to projects menu
                return redirect(url_for('projects.enter_project', project_id=project_id))
            else:
                print("DEBUG: project_id is None - showing 'Failed to create project'")
                flash('Failed to create project', 'error')

        except Exception as e:
            flash(f'Error creating project: {e}', 'error')

    return render_template('create_project.html',
                         user=user,
                         user_groups=user_groups,
                         firebase_available=clean_firebase_service.is_available())


__all__ = ['create_project']
