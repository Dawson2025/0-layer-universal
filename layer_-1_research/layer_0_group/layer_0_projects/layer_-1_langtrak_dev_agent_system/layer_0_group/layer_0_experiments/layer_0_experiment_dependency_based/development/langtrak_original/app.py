from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_file, session, get_flashed_messages, g
import sqlite3
import os
import json
import subprocess
import shutil
import glob
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from collections import defaultdict
from datetime import datetime
import main  # Import the main terminal application
from src.tts_ipa import ipa_tts
# from firebase_service import firebase_service  # OLD - REMOVED
from services.firebase import clean_firebase_service
from src.storage_manager import storage_manager, StorageType
from services.firebase import firestore_db

# Import core helpers for module-level route decorators
from core.session import get_user_info
from core.decorators import require_auth, require_project_admin

# Configuration constants
UPLOAD_FOLDER = 'videos'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init_users_table():
    """Initialize users table and related authentication/project tables"""
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Create users table
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

    # Create projects table (may already exist from main.migrate_schema, but ensure it has all columns)
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

    # Ensure projects has cloud-related columns
    cursor.execute("PRAGMA table_info(projects)")
    project_columns = [column[1] for column in cursor.fetchall()]
    if 'cloud_project_id' not in project_columns:
        cursor.execute("ALTER TABLE projects ADD COLUMN cloud_project_id TEXT")
    if 'cloud_last_sync' not in project_columns:
        cursor.execute("ALTER TABLE projects ADD COLUMN cloud_last_sync TIMESTAMP")
    if 'migrated_to_cloud' not in project_columns:
        cursor.execute("ALTER TABLE projects ADD COLUMN migrated_to_cloud INTEGER DEFAULT 0")

    # Create groups table
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

    # Create group_memberships table
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

    # Create project_shares table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_shares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            group_id INTEGER,
            shared_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects (id),
            FOREIGN KEY (group_id) REFERENCES groups (id),
            UNIQUE(project_id, group_id)
        )
    """)

    # Ensure groups table has invite_code column
    cursor.execute("PRAGMA table_info(groups)")
    group_columns = [column[1] for column in cursor.fetchall()]
    if 'invite_code' not in group_columns:
        cursor.execute("ALTER TABLE groups ADD COLUMN invite_code TEXT")

    conn.commit()
    conn.close()

app = Flask(__name__)
app.secret_key = 'phoneme_tracker_secret_key_2024'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_firebase_config():
    """Return client-side Firebase configuration for web app authentication."""
    return {
        "apiKey": "AIzaSyCXoBKM6UQx5wCvBYQ_KvhCPmjcNyis9XE",
        "authDomain": "lang-trak-dev.firebaseapp.com",
        "projectId": "lang-trak-dev",
        "storageBucket": "lang-trak-dev.firebasestorage.app",
        "messagingSenderId": "894561101654",
        "appId": "1:894561101654:web:fc234c159fd669749d98f7"
    }

# Track if app has been fully initialized
_app_initialized = False

def create_app():
    """Create and configure the Flask application.
    
    Returns the module-level app instance with blueprints registered.
    Safe to call multiple times - initialization only happens once.
    """
    global app, _app_initialized
    
    # Return existing app if already initialized (prevents duplicate route registration)
    if _app_initialized:
        return app
    
    # Register feature blueprints
    from features.projects import projects_bp
    from features.words import words_bp
    from routes.api_routes import api_bp
    
    app.register_blueprint(projects_bp)
    app.register_blueprint(words_bp)
    app.register_blueprint(api_bp)

    # Legacy authentication helpers (kept for backwards compatibility with routes inside create_app)
    def get_user_info_legacy():
        """Get authenticated user information from session - supports both Firebase and email/password authentication"""
        user_data = None
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Check for Firebase authentication first
        if 'firebase_uid' in session:
            cursor.execute("SELECT id, username, email, firebase_uid FROM users WHERE firebase_uid = ? AND is_active = 1", (session['firebase_uid'],))
            user_data = cursor.fetchone()
        
        # Check for email/password authentication
        elif 'user_id' in session and 'auth_method' in session and session['auth_method'] == 'email_password':
            cursor.execute("SELECT id, username, email, firebase_uid FROM users WHERE id = ? AND is_active = 1", (session['user_id'],))
            user_data = cursor.fetchone()
        
        if not user_data:
            conn.close()
            return {'is_authenticated': False}
            
        current_project = None
        if 'current_project_id' in session:
            # First check if it's a Firebase project (string ID)
            if clean_firebase_service.is_available():
                try:
                    firebase_project = firestore_db.get_project(session['current_project_id'])
                    if firebase_project and firebase_project.get('user_id') == user_data[0]:
                        current_project = {
                            'id': firebase_project['id'],
                            'name': firebase_project['name'],
                            'is_owner': True  # Firebase projects are always owned by the user
                        }
                    else:
                        pass
                except Exception as e:
                    pass
            
            # If not found in Firebase, check SQLite (integer ID)
            if not current_project:
                try:
                    int_project_id = int(session['current_project_id'])
                    cursor.execute("""
                        SELECT p.id, p.name, p.user_id FROM projects p
                        WHERE p.id = ? AND (
                            p.user_id = ? OR 
                            p.id IN (
                                SELECT ps.project_id FROM project_shares ps
                                JOIN group_memberships gm ON ps.group_id = gm.group_id
                                WHERE gm.user_id = ?
                            )
                        )
                    """, (int_project_id, user_data[0], user_data[0]))
                    project_data = cursor.fetchone()
                    if project_data:
                        current_project = {
                            'id': project_data[0],
                            'name': project_data[1],
                            'is_owner': project_data[2] == user_data[0]
                        }
                except (ValueError, TypeError):
                    # project_id is not a valid integer, skip SQLite check
                    pass
                except Exception as e:
                    pass
        
        conn.close()
        
        return {
            'id': user_data[0],
            'name': user_data[1],
            'email': user_data[2],
            'firebase_uid': user_data[3],
            'roles': '',
            'is_authenticated': True,
            'current_project': current_project
        }

    def require_auth(f):
        """Decorator to require authentication for routes"""
        def decorated_function(*args, **kwargs):
            user = get_user_info()
            if not user['is_authenticated']:
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        decorated_function.__name__ = f.__name__
        return decorated_function

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
        except Exception as e:
            print(f"Error checking SQLite project ownership: {e}")
            return False

    def require_project_admin(f):
        """Decorator to require project admin access for routes"""
        def decorated_function(*args, **kwargs):
            user = get_user_info()
            if not user['is_authenticated']:
                return redirect(url_for('login'))
            
            # Check for current project in session (simplified approach like main_menu)
            if 'current_project_id' not in session:
                flash('Please enter a project to access admin tools', 'error')
                return redirect(url_for('dashboard'))
            
            # Check if user is the project owner
            project_id = session['current_project_id']
            if not is_project_owner(project_id, user['id']):
                flash('Access denied. Only project owners can access admin tools.', 'error')
                return redirect(url_for('main_menu'))
            
            return f(*args, **kwargs)
        decorated_function.__name__ = f.__name__
        return decorated_function

    # Custom Jinja filter for unique count
    @app.template_filter('unique_count')
    def unique_count_filter(items, attribute):
        """Get count of unique values for a given attribute"""
        if not items:
            return 0
        unique_values = set()
        for item in items:
            if hasattr(item, '__getitem__'):
                value = item.get(attribute)
            else:
                value = getattr(item, attribute, None)
            if value:
                unique_values.add(value)
        return len(unique_values)

    # Configuration
    UPLOAD_FOLDER = 'videos'
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    # Database initialization moved to main block to avoid import-time execution



    @app.route('/')

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

        return redirect(url_for('dashboard'))



    @app.route('/dashboard')

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

                project['storage_icon'] = '🌐'

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

                project['storage_icon'] = '💾'

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

    @app.route('/main-menu')
    @require_auth
    def main_menu():
        """Main application menu - only accessible when in a project context"""
        user = get_user_info()
        
        # Check for current project in session first (simpler approach)
        if 'current_project_id' not in session:
            flash('Please enter a project to access the main menu', 'error')
            return redirect(url_for('dashboard'))
        
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

    @app.route('/phonemes')
    def phonemes_menu():
        """Phoneme viewing options menu"""
        return render_template('phonemes_menu.html')


    @app.route('/phonemes/nested')
    @require_auth
    def display_nested():
        """Display phonemes in nested hierarchy (Terminal function: display_nested_phonemes)"""
        try:
            # Check if we're in a project context
            if 'current_project_id' not in session:
                flash('Please enter a project to view phonemes', 'error')
                return redirect(url_for('dashboard'))
            
            project_id = session['current_project_id']
            phonemes_data = []
            
            # For Firebase projects, get phonemes from Firestore
            # (Only when the project_id is a non-numeric string identifier.)
            if clean_firebase_service.is_available() and isinstance(project_id, str) and not project_id.isdigit():
                try:
                    firebase_project = firestore_db.get_project(project_id)
                    if firebase_project:
                        # Get all phonemes for this project
                        firebase_phonemes = firestore_db.get_project_phonemes(project_id)
                        
                        # Convert to tuple format expected by the rest of the function
                        phonemes_data = []
                        for phoneme_doc in firebase_phonemes:
                            phonemes_data.append((
                                phoneme_doc.get('syllable_type', ''),
                                phoneme_doc.get('position', ''),
                                phoneme_doc.get('length_type', ''),
                                phoneme_doc.get('group_type', ''),
                                phoneme_doc.get('subgroup_type', ''),
                                phoneme_doc.get('phoneme', ''),
                                phoneme_doc.get('frequency', 0)
                            ))
                        
                        # Sort phonemes
                        phonemes_data.sort(key=lambda p: (p[0], p[1], p[2], p[3], p[4], p[5]))
                        
                    else:
                        # Not a Firebase project, fallback to SQLite
                        conn = sqlite3.connect(main.DB_NAME)
                        cursor = conn.cursor()
                        
                        cursor.execute("""
                            SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                            FROM phonemes
                            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
                        """)
                        
                        phonemes_data = cursor.fetchall()
                        conn.close()
                except Exception as e:
                    print(f"Error getting Firebase phonemes: {e}")
                    # Fallback to SQLite
                    conn = sqlite3.connect(main.DB_NAME)
                    cursor = conn.cursor()
                    
                    cursor.execute("""
                        SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                        FROM phonemes
                        ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
                    """)
                    
                    phonemes_data = cursor.fetchall()
                    conn.close()
            else:
                # No Firebase available, use SQLite
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                    FROM phonemes
                    ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
                """)
                
                phonemes_data = cursor.fetchall()
                conn.close()

            # Organize data into nested structure
            nested_data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list)))))

            for syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency in phonemes_data:
                nested_data[syllable_type][position][length_type][group_type][subgroup_type].append({
                    'phoneme': phoneme,
                    'frequency': frequency
                })

            # Convert all nested defaultdicts to regular dicts
            result_data = {}
            for syl_type, syl_data in nested_data.items():
                result_data[syl_type] = {}
                for pos, pos_data in syl_data.items():
                    result_data[syl_type][pos] = {}
                    for len_type, len_data in pos_data.items():
                        result_data[syl_type][pos][len_type] = {}
                        for grp_type, grp_data in len_data.items():
                            result_data[syl_type][pos][len_type][grp_type] = dict(grp_data)

            return render_template('phonemes_nested.html', nested_data=result_data)
        except Exception as e:
            flash(f'Error displaying nested phonemes: {str(e)}', 'error')
            return redirect(url_for('phonemes_menu'))

    @app.route('/phonemes/full')
    @require_auth
    def display_full():
        """Display full phoneme hierarchy (Terminal function: display_full)"""
        try:
            # Check if we're in a project context
            if 'current_project_id' not in session:
                flash('Please enter a project to view phonemes', 'error')
                return redirect(url_for('dashboard'))
            
            project_id = session['current_project_id']
            phonemes_data = []
            
            # For Firebase projects, get phonemes from Firestore
            # (Only when the project_id is a non-numeric string identifier.)
            if clean_firebase_service.is_available() and isinstance(project_id, str) and not project_id.isdigit():
                try:
                    firebase_project = firestore_db.get_project(project_id)
                    if firebase_project:
                        # Get all phonemes for this project
                        firebase_phonemes = firestore_db.get_project_phonemes(project_id)
                        
                        # Convert to tuple format expected by the rest of the function
                        phonemes_data = []
                        for phoneme_doc in firebase_phonemes:
                            phonemes_data.append((
                                phoneme_doc.get('syllable_type', ''),
                                phoneme_doc.get('position', ''),
                                phoneme_doc.get('length_type', ''),
                                phoneme_doc.get('group_type', ''),
                                phoneme_doc.get('subgroup_type', ''),
                                phoneme_doc.get('phoneme', ''),
                                phoneme_doc.get('frequency', 0)
                            ))
                        
                        # Sort phonemes (frequency ASC for consistency)
                        phonemes_data.sort(key=lambda p: (p[0], p[1], p[2], p[6], p[3], p[4], p[5]))
                        
                    else:
                        # Not a Firebase project, fallback to SQLite
                        conn = sqlite3.connect(main.DB_NAME)
                        cursor = conn.cursor()
                        
                        cursor.execute("""
                            SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                            FROM phonemes
                            ORDER BY syllable_type, position, length_type, frequency ASC, group_type, subgroup_type, phoneme
                        """)
                        
                        phonemes_data = cursor.fetchall()
                        conn.close()
                except Exception as e:
                    print(f"Error getting Firebase phonemes: {e}")
                    # Fallback to SQLite
                    conn = sqlite3.connect(main.DB_NAME)
                    cursor = conn.cursor()
                    
                    cursor.execute("""
                        SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                        FROM phonemes
                        ORDER BY syllable_type, position, length_type, frequency ASC, group_type, subgroup_type, phoneme
                    """)
                    
                    phonemes_data = cursor.fetchall()
                    conn.close()
            else:
                # No Firebase available, use SQLite
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                    FROM phonemes
                    ORDER BY syllable_type, position, length_type, frequency ASC, group_type, subgroup_type, phoneme
                """)
                
                phonemes_data = cursor.fetchall()
                conn.close()

            # Calculate group frequencies and organize data
            full_data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'groups': defaultdict(lambda: {'subgroups': defaultdict(list), 'frequency': 0})})))

            for syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency in phonemes_data:
                # Add phoneme to subgroup
                full_data[syllable_type][position][length_type]['groups'][group_type]['subgroups'][subgroup_type].append({
                    'phoneme': phoneme,
                    'frequency': frequency
                })
                # Update group frequency
                full_data[syllable_type][position][length_type]['groups'][group_type]['frequency'] += frequency

            # Convert all nested defaultdicts to regular dicts
            result_data = {}
            for syl_type, syl_data in full_data.items():
                result_data[syl_type] = {}
                for pos, pos_data in syl_data.items():
                    result_data[syl_type][pos] = {}
                    for len_type, len_data in pos_data.items():
                        result_data[syl_type][pos][len_type] = {
                            'groups': {}
                        }
                        for grp_type, grp_data in len_data['groups'].items():
                            result_data[syl_type][pos][len_type]['groups'][grp_type] = {
                                'frequency': grp_data['frequency'],
                                'subgroups': dict(grp_data['subgroups'])
                            }

            return render_template('phonemes_full.html', full_data=result_data)
        except Exception as e:
            flash(f'Error displaying full hierarchy: {str(e)}', 'error')
            return redirect(url_for('phonemes_menu'))

    @app.route('/words')
    @require_auth
    def words_menu():
        """Words management menu"""
        user = get_user_info()
        return render_template('words_menu.html', user=user)

    @app.route('/words/display')
    @require_auth
    def display_words():
        """Display all words (Terminal function: display_words)"""
        try:
            user = get_user_info()
            
            # Check if we're in a project context (simplified session-based approach)
            if 'current_project_id' not in session:
                flash('Please enter a project to view words', 'error')
                return redirect(url_for('dashboard'))
                
            project_id = session['current_project_id']
            words_list = []
            
            # Check if it's a Firebase project first
            if clean_firebase_service.is_available():
                try:
                    firebase_project = firestore_db.get_project(project_id)
                    if firebase_project:
                        # Get words from Firestore
                        firebase_words = firestore_db.get_project_words(project_id)
                        for word in firebase_words:
                            # Parse english_words JSON safely
                            try:
                                english_words_data = word.get('english_words', [])
                                if isinstance(english_words_data, str):
                                    english_words_data = json.loads(english_words_data)
                                if isinstance(english_words_data, list):
                                    english_display = ', '.join(english_words_data)
                                else:
                                    english_display = str(english_words_data)
                            except (json.JSONDecodeError, TypeError):
                                english_display = word.get('english_words') or 'No translation'
                            
                            words_list.append({
                                'id': word.get('id', ''),
                                'language': word.get('language') or firebase_project.get('name', 'Unknown'),
                                'english_words': english_display,
                                'new_language_word': word.get('new_language_word') or 'Unnamed',
                                'ipa_phonetics': word.get('ipa_phonetics') or '',
                                'dictionary_phonetics': word.get('dictionary_phonetics') or '',
                                'video_path': word.get('video_path'),
                                'syllable_type': word.get('syllable_type') or '',
                                'onset_phoneme': word.get('onset_phoneme') or '',
                                'onset_length_type': word.get('onset_length_type') or '',
                                'nucleus_phoneme': word.get('nucleus_phoneme') or '',
                                'nucleus_length_type': word.get('nucleus_length_type') or '',
                                'coda_phoneme': word.get('coda_phoneme') or '',
                                'coda_length_type': word.get('coda_length_type') or ''
                            })
                        
                        return render_template('words_display.html', words=words_list)
                except Exception as e:
                    print(f"Error getting Firebase words: {e}")
            
            # Fallback to SQLite for local projects
            try:
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()
                
                int_project_id = int(project_id)
                cursor.execute("""
                    SELECT id, language, english_words, new_language_word, ipa_phonetics, 
                           dictionary_phonetics, video_path, syllable_type, onset_phoneme, 
                           onset_length_type, nucleus_phoneme, nucleus_length_type,
                           coda_phoneme, coda_length_type
                    FROM words
                    WHERE project_id = ?
                    ORDER BY id DESC
                """, (int_project_id,))
                
                words_data = cursor.fetchall()
                conn.close()
            except (ValueError, TypeError):
                # Not a valid integer project_id, so no local words
                words_data = []
            
            # Convert SQLite results (if any) to list of dictionaries
            for word in words_data:
                # Parse english_words JSON safely
                try:
                    english_words_data = json.loads(word[2]) if word[2] else []
                    if isinstance(english_words_data, list):
                        english_display = ', '.join(english_words_data)
                    else:
                        english_display = str(english_words_data)
                except (json.JSONDecodeError, TypeError):
                    english_display = word[2] or 'No translation'

                words_list.append({
                    'id': word[0],
                    'language': word[1] or 'Constructed Language',
                    'english_words': english_display,
                    'new_language_word': word[3] or 'Unnamed',
                    'ipa_phonetics': word[4] or '',
                    'dictionary_phonetics': word[5] or '',
                    'video_path': word[6],
                    'syllable_type': word[7] or '',
                    'onset_phoneme': word[8] or '',
                    'onset_length_type': word[9] or '',
                    'nucleus_phoneme': word[10] or '',
                    'nucleus_length_type': word[11] or '',
                    'coda_phoneme': word[12] or '',
                    'coda_length_type': word[13] or ''
                })
            
            return render_template('words_display.html', words=words_list)
        except Exception as e:
            flash(f'Error displaying words: {str(e)}', 'error')
            return redirect(url_for('words_menu'))

    @app.route('/words/create')
    @require_auth
    def create_word_menu():
        """Word creation method selection"""
        return render_template('word_creation_menu.html')

    @app.route('/words/add')
    @require_auth
    def add_word():
        """Simple (non-table) word creation UI."""
        user = get_user_info()
        return render_template('add_word.html', user=user)

    @app.route('/words/create/table-based')
    @require_auth
    def create_word_table_based():
        """Table-based word creation (Terminal function: create_word_table_based)"""
        user = get_user_info()
        return render_template('word_creation_table.html', user=user)
    
    # Mark app as initialized and return
    # Note: _app_initialized is already declared global at function start
    _app_initialized = True
    return app

# ============================================================================
# ORPHAN CODE BLOCK - Commented out due to missing function definition
# This code was left behind after some refactoring. The api_update_word
# functionality is provided by features/words/api_operations.py
# ============================================================================
'''
        video_path = current_video_path  # Keep current video by default
        firebase_video_url = None
        if 'video' in request.files:
            video_file = request.files['video']
            if video_file and video_file.filename and allowed_file(video_file.filename):
                # Create safe filename
                safe_word = "".join(c for c in data.get('new_language_word', 'word') if c.isalnum() or c in (' ', '-', '_')).strip()
                if not safe_word:
                    safe_word = "word"
                filename = secure_filename(f"{safe_word}_{video_file.filename}")
                
                # Check if we're in a Firebase project and upload to Firebase Storage
                project_id = session.get('current_project_id')
                if project_id and clean_firebase_service.is_available():
                    try:
                        firebase_project = firestore_db.get_project(project_id)
                        if firebase_project:
                            # Remove old Firebase video if it exists and is a Firebase URL
                            if current_video_path and current_video_path.startswith('https://storage.googleapis.com'):
                                # Extract storage path from Firebase URL
                                try:
                                    # Firebase URLs have format: https://storage.googleapis.com/lang-trak-dev.firebasestorage.app/videos/...
                                    url_parts = current_video_path.split('/')
                                    if 'videos' in url_parts:
                                        videos_index = url_parts.index('videos')
                                        storage_path = '/'.join(url_parts[videos_index:])
                                        clean_firebase_service.delete_file(storage_path)
                                        print(f"DEBUG: Deleted old Firebase video: {storage_path}")
                                except Exception as e:
                                    print(f"DEBUG: Could not delete old Firebase video: {e}")
                            elif current_video_path and os.path.exists(current_video_path):
                                # Remove old local video file
                                try:
                                    os.remove(current_video_path)
                                    print(f"DEBUG: Deleted old local video: {current_video_path}")
                                except OSError as e:
                                    print(f"Error removing old video file {current_video_path}: {e}")
                            
                            # Upload to Firebase Storage
                            user_id = user['id'] if user['is_authenticated'] else 'anonymous'
                            storage_path = f"videos/{user_id}/{project_id}/{filename}"
                            
                            # Get file extension for content type
                            file_extension = filename.rsplit('.', 1)[1].lower()
                            content_type_map = {
                                'mp4': 'video/mp4',
                                'avi': 'video/x-msvideo',
                                'mov': 'video/quicktime',
                                'mkv': 'video/x-matroska',
                                'webm': 'video/webm'
                            }
                            content_type = content_type_map.get(file_extension, 'video/mp4')
                            
                            # Upload file to Firebase Storage
                            result = clean_firebase_service.upload_file_from_memory(
                                video_file.read(),
                                storage_path,
                                content_type=content_type
                            )
                            
                            if result and result.get('success'):
                                firebase_video_url = result.get('public_url')
                                video_path = firebase_video_url  # Store Firebase URL as video_path
                                print(f"DEBUG: Video updated in Firebase Storage: {firebase_video_url}")
                            else:
                                print(f"DEBUG: Failed to upload video to Firebase Storage")
                                # Fallback to local storage
                                video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
                                video_file.seek(0)  # Reset file pointer
                                try:
                                    video_file.save(video_path)
                                except IOError as e:
                                    print(f"Error saving new video file {video_path}: {e}")
                                    return jsonify({'success': False, 'error': f'Failed to save video file: {e}'})
                        else:
                            # Not a Firebase project, use local storage
                            # Remove old video file if it exists
                            if current_video_path and os.path.exists(current_video_path):
                                try:
                                    os.remove(current_video_path)
                                except OSError as e:
                                    print(f"Error removing old video file {current_video_path}: {e}")
                            
                            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
                            try:
                                video_file.save(video_path)
                            except IOError as e:
                                print(f"Error saving new video file {video_path}: {e}")
                                return jsonify({'success': False, 'error': f'Failed to save video file: {e}'})
                    except Exception as e:
                        print(f"Error uploading to Firebase Storage during edit: {e}")
                        # Fallback to local storage
                        # Remove old video file if it exists
                        if current_video_path and os.path.exists(current_video_path):
                            try:
                                os.remove(current_video_path)
                            except OSError as e:
                                print(f"Error removing old video file {current_video_path}: {e}")
                        
                        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
                        video_file.seek(0)  # Reset file pointer
                        try:
                            video_file.save(video_path)
                        except IOError as e:
                            print(f"Error saving new video file {video_path}: {e}")
                            return jsonify({'success': False, 'error': f'Failed to save video file: {e}'})
                else:
                    # Local project or Firebase not available, use local storage
                    # Remove old video file if it exists
                    if current_video_path and os.path.exists(current_video_path):
                        try:
                            os.remove(current_video_path)
                        except OSError as e:
                            print(f"Error removing old video file {current_video_path}: {e}")
                    
                    video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
                    try:
                        video_file.save(video_path)
                    except IOError as e:
                        print(f"Error saving new video file {video_path}: {e}")
                        return jsonify({'success': False, 'error': f'Failed to save video file: {e}'})

        # Sync dictionary phonetics with IPA
        ipa_phonetics = data.get('ipa_phonetics', '')
        dictionary_phonetics = ipa_phonetics  # Always match IPA

        # Get project_id from data, or use current if not provided
        project_id = data.get('project_id', current_project_id)

        # Update word data
        cursor.execute("""
            UPDATE words SET
                language = ?, english_words = ?, new_language_word = ?,
                ipa_phonetics = ?, dictionary_phonetics = ?, syllable_type = ?,
                onset_phoneme = ?, onset_length_type = ?,
                nucleus_phoneme = ?, nucleus_length_type = ?,
                coda_phoneme = ?, coda_length_type = ?, video_path = ?,
                project_id = ?
            WHERE id = ?
        """, (
            data.get('language', ''),
            data.get('english_words', ''),
            data.get('new_language_word', ''),
            ipa_phonetics,
            dictionary_phonetics,
            data.get('syllable_type', ''),
            data.get('onset_phoneme', ''),
            data.get('onset_length_type', ''),
            data.get('nucleus_phoneme', ''),
            data.get('nucleus_length_type', ''),
            data.get('coda_phoneme', ''),
            data.get('coda_length_type', ''),
            video_path,
            project_id, # Update project_id
            word_id
        ))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Word updated successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
'''
# END OF ORPHAN CODE BLOCK
# ============================================================================

# MODULE-LEVEL ROUTES (legacy - reference the module-level 'app' defined at top of file)

@app.route('/api/remove-video/<int:word_id>', methods=['POST'])
@require_auth
def api_remove_video(word_id):
    """API endpoint to remove video from a word"""
    try:
        user = get_user_info()
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Get current video path and verify ownership
        cursor.execute("SELECT video_path FROM words WHERE id = ? AND user_id = ?", (word_id, user['id']))
        word_data = cursor.fetchone()

        if not word_data:
            return jsonify({'success': False, 'error': 'Word not found'})

        video_path = word_data[0]

        # Remove video file if it exists
        if video_path:
            # Check if it's a Firebase URL
            if video_path.startswith('https://storage.googleapis.com'):
                # Extract storage path from Firebase URL
                try:
                    url_parts = video_path.split('/')
                    if 'videos' in url_parts:
                        videos_index = url_parts.index('videos')
                        storage_path = '/'.join(url_parts[videos_index:])
                        clean_firebase_service.delete_file(storage_path)
                        print(f"DEBUG: Deleted Firebase video: {storage_path}")
                except Exception as e:
                    print(f"Error removing Firebase video file {video_path}: {e}")
            elif os.path.exists(video_path):
                # Local file
                try:
                    os.remove(video_path)
                    print(f"DEBUG: Deleted local video: {video_path}")
                except OSError as e:
                    print(f"Error removing local video file {video_path}: {e}")

        # Update database to remove video path
        cursor.execute("UPDATE words SET video_path = NULL WHERE id = ?", (word_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Video removed successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/delete-word/<int:word_id>', methods=['DELETE'])
@require_auth
def api_delete_word(word_id):
    """API endpoint to delete a word (SQLite/integer IDs)"""
    try:
        user = get_user_info()
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Get word data before deletion for frequency updates and video cleanup
        cursor.execute("""
            SELECT syllable_type, onset_phoneme, onset_length_type,
                   nucleus_phoneme, nucleus_length_type,
                   coda_phoneme, coda_length_type, video_path
            FROM words WHERE id = ? AND user_id = ?
        """, (word_id, user['id']))

        word_data = cursor.fetchone()
        if not word_data:
            return jsonify({'success': False, 'error': 'Word not found'})

        # Delete the word
        cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))

        # Update phoneme frequencies (decrease)
        syllable_type = word_data[0]
        positions = [
            ('onset', word_data[1], word_data[2]),
            ('nucleus', word_data[3], word_data[4]),
            ('coda', word_data[5], word_data[6])
        ]

        for position, phoneme, length_type in positions:
            if phoneme:
                cursor.execute("""
                    UPDATE phonemes SET frequency = frequency - 1
                    WHERE syllable_type = ? AND position = ? AND length_type = ? AND phoneme = ?
                    AND frequency > 0
                """, (syllable_type, position, length_type, phoneme))

        # Delete video file if exists
        video_path = word_data[7]
        if video_path:
            # Check if it's a Firebase URL
            if video_path.startswith('https://storage.googleapis.com'):
                # Extract storage path from Firebase URL
                try:
                    url_parts = video_path.split('/')
                    if 'videos' in url_parts:
                        videos_index = url_parts.index('videos')
                        storage_path = '/'.join(url_parts[videos_index:])
                        clean_firebase_service.delete_file(storage_path)
                        print(f"DEBUG: Deleted Firebase video during word deletion: {storage_path}")
                except Exception as e:
                    print(f"Error removing Firebase video file {video_path} during word deletion: {e}")
            elif os.path.exists(video_path):
                # Local file
                try:
                    os.remove(video_path)
                    print(f"DEBUG: Deleted local video during word deletion: {video_path}")
                except OSError as e:
                    print(f"Error removing local video file {video_path} during word deletion: {e}")

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Word deleted successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/delete-word/<word_id>', methods=['DELETE'])
@require_auth
def api_delete_word_flexible(word_id):
    """API endpoint to delete a word that handles both integer and string IDs"""
    try:
        user = get_user_info()
        
        # Check if it's a Firebase project first
        if 'current_project_id' in session:
            project_id = session['current_project_id']
            
            # Try Firebase first
            if clean_firebase_service.is_available():
                try:
                    firebase_project = firestore_db.get_project(project_id)
                    if firebase_project:
                        # Get word from Firestore first to check video path
                        word_doc = firestore_db.get_word_by_id(project_id, word_id)
                        if word_doc:
                            # Delete video if exists
                            video_path = word_doc.get('video_path')
                            if video_path and video_path.startswith('https://storage.googleapis.com'):
                                try:
                                    url_parts = video_path.split('/')
                                    if 'videos' in url_parts:
                                        videos_index = url_parts.index('videos')
                                        storage_path = '/'.join(url_parts[videos_index:])
                                        clean_firebase_service.delete_file(storage_path)
                                        print(f"DEBUG: Deleted Firebase video during word deletion: {storage_path}")
                                except Exception as e:
                                    print(f"Error removing Firebase video file {video_path}: {e}")
                            
                            # Delete word from Firestore
                            success = firestore_db.delete_word(word_id)
                            if success:
                                return jsonify({'success': True, 'message': 'Word deleted successfully!'})
                            else:
                                return jsonify({'success': False, 'error': 'Failed to delete word from Firebase'})
                        else:
                            return jsonify({'success': False, 'error': 'Word not found in Firebase'})
                except Exception as e:
                    print(f"Error deleting Firebase word: {e}")
        
        # Fallback to SQLite for integer IDs
        try:
            int_word_id = int(word_id)
            return api_delete_word(int_word_id)
        except ValueError:
            return jsonify({'success': False, 'error': 'Invalid word ID format'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/admin')
@require_project_admin
def admin_menu():
    """Admin panel menu (Terminal function: admin_menu)"""
    user = get_user_info()
    return render_template('admin_menu.html', user=user)

@app.route('/admin/phonemes')
@require_project_admin
def admin_phonemes():
    """Admin phoneme management"""
    return render_template('admin_phonemes.html')

@app.route('/api/admin/phonemes')
@require_project_admin
def api_admin_phonemes():
    """API endpoint to get all phonemes for admin management"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, syllable_type, position, length_type, group_type, 
                   subgroup_type, phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
        """)

        phonemes = cursor.fetchall()
        conn.close()

        phonemes_list = []
        for phoneme in phonemes:
            phonemes_list.append({
                'id': phoneme[0],
                'syllable_type': phoneme[1],
                'position': phoneme[2],
                'length_type': phoneme[3],
                'group_type': phoneme[4],
                'subgroup_type': phoneme[5],
                'phoneme': phoneme[6],
                'frequency': phoneme[7]
            })

        return jsonify({'success': True, 'phonemes': phonemes_list})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/add-phoneme', methods=['POST'])
@require_project_admin
def api_admin_add_phoneme():
    """API endpoint to add a new phoneme (Terminal function: add_new_phoneme)"""
    try:
        data = request.get_json()

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO phonemes (syllable_type, position, length_type, group_type, 
                                subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get('syllable_type'),
            data.get('position'),
            data.get('length_type'),
            data.get('group_type'),
            data.get('subgroup_type'),
            data.get('phoneme'),
            data.get('frequency', 0)
        ))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Phoneme added successfully!'})

    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'error': 'Phoneme already exists'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/update-phoneme-frequency', methods=['POST'])
@require_project_admin
def api_admin_update_phoneme_frequency():
    """API endpoint to update phoneme frequency (Terminal functions: increase/decrease_frequency)"""
    try:
        data = request.get_json()
        phoneme_id = data.get('id')
        increment = data.get('increment', 1)

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE phonemes SET frequency = frequency + ?
            WHERE id = ? AND (frequency + ?) >= 0
        """, (increment, phoneme_id, increment))

        if cursor.rowcount == 0:
            return jsonify({'success': False, 'error': 'Cannot reduce frequency below 0 or phoneme not found'})

        conn.commit()
        conn.close()

        action = "increased" if increment > 0 else "decreased"
        return jsonify({'success': True, 'message': f'Phoneme frequency {action} successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/recalculate-phoneme-frequencies', methods=['POST'])
@require_project_admin
def api_admin_recalculate_phoneme_frequencies():
    """API endpoint to recalculate all phoneme frequencies based on actual word usage"""
    try:
        project_id = session.get('current_project_id')
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First, reset all phoneme frequencies to 0
        cursor.execute("UPDATE phonemes SET frequency = 0")
        
        # Get all words (filtered by project if applicable)
        if project_id:
            cursor.execute("""
                SELECT onset_phoneme, onset_length_type, nucleus_phoneme, nucleus_length_type, 
                       coda_phoneme, coda_length_type, syllable_type, syllables_data
                FROM words 
                WHERE project_id = ?
            """, (project_id,))
        else:
            cursor.execute("""
                SELECT onset_phoneme, onset_length_type, nucleus_phoneme, nucleus_length_type, 
                       coda_phoneme, coda_length_type, syllable_type, syllables_data
                FROM words
            """)
        
        words = cursor.fetchall()
        total_updates = 0
        
        # Count phoneme usage from words
        for word_data in words:
            # Safely unpack word data
            if len(word_data) >= 8:
                onset, onset_len, nucleus, nucleus_len, coda, coda_len, syl_type, syllables_data = word_data
            else:
                onset, onset_len, nucleus, nucleus_len, coda, coda_len, syl_type = word_data
                syllables_data = None
            
            # Handle multi-syllable words
            if syllables_data:
                try:
                    import json
                    syllables_data = json.loads(syllables_data)
                    for syllable in syllables_data:
                        syl_type_current = syllable.get('syllableType', 'CVC')
                        phonemes = syllable.get('phonemes', {})
                        
                        for position in ['onset', 'nucleus', 'coda']:
                            if position in phonemes:
                                phoneme_info = phonemes[position]
                                phoneme = phoneme_info.get('phoneme')
                                length_type = phoneme_info.get('length_type', '')
                                
                                if phoneme:
                                    cursor.execute("""
                                        UPDATE phonemes 
                                        SET frequency = frequency + 1 
                                        WHERE syllable_type = ? AND position = ? AND length_type = ? AND phoneme = ?
                                    """, (syl_type_current, position, length_type, phoneme))
                                    total_updates += cursor.rowcount
                except:
                    pass  # If syllables_data parsing fails, fall back to single syllable
            
            # Handle single-syllable words (backward compatibility)
            if not syllables_data:
                if onset:
                    cursor.execute("""
                        UPDATE phonemes 
                        SET frequency = frequency + 1 
                        WHERE syllable_type = ? AND position = 'onset' AND length_type = ? AND phoneme = ?
                    """, (syl_type, onset_len, onset))
                    total_updates += cursor.rowcount
                
                if nucleus:
                    cursor.execute("""
                        UPDATE phonemes 
                        SET frequency = frequency + 1 
                        WHERE syllable_type = ? AND position = 'nucleus' AND length_type = ? AND phoneme = ?
                    """, (syl_type, nucleus_len, nucleus))
                    total_updates += cursor.rowcount
                
                if coda:
                    cursor.execute("""
                        UPDATE phonemes 
                        SET frequency = frequency + 1 
                        WHERE syllable_type = ? AND position = 'coda' AND length_type = ? AND phoneme = ?
                    """, (syl_type, coda_len, coda))
                    total_updates += cursor.rowcount
        
        conn.commit()
        conn.close()
        
        message = f'Phoneme frequencies recalculated successfully. Processed {len(words)} words with {total_updates} frequency updates.'
        return jsonify({'success': True, 'message': message, 'words_processed': len(words), 'updates': total_updates})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/phoneme-usage/<int:phoneme_id>')
@require_project_admin
def api_admin_phoneme_usage(phoneme_id):
    """API endpoint to get words that use a specific phoneme"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First, get phoneme details
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, 
                   subgroup_type, phoneme, frequency 
            FROM phonemes WHERE id = ?
        """, (phoneme_id,))

        phoneme_data = cursor.fetchone()
        if not phoneme_data:
            conn.close()
            return jsonify({'success': False, 'error': 'Phoneme not found'})

        syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency = phoneme_data

        # Find words using this phoneme
        cursor.execute("""
            SELECT id, language, english_words, new_language_word, ipa_phonetics, 
                   dictionary_phonetics, syllable_type, onset_phoneme, onset_length_type,
                   nucleus_phoneme, nucleus_length_type, coda_phoneme, coda_length_type,
                   video_path, project_id
            FROM words 
            WHERE (onset_phoneme = ? AND onset_length_type = ?) 
               OR (nucleus_phoneme = ? AND nucleus_length_type = ?) 
               OR (coda_phoneme = ? AND coda_length_type = ?)
            ORDER BY id DESC
        """, (phoneme, length_type, phoneme, length_type, phoneme, length_type))

        words_data = cursor.fetchall()

        # Get available replacement phonemes for this position
        cursor.execute("""
            SELECT phoneme, group_type, subgroup_type, length_type
            FROM phonemes
            WHERE syllable_type = ? AND position = ? AND id != ?
            ORDER BY length_type, group_type, subgroup_type, phoneme
        """, (syllable_type, position, phoneme_id))

        replacement_options = []
        for replacement_data in cursor.fetchall():
            replacement_options.append({
                'phoneme': replacement_data[0],
                'group_type': replacement_data[1],
                'subgroup_type': replacement_data[2],
                'length_type': replacement_data[3]
            })

        conn.close()

        # Convert to list of dictionaries with position information
        words_list = []
        for word in words_data:
            # Determine which position(s) use this phoneme
            positions_used = []
            if word[7] == phoneme and word[8] == length_type:  # onset
                positions_used.append('onset')
            if word[9] == phoneme and word[10] == length_type:  # nucleus
                positions_used.append('nucleus')
            if word[11] == phoneme and word[12] == length_type:  # coda
                positions_used.append('coda')

            # Parse english_words JSON safely
            try:
                english_words_data = json.loads(word[2]) if word[2] else []
                if isinstance(english_words_data, list):
                    english_display = ', '.join(english_words_data)
                else:
                    english_display = str(word[2])
            except (json.JSONDecodeError, TypeError):
                english_display = word[2] or 'No translation'

            words_list.append({
                'id': word[0],
                'language': word[1] or 'Constructed Language',
                'english_words': english_display,
                'new_language_word': word[3] or 'Unnamed',
                'ipa_phonetics': word[4] or '',
                'dictionary_phonetics': word[5] or '',
                'syllable_type': word[6] or '',
                'video_path': word[13],
                'project_id': word[14],
                'positions_used': positions_used
            })

        return jsonify({
            'success': True,
            'phoneme': {
                'id': phoneme_id,
                'syllable_type': syllable_type,
                'position': position,
                'length_type': length_type,
                'group_type': group_type,
                'subgroup_type': subgroup_type,
                'phoneme': phoneme,
                'frequency': frequency
            },
            'words': words_list,
            'replacement_options': replacement_options,
            'count': len(words_list)
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/delete-phoneme/<int:phoneme_id>', methods=['DELETE'])
@require_project_admin
def api_admin_delete_phoneme(phoneme_id):
    """API endpoint to delete a phoneme with conflict resolution similar to template application"""
    try:
        data = request.get_json() or {}
        force_delete = data.get('force_delete', False)
        phoneme_handling = data.get('phoneme_handling', {}) # Stores handling strategy for each conflicting phoneme

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First, get phoneme details before deletion
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, 
                   subgroup_type, phoneme, frequency 
            FROM phonemes WHERE id = ?
        """, (phoneme_id,))

        phoneme_data = cursor.fetchone()
        if not phoneme_data:
            conn.close()
            return jsonify({'success': False, 'error': 'Phoneme not found'})

        syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency = phoneme_data

        # Check if phoneme is used in any words and get detailed information
        if position == 'onset':
            cursor.execute("""
                SELECT id, english_words, new_language_word, ipa_phonetics 
                FROM words WHERE onset_phoneme = ? AND onset_length_type = ?
            """, (phoneme, length_type))
        elif position == 'nucleus':
            cursor.execute("""
                SELECT id, english_words, new_language_word, ipa_phonetics 
                FROM words WHERE nucleus_phoneme = ? AND nucleus_length_type = ?
            """, (phoneme, length_type))
        elif position == 'coda':
            cursor.execute("""
                SELECT id, english_words, new_language_word, ipa_phonetics 
                FROM words WHERE coda_phoneme = ? AND coda_length_type = ?
            """, (phoneme, length_type))

        words_using_phoneme = cursor.fetchall()

        # If phoneme is in use and not forced, return conflict info
        if words_using_phoneme and not force_delete:
            # Get available replacement phonemes for the same position (any length type) from other phonemes
            cursor.execute("""
                SELECT phoneme, group_type, subgroup_type, length_type
                FROM phonemes
                WHERE syllable_type = ? AND position = ? AND id != ?
                ORDER BY length_type, group_type, subgroup_type, phoneme
            """, (syllable_type, position, phoneme_id))

            replacement_options = []
            for replacement_data in cursor.fetchall():
                replacement_options.append({
                    'phoneme': replacement_data[0] or '',
                    'group_type': replacement_data[1] or 'Other',
                    'subgroup_type': replacement_data[2] or 'none',
                    'length_type': replacement_data[3] or 'unknown'
                })

            # Format word details
            phoneme_word_details = []
            for word_data in words_using_phoneme:
                try:
                    english_words_data = json.loads(word_data[1]) if word_data[1] else []
                    if isinstance(english_words_data, list):
                        english_display = ', '.join(english_words_data)
                    else:
                        english_display = str(word_data[1])
                except (json.JSONDecodeError, TypeError):
                    english_display = word_data[1] or 'No translation'

                phoneme_word_details.append({
                    'id': word_data[0],
                    'english_words': english_display,
                    'new_language_word': word_data[2] or 'Unnamed',
                    'ipa_phonetics': word_data[3] or ''
                })

            conn.close()
            return jsonify({
                'success': False,
                'error': 'phoneme_in_use',
                'phoneme_info': {
                    'id': phoneme_id,
                    'phoneme': phoneme,
                    'syllable_type': syllable_type,
                    'position': position,
                    'length_type': length_type,
                    'group_type': group_type,
                    'subgroup_type': subgroup_type,
                    'frequency': frequency
                },
                'words_using_phoneme': phoneme_word_details,
                'replacement_options': replacement_options, # Pass replacement options
                'words_count': len(words_using_phoneme),
                'message': f'Phoneme "{phoneme}" is used in {len(words_using_phoneme)} word(s). Choose how to handle the conflicts.'
            })

        # Handle phoneme conflicts if force_delete is True or no words use it
        words_updated = 0
        words_with_orphaned_phonemes = 0

        if phoneme_handling and force_delete:
            # Handle phoneme conflicts based on user choices
            pass

        # Delete the phoneme from the phonemes table
        cursor.execute("DELETE FROM phonemes WHERE id = ?", (phoneme_id,))

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'success': False, 'error': 'Phoneme not found'})

        conn.commit()
        conn.close()

        # Prepare success message
        success_msg = f'Phoneme "{phoneme}" deleted successfully!'
        if words_updated:
            success_msg += f' Updated {words_updated} words.'
        if words_with_orphaned_phonemes:
            success_msg += f' {words_with_orphaned_phonemes} words kept their original phoneme (orphaned).'

        return jsonify({
            'success': True, 
            'message': success_msg,
            'statistics': {
                'words_updated': words_updated,
                'words_with_orphaned_phonemes': words_with_orphaned_phonemes
            }
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/bulk-delete-words', methods=['POST'])
@require_project_admin
def api_admin_bulk_delete_words():
    """API endpoint to delete multiple words at once"""
    try:
        data = request.get_json()
        word_ids = data.get('word_ids', [])

        if not word_ids:
            return jsonify({'success': False, 'error': 'No word IDs provided'})

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        deleted_count = 0
        video_files_to_delete = []

        for word_id in word_ids:
            # Get word data before deletion for frequency updates and video cleanup
            cursor.execute("""
                SELECT syllable_type, onset_phoneme, onset_length_type,
                       nucleus_phoneme, nucleus_length_type,
                       coda_phoneme, coda_length_type, video_path
                FROM words WHERE id = ?
            """, (word_id,))

            word_data = cursor.fetchone()
            if word_data:
                # Delete the word
                cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))
                if cursor.rowcount > 0:
                    deleted_count += 1

                    # Update phoneme frequencies (decrease)
                    syllable_type = word_data[0]
                    positions = [
                        ('onset', word_data[1], word_data[2]),
                        ('nucleus', word_data[3], word_data[4]),
                        ('coda', word_data[5], word_data[6])
                    ]

                    for position, phoneme, length_type in positions:
                        if phoneme:
                            cursor.execute("""
                                UPDATE phonemes SET frequency = frequency - 1
                                WHERE syllable_type = ? AND position = ? AND length_type = ? AND phoneme = ?
                                AND frequency > 0
                            """, (syllable_type, position, length_type, phoneme))

                    # Track video file for deletion
                    if word_data[7]:
                        video_files_to_delete.append(word_data[7])

        # Delete video files
        for video_path in video_files_to_delete:
            if os.path.exists(video_path):
                try:
                    os.remove(video_path)
                except OSError as e:
                    print(f"Error removing video file {video_path} during bulk deletion: {e}")

        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': f'Successfully deleted {deleted_count} words!',
            'deleted_count': deleted_count
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/delete-unused-phonemes', methods=['POST'])
@require_project_admin
def api_admin_delete_unused_phonemes():
    """API endpoint to delete all phonemes with frequency 0"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First count how many will be deleted
        cursor.execute("SELECT COUNT(*) FROM phonemes WHERE frequency = 0")
        count_to_delete = cursor.fetchone()[0]

        # Delete unused phonemes
        cursor.execute("DELETE FROM phonemes WHERE frequency = 0")

        conn.commit()
        conn.close()

        return jsonify({
            'success': True, 
            'message': f'Successfully deleted {count_to_delete} unused phonemes!',
            'deleted_count': count_to_delete
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/reset-database', methods=['POST'])
@require_project_admin
def api_admin_reset_database():
    """API endpoint to reset database (Terminal function: reset_database)"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Create templates table if it doesn't exist
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

        # Backup templates before reset
        cursor.execute("SELECT name, description, template_data, phoneme_count, created_at FROM phoneme_templates")
        templates_backup = cursor.fetchall()

        # Clear words and phonemes only (preserve templates)
        cursor.execute("DELETE FROM words")
        cursor.execute("DELETE FROM phonemes")

        # Reset auto-increment counters
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='words'")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='phonemes'")

        conn.commit()
        conn.close()

        # Reset the phonemes to default configuration (use separate connection)
        main.insert_sample_data()

        template_msg = f" Preserved {len(templates_backup)} phoneme templates." if templates_backup else ""
        return jsonify({'success': True, 'message': f'Database reset successfully! All words deleted and phonemes reset to default.{template_msg}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/admin/templates')
@require_project_admin
def admin_templates():
    """Admin templates management page"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Create templates table if it doesn't exist
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

        # Get all saved templates (if any exist)
        cursor.execute("""
            SELECT id, name, description, phoneme_count, created_at
            FROM phoneme_templates
            ORDER BY created_at DESC
        """)
        templates = cursor.fetchall()

        # Get current phonemes for template creation
        cursor.execute("SELECT phoneme, frequency FROM phonemes ORDER BY phoneme") # Fetch phoneme symbol
        current_phonemes = cursor.fetchall()

        conn.close()

        return render_template('admin_templates.html', templates=templates, current_phonemes=current_phonemes)
    except Exception as e:
        print(f"Error loading templates: {e}")
        return render_template('admin_templates.html', templates=[], current_phonemes=[])

@app.route('/api/templates', methods=['POST'])
def api_create_template():
    """Create a new phoneme template"""
    try:
        data = request.get_json()
        template_name = data.get('name', '').strip()
        description = data.get('description', '').strip()

        if not template_name:
            return jsonify({'success': False, 'error': 'Template name is required'})

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Get current phonemes with full hierarchy
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, subgroup_type, 
                   sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency 
            FROM phonemes ORDER BY phoneme
        """)
        phonemes = cursor.fetchall()

        if not phonemes:
            conn.close()
            return jsonify({'success': False, 'error': 'No phonemes available to create template'})

        # Create template data (JSON format) with full hierarchy
        template_data = {
            'phonemes': []
        }
        
        for phoneme in phonemes:
            template_data['phonemes'].append({
                'syllable_type': phoneme[0],
                'position': phoneme[1],
                'length_type': phoneme[2],
                'group_type': phoneme[3],
                'subgroup_type': phoneme[4],
                'sub_subgroup_type': phoneme[5],
                'sub_sub_subgroup_type': phoneme[6],
                'phoneme': phoneme[7],
                'frequency': 0  # Reset frequencies to 0 for new template
            })

        # Insert template
        cursor.execute("""
            INSERT INTO phoneme_templates (name, description, template_data, phoneme_count)
            VALUES (?, ?, ?, ?)
        """, (template_name, description, json.dumps(template_data), len(phonemes)))

        template_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': f'Template "{template_name}" created successfully', 'template_id': template_id})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/templates/<int:template_id>', methods=['DELETE'])
def api_delete_template(template_id):
    """Delete a phoneme template"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM phoneme_templates WHERE id = ?", (template_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template deleted successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/templates/<int:template_id>/apply', methods=['POST'])
def api_apply_template(template_id):
    """Apply a template to current phonemes"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Get template data
        cursor.execute("SELECT template_data FROM phoneme_templates WHERE id = ?", (template_id,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            return jsonify({'success': False, 'error': 'Template not found'})

        template_data = json.loads(result[0])
        template_phonemes = template_data.get('phonemes', {})

        # Apply template phonemes to current database
        # Handle both old format (dict with phoneme as key) and new format (list of phoneme objects)
        if isinstance(template_phonemes, dict):
            # Old format - just update frequencies
            for symbol, data in template_phonemes.items():
                frequency = data.get('frequency', 0)
                cursor.execute("""
                    UPDATE phonemes SET frequency = ? WHERE phoneme = ?
                """, (frequency, symbol))
        else:
            # New format - full phoneme data
            for phoneme_data in template_phonemes:
                frequency = phoneme_data.get('frequency', 0)
                cursor.execute("""
                    INSERT OR REPLACE INTO phonemes (syllable_type, position, length_type, group_type, 
                                                  subgroup_type, phoneme, frequency, sub_subgroup_type, 
                                                  sub_sub_subgroup_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    phoneme_data.get('syllable_type'),
                    phoneme_data.get('position'),
                    phoneme_data.get('length_type'),
                    phoneme_data.get('group_type'),
                    phoneme_data.get('subgroup_type'),
                    phoneme_data.get('phoneme'),
                    frequency,
                    phoneme_data.get('sub_subgroup_type'),
                    phoneme_data.get('sub_sub_subgroup_type')
                ))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template applied successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/export-template', methods=['POST'])
@require_project_admin
def api_admin_export_template():
    """API endpoint to export current phonemes as a template"""
    try:
        data = request.get_json()
        template_name = data.get('name', 'Phoneme Template')
        template_description = data.get('description', '')

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Create templates table if it doesn't exist
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

        # Get all current phonemes with full 4-level hierarchy
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, 
                   subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme
        """)

        phonemes = cursor.fetchall()

        # Convert to template format
        template_data = {
            'name': template_name,
            'description': template_description,
            'export_date': datetime.now().isoformat(), # Use isoformat for string representation
            'phonemes': []
        }

        for phoneme in phonemes:
            template_data['phonemes'].append({
                'syllable_type': phoneme[0],
                'position': phoneme[1],
                'length_type': phoneme[2],
                'group_type': phoneme[3],
                'subgroup_type': phoneme[4],
                'sub_subgroup_type': phoneme[5],
                'sub_sub_subgroup_type': phoneme[6],
                'phoneme': phoneme[7],
                'frequency': phoneme[8]
            })

        # Save template to database
        cursor.execute("""
            INSERT INTO phoneme_templates (name, description, template_data, phoneme_count)
            VALUES (?, ?, ?, ?)
        """, (template_name, template_description, json.dumps(template_data), len(phonemes)))

        template_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template exported successfully!', 'template_id': template_id})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Cloud Phoneme Templates API
@app.route('/api/cloud-templates', methods=['GET'])
def api_get_cloud_templates():
    """Get available cloud phoneme templates"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})
        
        # Get templates from Firebase
        templates = firestore_db.get_phoneme_templates(user_id=user_id, include_public=True)
        
        # Format templates for frontend
        template_list = []
        for template in templates:
            template_list.append({
                'id': template['id'],
                'name': template.get('name', ''),
                'description': template.get('description', ''),
                'language_family': template.get('language_family', ''),
                'phoneme_count': len(template.get('phonemes', [])),
                'created_by': template.get('created_by'),
                'is_public': template.get('is_public', False),
                'is_system_default': template.get('is_system_default', False),
                'created_at': template.get('created_at'),
                'is_mine': template.get('created_by') == user_id
            })
        
        return jsonify({'success': True, 'templates': template_list})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/cloud-templates', methods=['POST'])
def api_upload_template_to_cloud():
    """Upload current project phonemes as a cloud template"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})
        
        data = request.get_json()
        template_name = data.get('name', '').strip()
        description = data.get('description', '').strip()
        language_family = data.get('language_family', '').strip()
        is_public = data.get('is_public', False)
        
        if not template_name:
            return jsonify({'success': False, 'error': 'Template name is required'})
        
        # Get current project info
        user_info = get_user_info()
        current_project = user_info.get('current_project')
        if not current_project:
            return jsonify({'success': False, 'error': 'No active project'})
        
        project_id = current_project['id']
        
        # Get phonemes from current project
        if clean_firebase_service.is_available() and len(str(project_id)) > 10:  # Firebase project
            phonemes = firestore_db.get_project_phonemes(project_id)
            
            # Convert Firebase phonemes to template format
            template_phonemes = []
            for phoneme in phonemes:
                template_phonemes.append({
                    'syllable_type': phoneme.get('syllable_type'),
                    'position': phoneme.get('position'),
                    'length_type': phoneme.get('length_type'),
                    'group_type': phoneme.get('group_type'),
                    'subgroup_type': phoneme.get('subgroup_type'),
                    'sub_subgroup_type': phoneme.get('sub_subgroup_type', ''),
                    'sub_sub_subgroup_type': phoneme.get('sub_sub_subgroup_type', ''),
                    'phoneme': phoneme.get('phoneme'),
                    'frequency': 0  # Reset frequencies for template
                })
        else:
            # Local project - get from SQLite
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT syllable_type, position, length_type, group_type, 
                       subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme
                FROM phonemes
                ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
            """)
            
            phonemes = cursor.fetchall()
            conn.close()
            
            template_phonemes = []
            for phoneme in phonemes:
                template_phonemes.append({
                    'syllable_type': phoneme[0],
                    'position': phoneme[1],
                    'length_type': phoneme[2],
                    'group_type': phoneme[3],
                    'subgroup_type': phoneme[4],
                    'sub_subgroup_type': phoneme[5] or '',
                    'sub_sub_subgroup_type': phoneme[6] or '',
                    'phoneme': phoneme[7],
                    'frequency': 0  # Reset frequencies for template
                })
        
        if not template_phonemes:
            return jsonify({'success': False, 'error': 'No phonemes found in current project'})
        
        # Create template data
        template_data = {
            'name': template_name,
            'description': description,
            'language_family': language_family,
            'phonemes': template_phonemes,
            'created_by': user_id,
            'is_public': is_public,
            'is_system_default': False
        }
        
        # Upload to Firebase
        template_id = firestore_db.create_phoneme_template(template_data)
        
        if template_id:
            return jsonify({
                'success': True, 
                'message': f'Template "{template_name}" uploaded to cloud successfully!',
                'template_id': template_id
            })
        else:
            return jsonify({'success': False, 'error': 'Failed to upload template to cloud'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/cloud-templates/<template_id>/download', methods=['POST'])
def api_download_cloud_template(template_id):
    """Download and apply a cloud template to current project"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})
        
        data = request.get_json() or {}
        target_storage = data.get('target_storage', 'current')  # 'current', 'local', or 'firebase'
        
        # Get current project info
        user_info = get_user_info()
        current_project = user_info.get('current_project')
        if not current_project:
            return jsonify({'success': False, 'error': 'No active project'})
        
        project_id = current_project['id']
        
        # Get template from Firebase
        template = firestore_db.get_phoneme_template(template_id)
        if not template:
            return jsonify({'success': False, 'error': 'Template not found'})
        
        template_phonemes = template.get('phonemes', [])
        if not template_phonemes:
            return jsonify({'success': False, 'error': 'Template has no phonemes'})
        
        # Apply to current project based on storage type
        if target_storage == 'current' or target_storage == 'firebase':
            if firestore_db.is_available() and len(str(project_id)) > 10:  # Firebase project
                # Clear existing phonemes for this project
                existing_phonemes = firestore_db.get_project_phonemes(project_id)
                for phoneme in existing_phonemes:
                    firestore_db.delete_phoneme(phoneme['id'])
                
                # Apply template to Firebase project
                success = firestore_db.initialize_project_phonemes_from_template(project_id, template_id, user_id)
                
                if success:
                    return jsonify({
                        'success': True, 
                        'message': f'Template "{template["name"]}" applied to Firebase project successfully!'
                    })
                else:
                    return jsonify({'success': False, 'error': 'Failed to apply template to Firebase project'})
            
            elif target_storage == 'current':  # Local project
                # Apply to local SQLite database
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()
                
                # Clear existing phonemes
                cursor.execute("DELETE FROM phonemes")
                
                # Apply template phonemes
                for phoneme_data in template_phonemes:
                    cursor.execute("""
                        INSERT INTO phonemes (syllable_type, position, length_type, group_type, 
                                              subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        phoneme_data.get('syllable_type'),
                        phoneme_data.get('position'),
                        phoneme_data.get('length_type'),
                        phoneme_data.get('group_type'),
                        phoneme_data.get('subgroup_type'),
                        phoneme_data.get('sub_subgroup_type', ''),
                        phoneme_data.get('sub_sub_subgroup_type', ''),
                        phoneme_data.get('phoneme'),
                        phoneme_data.get('frequency', 0)
                    ))
                
                conn.commit()
                conn.close()
                
                return jsonify({
                    'success': True, 
                    'message': f'Template "{template["name"]}" applied to local project successfully!'
                })
        
        elif target_storage == 'local':
            # Force apply to local SQLite regardless of current project type
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            
            # Create local template
            template_data = {
                'name': template['name'],
                'description': template.get('description', ''),
                'export_date': datetime.now().isoformat(),
                'phonemes': template_phonemes
            }
            
            cursor.execute("""
                INSERT INTO phoneme_templates (name, description, template_data, phoneme_count)
                VALUES (?, ?, ?, ?)
            """, (
                template['name'] + ' (Downloaded)',
                template.get('description', '') + ' (Downloaded from cloud)',
                json.dumps(template_data),
                len(template_phonemes)
            ))
            
            conn.commit()
            conn.close()
            
            return jsonify({
                'success': True,
                'message': f'Template "{template["name"]}" downloaded and saved locally!'
            })
        
        return jsonify({'success': False, 'error': 'Invalid target storage type'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/cloud-templates/<template_id>', methods=['DELETE'])
def api_delete_cloud_template(template_id):
    """Delete a cloud template (only if owned by user)"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})
        
        # Get template to check ownership
        template = firestore_db.get_phoneme_template(template_id)
        if not template:
            return jsonify({'success': False, 'error': 'Template not found'})
        
        if template.get('created_by') != user_id:
            return jsonify({'success': False, 'error': 'You can only delete templates you created'})
        
        # Delete template
        success = firestore_db.delete_phoneme_template(template_id)
        
        if success:
            return jsonify({
                'success': True,
                'message': f'Template "{template["name"]}" deleted successfully!'
            })
        else:
            return jsonify({'success': False, 'error': 'Failed to delete template'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/apply-template/<int:template_id>', methods=['POST'])
@require_project_admin
def api_admin_apply_template(template_id):
    """API endpoint to apply a phoneme template with enhanced validation and options"""
    try:
        data = request.get_json() or {}
        preserve_frequencies = data.get('preserve_frequencies', False)
        force_apply = data.get('force_apply', False)
        phoneme_handling = data.get('phoneme_handling', {})  # New: phoneme-specific handling options

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Get template data
        cursor.execute("""
            SELECT name, template_data FROM phoneme_templates WHERE id = ?
        """, (template_id,))

        result = cursor.fetchone()
        if not result:
            conn.close()
            return jsonify({'success': False, 'error': 'Template not found'})

        template_name, template_data_json = result
        template_data = json.loads(template_data_json)

        # Get current phonemes with their usage details
        cursor.execute("""
            SELECT id, syllable_type, position, length_type, group_type, 
                   subgroup_type, phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
        """)
        current_phonemes = cursor.fetchall()

        # Create sets and dictionaries for comparison
        template_phonemes_set = set()
        template_phonemes_dict = {}

        for phoneme_data in template_data['phonemes']:
            key = (
                phoneme_data.get('syllable_type'),
                phoneme_data.get('position'), 
                phoneme_data.get('length_type'),
                phoneme_data.get('group_type'),
                phoneme_data.get('subgroup_type'),
                phoneme_data.get('phoneme')
            )
            template_phonemes_set.add(key)
            template_phonemes_dict[key] = phoneme_data

        current_phonemes_set = set()
        current_phonemes_dict = {}

        for phoneme in current_phonemes:
            key = (
                phoneme[1], phoneme[2], phoneme[3], phoneme[4], phoneme[5], phoneme[6]
            ) # Use relevant fields as key
            current_phonemes_set.add(key)
            current_phonemes_dict[key] = {
                'id': phoneme[0],
                'syllable_type': phoneme[1],
                'position': phoneme[2],
                'length_type': phoneme[3],
                'group_type': phoneme[4],
                'subgroup_type': phoneme[5],
                'phoneme': phoneme[6],
                'frequency': phoneme[7]
            }

        # Find phonemes that will be removed
        phonemes_to_remove = current_phonemes_set - template_phonemes_set
        phonemes_in_common = current_phonemes_set & template_phonemes_set
        phonemes_to_add = template_phonemes_set - current_phonemes_set

        # Check if any phonemes to be removed are used in words
        phonemes_in_use = []
        phoneme_word_details = {}

        if phonemes_to_remove and not force_apply:
            for phoneme_key in phonemes_to_remove:
                syllable_type, position, length_type, group_type, subgroup_type, phoneme = phoneme_key

                # Get detailed word information for this phoneme
                if position == 'onset':
                    cursor.execute("""
                        SELECT id, english_words, new_language_word, ipa_phonetics 
                        FROM words WHERE onset_phoneme = ? AND onset_length_type = ?
                    """, (phoneme, length_type))
                elif position == 'nucleus':
                    cursor.execute("""
                        SELECT id, english_words, new_language_word, ipa_phonetics 
                        FROM words WHERE nucleus_phoneme = ? AND nucleus_length_type = ?
                    """, (phoneme, length_type))
                elif position == 'coda':
                    cursor.execute("""
                        SELECT id, english_words, new_language_word, ipa_phonetics 
                        FROM words WHERE coda_phoneme = ? AND coda_length_type = ?
                    """, (phoneme, length_type))

                words_using_phoneme = cursor.fetchall()
                if words_using_phoneme:
                    # Create a unique key for this phoneme instance (position + length_type + phoneme)
                    # to handle cases where the same phoneme might appear with different length_types.
                    phoneme_key_str = f"{phoneme}_{position}_{length_type}" 
                    phoneme_word_details[phoneme_key_str] = []

                    for word_data in words_using_phoneme:
                        try:
                            english_words_data = json.loads(word_data[1]) if word_data[1] else []
                            if isinstance(english_words_data, list):
                                english_display = ', '.join(english_words_data)
                            else:
                                english_display = str(word_data[1])
                        except (json.JSONDecodeError, TypeError):
                            english_display = word_data[1] or 'No translation'

                        phoneme_word_details[phoneme_key_str].append({
                            'id': word_data[0],
                            'english_words': english_display,
                            'new_language_word': word_data[2] or 'Unnamed',
                            'ipa_phonetics': word_data[3] or ''
                        })

                    phonemes_in_use.append({
                        'phoneme': phoneme,
                        'position': position,
                        'length_type': length_type,
                        'group_type': group_type,
                        'subgroup_type': subgroup_type,
                        'usage_count': len(words_using_phoneme),
                        'phoneme_key': phoneme_key_str # Use the generated key
                    })

        # If phonemes are in use and not forced, return conflict info with word details
        if phonemes_in_use and not force_apply:
            replacement_options = {}

            # Get all available phonemes from the template for each position
            template_phonemes_by_position = {}
            for template_phoneme_key, template_p_data in template_phonemes_dict.items():
                position = template_p_data.get('position')
                if position not in template_phonemes_by_position:
                    template_phonemes_by_position[position] = []

            # Fetch replacement options for each phoneme in use
            for item_in_use in phonemes_in_use:
                position = item_in_use['position']
                
                # Get all phonemes from the template that match this position
                available_replacements = []
                for template_p_key, template_p_data in template_phonemes_dict.items():
                    if template_p_data.get('position') == position:
                        available_replacements.append({
                            'phoneme': template_p_data.get('phoneme'),
                            'group_type': template_p_data.get('group_type'),
                            'subgroup_type': template_p_data.get('subgroup_type'),
                            'length_type': template_p_data.get('length_type')
                        })
                replacement_options[item_in_use['phoneme_key']] = available_replacements


            conn.close()
            return jsonify({
                'success': False,
                'error': 'phonemes_in_use',
                'phonemes_in_use': phonemes_in_use,
                'phoneme_word_details': phoneme_word_details,
                'replacement_options': replacement_options,
                'phonemes_to_remove_count': len(phonemes_to_remove),
                'phonemes_to_add_count': len(phonemes_to_add),
                'phonemes_in_common_count': len(phonemes_in_common),
                'template_name': template_name,
                'message': f'{len(phonemes_in_use)} phonemes from the current set are used in words and would be removed by this template.'
            })

        # Apply the template with phoneme handling
        words_updated = 0
        words_with_orphaned_phonemes = 0

        if phoneme_handling and force_apply:
            # Handle phoneme conflicts based on user choices
            pass

        # Clear existing phonemes and insert template phonemes
        cursor.execute("DELETE FROM phonemes")

        preserved_count = 0
        new_count = 0

        for template_p_data in template_data['phonemes']:
            frequency = template_p_data.get('frequency', 0)
            new_count += 1

            cursor.execute("""
                INSERT INTO phonemes (syllable_type, position, length_type, group_type, subgroup_type, 
                                    phoneme, frequency, sub_subgroup_type, sub_sub_subgroup_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                template_p_data.get('syllable_type'),
                template_p_data.get('position'),
                template_p_data.get('length_type'),
                template_p_data.get('group_type'),
                template_p_data.get('subgroup_type'),
                template_p_data.get('phoneme'),
                frequency,
                template_p_data.get('sub_subgroup_type'),
                template_p_data.get('sub_sub_subgroup_type')
            ))

        conn.commit()
        conn.close()

        applied_msg = f'Template "{template_name}" applied successfully!'
        if new_count > 0:
            applied_msg += f' Added {new_count} phonemes.'

        return jsonify({
            'success': True, 
            'message': applied_msg,
            'statistics': {
                'phonemes_added': new_count,
                'phonemes_removed': len(phonemes_to_remove),
                'phonemes_preserved': preserved_count
            }
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/admin/download-template/<int:template_id>')
@require_project_admin
def api_admin_download_template(template_id):
    """API endpoint to download a phoneme template as JSON file"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT name, template_data FROM phoneme_templates WHERE id = ?", (template_id,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            return jsonify({'success': False, 'error': 'Template not found'}), 404

        template_name, template_data = result

        from flask import Response
        response = Response(
            template_data,
            mimetype='application/json',
            headers={'Content-Disposition': f'attachment; filename="{template_name.replace(" ", "_")}.json"'}
        )
        return response

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/admin/import-template', methods=['POST'])
@require_project_admin
def api_admin_import_template():
    """API endpoint to import a phoneme template from JSON file or by template_id"""
    try:
        request_data = request.get_json()
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Check if importing by template_id
        if 'template_id' in request_data:
            template_id = request_data['template_id']
            
            # Get template data from database
            cursor.execute("""
                SELECT name, description, template_data FROM phoneme_templates 
                WHERE id = ?
            """, (template_id,))
            
            result = cursor.fetchone()
            if not result:
                return jsonify({'success': False, 'error': 'Template not found'})
            
            template_name, template_description, template_data_json = result
            template_data = json.loads(template_data_json)
        else:
            # Import full template data
            template_data = request_data
            required_keys = ['name', 'phonemes']
            for key in required_keys:
                if key not in template_data:
                    return jsonify({'success': False, 'error': f'Missing required field: {key}'})
            
            template_name = template_data['name'] + ' (Imported)'
            template_description = template_data.get('description', 'Imported template')

        # Clear existing phonemes
        cursor.execute("DELETE FROM phonemes")
        
        # Import phonemes from template
        phoneme_count = 0
        for phoneme_data in template_data['phonemes']:
            cursor.execute("""
                INSERT INTO phonemes (syllable_type, position, length_type, group_type, 
                                    subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, 
                                    phoneme, frequency)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                phoneme_data['syllable_type'],
                phoneme_data['position'],
                phoneme_data['length_type'],
                phoneme_data['group_type'],
                phoneme_data['subgroup_type'],
                phoneme_data['sub_subgroup_type'],
                phoneme_data['sub_sub_subgroup_type'],
                phoneme_data['phoneme'],
                phoneme_data['frequency']
            ))
            phoneme_count += 1

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': f'Template imported successfully! {phoneme_count} phonemes restored.'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/delete-template/<int:template_id>', methods=['DELETE'])
@require_project_admin
def api_admin_delete_template(template_id):
    """API endpoint to delete a phoneme template"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM phoneme_templates WHERE id = ?", (template_id,))
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'success': False, 'error': 'Template not found'})

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template deleted successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/reset-to-default', methods=['POST'])
@require_project_admin
def api_admin_reset_to_default():
    """API endpoint to reset phonemes to default configuration (keeps words)"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM phonemes")
        main.insert_sample_data() # Re-insert default data

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Phonemes reset to default configuration successfully! (Words preserved)'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/fix-video-paths', methods=['POST'])
@require_project_admin
def api_admin_fix_video_paths():
    """API endpoint to fix corrupted video paths in the database"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT id, video_path FROM words WHERE video_path IS NOT NULL")
        words_with_videos = cursor.fetchall()

        fixed_count = 0
        removed_count = 0

        for word_id, video_path in words_with_videos:
            if video_path:
                normalized_path = video_path.replace('\\', '/')
                if normalized_path.startswith('videos/videos/'):
                    normalized_path = normalized_path[7:]

                if os.path.exists(normalized_path):
                    if normalized_path != video_path:
                        cursor.execute("UPDATE words SET video_path = ? WHERE id = ?", (normalized_path, word_id))
                        fixed_count += 1
                else:
                    cursor.execute("UPDATE words SET video_path = NULL WHERE id = ?", (word_id,))
                    removed_count += 1

        conn.commit()
        conn.close()

        message = f'Fixed {fixed_count} video paths and removed {removed_count} invalid video references.'
        return jsonify({'success': True, 'message': message})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/templates')
@require_project_admin
def api_admin_get_templates():
    """API endpoint to get all saved templates"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

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

        cursor.execute("SELECT id, name, description, phoneme_count, created_at FROM phoneme_templates ORDER BY created_at DESC")
        templates = cursor.fetchall()
        conn.close()

        templates_list = []
        for template in templates:
            templates_list.append({
                'id': template[0],
                'name': template[1],
                'description': template[2],
                'phoneme_count': template[3],
                'created_at': template[4]
            })
        return jsonify({'success': True, 'templates': templates_list})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/groups')
@require_auth
def groups_menu():
    """Groups management menu"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Get user's groups (both admin and member)
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
    return render_template('groups_menu.html', groups=groups, user=user)

@app.route('/groups/create', methods=['GET', 'POST'])
@require_auth
def create_group():
    """Create a new group"""
    user = get_user_info()

    if request.method == 'POST':
        group_name = request.form.get('name', '').strip()
        group_description = request.form.get('description', '').strip()

        if not group_name:
            flash('Group name is required', 'error')
            return render_template('create_group.html', user=user)

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        try:
            # Create group
            cursor.execute("""
                INSERT INTO groups (name, description, admin_user_id) 
                VALUES (?, ?, ?)
            """, (group_name, group_description, user['id']))

            group_id = cursor.lastrowid

            # Add creator as member
            cursor.execute("""
                INSERT INTO group_memberships (group_id, user_id) 
                VALUES (?, ?)
            """, (group_id, user['id']))

            # Create initial invite link
            import secrets
            invite_token = secrets.token_urlsafe(32)
            cursor.execute("""
                INSERT INTO group_invites (group_id, invite_token, created_by, expires_at)
                VALUES (?, ?, ?, datetime('now', '+30 days'))
            """, (group_id, invite_token, user['id']))

            conn.commit()
            flash(f'Group "{group_name}" created successfully!', 'success')
            return redirect(url_for('groups_menu'))

        except Exception as e:
            flash(f'Error creating group: {str(e)}', 'error')
        finally:
            conn.close()

    return render_template('create_group.html', user=user)

@app.route('/groups/<int:group_id>')
@require_auth
def group_detail(group_id):
    """Group detail page"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Get group info and verify membership
    cursor.execute("""
        SELECT g.name, g.description, g.created_at, g.user_id
        FROM project_groups g
        WHERE g.id = ?
    """, (group_id,))

    group_data = cursor.fetchone()
    if not group_data:
        flash('Group not found or access denied', 'error')
        conn.close()
        return redirect(url_for('groups_menu'))

    group = {
        'id': group_data[0],
        'name': group_data[1],
        'description': group_data[2],
        'admin_user_id': group_data[3],
        'is_admin': bool(group_data[4])
    }

    # Get group members
    cursor.execute("""
        SELECT u.username, gm.joined_at
        FROM group_memberships gm
        JOIN users u ON gm.user_id = u.id
        WHERE gm.group_id = ?
        ORDER BY gm.joined_at
    """, (group_id,))

    members = []
    for member in cursor.fetchall():
        members.append({
            'user_id': member[0],
            'joined_at': member[1]
        })

    # Get group projects (only shared projects)
    cursor.execute("""
        SELECT p.id, p.name, p.created_at, COUNT(w.id) as word_count, u.username as creator, ps.shared_at
        FROM projects p
        LEFT JOIN words w ON p.id = w.project_id
        JOIN users u ON p.user_id = u.id
        JOIN project_shares ps ON p.id = ps.project_id
        WHERE ps.group_id = ?
        GROUP BY p.id, p.name, p.created_at, u.username, ps.shared_at
        ORDER BY ps.shared_at DESC
    """, (group_id,))

    projects = []
    for project in cursor.fetchall():
        projects.append({
            'id': project[0],
            'name': project[1],
            'created_at': project[2],
            'word_count': project[3],
            'creator': project[4],
            'shared_at': project[5]
        })

    # Get current invite link if admin
    invite_link = None
    if group['is_admin']:
        cursor.execute("SELECT invite_code FROM project_groups WHERE id = ?", (group_id,))
        invite_data = cursor.fetchone()
        if invite_data:
            invite_link = {
                'token': invite_data[0],
                'expires_at': invite_data[1],
                'url': f"{request.host_url}groups/join/{invite_data[0]}"
            }

    conn.close()
    return render_template('group_detail.html', group=group, members=members, projects=projects, invite_link=invite_link, user=user)

@app.route('/groups/join/<invite_token>')
def join_group_via_invite(invite_token):
    """Join group via invite link"""
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Verify invite token
    cursor.execute("""
        SELECT id, name, invite_code FROM project_groups
        WHERE invite_code = ? AND user_id IS NOT NULL
        -- Removed expires_at check as invite_code is now directly on project_groups
    """, (invite_token,))

    invite_data = cursor.fetchone()
    if not invite_data:
        flash('Invalid or expired invite link', 'error')
        conn.close()
        return redirect(url_for('index'))

    group_id, group_name, invite_code_from_db = invite_data # Get actual invite code
    # The expires_at logic is removed as invite_code is always valid.
    # if invite_data[2] < datetime.now(): # Old expires_at check
    #    flash('Invalid or expired invite link', 'error')
    #    conn.close()
    #    return redirect(url_for('index'))

    # Check if user is logged in
    user = get_user_info()
    if not user['is_authenticated']:
        # Store invite token in session for after registration/login
        session['pending_group_invite'] = invite_token # Still use invite_token
        flash(f'Please create an account or sign in to join "{group_name}"', 'info')
        return redirect(url_for('login'))

    # Check if already a member
    cursor.execute("""
        SELECT id FROM group_memberships
        WHERE group_id = ? AND user_id = ?
    """, (group_id, user['id']))

    if cursor.fetchone():
        flash(f'You are already a member of "{group_name}"', 'info')
        conn.close()
        return redirect(url_for('group_detail', group_id=group_id))

    # Add user to group
    try:
        cursor.execute("""
            INSERT INTO group_memberships (group_id, user_id)
            VALUES (?, ?)
        """, (group_id, user['id']))
        conn.commit()
        flash(f'Successfully joined "{group_name}"!', 'success')
        conn.close()
        return redirect(url_for('group_detail', group_id=group_id))
    except Exception as e:
        flash(f'Error joining group: {str(e)}', 'error')
        conn.close()
        return redirect(url_for('groups_menu'))

@app.route('/api/groups/<int:group_id>/regenerate-invite', methods=['POST'])
@require_auth
def api_regenerate_invite_link(group_id):
    """Regenerate invite link for group (admin only)"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Verify admin status
    cursor.execute("""
        SELECT user_id FROM project_groups WHERE id = ?
    """, (group_id,))

    group_data = cursor.fetchone()
    if not group_data or group_data[0] != user['id']:
        conn.close()
        return jsonify({'success': False, 'error': 'Access denied'})

    try:
        # Create new invite token and update project_groups
        import secrets
        invite_code = secrets.token_urlsafe(32)
        cursor.execute("""
            UPDATE project_groups SET invite_code = ?
            WHERE id = ? AND user_id = ?
        """, (invite_code, group_id, user['id']))

        conn.commit()

        invite_url = f"{request.host_url}groups/join/{invite_code}"

        conn.close()
        return jsonify({
            'success': True,
            'invite_link': {
                'token': invite_code,
                'url': invite_url
            },
            'message': 'New invite link generated successfully!'
        })

    except Exception as e:
        conn.close()
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/groups/<int:group_id>/projects', methods=['POST'])
@require_auth
def api_create_group_project(group_id):
    """Create a new project for the group"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    try:
        # Verify group membership
        cursor.execute("""
            SELECT id FROM group_memberships
            WHERE group_id = ? AND user_id = ?
        """, (group_id, user['id']))

        if not cursor.fetchone():
            return jsonify({'success': False, 'error': 'Access denied'})

        data = request.get_json()
        project_name = data.get('name', '').strip()
        
        # print(f"DEBUG: api_create_group_project - Received request.json: {request.json}")
        # print(f"DEBUG: api_create_group_project - Extracted group_id={group_id}, user_id={user['id']}, project_name='{project_name}'")

        if not project_name:
            return jsonify({'success': False, 'error': 'Project name is required'})

        # Create project (storage_manager handles its own connection/commit for _create_project_sqlite)
        project_id = storage_manager._create_project_sqlite({
            'name': project_name,
            'user_id': user['id'],
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        project_identifier = f"local:{project_id}"

        # print(f"DEBUG: api_create_group_project - Created project_id={project_id}, project_identifier={project_identifier}")

        # Automatically share the project with the group
        insert_sql = """
            INSERT INTO project_shares (project_id, group_id, shared_by, project_identifier, storage_type)
            VALUES (?, ?, ?, ?, ?)
        """
        insert_params = (project_id, group_id, user['id'], project_identifier, 'local')

        # print(f"DEBUG: api_create_group_project - Executing INSERT: {insert_sql} with params: {insert_params}")
        cursor.execute(insert_sql, insert_params)

        conn.commit()

        return jsonify({
            'success': True,
            'message': f'Project "{project_name}" created and shared with group successfully!',
            'project_id': project_id,
            'project_identifier': project_identifier
        })

    except sqlite3.IntegrityError as e:
        conn.rollback()
        print(f"ERROR: api_create_group_project - IntegrityError details: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': f'Database integrity error: {e}'})
    except Exception as e:
        conn.rollback()
        import traceback
        print(f"ERROR: api_create_group_project - Unexpected error: {e}")
        traceback.print_exc()
        return jsonify({'success': False, 'error': f'An unexpected error occurred: {e}'})
    finally:
        conn.close()

@app.route('/api/tts/ipa', methods=['POST'])
def api_tts_ipa():
    """Generate audio from IPA text using best available TTS backend"""
    try:
        data = request.get_json()
        ipa_text = data.get('ipa', '').strip()
        
        if not ipa_text:
            return jsonify({'success': False, 'error': 'IPA text is required'}), 400
        
        # Generate audio using best available backend (eSpeak-NG preferred, Azure fallback)
        audio_base64 = ipa_tts.generate_ipa_audio(ipa_text)
        
        if audio_base64:
            return jsonify({
                'success': True,
                'audio_data': audio_base64,
                'ipa_input': ipa_text,
                'backend': 'Azure TTS (SSML Phonemes)',
                'format': 'mp3'
            })
        else:
            return jsonify({
                'success': False, 
                'error': 'Failed to generate audio with available TTS backends'
            }), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/tts/phoneme', methods=['POST'])
def api_tts_phoneme():
    """Generate audio for individual phoneme using best available TTS backend"""
    try:
        data = request.get_json()
        phoneme = data.get('phoneme', '').strip()
        position = data.get('position', 'standalone')
        
        if not phoneme:
            return jsonify({'success': False, 'error': 'Phoneme is required'}), 400
        
        # Generate audio for phoneme using best available backend
        audio_base64 = ipa_tts.generate_phoneme_audio(phoneme, position)
        
        if audio_base64:
            return jsonify({
                'success': True,
                'audio_data': audio_base64,
                'phoneme': phoneme,
                'position': position,
                'backend': 'Azure TTS (SSML Phonemes)',
                'format': 'mp3'
            })
        else:
            return jsonify({
                'success': False, 
                'error': 'Failed to generate phoneme audio with available TTS backends'
            }), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/phonemes/check-single', methods=['POST'])
def api_check_single_phoneme():
    """Check if a string represents a single phoneme block in the database"""
    try:
        data = request.get_json()
        phoneme = data.get('phoneme', '').strip()
        
        if not phoneme:
            return jsonify({'success': False, 'error': 'Phoneme is required'}), 400
        
        # Check if the phoneme exists in the database as a single phoneme
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT COUNT(*) FROM phonemes 
            WHERE phoneme = ?
        """, (phoneme,))
        
        count = cursor.fetchone()[0]
        conn.close()
        
        is_single_phoneme = count > 0
        
        return jsonify({
            'success': True,
            'phoneme': phoneme,
            'is_single_phoneme': is_single_phoneme
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/tts/status')
def api_tts_status():
    """Check TTS system status and capabilities"""
    # Get Azure TTS availability from the TTS engine
    azure_available = ipa_tts.azure_available
    
    backends = []
    if azure_available:
        backends.append({
            'name': 'Azure TTS',
            'type': 'ssml_phonemes',
            'format': 'mp3',
            'priority': 1,
            'supports_raw_ipa': True,
            'supports_made_up_words': True
        })
    
    return jsonify({
        'primary_backend': 'Azure TTS' if azure_available else 'None',
        'backends_available': backends,
        'total_backends': len(backends),
        'supports_ipa': azure_available,
        'supports_made_up_words': azure_available,
        'installation_notes': 'Azure TTS required - set AZURE_SPEECH_KEY environment variable' if not azure_available else None
    })

@app.route('/test-audio')
def test_audio():
    """Test page for audio debugging"""
    return send_file('test_audio.html')

@app.route('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    return {'status': 'healthy', 'message': 'Phoneme Tracker Flask app is running'}, 200

@app.route('/api/migrate-project/<int:project_id>', methods=['POST'])
@require_auth
def api_migrate_project(project_id):
    """API endpoint to migrate a local project to Firebase"""
    try:
        user = get_user_info()
        
        # Check if Firebase is available
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False, 
                'error': 'Firebase service not available'
            })
        
        # Verify user owns this project
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        local_project = cursor.fetchone()
        
        if not local_project:
            return jsonify({
                'success': False, 
                'error': 'Project not found or access denied'
            })
        
        project_name = local_project[0]
        
        # Create Firebase project
        firebase_project_data = {
            'name': project_name,
            'user_id': user['id']
        }
        firebase_project_id = firestore_db.create_project(firebase_project_data)
        
        if not firebase_project_id:
            return jsonify({
                'success': False, 
                'error': 'Failed to create Firebase project'
            })
        
        migration_stats = {
            'words_migrated': 0,
            'videos_migrated': 0,
            'phonemes_migrated': 0,
            'errors': []
        }
        
        # Migrate words
        cursor.execute("""
            SELECT id, language, english_words, new_language_word, ipa_phonetics, 
                   dictionary_phonetics, video_path, syllable_type, onset_phoneme,
                   onset_length_type, nucleus_phoneme, nucleus_length_type,
                   coda_phoneme, coda_length_type
            FROM words WHERE project_id = ?
        """, (project_id,))
        
        words = cursor.fetchall()
        
        for word_row in words:
            try:
                # Migrate video if it exists and is local
                video_path = word_row[6]
                firebase_video_url = None
                
                if video_path and not video_path.startswith('https://') and os.path.exists(video_path):
                    # Upload video to Firebase Storage
                    filename = os.path.basename(video_path)
                    storage_path = f"videos/{user['id']}/{firebase_project_id}/{filename}"
                    
                    # Read local video file
                    with open(video_path, 'rb') as video_file:
                        video_data = video_file.read()
                    
                    # Determine content type
                    file_extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else 'mp4'
                    content_type_map = {
                        'mp4': 'video/mp4',
                        'avi': 'video/x-msvideo',
                        'mov': 'video/quicktime',
                        'mkv': 'video/x-matroska',
                        'webm': 'video/webm'
                    }
                    content_type = content_type_map.get(file_extension, 'video/mp4')
                    
                    # Upload to Firebase Storage
                    result = clean_firebase_service.upload_file_from_memory(
                        video_data,
                        storage_path,
                        content_type=content_type
                    )
                    
                    if result and result.get('success'):
                        firebase_video_url = result.get('public_url')
                        migration_stats['videos_migrated'] += 1
                    else:
                        migration_stats['errors'].append(f"Failed to upload video for word '{word_row[3]}'")
                
                # Parse English words from SQLite JSON to Firebase array
                try:
                    english_words_data = json.loads(word_row[2]) if word_row[2] else []
                    # Ensure it's a list
                    if isinstance(english_words_data, str):
                        english_words_data = [english_words_data]
                    elif not isinstance(english_words_data, list):
                        english_words_data = [str(english_words_data)]
                except (json.JSONDecodeError, TypeError):
                    # Fallback: treat as single string
                    english_words_data = [word_row[2]] if word_row[2] else []
                
                # Create word in Firebase
                word_data = {
                    'language': word_row[1],
                    'english_words': english_words_data,
                    'new_language_word': word_row[3],
                    'ipa_phonetics': word_row[4],
                    'dictionary_phonetics': word_row[5],
                    'video_path': firebase_video_url or video_path,  # Use Firebase URL if uploaded, otherwise keep original
                    'syllable_type': word_row[7],
                    'onset_phoneme': word_row[8],
                    'onset_length_type': word_row[9],
                    'nucleus_phoneme': word_row[10],
                    'nucleus_length_type': word_row[11],
                    'coda_phoneme': word_row[12],
                    'coda_length_type': word_row[13],
                    'user_id': user['id'],
                    'project_id': firebase_project_id
                }
                
                firebase_word_id = firestore_db.create_word(word_data)
                if firebase_word_id:
                    migration_stats['words_migrated'] += 1
                else:
                    migration_stats['errors'].append(f"Failed to create Firebase word for '{word_row[3]}'")
                    
            except Exception as e:
                migration_stats['errors'].append(f"Error migrating word '{word_row[3]}': {str(e)}")
        
        # Migrate phonemes
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, subgroup_type,
                   sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type
        """)
        
        phonemes = cursor.fetchall()
        
        for phoneme_row in phonemes:
            try:
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
                    'project_id': firebase_project_id,
                    'user_id': user['id']
                }
                
                firebase_phoneme_id = firestore_db.create_phoneme(phoneme_data)
                if firebase_phoneme_id:
                    migration_stats['phonemes_migrated'] += 1
                else:
                    migration_stats['errors'].append(f"Failed to create Firebase phoneme '{phoneme_row[7]}'")
                    
            except Exception as e:
                migration_stats['errors'].append(f"Error migrating phoneme '{phoneme_row[7]}': {str(e)}")
        
        conn.close()
        
        return jsonify({
            'success': True,
            'message': f'Project "{project_name}" migrated successfully to Firebase',
            'firebase_project_id': firebase_project_id,
            'stats': migration_stats
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'error': f'Migration failed: {str(e)}'
        })

@app.route('/api/storage/test')
@require_auth
def test_firebase_storage():
    """Test Firebase Storage connectivity"""
    if not clean_firebase_service.is_available():
        return jsonify({
            'success': False,
            'error': 'Firebase service not available',
            'storage_ready': False
        })
    
    # Check if bucket is available
    bucket_available = hasattr(clean_firebase_service, 'bucket') and clean_firebase_service.bucket is not None
    
    return jsonify({
        'success': True,
        'message': 'Firebase Storage connectivity test',
        'storage_ready': bucket_available,
        'bucket_name': f'{clean_firebase_service.config.get_project_id()}.firebasestorage.app' if bucket_available else None
    })

@app.route('/firebase-test')
def firebase_test():
    """Firebase diagnostic test page"""
    return render_template('firebase_test.html')

# Phoneme Template Routes
@app.route('/api/phoneme-templates')
@require_auth
def api_get_phoneme_templates():
    """Get available phoneme templates"""
    try:
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False,
                'error': 'Firebase service not available',
                'templates': []
            })
        
        user = get_user_info()
        templates = firestore_db.get_phoneme_templates(user['id'], include_public=True)
        
        return jsonify({
            'success': True,
            'templates': templates
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'templates': []
        })

@app.route('/api/phoneme-templates', methods=['POST'])
@require_auth
def api_create_phoneme_template():
    """Create a new phoneme template from current SQLite phonemes"""
    try:
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False,
                'error': 'Firebase service not available'
            })
        
        user = get_user_info()
        data = request.get_json()
        
        # Get current SQLite phonemes
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, 
                   subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, 
                   phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, phoneme
        """)
        phonemes_data = cursor.fetchall()
        conn.close()
        
        # Convert to template format
        phonemes_list = []
        for phoneme_row in phonemes_data:
            phonemes_list.append({
                'syllable_type': phoneme_row[0],
                'position': phoneme_row[1],
                'length_type': phoneme_row[2],
                'group_type': phoneme_row[3],
                'subgroup_type': phoneme_row[4],
                'sub_subgroup_type': phoneme_row[5],
                'sub_sub_subgroup_type': phoneme_row[6],
                'phoneme': phoneme_row[7],
                'frequency': phoneme_row[8]
            })
        
        template_data = {
            'name': data.get('name', 'Unnamed Template'),
            'description': data.get('description', ''),
            'language_family': data.get('language_family', ''),
            'phonemes': phonemes_list,
            'created_by': user['id'],
            'is_public': data.get('is_public', False)
        }
        
        template_id = firestore_db.create_phoneme_template(template_data)
        if template_id:
            return jsonify({
                'success': True,
                'template_id': template_id,
                'message': f'Template "{template_data["name"]}" created successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to create template'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/phoneme-templates/<template_id>', methods=['DELETE'])
@require_auth
def api_delete_phoneme_template(template_id):
    """Delete a phoneme template"""
    try:
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False,
                'error': 'Firebase service not available'
            })
        
        user = get_user_info()
        
        # Check if user owns the template
        template = firestore_db.get_phoneme_template(template_id)
        if not template:
            return jsonify({
                'success': False,
                'error': 'Template not found'
            })
        
        if template.get('created_by') != user['id']:
            return jsonify({
                'success': False,
                'error': 'Access denied. You can only delete your own templates.'
            })
        
        success = firestore_db.delete_phoneme_template(template_id)
        if success:
            return jsonify({
                'success': True,
                'message': 'Template deleted successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to delete template'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/projects/<project_id>/apply-template/<template_id>', methods=['POST'])
@require_auth
def api_apply_phoneme_template(project_id, template_id):
    """Apply a phoneme template to a Firebase project"""
    try:
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False,
                'error': 'Firebase service not available'
            })
        
        user = get_user_info()
        
        # Check if user owns the project
        if not is_project_owner(project_id, user['id']):
            return jsonify({
                'success': False,
                'error': 'Access denied. Only project owners can apply templates.'
            })
        
        # Apply the template
        success = firestore_db.initialize_project_phonemes_from_template(
            project_id, template_id, user['id']
        )
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Template applied successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to apply template'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route - Firebase authentication only"""
    # Check if user is already authenticated with Firebase
    if 'firebase_uid' in session:
        return redirect(url_for('dashboard'))
    
    firebase_config = get_firebase_config()
    
    return render_template('login.html', firebase_config=firebase_config)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration route - Local email/password registration"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Validation
        if not username or not email or not password:
            flash('All fields are required', 'error')
            return render_template('login.html', firebase_config=get_firebase_config())

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('login.html', firebase_config=get_firebase_config())

        if len(password) < 6:
            flash('Password must be at least 6 characters long', 'error')
            return render_template('login.html', firebase_config=get_firebase_config())

        # Check if user already exists
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ? OR username = ?", (email, username))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email or username already exists', 'error')
            conn.close()
            return render_template('login.html', firebase_config=get_firebase_config())

        # Create new user
        from werkzeug.security import generate_password_hash
        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        # Log them in automatically
        session['user_id'] = user_id
        session['username'] = username
        session['auth_method'] = 'email_password'
        flash(f'Account created successfully! Welcome, {username}!', 'success')

        # Check for pending group invite
        if 'pending_group_invite' in session:
            invite_token = session.pop('pending_group_invite')
            return redirect(url_for('join_group_via_invite', invite_token=invite_token))

        return redirect(url_for('index'))

    return render_template('login.html', firebase_config=get_firebase_config())

