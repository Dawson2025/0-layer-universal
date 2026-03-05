# resource_id: "43e5d063-bb12-4ed1-8cbe-5546d37a6c3b"
# resource_type: "document"
# resource_name: "routes"
"""
L6 Language Content — Blueprint Routes

Word display/creation pages, word deletion APIs, video removal/serving,
bulk word deletion (admin), and video path fixing (admin).
"""

from flask import (
    Blueprint, render_template, request, jsonify, redirect,
    url_for, flash, session, send_file, current_app,
)
import sqlite3
import os
import json

import main  # main.DB_NAME
from l2_infrastructure.auth import require_auth, require_project_admin
from l3_users.sessions.session import get_user_info
from l2_infrastructure.firebase import clean_firebase_service, firestore_db

l6_bp = Blueprint('l6_language_content', __name__)


# ---------------------------------------------------------------------------
# Page routes — word display / creation
# ---------------------------------------------------------------------------

@l6_bp.route('/words')
@require_auth
def words_menu():
    """Words management menu"""
    user = get_user_info()
    return render_template('words_menu.html', user=user)


@l6_bp.route('/words/display')
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


@l6_bp.route('/words/create')
@require_auth
def create_word_menu():
    """Word creation method selection"""
    return render_template('word_creation_menu.html')


@l6_bp.route('/words/add')
@require_auth
def add_word():
    """Simple (non-table) word creation UI."""
    user = get_user_info()
    return render_template('add_word.html', user=user)


@l6_bp.route('/words/create/table-based')
@require_auth
def create_word_table_based():
    """Table-based word creation (Terminal function: create_word_table_based)"""
    user = get_user_info()
    return render_template('word_creation_table.html', user=user)


# ---------------------------------------------------------------------------
# API routes — video removal
# ---------------------------------------------------------------------------

@l6_bp.route('/api/remove-video/<int:word_id>', methods=['POST'])
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


# ---------------------------------------------------------------------------
# API routes — word deletion
# ---------------------------------------------------------------------------

@l6_bp.route('/api/delete-word/<int:word_id>', methods=['DELETE'])
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


@l6_bp.route('/api/delete-word/<word_id>', methods=['DELETE'])
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


# ---------------------------------------------------------------------------
# API routes — admin: bulk word deletion
# ---------------------------------------------------------------------------

@l6_bp.route('/api/admin/bulk-delete-words', methods=['POST'])
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


# ---------------------------------------------------------------------------
# API routes — admin: fix video paths
# ---------------------------------------------------------------------------

@l6_bp.route('/api/admin/fix-video-paths', methods=['POST'])
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


# ---------------------------------------------------------------------------
# Static file serving — videos
# ---------------------------------------------------------------------------

@l6_bp.route('/videos/<path:filename>')
def serve_video(filename):
    """Serve video files"""
    try:
        normalized_filename = filename.replace('\\', '/')
        if normalized_filename.startswith('videos/'):
            normalized_filename = normalized_filename[7:]

        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], normalized_filename)

        if not os.path.exists(file_path):
            return jsonify({'error': 'Video file not found'}), 404
        return send_file(file_path)
    except Exception as e:
        return jsonify({'error': f'Error serving video: {str(e)}'}), 500
