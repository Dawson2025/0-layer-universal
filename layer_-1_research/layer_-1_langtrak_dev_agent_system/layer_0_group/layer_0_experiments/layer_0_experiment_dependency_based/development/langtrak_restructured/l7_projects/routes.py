"""L7 Projects Layer - All project, dashboard, and navigation routes.

Consolidates:
- / (index redirect)
- /dashboard (user dashboard)
- /main-menu (main navigation)
- /projects (projects list)
- /projects/group/<id> (projects by group)
- /projects/create (create project)
- /projects/<id>/migrate-to-cloud (migrate to cloud)
- /projects/<id>/enter (enter project)
- /projects/exit (exit project)
- /projects/<id>/edit (edit project)
- /api/projects/<id>/rename (rename API)
- /api/projects/<id>/branch (branch API)
- /api/projects/shared (shared projects API)
- Template application helpers
"""

import sqlite3

from flask import (
    Blueprint,
    flash,
    get_flashed_messages,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

import main
from l2_infrastructure.auth import require_auth, require_project_admin
from l3_users.sessions.session import get_user_info
from l2_infrastructure.firebase import clean_firebase_service, firestore_db
from l2_infrastructure.storage import storage_manager, StorageType

l7_bp = Blueprint('l7_projects', __name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_project_owner(project_id, user_id):
    """Check if user is the owner of a project (works with both Firebase and SQLite)"""
    # First check if it's a Firebase project
    if clean_firebase_service.is_available():
        try:
            firebase_project = firestore_db.get_project(project_id)
            if firebase_project:
                return firebase_project.get('user_id') == user_id
        except Exception as e:
            print(f"Error checking Firebase project ownership: {e}")

    # Check SQLite projects (for local projects or if Firebase fails)
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Try to convert to int for SQLite lookup
        int_project_id = int(project_id)
        cursor.execute("SELECT user_id FROM projects WHERE id = ?", (int_project_id,))
        result = cursor.fetchone()
        conn.close()

        return result and result[0] == user_id
    except (ValueError, TypeError):
        # project_id is not a valid integer, so it's not a SQLite project
        return False


def apply_template_to_new_project(project_id, template_selection, user_id, storage_type):
    """Apply a selected template to a newly created project"""
    try:
        if ':' not in template_selection:
            return False

        template_type, template_id = template_selection.split(':', 1)
        print(f"DEBUG: Applying {template_type} template {template_id} to project {project_id}")

        if template_type == 'local':
            # Apply local SQLite template
            return apply_local_template_to_project(project_id, template_id, user_id, storage_type)
        elif template_type == 'cloud':
            # Apply cloud Firebase template
            return apply_cloud_template_to_project(project_id, template_id, user_id, storage_type)
        else:
            print(f"DEBUG: Unknown template type: {template_type}")
            return False

    except Exception as e:
        print(f"Error applying template to new project: {e}")
        return False


def apply_local_template_to_project(project_id, template_id, user_id, storage_type):
    """Apply a local SQLite template to a project"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Get template phonemes from SQLite
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type,
                   subgroup_type, sub_subgroup_type, sub_sub_subgroup_type,
                   phoneme, frequency
            FROM template_phonemes
            WHERE template_id = ?
            ORDER BY syllable_type, position, length_type, phoneme
        """, (template_id,))

        template_phonemes = cursor.fetchall()
        conn.close()

        if not template_phonemes:
            print(f"DEBUG: No phonemes found for local template {template_id}")
            return False

        # Apply phonemes to the project based on storage type
        if storage_type == StorageType.CLOUD:
            # For cloud projects, create phonemes in Firebase
            for phoneme_row in template_phonemes:
                phoneme_data = {
                    'syllable_type': phoneme_row[0],
                    'position': phoneme_row[1],
                    'length_type': phoneme_row[2],
                    'group_type': phoneme_row[3],
                    'subgroup_type': phoneme_row[4],
                    'sub_subgroup_type': phoneme_row[5],
                    'sub_sub_subgroup_type': phoneme_row[6],
                    'phoneme': phoneme_row[7],
                    'frequency': phoneme_row[8],
                    'project_id': project_id,
                    'user_id': user_id
                }
                firestore_db.create_phoneme(phoneme_data)
        else:
            # For local projects, create phonemes in SQLite
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()

            for phoneme_row in template_phonemes:
                cursor.execute("""
                    INSERT INTO project_phonemes
                    (project_id, syllable_type, position, length_type, group_type,
                     subgroup_type, sub_subgroup_type, sub_sub_subgroup_type,
                     phoneme, frequency)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (project_id, phoneme_row[0], phoneme_row[1], phoneme_row[2],
                      phoneme_row[3], phoneme_row[4], phoneme_row[5], phoneme_row[6],
                      phoneme_row[7], phoneme_row[8]))

            conn.commit()
            conn.close()

        return True

    except Exception as e:
        print(f"Error applying local template: {e}")
        return False


def apply_cloud_template_to_project(project_id, template_id, user_id, storage_type):
    """Apply a cloud Firebase template to a project"""
    try:
        # Use the Firebase template application method
        if storage_type == StorageType.CLOUD:
            # For cloud projects, use Firebase template initialization
            return firestore_db.initialize_project_phonemes_from_template(project_id, template_id, user_id)
        else:
            # For local projects, get cloud template and apply to SQLite
            template = firestore_db.get_phoneme_template(template_id)
            if not template:
                print(f"DEBUG: Cloud template {template_id} not found")
                return False

            template_phonemes = template.get('phonemes', [])
            if not template_phonemes:
                print(f"DEBUG: Cloud template {template_id} has no phonemes")
                return False

            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()

            for phoneme_data in template_phonemes:
                cursor.execute("""
                    INSERT INTO project_phonemes
                    (project_id, syllable_type, position, length_type, group_type,
                     subgroup_type, sub_subgroup_type, sub_sub_subgroup_type,
                     phoneme, frequency)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (project_id,
                      phoneme_data.get('syllable_type'),
                      phoneme_data.get('position'),
                      phoneme_data.get('length_type'),
                      phoneme_data.get('group_type'),
                      phoneme_data.get('subgroup_type'),
                      phoneme_data.get('sub_subgroup_type', ''),
                      phoneme_data.get('sub_sub_subgroup_type', ''),
                      phoneme_data.get('phoneme'),
                      phoneme_data.get('frequency', 0)))

            conn.commit()
            conn.close()

            return True

    except Exception as e:
        print(f"Error applying cloud template: {e}")
        return False


# ---------------------------------------------------------------------------
# Routes: Index
# ---------------------------------------------------------------------------

@l7_bp.route('/')
def index():
    """Main menu - redirects to login for unauthenticated users, shows project dashboard for authenticated users"""

    # Quick health check for deployment monitoring
    user_agent = request.headers.get('User-Agent', '')
    if user_agent.startswith('GoogleHC') or 'health' in request.args:
        return {'status': 'healthy', 'message': 'Flask app is running'}, 200

    # Get user information
    user = get_user_info()

    # If not authenticated, redirect to login
    if not user['is_authenticated']:
        return redirect(url_for('login'))

    # If authenticated, show projects and groups dashboard
    return redirect(url_for('l7_projects.dashboard'))


# ---------------------------------------------------------------------------
# Routes: Dashboard
# ---------------------------------------------------------------------------

@l7_bp.route('/dashboard')
@require_auth
def dashboard():
    """User dashboard showing projects and groups"""
    user = get_user_info()

    # If the user just authenticated from a group invite flow, complete the join.
    if 'pending_group_invite' in session:
        invite_token = session.pop('pending_group_invite')
        return redirect(url_for('join_group_via_invite', invite_token=invite_token))

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Get user's projects from both storage types using storage manager
    print(f"DEBUG: Dashboard fetching projects for user {user['id']}")

    # Check Firebase projects directly
    if clean_firebase_service.is_available():
        try:
            firebase_projects = firestore_db.get_user_projects(user['id'])
            print(f"DEBUG: Direct Firebase query returned {len(firebase_projects)} projects: {[p.get('name', 'no name') for p in firebase_projects]}")
        except Exception as e:
            print(f"DEBUG: Error getting Firebase projects directly: {e}")

    projects = storage_manager.get_projects(user['id'])
    print(f"DEBUG: Dashboard retrieved {len(projects)} projects: {[p.get('name', 'no name') for p in projects]}")
    print(f"DEBUG: Project storage types: {[(p.get('name'), p.get('storage_type')) for p in projects]}")

    # Add word count and storage metadata for each project
    for project in projects:
        print(f"DEBUG: Dashboard processing project {project.get('name')} with storage_type: {project.get('storage_type')}, id: {project.get('id')} (type: {type(project.get('id'))})")
        # Get word count
        if project.get('storage_type') == 'cloud':
            # For cloud projects, count words in Firestore
            try:
                firestore_words = firestore_db.get_project_words(project['id'])
                project['word_count'] = len(firestore_words) if firestore_words else 0
            except Exception as e:
                print(f"Error counting Firestore words for project {project['id']}: {e}")
                project['word_count'] = 0
            project['storage_icon'] = '\U0001f310'
            project['storage_label'] = 'Cloud'
            project['can_migrate'] = False
        else:
            # For local projects, count words in SQLite
            project_id = project.get('id')
            print(f"DEBUG: Dashboard counting words for local project {project_id}")
            if project_id:
                cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (project_id,))
                word_count = cursor.fetchone()[0]
            else:
                print(f"DEBUG: No project ID found for project: {project}")
                word_count = 0
            project['word_count'] = word_count
            project['storage_icon'] = '\U0001f4be'
            project['storage_label'] = 'Local'
            project['can_migrate'] = clean_firebase_service.is_available()

    # Get shared projects (projects from group members that are shared)
    cursor.execute("""
        SELECT DISTINCT p.id, p.name, p.created_at, p.updated_at, u.username as owner_name, g.name as group_name
        FROM projects p
        JOIN users u ON p.user_id = u.id
        JOIN project_shares ps ON p.id = ps.project_id
        JOIN project_groups g ON ps.group_id = g.id
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ? AND p.user_id != ?
        ORDER BY p.updated_at DESC
    """, (user['id'], user['id']))

    shared_projects = []
    for project in cursor.fetchall():
        # Get word count for each shared project
        cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (project[0],))
        word_count = cursor.fetchone()[0]

        shared_projects.append({
            'id': project[0],
            'name': project[1],
            'created_at': project[2],
            'updated_at': project[3],
            'word_count': word_count,
            'owner_name': project[4],
            'group_name': project[5]
        })

    # Get user's groups
    cursor.execute("""
        SELECT g.id, g.name, g.description, g.created_at, g.user_id,
               CASE WHEN g.user_id = ? THEN 1 ELSE 0 END as is_admin
        FROM project_groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ?
        ORDER BY g.created_at DESC
    """, (user['id'], user['id']))

    groups = []
    for group in cursor.fetchall():
        groups.append({
            'id': group[0],
            'name': group[1],
            'description': group[2],
            'created_at': group[3],
            'admin_user_id': group[4],
            'is_admin': bool(group[5])
        })

    conn.close()

    return render_template('dashboard.html', projects=projects, shared_projects=shared_projects, groups=groups, user=user)