@app.route('/logout')
def logout():
    """Logout route - Firebase authentication only"""
    # Clear server-side session
    session.clear()
    
    # Redirect to login page with success message
    flash('You have been signed out successfully.', 'success')
    return redirect(url_for('login'))

# Firebase Authentication Routes
@app.route('/api/auth/firebase-login', methods=['POST'])
def firebase_login():
    """Handle Firebase authentication login"""
    try:
        data = request.get_json()
        firebase_uid = data.get('uid')
        email = data.get('email')
        display_name = data.get('displayName')
        photo_url = data.get('photoURL')
        
        if not firebase_uid or not email:
            return jsonify({'success': False, 'error': 'Missing required data'}), 400
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Check if user exists with this Firebase UID
        cursor.execute("SELECT id, username, email FROM users WHERE firebase_uid = ?", (firebase_uid,))
        user_data = cursor.fetchone()
        
        if user_data:
            # User exists, log them in
            user_id = user_data[0]
            username = user_data[1]
        else:
            # Check if user exists with this email (legacy user)
            cursor.execute("SELECT id, username FROM users WHERE email = ?", (email,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                # Update existing user with Firebase UID
                user_id = existing_user[0]
                username = existing_user[1]
                cursor.execute("UPDATE users SET firebase_uid = ? WHERE id = ?", (firebase_uid, user_id))
            else:
                # Create new user
                username = display_name or email.split('@')[0]
                
                # Ensure username is unique
                base_username = username
                counter = 1
                while True:
                    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
                    if not cursor.fetchone():
                        break
                    username = f"{base_username}_{counter}"
                    counter += 1
                
                cursor.execute("""
                    INSERT INTO users (username, email, password_hash, firebase_uid)
                    VALUES (?, ?, ?, ?)
                """, (username, email, 'firebase_user', firebase_uid))
                
                user_id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
        # Set session
        session['firebase_uid'] = firebase_uid
        session['user_id'] = user_id  # Keep for compatibility
        session['username'] = username
        
        return jsonify({'success': True, 'message': f'Welcome, {username}!'})
        
    except Exception as e:
        print(f"Firebase login error: {e}")
        return jsonify({'success': False, 'error': 'Authentication failed'}), 500

@app.route('/api/auth/logout', methods=['POST'])
def api_logout():
    """API logout route for Firebase"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

# Email/Password Authentication Routes
@app.route('/api/auth/email-login', methods=['POST'])
def email_login():
    """Handle email/password login"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            return jsonify({'success': False, 'error': 'Email and password are required'}), 400
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Find user by email
        cursor.execute("SELECT id, username, email, password_hash FROM users WHERE email = ? AND is_active = 1", (email,))
        user_data = cursor.fetchone()
        
        if not user_data:
            return jsonify({'success': False, 'error': 'Invalid email or password'}), 401
        
        user_id, username, user_email, password_hash = user_data
        
        # Check password (handle both Firebase users and regular users)
        if password_hash == 'firebase_user':
            return jsonify({'success': False, 'error': 'This account uses Google Sign-In. Please use the Google Sign-In option.'}), 401
        
        if not check_password_hash(password_hash, password):
            return jsonify({'success': False, 'error': 'Invalid email or password'}), 401
        
        conn.close()
        
        # Set session for email/password authentication
        session['user_id'] = user_id
        session['username'] = username
        session['email'] = user_email
        session['auth_method'] = 'email_password'
        
        return jsonify({'success': True, 'message': f'Welcome back, {username}!'})
        
    except Exception as e:
        print(f"Email login error: {e}")
        return jsonify({'success': False, 'error': 'Login failed'}), 500

@app.route('/api/auth/email-register', methods=['POST'])
def email_register():
    """Handle email/password registration"""
    try:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not username or not email or not password:
            return jsonify({'success': False, 'error': 'All fields are required'}), 400
        
        if len(password) < 6:
            return jsonify({'success': False, 'error': 'Password must be at least 6 characters long'}), 400
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Check if username already exists
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return jsonify({'success': False, 'error': 'Username already exists'}), 400
        
        # Check if email already exists
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            return jsonify({'success': False, 'error': 'Email already registered'}), 400
        
        # Create new user
        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Account created successfully'})
        
    except Exception as e:
        print(f"Email registration error: {e}")
        return jsonify({'success': False, 'error': 'Registration failed'}), 500

@app.route('/auth/email', methods=['POST'])
def email_auth():
    """Handle Firebase email/password authentication"""
    try:
        print("Email auth endpoint called")
        data = request.get_json()
        print(f"Received data: {data}")
        
        uid = data.get('uid')
        email = data.get('email', '')
        display_name = data.get('displayName', '')
        photo_url = data.get('photoURL', '')

        if not uid or not email:
            print("Missing authentication data")
            return jsonify({'success': False, 'error': 'Missing authentication data'}), 400

        # Store user info in session
        session['firebase_uid'] = uid
        session['user_email'] = email
        session['user_name'] = display_name
        session['user_photo'] = photo_url

        # Check if user exists in local database, create if not
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM users WHERE firebase_uid = ?", (uid,))
        existing_user = cursor.fetchone()

        if not existing_user:
            # Create new user in local database (Firebase Auth users don't need password_hash)
            cursor.execute("""
                INSERT INTO users (firebase_uid, email, username, password_hash, created_at, is_active)
                VALUES (?, ?, ?, NULL, CURRENT_TIMESTAMP, 1)
            """, (uid, email, display_name))
            conn.commit()
            print(f"Created new user: {uid}")
        else:
            print(f"User already exists: {uid}")

        conn.close()

        return jsonify({'success': True, 'message': 'Email authentication successful'})

    except Exception as e:
        print(f"Email auth error: {e}")
        return jsonify({'success': False, 'error': 'Authentication failed'}), 500

@app.route('/auth/google', methods=['POST'])
def google_auth():
    """Handle Google OAuth authentication"""
    try:
        print("Google auth endpoint called")
        data = request.get_json()
        print(f"Received data: {data}")
        id_token = data.get('idToken')
        user_data = data.get('user', {})
        
        if not id_token or not user_data:
            print("Missing authentication data")
            return jsonify({'success': False, 'error': 'Missing authentication data'}), 400
        
        # Check if we're in development mode with Firebase emulators
        is_development = os.getenv('FIREBASE_AUTH_EMULATOR_HOST') is not None
        print(f"DEBUG: FIREBASE_AUTH_EMULATOR_HOST = {os.getenv('FIREBASE_AUTH_EMULATOR_HOST')}")
        print(f"DEBUG: is_development = {is_development}")
        
        if is_development:
            print("🔧 Development mode: Using Firebase Auth Emulator")
            # In development with emulators, we can trust the user data from the client
            # since the emulator handles the OAuth flow
            firebase_uid = user_data.get('uid')
            if not firebase_uid:
                return jsonify({'success': False, 'error': 'Missing user UID in development mode'}), 400
            print(f"Development mode: Using UID {firebase_uid}")
        else:
            print("🔒 Production mode: Verifying token with Firebase Admin SDK")
            # In production, verify the token if possible, otherwise trust client data
            firebase_uid = None
            
            # Try to verify token if Firebase Admin is available and token is valid
            if id_token and id_token != 'emulator_token':
                try:
                    # Ensure Firebase Admin is initialized
                    if clean_firebase_service.is_available() and clean_firebase_service.app:
                        from firebase_admin import auth as firebase_auth
                        decoded_token = firebase_auth.verify_id_token(id_token)
                        firebase_uid = decoded_token['uid']
                        print(f"Token verified successfully for user: {firebase_uid}")
                    else:
                        print("⚠️ Firebase Admin not initialized, using client-provided UID")
                        firebase_uid = user_data.get('uid')
                except Exception as firebase_error:
                    print(f"⚠️ Firebase token verification error: {firebase_error}")
                    print("Falling back to client-provided UID")
                    firebase_uid = user_data.get('uid')
            else:
                # Use client-provided UID if no valid token
                firebase_uid = user_data.get('uid')
            
            if not firebase_uid:
                print("Missing user UID")
                return jsonify({'success': False, 'error': 'Missing user UID'}), 400
        
        # Store user info in session
        session['firebase_uid'] = firebase_uid
        session['user_email'] = user_data.get('email', '')
        session['user_name'] = user_data.get('displayName', '')
        session['user_photo'] = user_data.get('photoURL', '')
        
        # Check if user exists in local database, create if not
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM users WHERE firebase_uid = ?", (firebase_uid,))
        existing_user = cursor.fetchone()
        
        if not existing_user:
            # Create new user in local database (Google OAuth users don't need password_hash)
            cursor.execute("""
                INSERT INTO users (firebase_uid, email, username, password_hash, created_at, is_active)
                VALUES (?, ?, ?, NULL, CURRENT_TIMESTAMP, 1)
            """, (firebase_uid, user_data.get('email', ''), user_data.get('displayName', '')))
            conn.commit()
            print(f"Created new user: {firebase_uid}")
        else:
            print(f"User already exists: {firebase_uid}")
        
        conn.close()
        
        mode_text = "development mode" if is_development else "production mode"
        return jsonify({'success': True, 'message': f'Google authentication successful ({mode_text})'})
            
    except Exception as e:
        print(f"Google auth error: {e}")
        return jsonify({'success': False, 'error': 'Authentication failed'}), 500

@app.route('/projects')
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
            project['storage_icon'] = '🌐'
            project['storage_label'] = 'Cloud'
            project['can_migrate'] = False
        else:
            # For local projects, count words in SQLite
            print(f"DEBUG: Counting words for local project {project.get('id')}")
            cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (project.get('id'),))
            word_count = cursor.fetchone()[0]
            project['word_count'] = word_count
            project['storage_icon'] = '💾'
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

@app.route('/projects/group/<int:group_id>')
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
        return redirect(url_for('dashboard'))

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

@app.route('/projects/create', methods=['GET', 'POST'])
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
                return redirect(url_for('main_menu'))
            else:
                print("DEBUG: project_id is None - showing 'Failed to create project'")
                flash('Failed to create project', 'error')
                
        except Exception as e:
            flash(f'Error creating project: {e}', 'error')

    return render_template('create_project.html', user=user, user_groups=user_groups,
                         firebase_available=clean_firebase_service.is_available())

@app.route('/projects/<project_id>/migrate-to-cloud', methods=['POST'])
@require_auth
def migrate_project_to_cloud(project_id):
    """Migrate a local project to cloud storage"""
    user = get_user_info()
    if not user:
        return redirect(url_for('login'))
    
    if not clean_firebase_service.is_available():
        flash('Cloud storage is not available', 'error')
        return redirect(url_for('projects_menu'))
    
    success, message = storage_manager.migrate_project_to_cloud(project_id, user['id'])
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    
    return redirect(url_for('projects_menu'))

@app.route('/projects/<project_id>/enter')
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
        return redirect(url_for('main_menu'))
    else:
        flash('Project not found or access denied', 'error')
        return redirect(url_for('dashboard'))

@app.route('/projects/exit')
@require_auth
def exit_project():
    """Exit current project"""
    if 'current_project_id' in session:
        del session['current_project_id']
        flash('Exited project', 'success')

    return redirect(url_for('dashboard'))

@app.route('/projects/<project_id>/edit', methods=['GET', 'POST'])
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
        return redirect(url_for('projects_menu'))

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
            return redirect(url_for('projects_menu'))

        except sqlite3.IntegrityError:
            flash('A project with this name already exists', 'error')
        finally:
            conn.close()

    conn.close()
    return render_template('edit_project.html', project={'id': project_id, 'name': project[0]}, user=user)

@app.route('/api/projects/<project_id>/rename', methods=['POST'])
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
        return jsonify({'success': True, 'message': f'Project renamed to \"{new_name}\" successfully!'})
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': f'Error renaming project: {e}'})
    finally:
        conn.close()

@app.route('/api/projects/<project_id>/branch', methods=['POST'])
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
                'message': f'Project branched successfully as \"{branch_name}\"!',
                'new_project_id': new_project_id,
            }
        )
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': f'Error branching project: {e}'})
    finally:
        conn.close()

