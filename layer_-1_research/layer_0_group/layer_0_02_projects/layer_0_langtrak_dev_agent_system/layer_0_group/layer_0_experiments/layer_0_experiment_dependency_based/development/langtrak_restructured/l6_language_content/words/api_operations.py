# resource_id: "6b93c65d-e778-4797-b401-e3bedaf00e76"
# resource_type: "document"
# resource_name: "api_operations"
"""
Word API Operations Module

Handles API endpoints for word creation, updating, and deletion.
Agents can work on API improvements without affecting routes or display logic.

Note: Named api_operations.py to avoid conflict with existing api.py stub.
"""

from flask import request, jsonify
from werkzeug.utils import secure_filename
import sqlite3
import os
import json

from core.database import DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from services.firebase import clean_firebase_service
from src.storage_manager import storage_manager
import main
from . import words_bp


def allowed_file(filename):
    """Check if file extension is allowed for uploads."""
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@words_bp.route('/api/create-word', methods=['POST'])
def api_create_word():
    """
    API endpoint to create a word from selected phonemes.

    Accepts both form data and JSON data.

    Request Data:
        language: Language name (default: 'Constructed Language')
        english_words: English translations
        new_language_word: Word in constructed language
        syllable_type: Syllable structure (default: 'CVC')
        onset_phoneme, nucleus_phoneme, coda_phoneme: Selected phonemes
        onset_length_type, nucleus_length_type, coda_length_type: Length types
        video: Optional video file upload

    Returns:
        JSON response with success status and created word data
    """
    try:
        # Handle both form data and JSON data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Extract data from request
        language = data.get('language', 'Constructed Language')
        english_words = data.get('english_words', '')
        new_language_word = data.get('new_language_word', '')
        project_id = data.get('project_id')

        # Check for multi-syllable data (new format)
        syllables_data = None
        syllable_type = 'CVC'  # Default value

        if 'syllables' in data:
            syllables_json = data.get('syllables')
            if isinstance(syllables_json, str):
                syllables_data = json.loads(syllables_json)
            else:
                syllables_data = syllables_json

        # Build selected phonemes from syllables data OR fall back to individual form fields (backward compatibility)
        selected_phonemes = {}  # Initialize for both paths

        if syllables_data:
            # New multi-syllable format
            ipa_parts = []
            phoneme_data = {}

            # Build complete IPA from all syllables
            for syllable in syllables_data:
                for position in ['onset', 'nucleus', 'coda']:
                    if position in syllable.get('phonemes', {}):
                        phoneme_info = syllable['phonemes'][position]
                        ipa_parts.append(phoneme_info['phoneme'])

            # Use first syllable for backward compatibility fields
            if len(syllables_data) > 0 and 'phonemes' in syllables_data[0]:
                first_syllable = syllables_data[0]
                syllable_type = first_syllable.get('syllableType', 'CVC')
                phoneme_data['syllable_type'] = syllable_type

                for position in ['onset', 'nucleus', 'coda']:
                    if position in first_syllable['phonemes']:
                        phoneme_info = first_syllable['phonemes'][position]
                        phoneme_data[f'{position}_phoneme'] = phoneme_info['phoneme']
                        phoneme_data[f'{position}_length_type'] = phoneme_info.get('length_type', '')

            ipa_phonetics = ''.join(ipa_parts)
            dictionary_phonetics = ipa_phonetics

        else:
            # Old single-syllable format (backward compatibility)
            for position in ['onset', 'nucleus', 'coda']:
                phoneme_key = f'{position}_phoneme'
                length_type_key = f'{position}_length_type'
                if phoneme_key in data and data[phoneme_key]:
                    selected_phonemes[position] = {
                        'phoneme': data[phoneme_key],
                        'length_type': data.get(length_type_key, '')
                    }

            syllable_type = data.get('syllable_type', 'CVC')

            # Build IPA phonetics from selected phonemes
            ipa_parts = []
            phoneme_data = {}

            for position in ['onset', 'nucleus', 'coda']:
                if position in selected_phonemes:
                    phoneme_info = selected_phonemes[position]
                    ipa_parts.append(phoneme_info['phoneme'])

                    # Store structured phoneme data
                    phoneme_data[f'{position}_phoneme'] = phoneme_info['phoneme']
                    phoneme_data[f'{position}_length_type'] = phoneme_info['length_type']

            ipa_phonetics = ''.join(ipa_parts)
            dictionary_phonetics = ipa_phonetics  # Always sync dictionary phonetics with IPA

        # Handle video upload if provided
        video_path = None
        if 'video' in request.files:
            video_file = request.files['video']
            if video_file and video_file.filename and allowed_file(video_file.filename):
                # Create safe filename
                safe_word = "".join(c for c in new_language_word if c.isalnum() or c in (' ', '-', '_')).strip()
                if not safe_word:
                    safe_word = "word"
                filename = secure_filename(f"{safe_word}_{video_file.filename}")
                # Get upload folder from app config or use default
                upload_folder = os.path.join(os.getcwd(), 'uploads')
                os.makedirs(upload_folder, exist_ok=True)
                video_path = os.path.join(upload_folder, filename).replace('\\', '/')
                video_file.save(video_path)

        # Save to database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Set the syllable type in phoneme_data (use first syllable's type if multi-syllable)
        if 'syllable_type' not in phoneme_data and syllables_data and len(syllables_data) > 0:
            phoneme_data['syllable_type'] = syllables_data[0].get('syllableType', 'CVC')

        # Get current user
        user = get_user_info()
        user_id = user['id'] if user['is_authenticated'] else None

        # Use current project if available, otherwise use provided project_id
        current_project_id = None
        current_project = user.get('current_project')
        if current_project:
            current_project_id = current_project['id']

        # Use the structured word creation function with correct parameters
        word_id = main.add_new_word_with_structure(
            cursor, conn, language, english_words, new_language_word,
            ipa_phonetics, dictionary_phonetics, phoneme_data, video_path
        )

        # Always update the word with user_id and project_id, and save syllables_data if present
        if word_id:
            if syllables_data:
                # Save multi-syllable data
                cursor.execute("UPDATE words SET user_id = ?, project_id = ?, syllables_data = ? WHERE id = ?",
                             (user_id, current_project_id, json.dumps(syllables_data), word_id))
            else:
                # Single syllable (backward compatibility)
                cursor.execute("UPDATE words SET user_id = ?, project_id = ? WHERE id = ?",
                             (user_id, current_project_id, word_id))

        def fetch_phoneme_metadata(syl_type, pos, len_type, pho):
            cursor.execute(
                """
                SELECT group_type, subgroup_type, sub_subgroup_type, sub_sub_subgroup_type
                FROM phonemes
                WHERE syllable_type = ? AND position = ? AND length_type = ? AND phoneme = ?
                """,
                (syl_type, pos, len_type, pho),
            )
            row = cursor.fetchone()
            return {
                'syllable_type': syl_type,
                'position': pos,
                'length_type': len_type,
                'phoneme': pho,
                'group_type': row[0] if row else None,
                'subgroup_type': row[1] if row else None,
                'sub_subgroup_type': row[2] if row else None,
                'sub_sub_subgroup_type': row[3] if row else None,
                'user_id': user_id,
            }

        # Determine cloud project context (if any)
        cloud_project_id = None
        if current_project:
            if current_project.get('storage_type') == 'cloud':
                cloud_project_id = current_project.get('id')
            elif current_project.get('cloud_project_id'):
                cloud_project_id = current_project.get('cloud_project_id')

        # Update phoneme frequencies for all syllables
        if syllables_data:
            # Multi-syllable: update frequencies for all phonemes in all syllables
            for syllable in syllables_data:
                syl_type = syllable.get('syllableType', 'CVC')
                for position in ['onset', 'nucleus', 'coda']:
                    if position in syllable.get('phonemes', {}):
                        phoneme_info = syllable['phonemes'][position]
                        main.update_phoneme_frequency(
                            cursor, conn, syl_type, position,
                            phoneme_info.get('length_type', ''), phoneme_info['phoneme']
                        )
                        if cloud_project_id and clean_firebase_service.is_available():
                            record = fetch_phoneme_metadata(
                                syl_type,
                                position,
                                phoneme_info.get('length_type', ''),
                                phoneme_info['phoneme']
                            )
                            storage_manager.increment_cloud_phoneme_frequency(cloud_project_id, record)
        else:
            # Single syllable (backward compatibility)
            for position in ['onset', 'nucleus', 'coda']:
                if position in selected_phonemes:
                    phoneme_info = selected_phonemes[position]
                    main.update_phoneme_frequency(
                        cursor, conn, syllable_type, position,
                        phoneme_info['length_type'], phoneme_info['phoneme']
                    )
                    if cloud_project_id and clean_firebase_service.is_available():
                        record = fetch_phoneme_metadata(
                            syllable_type,
                            position,
                            phoneme_info['length_type'],
                            phoneme_info['phoneme']
                        )
                        storage_manager.increment_cloud_phoneme_frequency(cloud_project_id, record)

        stored_english_words = []
        if word_id:
            cursor.execute("SELECT english_words FROM words WHERE id = ?", (word_id,))
            english_row = cursor.fetchone()
            if english_row and english_row[0]:
                try:
                    stored_english_words = json.loads(english_row[0])
                except json.JSONDecodeError:
                    stored_english_words = [english_row[0]]

        conn.commit()

        cloud_word_id = None
        if word_id and cloud_project_id and clean_firebase_service.is_available():
            word_payload = {
                'language': language,
                'english_words': stored_english_words or english_words,
                'new_language_word': new_language_word,
                'ipa_phonetics': ipa_phonetics,
                'dictionary_phonetics': dictionary_phonetics,
                'syllable_type': phoneme_data.get('syllable_type', syllable_type),
                'onset_phoneme': phoneme_data.get('onset_phoneme'),
                'onset_length_type': phoneme_data.get('onset_length_type'),
                'nucleus_phoneme': phoneme_data.get('nucleus_phoneme'),
                'nucleus_length_type': phoneme_data.get('nucleus_length_type'),
                'coda_phoneme': phoneme_data.get('coda_phoneme'),
                'coda_length_type': phoneme_data.get('coda_length_type'),
                'video_path': video_path,
                'user_id': user_id,
                'source': 'api_create_word',
            }
            if syllables_data:
                word_payload['syllables_data'] = syllables_data
            cloud_word_id = storage_manager.create_cloud_word(cloud_project_id, word_payload)

        conn.close()

        response_project_id = cloud_project_id or current_project_id or project_id
        response_english_words = stored_english_words or english_words

        # Gate success on confirmed cloud write if operating in a cloud project context
        if cloud_project_id and clean_firebase_service.is_available() and not cloud_word_id:
            return jsonify({'success': False, 'error': 'Failed to create word in cloud'}), 502

        return jsonify({
            'success': True,
            'message': 'Word created successfully!',
            'word': {
                'language': language,
                'english_words': response_english_words,
                'new_language_word': new_language_word,
                'ipa_phonetics': ipa_phonetics,
                'syllable_type': syllable_type,
                'project_id': response_project_id
            }
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@words_bp.route('/api/update-word/<int:word_id>', methods=['POST'])
@require_auth
def api_update_word(word_id):
    """
    API endpoint to update an existing word.

    Args:
        word_id: ID of the word to update

    Request Data:
        language, english_words, new_language_word, ipa_phonetics, etc.
        video: Optional new video file

    Returns:
        JSON response with success status
    """
    try:
        user = get_user_info()
        # Handle both form data and JSON data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get current video path and verify ownership
        cursor.execute("SELECT video_path, project_id FROM words WHERE id = ? AND user_id = ?", (word_id, user['id']))
        current_data = cursor.fetchone()
        if not current_data:
            return jsonify({'success': False, 'error': 'Word not found or access denied'})

        current_video_path = current_data[0]
        current_project_id = current_data[1]

        # Handle video upload if provided
        video_path = current_video_path  # Keep current video by default
        if 'video' in request.files:
            video_file = request.files['video']
            if video_file and video_file.filename and allowed_file(video_file.filename):
                # Remove old video file if it exists
                if current_video_path and os.path.exists(current_video_path):
                    try:
                        os.remove(current_video_path)
                    except OSError as e:
                        print(f"Error removing old video file {current_video_path}: {e}")

                # Save new video
                safe_word = "".join(c for c in data.get('new_language_word', 'word') if c.isalnum() or c in (' ', '-', '_')).strip()
                if not safe_word:
                    safe_word = "word"
                filename = secure_filename(f"{safe_word}_{video_file.filename}")
                upload_folder = os.path.join(os.getcwd(), 'uploads')
                os.makedirs(upload_folder, exist_ok=True)
                video_path = os.path.join(upload_folder, filename).replace('\\', '/')
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

        # Update word
        cursor.execute("""
            UPDATE words SET
                language = ?,
                english_words = ?,
                new_language_word = ?,
                ipa_phonetics = ?,
                dictionary_phonetics = ?,
                video_path = ?,
                syllable_type = ?,
                onset_phoneme = ?,
                onset_length_type = ?,
                nucleus_phoneme = ?,
                nucleus_length_type = ?,
                coda_phoneme = ?,
                coda_length_type = ?,
                project_id = ?
            WHERE id = ? AND user_id = ?
        """, (
            data.get('language', 'Constructed Language'),
            data.get('english_words', ''),
            data.get('new_language_word', ''),
            ipa_phonetics,
            dictionary_phonetics,
            video_path,
            data.get('syllable_type', 'CVC'),
            data.get('onset_phoneme'),
            data.get('onset_length_type'),
            data.get('nucleus_phoneme'),
            data.get('nucleus_length_type'),
            data.get('coda_phoneme'),
            data.get('coda_length_type'),
            project_id,
            word_id,
            user['id']
        ))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Word updated successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@words_bp.route('/api/delete-word/<int:word_id>', methods=['DELETE'])
@require_auth
def api_delete_word(word_id):
    """
    API endpoint to delete a word.

    Also handles:
    - Decreasing phoneme frequency counts
    - Removing associated video files

    Args:
        word_id: ID of the word to delete

    Returns:
        JSON response with success status
    """
    try:
        user = get_user_info()
        conn = sqlite3.connect(DB_NAME)
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
        if video_path and os.path.exists(video_path):
            try:
                os.remove(video_path)
            except OSError as e:
                print(f"Error removing video file {video_path} during word deletion: {e}")

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Word deleted successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@words_bp.route('/api/remove-video/<int:word_id>', methods=['POST'])
@require_auth
def api_remove_video(word_id):
    """
    API endpoint to remove video from a word without deleting the word.

    Args:
        word_id: ID of the word

    Returns:
        JSON response with success status
    """
    try:
        user = get_user_info()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get current video path and verify ownership
        cursor.execute("SELECT video_path FROM words WHERE id = ? AND user_id = ?", (word_id, user['id']))
        result = cursor.fetchone()

        if not result:
            return jsonify({'success': False, 'error': 'Word not found or access denied'})

        video_path = result[0]

        # Delete video file if exists
        if video_path and os.path.exists(video_path):
            try:
                os.remove(video_path)
            except OSError as e:
                print(f"Error removing video file {video_path}: {e}")
                return jsonify({'success': False, 'error': f'Failed to remove video file: {e}'})

        # Update database to remove video path
        cursor.execute("UPDATE words SET video_path = NULL WHERE id = ?", (word_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Video removed successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


__all__ = ['api_create_word', 'api_update_word', 'api_delete_word', 'api_remove_video']
