# resource_id: "1242ec4c-a00b-4157-8d04-287d691a0206"
# resource_type: "document"
# resource_name: "display"
"""
Word Display Module

Handles viewing and displaying words in various formats.
Agents can work on display enhancements without affecting creation, search, or editing.
"""

from flask import render_template, redirect, url_for, flash
import sqlite3
import json

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from services.firebase import firestore_db
from . import words_bp


@words_bp.route('/words')
@require_auth
def words_menu():
    """Words management menu - main landing page."""
    user = get_user_info()
    return render_template('words/words_menu.html', user=user)


@words_bp.route('/words/display')
@require_auth
def display_words():
    """
    Display all words for the current project or user.

    Supports both local (SQLite) and cloud (Firestore) storage.
    """
    try:
        user = get_user_info()
        current_project = user.get('current_project')

        # Handle cloud storage
        if current_project and current_project.get('storage_type') == 'cloud':
            words_data = _get_cloud_words(current_project['id'])
            return render_template('words/words_display.html', words=words_data)

        # Handle local storage
        words_data = _get_local_words(user, current_project)
        return render_template('words/words_display.html', words=words_data)

    except Exception as e:
        flash(f'Error displaying words: {str(e)}', 'error')
        return redirect(url_for('words.words_menu'))


def _get_cloud_words(project_id: str) -> list:
    """
    Retrieve words from Firestore for cloud projects.

    Args:
        project_id: Cloud project identifier

    Returns:
        List of word dictionaries
    """
    cloud_words = firestore_db.get_project_words(project_id)
    words_data = []

    for word in cloud_words:
        # Handle english_words field (can be list or string)
        english_words = word.get('english_words')
        if isinstance(english_words, list):
            english_display = ', '.join(english_words)
        elif isinstance(english_words, str):
            english_display = english_words
        else:
            english_display = ''

        words_data.append({
            'id': word.get('id'),
            'language': word.get('language') or 'Constructed Language',
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

    return words_data


def _get_local_words(user: dict, current_project: dict = None) -> list:
    """
    Retrieve words from SQLite for local projects.

    Args:
        user: User information dictionary
        current_project: Current project context (optional)

    Returns:
        List of word dictionaries
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if current_project:
        cursor.execute("""
            SELECT id, language, english_words, new_language_word, ipa_phonetics,
                   dictionary_phonetics, video_path, syllable_type, onset_phoneme,
                   onset_length_type, nucleus_phoneme, nucleus_length_type,
                   coda_phoneme, coda_length_type
            FROM words
            WHERE project_id = ?
            ORDER BY id DESC
        """, (current_project['id'],))
    else:
        # Show all words for the user, including those without project_id (legacy words)
        cursor.execute("""
            SELECT id, language, english_words, new_language_word, ipa_phonetics,
                   dictionary_phonetics, video_path, syllable_type, onset_phoneme,
                   onset_length_type, nucleus_phoneme, nucleus_length_type,
                   coda_phoneme, coda_length_type
            FROM words
            WHERE user_id = ? OR (user_id IS NULL AND project_id IS NULL)
            ORDER BY id DESC
        """, (user['id'],))

    words_data = cursor.fetchall()
    conn.close()

    # Convert to list of dictionaries
    words_list = []
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

    return words_list


__all__ = ['words_menu', 'display_words']
