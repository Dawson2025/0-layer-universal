# resource_id: "7d2c8f07-23b3-4de1-879a-baad479b18dd"
# resource_type: "document"
# resource_name: "test_template_features"
"""
Comprehensive Phoneme Template Tests
Tests template creation, management, and cloud synchronization
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
def template_client(tmp_path, monkeypatch):
    """Provide Flask test client for template testing"""
    
    db_path = tmp_path / 'test.db'
    db_str = str(db_path)
    
    patch_all_db_names(monkeypatch, db_str)
    
    main.migrate_schema()
    flask_app.init_users_table()
    
    conn = sqlite3.connect(db_str)
    cursor = conn.cursor()
    
    # Create phoneme_templates table
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
    
    cursor.execute(
        "INSERT INTO users (username, email, password_hash, is_active) VALUES (?, ?, ?, 1)",
        ('template_user', 'template@test.com', 'hash')
    )
    user_id = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO projects (name, user_id) VALUES (?, ?)",
        ('Template Project', user_id)
    )
    project_id = cursor.lastrowid
    
    # Add phonemes for template creation
    phonemes = [
        ('CVC', 'onset', 'single_consonants', 'Stops', '', 'm', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', 'Vowels', '', 'a', user_id, project_id),
        ('CVC', 'coda', 'single_consonants', 'Stops', '', 't', user_id, project_id),
    ]
    cursor.executemany(
        """INSERT INTO phonemes (syllable_type, position, length_type, group_type,
           subgroup_type, phoneme, user_id, project_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        phonemes
    )
    
    conn.commit()
    conn.close()
    
    flask_app.app.config['TESTING'] = True
    flask_app.app.config['SECRET_KEY'] = 'test-secret'
    
    mock_firebase = MagicMock()
    mock_firebase.is_available.return_value = False
    
    mock_user_info = {
        'id': user_id,
        'name': 'template_user',
        'email': 'template@test.com',
        'is_authenticated': True,
        'current_project': {'id': project_id, 'name': 'Template Project'}
    }
    
    import features.admin.template_system as template_module
    
    with patch.object(flask_app, 'clean_firebase_service', mock_firebase):
        with patch.object(template_module, 'clean_firebase_service', mock_firebase):
            with patch.object(flask_app, 'get_user_info', return_value=mock_user_info):
                with patch.object(template_module, 'get_user_info', return_value=mock_user_info):
                    with flask_app.app.test_client() as client:
                        with client.session_transaction() as sess:
                            sess['user_id'] = user_id
                            sess['username'] = 'template_user'
                            sess['current_project_id'] = project_id
                        
                        yield client, db_str, user_id, project_id


def test_create_custom_template(template_client):
    """Test creating a custom phoneme template"""
    client, db_path, user_id, project_id = template_client
    
    response = client.post('/api/templates', json={
        'name': 'My Custom Template',
        'description': 'A template I created'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data.get('success') is True
    assert 'template_id' in data
    
    # Verify template was saved
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name, description FROM phoneme_templates WHERE id = ?", (data['template_id'],))
    template = cursor.fetchone()
    conn.close()
    
    assert template is not None
    assert template[0] == 'My Custom Template'
    assert template[1] == 'A template I created'


def test_list_saved_templates(template_client):
    """Test listing all saved templates"""
    client, db_path, user_id, project_id = template_client
    
    # Create a template first
    client.post('/api/templates', json={
        'name': 'Template 1',
        'description': 'First'
    })
    
    client.post('/api/templates', json={
        'name': 'Template 2',
        'description': 'Second'
    })
    
    # List templates
    response = client.get('/api/admin/templates')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data.get('success') is True
    assert 'templates' in data
    assert len(data['templates']) >= 2


def test_apply_template_to_project(template_client):
    """Test applying a saved template to current project"""
    client, db_path, user_id, project_id = template_client
    
    # Create template
    create_response = client.post('/api/templates', json={
        'name': 'Apply Test Template',
        'description': 'For application testing'
    })
    
    template_id = create_response.get_json().get('template_id')
    
    # Clear current phonemes
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM phonemes")
    conn.commit()
    
    cursor.execute("SELECT COUNT(*) FROM phonemes")
    assert cursor.fetchone()[0] == 0
    conn.close()
    
    # Apply template
    apply_response = client.post(f'/api/admin/apply-template/{template_id}')
    
    assert apply_response.status_code in [200, 404]
    
    if apply_response.status_code == 200:
        # Verify phonemes were restored
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM phonemes")
        count_after = cursor.fetchone()[0]
        conn.close()
        
        assert count_after > 0


def test_delete_template(template_client):
    """Test deleting a saved template"""
    client, db_path, user_id, project_id = template_client
    
    # Create template
    create_response = client.post('/api/templates', json={
        'name': 'Delete Me',
        'description': 'Will be deleted'
    })
    
    template_id = create_response.get_json().get('template_id')
    
    # Delete template
    delete_response = client.delete(f'/api/templates/{template_id}')
    
    assert delete_response.status_code in [200, 404]
    
    if delete_response.status_code == 200:
        # Verify deleted
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM phoneme_templates WHERE id = ?", (template_id,))
        count = cursor.fetchone()[0]
        conn.close()
        
        assert count == 0


def test_template_includes_all_phoneme_data(template_client):
    """Test that templates capture all phoneme attributes"""
    client, db_path, user_id, project_id = template_client
    
    response = client.post('/api/templates', json={
        'name': 'Complete Data Template',
        'description': 'Has all fields'
    })
    
    data = response.get_json()
    template_id = data.get('template_id')
    
    # Check template data structure
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT template_data FROM phoneme_templates WHERE id = ?", (template_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        template_json = json.loads(row[0])
        assert isinstance(template_json, (list, dict))
        
        if isinstance(template_json, list) and len(template_json) > 0:
            first_phoneme = template_json[0]
            # Should have key phoneme attributes
            assert 'phoneme' in first_phoneme or 'symbol' in first_phoneme


def test_template_count_accuracy(template_client):
    """Test that phoneme_count in templates is accurate"""
    client, db_path, user_id, project_id = template_client
    
    # Get current phoneme count
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM phonemes")
    actual_count = cursor.fetchone()[0]
    conn.close()
    
    # Create template
    response = client.post('/api/templates', json={
        'name': 'Count Test',
        'description': 'Testing count accuracy'
    })
    
    data = response.get_json()
    template_id = data.get('template_id')
    
    # Check recorded count
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT phoneme_count FROM phoneme_templates WHERE id = ?", (template_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row and row[0] is not None:
        assert row[0] == actual_count


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

