# resource_id: "4b674b08-9590-476a-ac25-a1063edcbeea"
# resource_type: "document"
# resource_name: "routes"
"""
L2 Infrastructure Routes

Routes for: Auth (L2.5), TTS (shared), Storage (L2.4), DB Admin (L2.6),
Firebase Sync (L2.7), Health/Config (L2.1)
"""

from flask import render_template, request, jsonify, redirect, url_for, flash, send_file, session
import sqlite3
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

import main
from . import l2_bp
from .firebase import clean_firebase_service, firestore_db
from .storage import storage_manager, StorageType
from .tts import ipa_tts
from .auth import require_auth, require_project_admin


# ============================================================
# L2.1 App Factory — Health & Config
# ============================================================

@l2_bp.route('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    return {'status': 'healthy', 'message': 'Phoneme Tracker Flask app is running'}, 200


@l2_bp.route('/test-audio')
def test_audio():
    """Test page for audio debugging"""
    return send_file('test_audio.html')


@l2_bp.route('/firebase-test')
def firebase_test():
    """Firebase diagnostic test page"""
    return render_template('firebase_test.html')


# ============================================================
# L2.5 Auth — Login, Registration, Logout
# ============================================================

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


def get_user_info():
    """Get authenticated user information from session"""
    from l3_users.sessions.session import get_user_info as _get_user_info
    return _get_user_info()


def is_project_owner(project_id, user_id):
    """Check if user is the owner of a project (works with both Firebase and SQLite)"""
    if clean_firebase_service.is_available():
        try:
            firebase_project = firestore_db.get_project(project_id)
            if firebase_project:
                return firebase_project.get('user_id') == user_id
        except Exception:
            pass

    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        int_project_id = int(project_id)
        cursor.execute("SELECT user_id FROM projects WHERE id = ?", (int_project_id,))
        result = cursor.fetchone()
        conn.close()
        return result and result[0] == user_id
    except (ValueError, TypeError):
        return False
    except Exception:
        return False


@l2_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login route - Firebase authentication only"""
    if 'firebase_uid' in session:
        return redirect(url_for('l7_projects.dashboard'))
    firebase_config = get_firebase_config()
    return render_template('login.html', firebase_config=firebase_config)


@l2_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registration route - Local email/password registration"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not username or not email or not password:
            flash('All fields are required', 'error')
            return render_template('login.html', firebase_config=get_firebase_config())

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('login.html', firebase_config=get_firebase_config())

        if len(password) < 6:
            flash('Password must be at least 6 characters long', 'error')
            return render_template('login.html', firebase_config=get_firebase_config())

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ? OR username = ?", (email, username))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email or username already exists', 'error')
            conn.close()
            return render_template('login.html', firebase_config=get_firebase_config())

        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        session['user_id'] = user_id
        session['username'] = username
        session['auth_method'] = 'email_password'
        flash(f'Account created successfully! Welcome, {username}!', 'success')

        if 'pending_group_invite' in session:
            invite_token = session.pop('pending_group_invite')
            return redirect(url_for('l8_teams.join_group_via_invite', invite_token=invite_token))

        return redirect(url_for('l2_infrastructure.index'))

    return render_template('login.html', firebase_config=get_firebase_config())


@l2_bp.route('/logout')
def logout():
    """Logout route"""
    session.clear()
    flash('You have been signed out successfully.', 'success')
    return redirect(url_for('l2_infrastructure.login'))


@l2_bp.route('/api/auth/firebase-login', methods=['POST'])
def firebase_login():
    """Handle Firebase authentication login"""
    try:
        data = request.get_json()
        firebase_uid = data.get('uid')
        email = data.get('email')
        display_name = data.get('displayName')

        if not firebase_uid or not email:
            return jsonify({'success': False, 'error': 'Missing required data'}), 400

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT id, username, email FROM users WHERE firebase_uid = ?", (firebase_uid,))
        user_data = cursor.fetchone()

        if user_data:
            user_id = user_data[0]
            username = user_data[1]
        else:
            cursor.execute("SELECT id, username FROM users WHERE email = ?", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                user_id = existing_user[0]
                username = existing_user[1]
                cursor.execute("UPDATE users SET firebase_uid = ? WHERE id = ?", (firebase_uid, user_id))
            else:
                username = display_name or email.split('@')[0]
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

        session['firebase_uid'] = firebase_uid
        session['user_id'] = user_id
        session['username'] = username

        return jsonify({'success': True, 'message': f'Welcome, {username}!'})

    except Exception as e:
        return jsonify({'success': False, 'error': 'Authentication failed'}), 500


@l2_bp.route('/api/auth/logout', methods=['POST'])
def api_logout():
    """API logout route for Firebase"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})


@l2_bp.route('/api/auth/email-login', methods=['POST'])
def email_login():
    """Handle email/password login"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'success': False, 'error': 'Email and password are required'}), 400

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, password_hash FROM users WHERE email = ? AND is_active = 1", (email,))
        user_data = cursor.fetchone()

        if not user_data:
            return jsonify({'success': False, 'error': 'Invalid email or password'}), 401

        user_id, username, user_email, password_hash = user_data

        if password_hash == 'firebase_user':
            return jsonify({'success': False, 'error': 'This account uses Google Sign-In.'}), 401

        if not check_password_hash(password_hash, password):
            return jsonify({'success': False, 'error': 'Invalid email or password'}), 401

        conn.close()

        session['user_id'] = user_id
        session['username'] = username
        session['email'] = user_email
        session['auth_method'] = 'email_password'

        return jsonify({'success': True, 'message': f'Welcome back, {username}!'})

    except Exception as e:
        return jsonify({'success': False, 'error': 'Login failed'}), 500


@l2_bp.route('/api/auth/email-register', methods=['POST'])
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

        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return jsonify({'success': False, 'error': 'Username already exists'}), 400

        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            return jsonify({'success': False, 'error': 'Email already registered'}), 400

        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Account created successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': 'Registration failed'}), 500


@l2_bp.route('/auth/email', methods=['POST'])
def email_auth():
    """Handle Firebase email/password authentication"""
    try:
        data = request.get_json()
        uid = data.get('uid')
        email = data.get('email', '')
        display_name = data.get('displayName', '')

        if not uid or not email:
            return jsonify({'success': False, 'error': 'Missing authentication data'}), 400

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users WHERE firebase_uid = ?", (uid,))
        existing = cursor.fetchone()

        if existing:
            session['user_id'] = existing[0]
            session['username'] = existing[1]
            session['firebase_uid'] = uid
            conn.close()
            return jsonify({'success': True, 'redirect': url_for('l7_projects.dashboard')})

        cursor.execute("SELECT id, username FROM users WHERE email = ?", (email,))
        email_user = cursor.fetchone()

        if email_user:
            cursor.execute("UPDATE users SET firebase_uid = ? WHERE id = ?", (uid, email_user[0]))
            conn.commit()
            session['user_id'] = email_user[0]
            session['username'] = email_user[1]
            session['firebase_uid'] = uid
            conn.close()
            return jsonify({'success': True, 'redirect': url_for('l7_projects.dashboard')})

        username = display_name or email.split('@')[0]
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
            VALUES (?, ?, 'firebase_user', ?)
        """, (username, email, uid))

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        session['user_id'] = user_id
        session['username'] = username
        session['firebase_uid'] = uid

        return jsonify({'success': True, 'redirect': url_for('l7_projects.dashboard')})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@l2_bp.route('/auth/google', methods=['POST'])
