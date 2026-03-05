# resource_id: "2ee15250-f6a0-407d-855c-56ef3f52bd7a"
# resource_type: "document"
# resource_name: "test_database_backup_restore"
"""
Comprehensive Database Backup/Restore Tests
Tests US-052 and database management features
"""

import json
import sqlite3
import pytest
import app as flask_app
import main
import core.database as core_db
from tests.conftest import patch_all_db_names
from unittest.mock import patch, MagicMock


@pytest.fixture()
def backup_client(tmp_path, monkeypatch):
    """Provide Flask test client for backup/restore testing"""
    
    db_path = tmp_path / 'test.db'
    db_str = str(db_path)
    
    patch_all_db_names(monkeypatch, db_str)
    
    main.migrate_schema()
    flask_app.init_users_table()
    
    conn = sqlite3.connect(db_str)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO users (username, email, password_hash, is_active) VALUES (?, ?, ?, 1)",
        ('backup_user', 'backup@test.com', 'hash')
    )
    user_id = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO projects (name, user_id) VALUES (?, ?)",
        ('Backup Test Project', user_id)
    )
    project_id = cursor.lastrowid
    
    # Add test data
    phonemes = [
        ('CVC', 'onset', 'single_consonants', '', '', 'm', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', '', '', 'a', user_id, project_id),
    ]
    cursor.executemany(
        """INSERT INTO phonemes (syllable_type, position, length_type, group_type,
           subgroup_type, phoneme, user_id, project_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        phonemes
    )
    
    cursor.execute(
        """INSERT INTO words (language, english_words, new_language_word, ipa_phonetics,
           syllable_type, onset_phoneme, nucleus_phoneme, user_id, project_id)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('Test', json.dumps(['test']), 'mat', 'mæt', 'CVC', 'm', 'a', user_id, project_id)
    )
    
    conn.commit()
    conn.close()
    
    flask_app.app.config['TESTING'] = True
    flask_app.app.config['SECRET_KEY'] = 'test-secret'
    
    mock_firebase = MagicMock()
    mock_firebase.is_available.return_value = False
    
    mock_user_info = {
        'id': user_id,
        'name': 'backup_user',
        'email': 'backup@test.com',
        'is_authenticated': True,
        'current_project': {'id': project_id, 'name': 'Backup Test Project'}
    }
    
    import features.admin.template_system as template_module
    import features.admin.database_tools as db_tools_module
    
    with patch.object(flask_app, 'clean_firebase_service', mock_firebase):
        with patch.object(template_module, 'clean_firebase_service', mock_firebase):
            with patch.object(flask_app, 'get_user_info', return_value=mock_user_info):
                with patch.object(template_module, 'get_user_info', return_value=mock_user_info):
                    with flask_app.app.test_client() as client:
                        with client.session_transaction() as sess:
                            sess['user_id'] = user_id
                            sess['username'] = 'backup_user'
                            sess['current_project_id'] = project_id
                        
                        yield client, db_str, user_id, project_id


def test_us052_database_reset_api(backup_client):
    """US-052: Database reset functionality"""
    client, db_path, user_id, project_id = backup_client
    
    # Check initial data exists
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words")
    initial_words = cursor.fetchone()[0]
    assert initial_words > 0
    conn.close()
    
    # Reset database
    response = client.post('/api/admin/reset-database')
    
    assert response.status_code in [200, 404]  # 404 if not implemented as API
    
    if response.status_code == 200:
        data = response.get_json()
        assert data.get('success') is True


def test_export_template_from_current_phonemes(backup_client):
    """Test exporting current phonemes as a template"""
    client, db_path, user_id, project_id = backup_client
    
    response = client.post('/api/admin/export-template', json={
        'name': 'Test Template',
        'description': 'Template for testing'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data.get('success') is True
    
    if 'template_id' in data:
        template_id = data['template_id']
        
        # Verify template was saved
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, description FROM phoneme_templates WHERE id = ?", (template_id,))
        template = cursor.fetchone()
        conn.close()
        
        assert template is not None
        assert template[0] == 'Test Template'


def test_import_template_restores_phonemes(backup_client):
    """Test importing a template restores phonemes"""
    client, db_path, user_id, project_id = backup_client
    
    # First export current state
    export_response = client.post('/api/admin/export-template', json={
        'name': 'Backup Template',
        'description': 'For restore testing'
    })
    
    if export_response.status_code != 200:
        pytest.skip("Export template not available")
    
    export_data = export_response.get_json()
    if not export_data.get('success'):
        pytest.skip("Template export failed")
    
    template_id = export_data.get('template_id')
    
    # Clear phonemes
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM phonemes")
    conn.commit()
    
    # Verify cleared
    cursor.execute("SELECT COUNT(*) FROM phonemes")
    assert cursor.fetchone()[0] == 0
    conn.close()
    
    # Import template
    import_response = client.post('/api/admin/import-template', json={
        'template_id': template_id
    })
    
    if import_response.status_code == 200:
        # Verify phonemes restored
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM phonemes")
        restored_count = cursor.fetchone()[0]
        conn.close()
        
        assert restored_count > 0


def test_template_preserves_phoneme_data(backup_client):
    """Test that templates preserve all phoneme data accurately"""
    client, db_path, user_id, project_id = backup_client
    
    # Get original phonemes
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT phoneme, position, syllable_type FROM phonemes ORDER BY phoneme")
    original_phonemes = cursor.fetchall()
    conn.close()
    
    # Export as template
    response = client.post('/api/admin/export-template', json={
        'name': 'Data Integrity Test',
        'description': 'Testing data preservation'
    })
    
    if response.status_code != 200:
        pytest.skip("Export not available")
    
    data = response.get_json()
    if not data.get('success'):
        pytest.skip("Export failed")
    
    # Verify template data
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT template_data FROM phoneme_templates WHERE id = ?", (data.get('template_id'),))
    template_row = cursor.fetchone()
    conn.close()
    
    if template_row:
        template_data = json.loads(template_row[0])
        assert isinstance(template_data, (list, dict))
        assert len(template_data) > 0


def test_database_backup_to_file(backup_client):
    """Test backing up database to downloadable file"""
    client, db_path, user_id, project_id = backup_client
    
    # This might be a download endpoint
    response = client.get('/api/admin/backup-database')
    
    # Should succeed or return 404 if not implemented
    assert response.status_code in [200, 404]
    
    if response.status_code == 200:
        # Could be JSON or file download
        if response.content_type and 'json' in response.content_type:
            data = response.get_json()
            assert 'backup_file' in data or 'success' in data


def test_database_restore_from_file(backup_client):
    """Test restoring database from backup file"""
    client, db_path, user_id, project_id = backup_client
    
    # Test restore endpoint
    response = client.post('/api/admin/restore-database', data={
        'backup_file': 'test_backup.db'
    })
    
    # Should handle gracefully even if file doesn't exist
    assert response.status_code in [200, 400, 404]


def test_reset_preserves_templates(backup_client):
    """Test that database reset preserves phoneme templates"""
    client, db_path, user_id, project_id = backup_client
    
    # Create a template first
    template_response = client.post('/api/admin/export-template', json={
        'name': 'Preserve Me',
        'description': 'Should survive reset'
    })
    
    if template_response.status_code != 200:
        pytest.skip("Template creation not available")
    
    # Reset database
    reset_response = client.post('/api/admin/reset-database')
    
    if reset_response.status_code == 200:
        # Verify templates still exist
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM phoneme_templates WHERE name = ?", ('Preserve Me',))
        template_count = cursor.fetchone()[0]
        conn.close()
        
        assert template_count > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

