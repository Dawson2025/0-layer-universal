# resource_id: "5154d194-6f40-4314-9c70-1efeae0c46e4"
# resource_type: "document"
# resource_name: "api_routes"
from flask import Blueprint, request, jsonify, session, url_for, redirect, flash
import sqlite3
import os
import json
from datetime import datetime
import main
from services.firebase import clean_firebase_service, firestore_db
from core.session import get_user_info
from core.decorators import require_auth

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/languages')
@require_auth
def get_languages():
    """API endpoint to get existing languages for the current user/project"""
    try:
        user = get_user_info()
        
        # Check if we're in a project context
        if 'current_project_id' not in session:
            return jsonify({
                'success': False,
                'error': 'Please enter a project to view languages'
            })
        
        project_id = session['current_project_id']
        languages = []
        
        # Check if it's a Firebase project first
        if clean_firebase_service.is_available():
            try:
                firebase_project = firestore_db.get_project(project_id)
                if firebase_project:
                    # Get words from Firebase and extract unique languages
                    firebase_words = firestore_db.get_project_words(project_id)
                    language_set = set()
                    for word in firebase_words:
                        language = word.get('language')
                        if language and language.strip():
                            language_set.add(language)
                    
                    languages = sorted(list(language_set))
                    
                    return jsonify({
                        'success': True,
                        'languages': languages
                    })
            except Exception as e:
                print(f"Error getting Firebase languages: {e}")
        
        # Fallback to SQLite for local projects
        try:
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            
            int_project_id = int(project_id)
            cursor.execute("""
                SELECT DISTINCT language 
                FROM words 
                WHERE language IS NOT NULL AND language != '' 
                AND project_id = ?
                ORDER BY language
            """, (int_project_id,))
            
            languages = [row[0] for row in cursor.fetchall()]
            conn.close()
        except (ValueError, TypeError):
            # Not a valid integer project_id
            languages = []
        return jsonify({
            'success': True,
            'languages': languages
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error loading languages: {str(e)}'
        })

@api_bp.route('/last-language')
@require_auth
def get_last_language():
    """API endpoint to get the last used language for the current user/project"""
    try:
        user = get_user_info()
        
        # Check if we're in a project context
        if 'current_project_id' not in session:
            return jsonify({
                'success': False,
                'error': 'Please enter a project to get language',
                'last_language': 'Constructed Language'
            })
        
        project_id = session['current_project_id']
        last_language = 'Constructed Language'
        
        # Check if it's a Firebase project first
        if clean_firebase_service.is_available():
            try:
                firebase_project = firestore_db.get_project(project_id)
                if firebase_project:
                    # Get most recent word from Firebase 
                    firebase_words = firestore_db.get_project_words(project_id)
                    if firebase_words:
                        # Sort by created_at if available, otherwise just use the first
                        try:
                            firebase_words.sort(key=lambda w: w.get('created_at', ''), reverse=True)
                        except:
                            pass
                        
                        for word in firebase_words:
                            language = word.get('language')
                            if language and language.strip():
                                last_language = language
                                break
                    
                    # If no language found, use project name as default
                    if last_language == 'Constructed Language':
                        last_language = firebase_project.get('name', 'Constructed Language')
                    
                    return jsonify({
                        'success': True,
                        'last_language': last_language
                    })
            except Exception as e:
                print(f"Error getting Firebase last language: {e}")
        
        # Fallback to SQLite for local projects
        try:
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            
            int_project_id = int(project_id)
            cursor.execute("""
                SELECT language 
                FROM words 
                WHERE language IS NOT NULL AND language != '' 
                AND project_id = ?
                ORDER BY id DESC
                LIMIT 1
            """, (int_project_id,))
            
            result = cursor.fetchone()
            if result:
                last_language = result[0]
            conn.close()
        except (ValueError, TypeError):
            # Not a valid integer project_id
            pass
        return jsonify({
            'success': True,
            'last_language': last_language
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error loading last language: {str(e)}',
            'last_language': 'Constructed Language'
        })