def google_auth():
    """Handle Google OAuth authentication"""
    try:
        data = request.get_json()
        uid = data.get('uid')
        email = data.get('email', '')
        display_name = data.get('displayName', '')

        if not uid or not email:
            return jsonify({'success': False, 'error': 'Missing authentication data'}), 400

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users WHERE firebase_uid = ?", (uid,))
        existing = cursor.fetchone()

        if existing:
            session['user_id'] = existing[0]
            session['username'] = existing[1]
            session['firebase_uid'] = uid
            conn.close()
            return jsonify({'success': True, 'redirect': url_for('l7_projects.dashboard')})

        cursor.execute("SELECT id, username FROM users WHERE email = ?", (email,))
        email_user = cursor.fetchone()

        if email_user:
            cursor.execute("UPDATE users SET firebase_uid = ? WHERE id = ?", (uid, email_user[0]))
            conn.commit()
            session['user_id'] = email_user[0]
            session['username'] = email_user[1]
            session['firebase_uid'] = uid
            conn.close()
            return jsonify({'success': True, 'redirect': url_for('l7_projects.dashboard')})

        username = display_name or email.split('@')[0]
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
            VALUES (?, ?, 'firebase_user', ?)
        """, (username, email, uid))

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        session['user_id'] = user_id
        session['username'] = username
        session['firebase_uid'] = uid

        return jsonify({'success': True, 'redirect': url_for('l7_projects.dashboard')})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# ============================================================
# L2 TTS Routes (shared infrastructure)
# ============================================================

@l2_bp.route('/api/tts/ipa', methods=['POST'])
def api_tts_ipa():
    """Generate audio from IPA text using best available TTS backend"""
    try:
        data = request.get_json()
        ipa_text = data.get('ipa', '').strip()

        if not ipa_text:
            return jsonify({'success': False, 'error': 'IPA text is required'}), 400

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


@l2_bp.route('/api/tts/phoneme', methods=['POST'])
def api_tts_phoneme():
    """Generate audio for individual phoneme"""
    try:
        data = request.get_json()
        phoneme = data.get('phoneme', '').strip()
        position = data.get('position', 'standalone')

        if not phoneme:
            return jsonify({'success': False, 'error': 'Phoneme is required'}), 400

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
                'error': 'Failed to generate phoneme audio'
            }), 500

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@l2_bp.route('/api/tts/status')
def api_tts_status():
    """Check TTS system status and capabilities"""
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
        'installation_notes': 'Azure TTS required - set AZURE_SPEECH_KEY' if not azure_available else None
    })


# ============================================================
# L2.4 Storage Routes
# ============================================================

@l2_bp.route('/api/storage/test')
@require_auth
def test_firebase_storage():
    """Test Firebase Storage connectivity"""
    if not clean_firebase_service.is_available():
        return jsonify({
            'success': False,
            'error': 'Firebase service not available',
            'storage_ready': False
        })

    bucket_available = hasattr(clean_firebase_service, 'bucket') and clean_firebase_service.bucket is not None

    return jsonify({
        'success': True,
        'message': 'Firebase Storage connectivity test',
        'storage_ready': bucket_available,
    })


@l2_bp.route('/api/migrate-project/<int:project_id>', methods=['POST'])
@require_auth
def api_migrate_project(project_id):
    """API endpoint to migrate a local project to Firebase"""
    try:
        user = get_user_info()

        if not clean_firebase_service.is_available():
            return jsonify({'success': False, 'error': 'Firebase service not available'})

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        local_project = cursor.fetchone()

        if not local_project:
            return jsonify({'success': False, 'error': 'Project not found or access denied'})

        project_name = local_project[0]

        firebase_project_data = {
            'name': project_name,
            'user_id': user['id']
        }
        firebase_project_id = firestore_db.create_project(firebase_project_data)

        if not firebase_project_id:
            return jsonify({'success': False, 'error': 'Failed to create Firebase project'})

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
                video_path = word_row[6]
                firebase_video_url = None

                if video_path and not video_path.startswith('https://') and os.path.exists(video_path):
                    filename = os.path.basename(video_path)
                    storage_path = f"videos/{user['id']}/{firebase_project_id}/{filename}"

                    with open(video_path, 'rb') as video_file:
                        video_data = video_file.read()

                    file_extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else 'mp4'
                    content_type_map = {
                        'mp4': 'video/mp4', 'avi': 'video/x-msvideo',
                        'mov': 'video/quicktime', 'mkv': 'video/x-matroska',
                        'webm': 'video/webm'
                    }
                    content_type = content_type_map.get(file_extension, 'video/mp4')

                    result = clean_firebase_service.upload_file_from_memory(
                        video_data, storage_path, content_type=content_type
                    )

                    if result and result.get('success'):
                        firebase_video_url = result.get('public_url')
                        migration_stats['videos_migrated'] += 1

                try:
                    english_words_data = json.loads(word_row[2]) if word_row[2] else []
                    if isinstance(english_words_data, str):
                        english_words_data = [english_words_data]
                    elif not isinstance(english_words_data, list):
                        english_words_data = [str(english_words_data)]
                except (json.JSONDecodeError, TypeError):
                    english_words_data = [word_row[2]] if word_row[2] else []

                word_data = {
                    'language': word_row[1],
                    'english_words': english_words_data,
                    'new_language_word': word_row[3],
                    'ipa_phonetics': word_row[4],
                    'dictionary_phonetics': word_row[5],
                    'video_path': firebase_video_url or video_path,
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

            except Exception as e:
                migration_stats['errors'].append(f"Error migrating word: {str(e)}")

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

            except Exception as e:
                migration_stats['errors'].append(f"Error migrating phoneme: {str(e)}")

        conn.close()

        return jsonify({
            'success': True,
            'message': f'Project "{project_name}" migrated successfully to Firebase',
            'firebase_project_id': firebase_project_id,
            'stats': migration_stats
        })

    except Exception as e:
        return jsonify({'success': False, 'error': f'Migration failed: {str(e)}'})


# ============================================================
# L2.6 DB Admin Routes (absorbed from L10)
# ============================================================

@l2_bp.route('/api/admin/reset-database', methods=['POST'])
@require_project_admin
def api_admin_reset_database():
    """API endpoint to reset database"""
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

        cursor.execute("SELECT name, description, template_data, phoneme_count, created_at FROM phoneme_templates")
        templates_backup = cursor.fetchall()

        cursor.execute("DELETE FROM words")
        cursor.execute("DELETE FROM phonemes")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='words'")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='phonemes'")

        conn.commit()
        conn.close()

        main.insert_sample_data()

        template_msg = f" Preserved {len(templates_backup)} phoneme templates." if templates_backup else ""
        return jsonify({'success': True, 'message': f'Database reset successfully!{template_msg}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l2_bp.route('/api/admin/reset-to-default', methods=['POST'])
@require_project_admin
def api_admin_reset_to_default():
    """Reset phonemes to default configuration (keeps words)"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM phonemes")
        main.insert_sample_data()
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Phonemes reset to default! (Words preserved)'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