# Note: /api/projects/<project_id>/merge is now in features/projects/api.py
# Note: /api/projects/<project_id>/delete is now in features/projects/api.py

@app.route('/api/projects/<project_id>/share', methods=['POST'])
@require_auth
def api_share_project(project_id):
    """Share a project with a group"""
    user = get_user_info()
    
    try:
        data = request.get_json()
        group_id = data.get('group_id')
        
        if not group_id:
            return jsonify({'success': False, 'error': 'Group ID is required'})
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Verify project belongs to user
        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        project = cursor.fetchone()
        
        if not project:
            return jsonify({'success': False, 'error': 'Project not found or access denied'})
        
        # Verify user is member of the group
        cursor.execute("""
            SELECT g.name FROM groups g
            JOIN group_memberships gm ON g.id = gm.group_id
            WHERE g.id = ? AND gm.user_id = ?
        """, (group_id, user['id']))
        
        group = cursor.fetchone()
        if not group:
            return jsonify({'success': False, 'error': 'Group not found or access denied'})
        
        # Check if already shared
        cursor.execute("""
            SELECT id FROM project_shares 
            WHERE project_id = ? AND group_id = ?
        """, (project_id, group_id))
        
        if cursor.fetchone():
            return jsonify({'success': False, 'error': 'Project is already shared with this group'})
        
        # Check if project uses cloud storage before sharing
        # Group projects must use cloud storage for collaboration
        project_storage_type = storage_manager.get_project_storage_type(project_id)
        
        if project_storage_type != 'cloud':
            # Try to migrate the project to cloud storage first
            if not clean_firebase_service.is_available():
                return jsonify({
                    'success': False, 
                    'error': 'Group projects require cloud storage, but cloud storage is not available. Please check your connection.'
                })
            
            # Attempt migration
            success, message = storage_manager.migrate_project_to_cloud(project_id, user['id'])
            if not success:
                return jsonify({
                    'success': False,
                    'error': f'Group projects require cloud storage. Migration failed: {message}'
                })
        
        # Share the project
        cursor.execute("""
            INSERT INTO project_shares (project_id, group_id, shared_by)
            VALUES (?, ?, ?)
        """, (project_id, group_id, user['id']))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'message': f'Project "{project[0]}" shared with group "{group[0]}" successfully! (Now using cloud storage for collaboration)'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/projects/<project_id>/shares')
