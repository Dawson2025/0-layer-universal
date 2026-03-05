# resource_id: "e12b7b2b-c40b-497f-9bdc-364f214025c6"
# resource_type: "document"
# resource_name: "search"
"""
Word Search Module

Handles word lookup and search functionality.
Agents can work on search improvements without affecting creation, display, or editing.
"""

from flask import render_template, request, jsonify
import sqlite3

from core.database import DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from . import words_bp


@words_bp.route('/words/lookup')
@require_auth
def lookup_word():
    """Word lookup interface - search form."""
    user = get_user_info()
    return render_template('words/word_lookup.html', user=user)


@words_bp.route('/api/lookup-word')
@require_auth
def api_lookup_word():
    """
    API endpoint for word lookup/search.

    Supports multiple search types:
    - english: Search English translations
    - new_language: Search constructed language words
    - ipa: Search IPA phonetics
    - dictionary: Search dictionary phonetics
    - all: Search all fields

    Query Parameters:
        type: Search type (default: 'english')
        term: Search term (required)
        project_id: Optional project filter

    Returns:
        JSON with search results
    """
    search_type = request.args.get('type', 'english')
    search_term = request.args.get('term', '').strip()
    project_id = request.args.get('project_id')

    if not search_term:
        return jsonify({'success': False, 'error': 'Search term is required'})

    try:
        user = get_user_info()
        results = _search_words(user, search_type, search_term, project_id)

        return jsonify({
            'success': True,
            'results': results,
            'count': len(results),
            'search_type': search_type,
            'search_term': search_term,
            'project_id': project_id
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


def _search_words(user: dict, search_type: str, search_term: str, project_id: str = None) -> list:
    """
    Search words based on type and term.

    Args:
        user: User information dictionary
        search_type: Type of search (english, new_language, ipa, dictionary, all)
        search_term: Term to search for
        project_id: Optional project filter

    Returns:
        List of matching word dictionaries
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Build base query based on project context
    current_project = user.get('current_project')
    if current_project:
        # All participants in a shared project can see all words in that project
        query = """
            SELECT id, language, english_words, new_language_word, ipa_phonetics,
                   dictionary_phonetics, video_path, syllable_type, project_id
            FROM words
            WHERE project_id = ?
        """
        params = [current_project['id']]
    elif project_id:
        # Searching specific project
        query = """
            SELECT id, language, english_words, new_language_word, ipa_phonetics,
                   dictionary_phonetics, video_path, syllable_type, project_id
            FROM words
            WHERE project_id = ?
        """
        params = [project_id]
    else:
        # No project context: show only user's words
        query = """
            SELECT id, language, english_words, new_language_word, ipa_phonetics,
                   dictionary_phonetics, video_path, syllable_type, project_id
            FROM words
            WHERE user_id = ?
        """
        params = [user['id']]

    # Add search term condition based on type
    like_term = f'%{search_term}%'

    if search_type == 'english':
        query += "AND english_words LIKE ? COLLATE NOCASE "
        params.append(like_term)
    elif search_type == 'new_language':
        query += "AND new_language_word LIKE ? COLLATE NOCASE "
        params.append(like_term)
    elif search_type == 'ipa':
        query += "AND ipa_phonetics LIKE ? COLLATE NOCASE "
        params.append(like_term)
    elif search_type == 'dictionary':
        query += "AND dictionary_phonetics LIKE ? COLLATE NOCASE "
        params.append(like_term)
    elif search_type == 'all':
        # Search across all fields
        query += (
            "AND ("
            "english_words LIKE ? COLLATE NOCASE OR "
            "new_language_word LIKE ? COLLATE NOCASE OR "
            "ipa_phonetics LIKE ? COLLATE NOCASE OR "
            "dictionary_phonetics LIKE ? COLLATE NOCASE OR "
            "language LIKE ? COLLATE NOCASE"
            ") "
        )
        params.extend([like_term] * 5)

    query += "ORDER BY id DESC"

    cursor.execute(query, tuple(params))
    results = cursor.fetchall()
    conn.close()

    # Convert to list of dictionaries
    words_list = []
    for word in results:
        words_list.append({
            'id': word[0],
            'language': word[1],
            'english_words': word[2],
            'new_language_word': word[3],
            'ipa_phonetics': word[4],
            'dictionary_phonetics': word[5],
            'video_path': word[6],
            'syllable_type': word[7],
            'project_id': word[8]
        })

    return words_list


__all__ = ['lookup_word', 'api_lookup_word']
