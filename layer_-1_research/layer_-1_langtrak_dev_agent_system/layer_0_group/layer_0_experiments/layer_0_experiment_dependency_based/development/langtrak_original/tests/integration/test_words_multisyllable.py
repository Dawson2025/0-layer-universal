import json
import sqlite3

import pytest

import app as flask_app
import main
import core.database as core_database
import core.session as core_session
import core.decorators as core_decorators
import features.words.api_operations as word_api
from src import tts_ipa


@pytest.fixture()
def app_client(tmp_path, monkeypatch):
    """Provide a Flask test client backed by an isolated SQLite database."""

    db_path = tmp_path / 'test.db'
    db_str = str(db_path)

    # Point every layer at the temporary database
    for module in (main, core_database, word_api):
        if hasattr(module, 'DB_NAME'):
            monkeypatch.setattr(module, 'DB_NAME', db_str, raising=False)

    # Avoid external dependencies and ensure deterministic behaviour
    monkeypatch.setattr(word_api.clean_firebase_service, 'is_available', lambda: False)
    monkeypatch.setattr(tts_ipa.ipa_tts, 'azure_available', False)
    monkeypatch.setattr(tts_ipa.ipa_tts, 'fake_enabled', True)
    monkeypatch.setenv('FORCE_FAKE_TTS', '1')

    # Ensure uploads land in an isolated folder within the tmp path
    uploads_dir = tmp_path / 'uploads'
    uploads_dir.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(word_api.os, 'getcwd', lambda: str(tmp_path))

    # Initialise schema
    main.migrate_schema()
    flask_app.init_users_table()

    # Seed user, project, and baseline phonemes
    conn = sqlite3.connect(db_str)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, password_hash, is_active) VALUES (?, ?, ?, 1)",
        ('tester', 'tester@example.com', 'hash')
    )
    user_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO projects (name, user_id) VALUES (?, ?)",
        ('Test Project', user_id)
    )
    project_id = cursor.lastrowid

    phoneme_rows = [
        ('CVC', 'onset', 'single_consonants', 'grp', 'sub', 'm', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', 'grp', 'sub', 'a', user_id, project_id),
        ('CVC', 'coda', 'single_consonants', 'grp', 'sub', 't', user_id, project_id),
        ('CVC', 'onset', 'single_consonants', 'grp', 'sub', 'n', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', 'grp', 'sub', 'o', user_id, project_id),
        ('CVC', 'coda', 'single_consonants', 'grp', 'sub', 'd', user_id, project_id),
    ]
    cursor.executemany(
        """
        INSERT INTO phonemes (syllable_type, position, length_type, group_type, subgroup_type, phoneme, user_id, project_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        phoneme_rows
    )
    conn.commit()
    conn.close()

    user_info = {
        'id': user_id,
        'name': 'tester',
        'email': 'tester@example.com',
        'roles': '',
        'is_authenticated': True,
        'current_project': {
            'id': project_id,
            'name': 'Test Project',
            'storage_type': 'local',
            'cloud_project_id': None,
        },
    }

    monkeypatch.setattr(core_session, 'get_user_info', lambda: user_info)
    monkeypatch.setattr(word_api, 'get_user_info', lambda: user_info)
    monkeypatch.setattr(core_decorators, 'get_user_info', lambda: user_info)
    monkeypatch.setattr(flask_app, 'get_user_info', lambda: user_info)
    monkeypatch.setattr(word_api.storage_manager, 'increment_cloud_phoneme_frequency', lambda *args, **kwargs: None)

    flask_app.app.config['TESTING'] = True

    with flask_app.app.test_client() as client:
        with client.session_transaction() as sess:
            sess['user_id'] = user_id
            sess['current_project_id'] = project_id
        yield client, db_str, uploads_dir, user_id, project_id


def test_api_create_word_multi_syllable_persists_structure(app_client):
    client, db_path, _, _user_id, _project_id = app_client

    payload = {
        'language': 'Test Tongue',
        'english_words': json.dumps(['alpha', 'beta']),
        'new_language_word': 'multitest',
        'project_id': 1,
        'syllables': [
            {
                'syllableType': 'CVC',
                'phonemes': {
                    'onset': {'phoneme': 'm', 'length_type': 'single_consonants'},
                    'nucleus': {'phoneme': 'a', 'length_type': 'monophthongs'},
                    'coda': {'phoneme': 't', 'length_type': 'single_consonants'},
                },
            },
            {
                'syllableType': 'CVC',
                'phonemes': {
                    'onset': {'phoneme': 'n', 'length_type': 'single_consonants'},
                    'nucleus': {'phoneme': 'o', 'length_type': 'monophthongs'},
                    'coda': {'phoneme': 'd', 'length_type': 'single_consonants'},
                },
            },
        ],
    }

    response = client.post('/api/create-word', json=payload)
    data = response.get_json()
    assert response.status_code == 200
    assert data['success'] is True

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT syllables_data, syllable_type, onset_phoneme, nucleus_phoneme, coda_phoneme FROM words WHERE new_language_word = ?", ('multitest',))
    row = cursor.fetchone()
    conn.close()

    assert row is not None
    stored_syllables = json.loads(row[0])
    assert len(stored_syllables) == 2
    assert stored_syllables[0]['phonemes']['onset']['phoneme'] == 'm'
    assert stored_syllables[1]['phonemes']['coda']['phoneme'] == 'd'
    assert row[1] == 'CVC'
    assert row[2] == 'm'
    assert row[3] == 'a'
    assert row[4] == 't'


def test_tts_preview_per_syllable(app_client, monkeypatch):
    client, _, _, _user_id, _project_id = app_client
    monkeypatch.setattr(tts_ipa.ipa_tts, 'generate_ipa_audio', lambda ipa: 'ZmFrZUF1ZGlv')

    syllables = ['ma', 'nod']
    for ipa in syllables:
        response = client.post('/api/tts/ipa', json={'ipa': ipa})
        data = response.get_json()
        assert response.status_code == 200
        assert data['success'] is True

    combined = ''.join(syllables)
    response = client.post('/api/tts/ipa', json={'ipa': combined})
    data = response.get_json()
    assert response.status_code == 200
    assert data['success'] is True


def test_remove_video_endpoint_clears_video_path(app_client):
    client, db_path, uploads_dir, user_id, project_id = app_client

    video_file = uploads_dir / 'demo.mp4'
    video_file.write_bytes(b'fake video content')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO words (language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics, syllable_type, onset_phoneme, onset_length_type, nucleus_phoneme, nucleus_length_type, coda_phoneme, coda_length_type, video_path, user_id, project_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            'Media Lang',
            json.dumps(['video']),
            'video-word',
            'video',
            'video',
            'CVC',
            'm',
            'single_consonants',
            'a',
            'monophthongs',
            't',
            'single_consonants',
            str(video_file),
            user_id,
            project_id,
        ),
    )
    word_id = cursor.lastrowid
    conn.commit()
    conn.close()

    response = client.post(f'/api/remove-video/{word_id}')
    data = response.get_json()
    assert response.status_code == 200
    assert data['success'] is True

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT video_path FROM words WHERE id = ?", (word_id,))
    stored_path = cursor.fetchone()[0]
    conn.close()

    assert stored_path is None
    assert not video_file.exists()