@require_auth
def api_get_project_shares(project_id):
    """Get current sharing information for a project"""
    user = get_user_info()
    
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Verify project belongs to user
        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        project = cursor.fetchone()
        
        if not project:
            return jsonify({'success': False, 'error': 'Project not found or access denied'})
        
        # Get current shares
        cursor.execute("""
            SELECT ps.group_id, g.name as group_name, ps.shared_at
            FROM project_shares ps
            JOIN project_groups g ON ps.group_id = g.id
            WHERE ps.project_id = ?
            ORDER BY ps.shared_at DESC
        """, (project_id,))
        
        shares = []
        for share in cursor.fetchall():
            shares.append({
                'group_id': share[0],
                'group_name': share[1],
                'shared_at': share[2]
            })
        
        conn.close()
        
        return jsonify({
            'success': True,
            'shares': shares
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/projects/<project_id>/unshare/<int:group_id>', methods=['DELETE'])
@require_auth
def api_unshare_project(project_id, group_id):
    """Remove project sharing from a group"""
    user = get_user_info()
    
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Verify project belongs to user
        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        project = cursor.fetchone()
        
        if not project:
            return jsonify({'success': False, 'error': 'Project not found or access denied'})
        
        # Get group name for response
        cursor.execute("SELECT name FROM groups WHERE id = ?", (group_id,))
        group = cursor.fetchone()
        
        # Remove the share
        cursor.execute("""
            DELETE FROM project_shares 
            WHERE project_id = ? AND group_id = ?
        """, (project_id, group_id))
        
        if cursor.rowcount == 0:
            return jsonify({'success': False, 'error': 'Project was not shared with this group'})
        
        conn.commit()
        conn.close()
        
        group_name = group[0] if group else 'Unknown Group'
        
        return jsonify({
            'success': True,
            'message': f'Project "{project[0]}" is no longer shared with "{group_name}"'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# User and Group Management API Endpoints

# User Management APIs
@app.route('/api/users/search', methods=['GET'])
@require_auth
def api_search_users():
    """Search users by username or email"""
    try:
        query = request.args.get('q', '').strip()
        if len(query) < 2:
            return jsonify({'success': False, 'error': 'Search query must be at least 2 characters'})
        
        users = firestore_db.search_users(query)
        return jsonify({'success': True, 'users': users})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/users/<user_id>/profile', methods=['GET'])
@require_auth
def api_get_user_profile(user_id):
    """Get user profile information"""
    try:
        profile = firestore_db.get_user_profile(user_id)
        if not profile:
            return jsonify({'success': False, 'error': 'User not found'})
        
        return jsonify({'success': True, 'user': profile})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Group Management APIs
@app.route('/api/groups', methods=['GET', 'POST'])
@require_auth
def api_groups():
    """Get user's groups or create a new group"""
    user_id = session.get('user_id')
    
    if request.method == 'GET':
        try:
            groups = firestore_db.get_user_groups(user_id)
            return jsonify({'success': True, 'groups': groups})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    elif request.method == 'POST':
        try:
            data = request.get_json()
            group_name = data.get('name', '').strip()
            description = data.get('description', '').strip()
            
            if not group_name:
                return jsonify({'success': False, 'error': 'Group name is required'})
            
            group_data = {
                'name': group_name,
                'description': description,
                'admin_user_id': user_id
            }
            
            group_id = firestore_db.create_group(group_data)
            if group_id:
                # Add creator as admin member
                result = firestore_db.add_group_member(group_id, user_id, 'admin')
                if result['success']:
                    return jsonify({
                        'success': True, 
                        'group_id': group_id,
                        'message': f'Group "{group_name}" created successfully!'
                    })
                else:
                    return jsonify({'success': False, 'error': result['error']})
            else:
                return jsonify({'success': False, 'error': 'Failed to create group'})
                
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/api/groups/<group_id>', methods=['GET', 'PUT', 'DELETE'])
@require_auth
def api_group_detail(group_id):
    """Get, update, or delete a specific group"""
    user_id = session.get('user_id')
    
    # Check if user has access to this group
    group = firestore_db.get_group(group_id)
    if not group:
        return jsonify({'success': False, 'error': 'Group not found'})
    
    # Check if user is a member of this group
    user_groups = firestore_db.get_user_groups(user_id)
    user_group_ids = [g['id'] for g in user_groups]
    
    if group_id not in user_group_ids:
        return jsonify({'success': False, 'error': 'Access denied'})
    
    if request.method == 'GET':
        try:
            members = firestore_db.get_group_members(group_id)
            group['members'] = members
            return jsonify({'success': True, 'group': group})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    elif request.method == 'PUT':
        # Only admin can update group
        if group.get('admin_user_id') != user_id:
            return jsonify({'success': False, 'error': 'Only group admin can update group'})
        
        try:
            data = request.get_json()
            update_data = {}
            
            if 'name' in data:
                update_data['name'] = data['name'].strip()
            if 'description' in data:
                update_data['description'] = data['description'].strip()
            
            if not update_data:
                return jsonify({'success': False, 'error': 'No valid fields to update'})
            
            success = firestore_db.update_group(group_id, update_data)
            if success:
                return jsonify({'success': True, 'message': 'Group updated successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to update group'})
                
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    elif request.method == 'DELETE':
        # Only admin can delete group
        if group.get('admin_user_id') != user_id:
            return jsonify({'success': False, 'error': 'Only group admin can delete group'})
        
        try:
            success = firestore_db.delete_group(group_id)
            if success:
                return jsonify({'success': True, 'message': 'Group deleted successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to delete group'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/api/groups/<group_id>/members', methods=['GET', 'POST'])
@require_auth
def api_group_members(group_id):
    """Get group members or add new member"""
    user_id = session.get('user_id')
    
    # Verify user has access to this group
    user_groups = firestore_db.get_user_groups(user_id)
    user_group_ids = [g['id'] for g in user_groups]
    
    if group_id not in user_group_ids:
        return jsonify({'success': False, 'error': 'Access denied'})
    
    if request.method == 'GET':
        try:
            members = firestore_db.get_group_members(group_id)
            return jsonify({'success': True, 'members': members})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    elif request.method == 'POST':
        # Check if user is admin of this group
        group = firestore_db.get_group(group_id)
        if group.get('admin_user_id') != user_id:
            return jsonify({'success': False, 'error': 'Only group admin can add members'})
        
        try:
            data = request.get_json()
            target_user_id = data.get('user_id')
            role = data.get('role', 'member')
            
            if not target_user_id:
                return jsonify({'success': False, 'error': 'User ID is required'})
            
            result = firestore_db.add_group_member(group_id, target_user_id, role)
            return jsonify(result)
            
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/api/groups/<group_id>/members/<member_user_id>', methods=['DELETE', 'PUT'])
@require_auth
def api_group_member_detail(group_id, member_user_id):
    """Remove member from group or update member role"""
    user_id = session.get('user_id')
    
    # Check if user is admin of this group
    group = firestore_db.get_group(group_id)
    if not group or group.get('admin_user_id') != user_id:
        return jsonify({'success': False, 'error': 'Access denied: Only group admin can manage members'})
    
    if request.method == 'DELETE':
        try:
            success = firestore_db.remove_group_member(group_id, member_user_id)
            if success:
                return jsonify({'success': True, 'message': 'Member removed successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to remove member'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            new_role = data.get('role', 'member')
            
            success = firestore_db.update_member_role(group_id, member_user_id, new_role)
            if success:
                return jsonify({'success': True, 'message': f'Member role updated to {new_role}'})
            else:
                return jsonify({'success': False, 'error': 'Failed to update member role'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

# Project Sharing APIs
@app.route('/api/projects/<project_id>/share', methods=['GET', 'POST'])
@require_auth
def api_project_sharing(project_id):
    """Get project shares or create new share"""
    user_id = session.get('user_id')
    
    # Check if user owns this project or has admin access
    if not firestore_db.user_has_project_access(user_id, project_id, 'admin'):
        project = firestore_db.get_project(project_id)
        if not project or project.get('user_id') != user_id:
            return jsonify({'success': False, 'error': 'Access denied: You must be the project owner or have admin access'})
    
    if request.method == 'GET':
        try:
            shares = firestore_db.get_project_shares(project_id)
            return jsonify({'success': True, 'shares': shares})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    elif request.method == 'POST':
        try:
            data = request.get_json()
            share_type = data.get('type', 'user')  # 'user' or 'group'
            permission_level = data.get('permission_level', 'read')
            
            if share_type == 'user':
                target_user_id = data.get('user_id')
                if not target_user_id:
                    return jsonify({'success': False, 'error': 'User ID is required'})
                
                result = firestore_db.share_project_with_user(project_id, target_user_id, user_id, permission_level)
            
            elif share_type == 'group':
                target_group_id = data.get('group_id')
                if not target_group_id:
                    return jsonify({'success': False, 'error': 'Group ID is required'})
                
                result = firestore_db.share_project_with_group(project_id, target_group_id, user_id, permission_level)
            
            else:
                return jsonify({'success': False, 'error': 'Invalid share type'})
            
            return jsonify(result)
            
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/api/projects/<project_id>/shares/<share_id>', methods=['DELETE', 'PUT'])
@require_auth
def api_project_share_detail(project_id, share_id):
    """Remove or update a project share"""
    user_id = session.get('user_id')
    
    # Check if user owns this project
    project = firestore_db.get_project(project_id)
    if not project or project.get('user_id') != user_id:
        return jsonify({'success': False, 'error': 'Access denied: Only project owner can manage shares'})
    
    if request.method == 'DELETE':
        try:
            success = firestore_db.remove_project_share(share_id)
            if success:
                return jsonify({'success': True, 'message': 'Share removed successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to remove share'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            new_permission = data.get('permission_level', 'read')
            
            success = firestore_db.update_project_share_permission(share_id, new_permission)
            if success:
                return jsonify({'success': True, 'message': f'Permission updated to {new_permission}'})
            else:
                return jsonify({'success': False, 'error': 'Failed to update permission'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/api/projects/shared', methods=['GET'])
@require_auth
def api_get_shared_projects():
    """Get all projects shared with the current user"""
    user_id = session.get('user_id')
    
    try:
        shared_projects = firestore_db.get_shared_projects(user_id)
        return jsonify({'success': True, 'projects': shared_projects})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/videos/<path:filename>')
def serve_video(filename):
    """Serve video files"""
    try:
        normalized_filename = filename.replace('\\', '/')
        if normalized_filename.startswith('videos/'):
            normalized_filename = normalized_filename[7:]

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], normalized_filename)

        if not os.path.exists(file_path):
            return jsonify({'error': 'Video file not found'}), 404
        return send_file(file_path)
    except Exception as e:
        return jsonify({'error': f'Error serving video: {str(e)}'}), 500

# Initialize database and create app at module load time
# This ensures all module-level @app.route decorators attach to the correct app instance
init_users_table()
app =create_app()

if __name__ == '__main__':
    # When run directly, start the development server
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