@api_bp.route('/suggestions')
@require_auth
def get_word_suggestions():
    """API endpoint to get word suggestions based on selected phonemes"""
    try:
        # Get parameters from request
        syllable_type = request.args.get('syllable_type', 'CVC')
        onset = request.args.get('onset', '')
        nucleus = request.args.get('nucleus', '')
        coda = request.args.get('coda', '')
        
        # Check if we have all required phonemes
        if not onset or not nucleus:
            return jsonify({
                'success': False,
                'error': 'Missing required phonemes',
                'suggestions': []
            })
        
        if syllable_type == 'CVC' and not coda:
            return jsonify({
                'success': False,
                'error': 'Coda phoneme required for CVC syllables',
                'suggestions': []
            })
        
        # Check if we're in a project context
        if 'current_project_id' not in session:
            return jsonify({
                'success': False,
                'error': 'Please enter a project to get suggestions',
                'suggestions': []
            })
        
        project_id = session['current_project_id']
        
        # Define positions based on syllable type
        positions = ['onset', 'nucleus'] if syllable_type == 'CV' else ['onset', 'nucleus', 'coda']
        
        # Build position mappings based on current project
        position_mappings = {}
        
        # Check if it's a Firebase project first
        if clean_firebase_service.is_available():
            try:
                firebase_project = firestore_db.get_project(project_id)
                if firebase_project:
                    # Get phonemes from Firebase for each position
                    for position in positions:
                        firebase_phonemes = firestore_db.get_project_phonemes(
                            project_id, syllable_type, position
                        )
                        
                        # Build position mapping
                        position_mappings[position] = {}
                        for i, phoneme_doc in enumerate(firebase_phonemes, 1):
                            position_mappings[position][i] = {
                                'phoneme': phoneme_doc.get('phoneme', ''),
                                'length_type': phoneme_doc.get('length_type', ''),
                                'group_type': phoneme_doc.get('group_type', ''),
                                'subgroup_type': phoneme_doc.get('subgroup_type', ''),
                                'frequency': phoneme_doc.get('frequency', 0)
                            }
                    
                    # Use Firebase phonemes for suggestions
                    use_firebase = True
                else:
                    use_firebase = False
            except Exception as e:
                print(f"Error getting Firebase phonemes for suggestions: {e}")
                use_firebase = False
        else:
            use_firebase = False
        
        if not use_firebase:
            # Fallback to SQLite - build position mappings from local phonemes
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            
            for position in positions:
                cursor.execute("""
                    SELECT phoneme, length_type, group_type, subgroup_type, frequency
                    FROM phonemes 
                    WHERE syllable_type = ? AND position = ?
                    ORDER BY frequency ASC, phoneme
                """, (syllable_type, position))
                
                phoneme_rows = cursor.fetchall()
                position_mappings[position] = {}
                
                for i, row in enumerate(phoneme_rows, 1):
                    position_mappings[position][i] = {
                        'phoneme': row[0],
                        'length_type': row[1],
                        'group_type': row[2],
                        'subgroup_type': row[3],
                        'frequency': row[4]
                    }
            
            conn.close()
        
        # Generate suggestions using the main.py function
        all_suggestions = main.generate_phoneme_suggestions(position_mappings, positions, max_suggestions=500)
        
        # Filter for conflicts 
        suggestions, conflicting_suggestions = main.filter_suggestions_for_conflicts(
            all_suggestions, positions, position_mappings
        )
        
        # Convert suggestions to the format expected by the frontend
        formatted_suggestions = []
        for suggestion in suggestions[:15]:  # Limit to first 15 like the terminal interface
            # Build IPA and phoneme details
            ipa_parts = []
            phoneme_details = []
            valid_suggestion = True
            
            for i, position in enumerate(positions):
                number = suggestion[i]
                if number in position_mappings[position]:
                    data = position_mappings[position][number]
                    ipa_parts.append(data['phoneme'])
                    phoneme_details.append({
                        'position': position,
                        'phoneme': data['phoneme'],
                        'frequency': data['frequency']
                    })
                else:
                    valid_suggestion = False
                    break
            
            if valid_suggestion:
                formatted_suggestions.append({
                    'numbers': suggestion,
                    'ipa': ''.join(ipa_parts),
                    'phonemes': phoneme_details
                })
        
        return jsonify({
            'success': True,
            'suggestions': formatted_suggestions,
            'total_available': len(suggestions),
            'conflicts_filtered': len(conflicting_suggestions)
        })
    
    except Exception as e:
        print(f"Error generating word suggestions: {e}")
        return jsonify({
            'success': False,
            'error': f'Error generating suggestions: {str(e)}',
            'suggestions': []
        })

