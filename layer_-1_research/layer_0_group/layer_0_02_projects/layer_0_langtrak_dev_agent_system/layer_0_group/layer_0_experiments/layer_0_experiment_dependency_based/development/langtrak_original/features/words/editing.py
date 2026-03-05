# resource_id: "c9e8743f-f5d5-420d-8ab2-6c6a4d811766"
# resource_type: "document"
# resource_name: "editing"
"""
Word Editing Module

Handles word editing, updating, and deletion.
Agents can work on editing improvements without affecting creation, display, or search.
"""

from flask import render_template, redirect, url_for, flash
import sqlite3

from core.database import DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from . import words_bp


@words_bp.route('/words/edit/<int:word_id>')
@require_auth
def edit_word(word_id):
    """
    Display word editing form.

    Args:
        word_id: ID of the word to edit

    Returns:
        Rendered edit form or redirect on error
    """
    try:
        user = get_user_info()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, language, english_words, new_language_word, ipa_phonetics,
                   dictionary_phonetics, video_path, syllable_type, onset_phoneme,
                   onset_length_type, nucleus_phoneme, nucleus_length_type,
                   coda_phoneme, coda_length_type, project_id
            FROM words WHERE id = ? AND user_id = ?
        """, (word_id, user['id']))

        word = cursor.fetchone()
        conn.close()

        if not word:
            flash('Word not found', 'error')
            return redirect(url_for('words.display_words'))

        word_data = {
            'id': word[0],
            'language': word[1],
            'english_words': word[2],
            'new_language_word': word[3],
            'ipa_phonetics': word[4],
            'dictionary_phonetics': word[5],
            'video_path': word[6],
            'syllable_type': word[7],
            'onset_phoneme': word[8],
            'onset_length_type': word[9],
            'nucleus_phoneme': word[10],
            'nucleus_length_type': word[11],
            'coda_phoneme': word[12],
            'coda_length_type': word[13],
            'project_id': word[14]
        }

        return render_template('words/word_edit.html', word=word_data)

    except Exception as e:
        flash(f'Error loading word: {str(e)}', 'error')
        return redirect(url_for('words.display_words'))


__all__ = ['edit_word']
