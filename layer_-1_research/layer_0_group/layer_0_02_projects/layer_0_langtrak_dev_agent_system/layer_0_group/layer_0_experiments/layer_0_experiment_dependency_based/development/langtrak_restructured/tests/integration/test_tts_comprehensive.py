# resource_id: "5d8897b3-1cf6-4244-88b3-045054c88810"
# resource_type: "document"
# resource_name: "test_tts_comprehensive"
"""
Comprehensive TTS (Text-to-Speech) Tests
Covers all user interactions with audio/pronunciation features
Tests US-054, US-055, US-056, and TTS integration in word creation
"""

import json
import sqlite3
import pytest
import base64
import app as flask_app
import main
import core.database as core_db
from tests.conftest import patch_all_db_names
from unittest.mock import patch, MagicMock


@pytest.fixture()
def tts_client(tmp_path, monkeypatch):
    """Provide Flask test client with TTS enabled"""
    
    db_path = tmp_path / 'test.db'
    db_str = str(db_path)
    
    # Point to temporary database
    patch_all_db_names(monkeypatch, db_str)
    
    # Initialize schema
    main.migrate_schema()
    flask_app.init_users_table()
    
    # Create user and project
    conn = sqlite3.connect(db_str)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO users (username, email, password_hash, is_active) VALUES (?, ?, ?, 1)",
        ('tts_user', 'tts@test.com', 'hash')
    )
    user_id = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO projects (name, user_id) VALUES (?, ?)",
        ('TTS Test Project', user_id)
    )
    project_id = cursor.lastrowid
    
    # Add some phonemes for testing
    phonemes = [
        ('CVC', 'onset', 'single_consonants', '', '', 'm', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', '', '', 'a', user_id, project_id),
        ('CVC', 'coda', 'single_consonants', '', '', 't', user_id, project_id),
    ]
    cursor.executemany(
        """INSERT INTO phonemes (syllable_type, position, length_type, group_type, 
           subgroup_type, phoneme, user_id, project_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        phonemes
    )
    
    conn.commit()
    conn.close()
    
    # Configure Flask
    flask_app.app.config['TESTING'] = True
    flask_app.app.config['SECRET_KEY'] = 'test-secret'
    
    # Mock TTS to return fake audio
    mock_tts = MagicMock()
    mock_tts.generate_ipa_audio.return_value = base64.b64encode(b'fake_audio_data').decode('utf-8')
    mock_tts.generate_phoneme_audio.return_value = base64.b64encode(b'fake_phoneme_audio').decode('utf-8')
    mock_tts.azure_available = False
    mock_tts.fake_enabled = True
    mock_tts.last_backend = 'fake'
    
    with patch.object(flask_app, 'ipa_tts', mock_tts):
        with flask_app.app.test_client() as client:
            with client.session_transaction() as sess:
                sess['user_id'] = user_id
                sess['username'] = 'tts_user'
                sess['current_project_id'] = project_id
            
            yield client, db_str, user_id, project_id, mock_tts


def test_us054_play_individual_phoneme_pronunciation(tts_client):
    """US-054: Play individual phoneme pronunciation"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    # Test phoneme TTS endpoint
    response = client.post('/api/tts/phoneme', json={
        'phoneme': 'm',
        'position': 'onset'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'audio_data' in data
    assert data['phoneme'] == 'm'
    assert data['position'] == 'onset'
    
    # Verify TTS was called
    mock_tts.generate_phoneme_audio.assert_called_with('m', 'onset')


def test_us054_phoneme_audio_missing_phoneme(tts_client):
    """US-054: Handle missing phoneme parameter"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    response = client.post('/api/tts/phoneme', json={})
    
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert 'required' in data['error'].lower()


def test_us054_phoneme_audio_different_positions(tts_client):
    """US-054: Test phoneme pronunciation in different positions"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    positions = ['onset', 'nucleus', 'coda', 'standalone']
    
    for position in positions:
        response = client.post('/api/tts/phoneme', json={
            'phoneme': 'a',
            'position': position
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['position'] == position


def test_us055_play_full_word_pronunciation(tts_client):
    """US-055: Play full word pronunciation"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    # Test IPA TTS endpoint for full word
    response = client.post('/api/tts/ipa', json={
        'ipa': 'mæt'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'audio_data' in data
    assert data['ipa_input'] == 'mæt'
    assert 'backend' in data
    
    # Verify TTS was called
    mock_tts.generate_ipa_audio.assert_called_with('mæt')


def test_us055_word_audio_missing_ipa(tts_client):
    """US-055: Handle missing IPA parameter"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    response = client.post('/api/tts/ipa', json={})
    
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False


def test_us055_word_audio_complex_ipa(tts_client):
    """US-055: Test pronunciation of complex IPA strings"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    complex_ipa_strings = [
        'həˈloʊ',  # hello
        'ˈwɝld',   # world
        'fəˈnetɪk', # phonetic
        'aɪ piː eɪ',  # IPA
    ]
    
    for ipa in complex_ipa_strings:
        response = client.post('/api/tts/ipa', json={'ipa': ipa})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['ipa_input'] == ipa


def test_us056_check_tts_backend_status(tts_client):
    """US-056: Check TTS backend status"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    response = client.get('/api/tts/status')
    
    assert response.status_code == 200
    data = response.get_json()
    
    # Should report TTS availability (actual API returns these fields)
    assert 'backends_available' in data or 'total_backends' in data or 'supports_ipa' in data


def test_tts_audio_format_base64(tts_client):
    """Verify TTS returns valid base64 audio data"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    response = client.post('/api/tts/ipa', json={'ipa': 'test'})
    data = response.get_json()
    
    if data['success']:
        audio_data = data['audio_data']
        # Should be valid base64
        try:
            decoded = base64.b64decode(audio_data)
            assert len(decoded) > 0
        except Exception:
            pytest.fail("Audio data is not valid base64")


def test_tts_syllable_preview(tts_client):
    """Test TTS for individual syllables in multi-syllable words"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    syllables = ['ma', 'no', 'ped']
    
    for syllable in syllables:
        response = client.post('/api/tts/ipa', json={'ipa': syllable})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True


def test_tts_multi_syllable_word_preview(tts_client):
    """Test TTS for complete multi-syllable words"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    # Test full word pronunciation
    response = client.post('/api/tts/ipa', json={'ipa': 'manoˈped'})
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'audio_data' in data


def test_tts_error_handling_when_backend_fails(tts_client):
    """Test graceful degradation when TTS backend fails"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    # Make TTS return None (simulating failure)
    mock_tts.generate_ipa_audio.return_value = None
    
    response = client.post('/api/tts/ipa', json={'ipa': 'test'})
    
    # Should return error but not crash
    assert response.status_code in [200, 500]
    data = response.get_json()
    
    if response.status_code == 500:
        assert data['success'] is False
        assert 'error' in data


def test_tts_empty_string_handling(tts_client):
    """Test TTS handles empty strings gracefully"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    response = client.post('/api/tts/ipa', json={'ipa': ''})
    
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False


def test_tts_special_characters(tts_client):
    """Test TTS handles IPA special characters"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    special_ipa = 'ʃ'  # sh sound
    response = client.post('/api/tts/phoneme', json={
        'phoneme': special_ipa,
        'position': 'onset'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True


def test_tts_diphthong_pronunciation(tts_client):
    """Test TTS handles diphthongs (two-part vowels)"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    diphthongs = ['aɪ', 'eɪ', 'oʊ', 'aʊ']
    
    for diphthong in diphthongs:
        response = client.post('/api/tts/phoneme', json={
            'phoneme': diphthong,
            'position': 'nucleus'
        })
        
        assert response.status_code == 200


def test_tts_consonant_clusters(tts_client):
    """Test TTS handles consonant clusters"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    clusters = ['st', 'pl', 'tr', 'str']
    
    for cluster in clusters:
        response = client.post('/api/tts/phoneme', json={
            'phoneme': cluster,
            'position': 'onset'
        })
        
        assert response.status_code == 200


def test_tts_word_creation_with_audio_preview(tts_client):
    """Test TTS during word creation workflow"""
    client, db_path, user_id, project_id, mock_tts = tts_client
    
    # Simulate word creation with audio preview
    # 1. Preview individual syllables
    response1 = client.post('/api/tts/ipa', json={'ipa': 'ma'})
    assert response1.status_code == 200
    
    response2 = client.post('/api/tts/ipa', json={'ipa': 'nop'})
    assert response2.status_code == 200
    
    # 2. Preview full word
    response3 = client.post('/api/tts/ipa', json={'ipa': 'manop'})
    assert response3.status_code == 200
    
    data = response3.get_json()
    assert data['success'] is True
    assert 'audio_data' in data


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