@api_bp.route('/phoneme-tables')
def get_phoneme_tables():
    """API endpoint to get phoneme tables for word creation"""
    try:
        syllable_type = request.args.get('syllable_type', 'CVC')
        positions = request.args.get('positions', 'onset,nucleus,coda').split(',')

        # Define length types for each position
        length_types = {
            "onset": ["single_consonants", "cluster2", "cluster3"],
            "nucleus": ["monophthongs", "diphthongs"],
            "coda": ["single_consonants", "cluster2", "cluster3"]
        }

        # Get filters from request or use defaults
        filters = {}
        for position in positions:
            filter_key = f"{position}_filter"

            # Set appropriate defaults based on position
            if position == 'nucleus':
                default_filter = 'monophthongs'
            else:  # onset or coda
                default_filter = 'single_consonants'

            filters[position] = request.args.get(filter_key, default_filter)

        # Check if we're in a project context and if it's a Firebase project
        project_id = session.get('current_project_id')
        use_firebase = False
        
        if project_id and clean_firebase_service.is_available():
            try:
                firebase_project = firestore_db.get_project(project_id)
                if firebase_project:
                    use_firebase = True
                    print(f"DEBUG: Using Firebase phonemes for project {project_id}")
            except Exception as e:
                print(f"Error checking Firebase project: {e}")
        
        tables_data = {}
        available_options = {}

        if use_firebase:
            # Get phonemes from Firebase
            for position in positions:
                # Initialize position data
                tables_data[position] = []
                available_options[position] = {
                    'length_types': length_types.get(position, []),
                    'phonemes_by_length': {}
                }

                # Get Firebase phonemes for this position and current filter
                print(f"DEBUG: Getting Firebase phonemes for project {project_id}, syllable_type {syllable_type}, position {position}")
                firebase_phonemes = firestore_db.get_project_phonemes(
                    project_id, syllable_type, position
                )
                print(f"DEBUG: Retrieved {len(firebase_phonemes)} phonemes for {position}")
                
                # Filter by length_type and sort
                filtered_phonemes = [
                    p for p in firebase_phonemes 
                    if p.get('length_type') == filters[position]
                ]
                filtered_phonemes.sort(key=lambda p: (p.get('frequency', 0), p.get('phoneme', '')))
                
                # Process Firebase phonemes for current filter
                for i, phoneme_doc in enumerate(filtered_phonemes, 1):
                    try:
                        phoneme_entry = {
                            'number': i,
                            'phoneme': str(phoneme_doc.get('phoneme', '')),
                            'length_type': str(phoneme_doc.get('length_type', '')),
                            'group_type': str(phoneme_doc.get('group_type', '')),
                            'subgroup_type': str(phoneme_doc.get('subgroup_type', '')),
                            'sub_subgroup_type': str(phoneme_doc.get('sub_subgroup_type', '')),
                            'sub_sub_subgroup_type': str(phoneme_doc.get('sub_sub_subgroup_type', '')),
                            'frequency': int(phoneme_doc.get('frequency', 0))
                        }
                        tables_data[position].append(phoneme_entry)
                    except (TypeError, ValueError) as e:
                        print(f"Error processing Firebase phoneme {i} for position {position}: {e}")
                        continue

                # Get all Firebase phonemes for this position (for all length types) to populate available_options
                all_position_phonemes = [
                    p for p in firebase_phonemes
                    if p.get('syllable_type') == syllable_type and p.get('position') == position
                ]
                
                for len_type in length_types.get(position, []):
                    phonemes_for_len_type = [
                        {
                            'phoneme': str(p.get('phoneme', '')),
                            'group_type': str(p.get('group_type', '')),
                            'subgroup_type': str(p.get('subgroup_type', '')),
                            'sub_subgroup_type': str(p.get('sub_subgroup_type', '')),
                            'sub_sub_subgroup_type': str(p.get('sub_sub_subgroup_type', ''))
                        }
                        for p in all_position_phonemes
                        if p.get('length_type') == len_type
                    ]
                    available_options[position]['phonemes_by_length'][len_type] = phonemes_for_len_type
        else:
            # Get phonemes from SQLite (original logic)
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            
            for position in positions:
                # Initialize position data
                tables_data[position] = []
                available_options[position] = {
                    'length_types': length_types.get(position, []),
                    'phonemes_by_length': {}
                }

                # Get phonemes for this position and current filter
                cursor.execute("""
                    SELECT phoneme, length_type, group_type, subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, frequency
                    FROM phonemes 
                    WHERE syllable_type = ? AND position = ? AND length_type = ?
                    ORDER BY frequency ASC, phoneme
                """, (syllable_type, position, filters[position]))

                phoneme_rows = cursor.fetchall()

                # Process phonemes for current filter
                for i, row in enumerate(phoneme_rows, 1):
                    try:
                        if row and len(row) >= 7:  # Ensure row exists and has all expected columns (including 4th level)
                            phoneme_entry = {
                                'number': i,
                                'phoneme': str(row[0]) if row[0] is not None else '',
                                'length_type': str(row[1]) if row[1] is not None else '',
                                'group_type': str(row[2]) if row[2] is not None else '',
                                'subgroup_type': str(row[3]) if row[3] is not None else '',
                                'sub_subgroup_type': str(row[4]) if row[4] is not None else '',
                                'sub_sub_subgroup_type': str(row[5]) if row[5] is not None else '',
                                'frequency': int(row[6]) if row[6] is not None else 0
                            }
                            tables_data[position].append(phoneme_entry)
                    except (IndexError, TypeError, ValueError) as e:
                        print(f"Error processing phoneme row {i} for position {position}: {e}")
                        print(f"Row data: {row}")
                        continue

                # Get all phonemes for this position (for all length types) to populate available_options
                for len_type in length_types.get(position, []):
                    cursor.execute("""
                        SELECT phoneme, group_type, subgroup_type, sub_subgroup_type, sub_sub_subgroup_type
                        FROM phonemes 
                        WHERE syllable_type = ? AND position = ? AND length_type = ?
                        ORDER BY phoneme
                    """, (syllable_type, position, len_type))

                    len_type_rows = cursor.fetchall()
                    phonemes_for_len_type = []

                    for row in len_type_rows:
                        try:
                            if row and len(row) >= 5:  # Updated to include 4th level
                                phoneme_option = {
                                    'phoneme': str(row[0]) if row[0] is not None else '',
                                    'group_type': str(row[1]) if row[1] is not None else '',
                                    'subgroup_type': str(row[2]) if row[2] is not None else '',
                                    'sub_subgroup_type': str(row[3]) if row[3] is not None else '',
                                    'sub_sub_subgroup_type': str(row[4]) if row[4] is not None else ''
                                }
                                phonemes_for_len_type.append(phoneme_option)
                        except (IndexError, TypeError) as e:
                            print(f"Error processing available option for {position} {len_type}: {e}")
                            continue

                    available_options[position]['phonemes_by_length'][len_type] = phonemes_for_len_type

            conn.close()

        # Get English words for conflict detection
        try:
            english_words = list(main.get_common_english_words_ipa())
        except Exception as e:
            print(f"Warning: Could not load English words: {e}")
            english_words = []

        return jsonify({
            'success': True,
            'tables': tables_data,
            'syllable_type': syllable_type,
            'positions': positions,
            'filters': filters,
            'english_words': english_words,
            'available_options': available_options
        })

    except Exception as e:
        print(f"Error in get_phoneme_tables: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False, 
            'error': f'Error loading phoneme tables: {str(e)}'
        })