# ---------------------------------------------------------------------------
# Routes: Main Menu / Navigation
# ---------------------------------------------------------------------------

@l7_bp.route('/main-menu')
@require_auth
def main_menu():
    """Main application menu - only accessible when in a project context"""
    user = get_user_info()

    # Check for current project in session first (simpler approach)
    if 'current_project_id' not in session:
        flash('Please enter a project to access the main menu', 'error')
        return redirect(url_for('l7_projects.dashboard'))

    # Get project info directly for display
    project_id = session['current_project_id']
    project_name = "Unknown Project"

    # Try to get project name from Firebase first
    if clean_firebase_service.is_available():
        try:
            firebase_project = firestore_db.get_project(project_id)
            if firebase_project:
                project_name = firebase_project.get('name', 'Unknown Project')
        except:
            pass

    # If not found in Firebase, try SQLite
    if project_name == "Unknown Project":
        try:
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM projects WHERE id = ?", (int(project_id),))
            result = cursor.fetchone()
            if result:
                project_name = result[0]
            conn.close()
        except:
            pass

    # Get word statistics for the current project
    stats = {
        'total_words': 0,
        'total_languages': 0,
        'words_with_videos': 0,
        'structured_words': 0
    }

    # For Firebase projects, get stats from Firestore
    if clean_firebase_service.is_available():
        try:
            words = firestore_db.get_project_words(project_id)
            if words:
                stats['total_words'] = len(words)
                languages = set(word.get('language') for word in words if word.get('language'))
                stats['total_languages'] = len(languages)
                stats['words_with_videos'] = sum(1 for word in words if word.get('video_path'))
                stats['structured_words'] = sum(1 for word in words if word.get('syllable_type'))
        except:
            # If Firebase fails, try SQLite
            try:
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (int(project_id),))
                stats['total_words'] = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(DISTINCT language) FROM words WHERE language IS NOT NULL AND project_id = ?", (int(project_id),))
                stats['total_languages'] = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM words WHERE video_path IS NOT NULL AND project_id = ?", (int(project_id),))
                stats['words_with_videos'] = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM words WHERE syllable_type IS NOT NULL AND project_id = ?", (int(project_id),))
                stats['structured_words'] = cursor.fetchone()[0]
                conn.close()
            except:
                pass
    else:
        # Local only - get stats from SQLite
        try:
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (int(project_id),))
            stats['total_words'] = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(DISTINCT language) FROM words WHERE language IS NOT NULL AND project_id = ?", (int(project_id),))
            stats['total_languages'] = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM words WHERE video_path IS NOT NULL AND project_id = ?", (int(project_id),))
            stats['words_with_videos'] = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM words WHERE syllable_type IS NOT NULL AND project_id = ?", (int(project_id),))
            stats['structured_words'] = cursor.fetchone()[0]
            conn.close()
        except:
            pass

    # Create a current_project dict with ownership info for template compatibility
    is_owner = is_project_owner(project_id, user['id'])
    current_project = {
        'id': project_id,
        'name': project_name,
        'is_owner': is_owner
    }
    user['current_project'] = current_project

    return render_template('main_menu.html', stats=stats, user=user)


# ---------------------------------------------------------------------------
# Routes: Projects List & Group Detail
# ---------------------------------------------------------------------------

@l7_bp.route('/projects')
@require_auth
def projects_menu():
    """Projects management menu"""
    print("DEBUG: === PROJECTS ROUTE CALLED ===")
    user = get_user_info()
    print(f"DEBUG: User info: {user}")

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Get user's projects from both storage types using storage manager
    print(f"DEBUG: Fetching projects for user {user['id']}")
    projects = storage_manager.get_projects(user['id'])
    print(f"DEBUG: Retrieved {len(projects)} projects: {[p.get('name', 'no name') for p in projects]}")

    # Add word count and storage metadata for each project
    for project in projects:
        print(f"DEBUG: Processing project {project.get('name')} with storage_type: {project.get('storage_type')}, id: {project.get('id')} (type: {type(project.get('id'))})")
        # Get word count
        if project.get('storage_type') == 'cloud':
            # For cloud projects, count words in Firestore (placeholder for now)
            project['word_count'] = 0  # TODO: Implement Firestore word counting
            project['storage_icon'] = '\U0001f310'
            project['storage_label'] = 'Cloud'
            project['can_migrate'] = False
        else:
            # For local projects, count words in SQLite
            print(f"DEBUG: Counting words for local project {project.get('id')}")
            cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (project.get('id'),))
            word_count = cursor.fetchone()[0]
            project['word_count'] = word_count
            project['storage_icon'] = '\U0001f4be'
            project['storage_label'] = 'Local'
            project['can_migrate'] = clean_firebase_service.is_available()

    # Get user's groups for sharing functionality
    cursor.execute("""
        SELECT g.id, g.name
        FROM project_groups g
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

    print(f"DEBUG: About to render template with {len(projects)} projects")
    print(f"DEBUG: First 3 projects: {projects[:3]}")
    print(f"DEBUG: Projects structure check:")
    for i, project in enumerate(projects[:3]):
        print(f"  Project {i}: {project}")

    return render_template('projects_menu.html', projects=projects, user=user, user_groups=user_groups)


@l7_bp.route('/projects/group/<int:group_id>')
@require_auth
def project_group_detail(group_id):
    """
    Display a list of projects (variants) belonging to a specific group.
    These are essentially the project variants for collaborative editing.
    """
    user = get_user_info()

    # Verify group membership and get group details
    group_detail = storage_manager.get_group_detail(group_id, user['id'])

    if not group_detail or not group_detail.get('is_member'):
        flash('Group not found or access denied.', 'error')
        return redirect(url_for('l7_projects.dashboard'))

    # Get all projects shared with this group
    shared_projects = storage_manager.get_projects_shared_with_group(group_id, user['id'])

    # Determine if the user is an admin of this group
    is_group_admin = group_detail.get('is_admin', False)

    return render_template(
        'project_group_detail.html',
        group=group_detail,
        projects=shared_projects,
        user=user,
        is_group_admin=is_group_admin
    )


# ---------------------------------------------------------------------------
# Routes: Project Creation
# ---------------------------------------------------------------------------

@l7_bp.route('/projects/create', methods=['GET', 'POST'])
@require_auth
def create_project():
    """Create a new project"""
    user = get_user_info()

    # Get user's groups for sharing functionality
    conn = sqlite3.connect(main.DB_NAME)
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
        template_selection = request.form.get('template_selection', '').strip()
        print(f"DEBUG: Extracted project_name='{project_name}', storage_type='{storage_type}', template_selection='{template_selection}'")

        if not project_name:
            flash('Project name is required', 'error')
            return render_template('create_project.html', user=user, user_groups=user_groups,
                                 firebase_available=clean_firebase_service.is_available())

        # Convert storage type string to enum
        storage_enum = StorageType.CLOUD if storage_type == 'cloud' else StorageType.LOCAL

        try:
            # Use storage manager to create project with selected storage type
            project_data = {
                'name': project_name,
                'user_id': user['id']
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
                # Apply template if selected
                if template_selection:
                    try:
                        print(f"DEBUG: Applying template '{template_selection}' to project {project_id}")
                        template_applied = apply_template_to_new_project(project_id, template_selection, user['id'], storage_enum)
                        if template_applied:
                            print(f"DEBUG: Template applied successfully to project {project_id}")
                        else:
                            print(f"DEBUG: Template application failed for project {project_id}")
                            flash('Project created but template application failed. Using default phonemes.', 'warning')
                    except Exception as template_error:
                        print(f"DEBUG: Template application error: {template_error}")
                        flash('Project created but template application failed. Using default phonemes.', 'warning')

                # Automatically switch to the new project and enter it
                session['current_project_id'] = project_id

                storage_label = "cloud (Firebase)" if storage_enum == StorageType.CLOUD else "local (SQLite)"
                template_message = f" with '{template_selection.split(':', 1)[1] if ':' in template_selection else template_selection}' template" if template_selection else ""
                if 'warning' not in [msg[0] for msg in get_flashed_messages(with_categories=True)]:
                    flash(f'Project "{project_name}" created successfully using {storage_label} storage{template_message}!', 'success')

                print("DEBUG: Redirecting to main menu to enter new project")
                return redirect(url_for('l7_projects.main_menu'))
            else:
                print("DEBUG: project_id is None - showing 'Failed to create project'")
                flash('Failed to create project', 'error')

        except Exception as e:
            flash(f'Error creating project: {e}', 'error')

    return render_template('create_project.html', user=user, user_groups=user_groups,
                         firebase_available=clean_firebase_service.is_available())


# ---------------------------------------------------------------------------
# Routes: Project Migration
# ---------------------------------------------------------------------------

@l7_bp.route('/projects/<project_id>/migrate-to-cloud', methods=['POST'])
@require_auth
def migrate_project_to_cloud(project_id):
    """Migrate a local project to cloud storage"""
    user = get_user_info()
    if not user:
        return redirect(url_for('login'))

    if not clean_firebase_service.is_available():
        flash('Cloud storage is not available', 'error')
        return redirect(url_for('l7_projects.projects_menu'))

    success, message = storage_manager.migrate_project_to_cloud(project_id, user['id'])

    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')

    return redirect(url_for('l7_projects.projects_menu'))


# ---------------------------------------------------------------------------
# Routes: Project Context (Enter/Exit)
# ---------------------------------------------------------------------------

@l7_bp.route('/projects/<project_id>/enter')
@require_auth
def enter_project(project_id):
    """Enter a specific project"""
    user = get_user_info()

    # Check if project exists in either storage type
    project = None
    project_name = None

    # First check if it's a Firebase project (string ID)
    if clean_firebase_service.is_available():
        try:
            firebase_project = firestore_db.get_project(project_id)
            if firebase_project and firebase_project.get('user_id') == user['id']:
                project = firebase_project
                project_name = firebase_project.get('name')
        except Exception as e:
            print(f"Error checking Firebase project: {e}")

    # If not found in Firebase, check SQLite (integer ID)
    if not project:
        try:
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()

            # Try to convert to int for SQLite lookup
            int_project_id = int(project_id)

            cursor.execute("""
                SELECT p.name, p.user_id FROM projects p
                WHERE p.id = ? AND (
                    p.user_id = ? OR
                    p.id IN (
                        SELECT ps.project_id FROM project_shares ps
                        JOIN group_memberships gm ON ps.group_id = gm.group_id
                        WHERE gm.user_id = ?
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
        return redirect(url_for('l7_projects.main_menu'))
    else:
        flash('Project not found or access denied', 'error')
        return redirect(url_for('l7_projects.dashboard'))


@l7_bp.route('/projects/exit')
@require_auth
def exit_project():
    """Exit current project"""
    if 'current_project_id' in session:
        del session['current_project_id']
        flash('Exited project', 'success')

    return redirect(url_for('l7_projects.dashboard'))


# ---------------------------------------------------------------------------
# Routes: Project Editing
# ---------------------------------------------------------------------------

@l7_bp.route('/projects/<project_id>/edit', methods=['GET', 'POST'])
@require_auth
def edit_project(project_id):
    """Edit project name"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Verify project belongs to user OR user is in a group with project owner
    cursor.execute("""
        SELECT p.name FROM projects p
        WHERE p.id = ? AND (
            p.user_id = ? OR
            p.user_id IN (
                SELECT gm.user_id
                FROM group_memberships gm1
                JOIN group_memberships gm ON gm1.group_id = gm.group_id
                WHERE gm1.user_id = ? AND gm.user_id = p.user_id
            )
        )
    """, (project_id, user['id'], user['id']))
    project = cursor.fetchone()

    if not project:
        flash('Project not found or access denied', 'error')
        conn.close()
        return redirect(url_for('l7_projects.projects_menu'))

    if request.method == 'POST':
        new_name = request.form.get('name', '').strip()

        if not new_name:
            flash('Project name is required', 'error')
            conn.close()
            return render_template('edit_project.html', project={'id': project_id, 'name': project[0]}, user=user)

        try:
            cursor.execute("""
                UPDATE projects
                SET name = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ? AND user_id = ?
            """, (new_name, project_id, user['id']))

            # Update language field in all words for this project
            cursor.execute("""
                UPDATE words
                SET language = ?
                WHERE project_id = ?
            """, (new_name, project_id))

            # Keep the grouped/variant projects list in sync: rename the associated project group.
            variant_identifier = f"local:{project_id}"
            cursor.execute(
                "SELECT group_id FROM project_variants_meta WHERE variant_identifier = ? AND user_id = ?",
                (variant_identifier, user['id']),
            )
            row = cursor.fetchone()
            group_id = row[0] if row and row[0] else variant_identifier
            cursor.execute(
                "UPDATE project_groups SET name = ?, updated_at = CURRENT_TIMESTAMP WHERE group_id = ? AND user_id = ?",
                (new_name, group_id, user['id']),
            )

            conn.commit()
            flash(f'Project renamed to "{new_name}" successfully!', 'success')
            return redirect(url_for('l7_projects.projects_menu'))

        except sqlite3.IntegrityError:
            flash('A project with this name already exists', 'error')
        finally:
            conn.close()

    conn.close()
    return render_template('edit_project.html', project={'id': project_id, 'name': project[0]}, user=user)


# ---------------------------------------------------------------------------
# Routes: API Endpoints
# ---------------------------------------------------------------------------

@l7_bp.route('/api/projects/<project_id>/rename', methods=['POST'])
@require_auth
def api_rename_project(project_id):
    """Rename a local project (used by projects menu prompt-based UI)."""
    user = get_user_info()
    payload = request.get_json(silent=True) if request.is_json else request.form.to_dict()
    new_name = (payload or {}).get('name', '')
    new_name = new_name.strip() if isinstance(new_name, str) else str(new_name).strip()

    if not new_name:
        return jsonify({'success': False, 'message': 'Project name is required'})

    try:
        int_project_id = int(project_id)
    except (TypeError, ValueError):
        return jsonify({'success': False, 'message': 'Rename is only supported for local projects right now'})

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM projects WHERE id = ? AND user_id = ?", (int_project_id, user['id']))
        if not cursor.fetchone():
            return jsonify({'success': False, 'message': 'Project not found or access denied'})

        cursor.execute(
            "UPDATE projects SET name = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ? AND user_id = ?",
            (new_name, int_project_id, user['id']),
        )
        cursor.execute("UPDATE words SET language = ? WHERE project_id = ?", (new_name, int_project_id))

        # Keep the grouped/variant projects list in sync: rename the associated project group.
        variant_identifier = f"local:{int_project_id}"
        cursor.execute(
            "SELECT group_id FROM project_variants_meta WHERE variant_identifier = ? AND user_id = ?",
            (variant_identifier, user['id']),
        )
        row = cursor.fetchone()
        group_id = row[0] if row and row[0] else variant_identifier
        cursor.execute(
            "UPDATE project_groups SET name = ?, updated_at = CURRENT_TIMESTAMP WHERE group_id = ? AND user_id = ?",
            (new_name, group_id, user['id']),
        )
        conn.commit()
        return jsonify({'success': True, 'message': f'Project renamed to "{new_name}" successfully!'})
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': f'Error renaming project: {e}'})
    finally:
        conn.close()


@l7_bp.route('/api/projects/<project_id>/branch', methods=['POST'])
@require_auth
def api_branch_project(project_id):
    """Create a local project variant by duplicating the project's phoneme inventory."""
    user = get_user_info()
    payload = request.get_json(silent=True) if request.is_json else request.form.to_dict()
    branch_name = (payload or {}).get('name', '')
    branch_name = branch_name.strip() if isinstance(branch_name, str) else str(branch_name).strip()

    if not branch_name:
        return jsonify({'success': False, 'message': 'Branch name is required'})

    try:
        int_project_id = int(project_id)
    except (TypeError, ValueError):
        return jsonify({'success': False, 'message': 'Branching is only supported for local projects right now'})

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (int_project_id, user['id']))
        original = cursor.fetchone()
        if not original:
            return jsonify({'success': False, 'message': 'Project not found or access denied'})

        cursor.execute(
            "INSERT INTO projects (name, user_id, created_at, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
            (branch_name, user['id']),
        )
        new_project_id = cursor.lastrowid

        # Copy phoneme inventory into the new project (including extended schema fields).
        cursor.execute(
            """
            INSERT INTO phonemes (
                syllable_type, position, length_type, group_type, subgroup_type,
                phoneme, frequency, project_id, user_id, "TEXT", sub_subgroup_type, sub_sub_subgroup_type
            )
            SELECT
                syllable_type, position, length_type, group_type, subgroup_type,
                phoneme, frequency, ?, user_id, "TEXT", sub_subgroup_type, sub_sub_subgroup_type
            FROM phonemes
            WHERE project_id = ?
            """,
            (new_project_id, int_project_id),
        )

        conn.commit()
        return jsonify(
            {
                'success': True,
                'message': f'Project branched successfully as "{branch_name}"!',
                'new_project_id': new_project_id,
            }
        )
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': f'Error branching project: {e}'})
    finally:
        conn.close()


@l7_bp.route('/api/projects/shared', methods=['GET'])
@require_auth
def api_get_shared_projects():
    """Get all projects shared with the current user"""
    user_id = session.get('user_id')

    try:
        shared_projects = firestore_db.get_shared_projects(user_id)
        return jsonify({'success': True, 'projects': shared_projects})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
