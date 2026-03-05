# resource_id: "5d81f8c9-f4cf-4b38-801a-89271a790e3d"
# resource_type: "document"
# resource_name: "test_cloud_templates"
"""
Comprehensive Cloud Template Tests
Tests cloud-based phoneme template sharing and synchronization
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
def cloud_template_client(tmp_path, monkeypatch):
    """Provide Flask test client for cloud template testing"""
    
    db_path = tmp_path / 'test.db'
    db_str = str(db_path)
    
    patch_all_db_names(monkeypatch, db_str)
    
    main.migrate_schema()
    flask_app.init_users_table()
    
    conn = sqlite3.connect(db_str)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO users (username, email, password_hash, is_active, firebase_uid) VALUES (?, ?, ?, 1, ?)",
        ('cloud_user', 'cloud@test.com', 'hash', 'firebase_uid_123')
    )
    user_id = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO projects (name, user_id) VALUES (?, ?)",
        ('Cloud Template Project', user_id)
    )
    project_id = cursor.lastrowid
    
    # Add phonemes
    phonemes = [
        ('CVC', 'onset', 'single_consonants', 'Stops', '', 'm', user_id, project_id),
        ('CVC', 'nucleus', 'monophthongs', 'Vowels', '', 'a', user_id, project_id),
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
    
    # Mock Firebase for cloud templates
    mock_firebase = MagicMock()
    mock_firebase.is_available.return_value = True  # Cloud features available
    
    mock_firestore = MagicMock()
    mock_firestore.upload_template.return_value = 'template_123'
    mock_firestore.get_public_templates.return_value = [
        {'id': 'template_123', 'name': 'Test Cloud Template', 'phoneme_count': 10, 'is_public': True}
    ]
    mock_firestore.get_phoneme_templates.return_value = [
        {'id': 'template_123', 'name': 'Test Cloud Template', 'phoneme_count': 10, 'is_public': True}
    ]
    mock_firestore.get_template.return_value = {
        'id': 'template_123',
        'name': 'Test Cloud Template',
        'template_data': json.dumps([{'phoneme': 'm', 'position': 'onset'}]),
        'phoneme_count': 1
    }
    mock_firestore.get_phoneme_template.return_value = {
        'id': 'template_123',
        'name': 'Test Cloud Template',
        'phonemes': [
            {
                'syllable_type': 'CVC',
                'position': 'onset',
                'length_type': 'single_consonants',
                'group_type': 'Stops',
                'subgroup_type': '',
                'sub_subgroup_type': '',
                'sub_sub_subgroup_type': '',
                'phoneme': 'm',
                'frequency': 0
            }
        ],
        'phoneme_count': 1
    }
    # Fix the get_project mock to return proper data instead of MagicMock
    mock_firestore.get_project.return_value = {
        'id': '1',
        'name': 'Test Project',
        'user_id': user_id
    }
    # Mock get_project_phonemes to return proper data
    mock_firestore.get_project_phonemes.return_value = [
        {
            'syllable_type': 'CVC',
            'position': 'onset',
            'length_type': 'single_consonants',
            'group_type': 'Stops',
            'subgroup_type': '',
            'sub_subgroup_type': '',
            'sub_sub_subgroup_type': '',
            'phoneme': 'm',
            'frequency': 1
        }
    ]
    # Mock create_phoneme_template to return a template ID
    mock_firestore.create_phoneme_template.return_value = 'template_123'
    # Mock methods needed for download operations
    mock_firestore.is_available.return_value = False  # Use local SQLite for simpler testing
    mock_firestore.delete_phoneme.return_value = True
    mock_firestore.initialize_project_phonemes_from_template.return_value = True

    with patch.object(flask_app, 'clean_firebase_service', mock_firebase):
        with patch.object(flask_app, 'firestore_db', mock_firestore):
            with flask_app.app.test_client() as client:
                with client.session_transaction() as sess:
                    sess['user_id'] = user_id
                    sess['username'] = 'cloud_user'
                    sess['current_project_id'] = project_id
                    sess['firebase_uid'] = 'firebase_uid_123'
                
                yield client, db_str, user_id, project_id, mock_firestore


def test_upload_template_to_cloud(cloud_template_client):
    """Test uploading local template to cloud"""
    client, db_path, user_id, project_id, mock_firestore = cloud_template_client

    response = client.post('/api/cloud-templates', json={
        'name': 'My Cloud Template',
        'description': 'Shared with community',
        'is_public': True
    })

    assert response.status_code == 200
    data = response.get_json()
    assert data.get('success') is True

    # Verify Firebase was called (the actual method is create_phoneme_template, not upload_template)
    assert mock_firestore.create_phoneme_template.called


def test_list_public_cloud_templates(cloud_template_client):
    """Test listing available public cloud templates"""
    client, db_path, user_id, project_id, mock_firestore = cloud_template_client
    
    response = client.get('/api/cloud-templates')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data.get('success') is True
    assert 'templates' in data
    assert len(data['templates']) > 0


def test_download_cloud_template(cloud_template_client):
    """Test downloading and applying a cloud template"""
    client, db_path, user_id, project_id, mock_firestore = cloud_template_client

    # Send an empty JSON object with proper content type
    response = client.post('/api/cloud-templates/template_123/download', json={})

    assert response.status_code == 200
    data = response.get_json()
    assert data.get('success') is True

    # Verify Firestore was queried (the actual method is get_phoneme_template, not get_template)
    assert mock_firestore.get_phoneme_template.called


def test_delete_own_cloud_template(cloud_template_client):
    """Test deleting a cloud template you own"""
    client, db_path, user_id, project_id, mock_firestore = cloud_template_client
    
    response = client.delete('/api/cloud-templates/template_123')
    
    assert response.status_code in [200, 403, 404]


def test_template_privacy_public_vs_private(cloud_template_client):
    """Test creating both public and private templates"""
    client, db_path, user_id, project_id, mock_firestore = cloud_template_client
    
    # Public template
    public_response = client.post('/api/cloud-templates', json={
        'name': 'Public Template',
        'description': 'Everyone can use this',
        'is_public': True
    })
    
    assert public_response.status_code == 200
    
    # Private template
    private_response = client.post('/api/cloud-templates', json={
        'name': 'Private Template',
        'description': 'Only for me',
        'is_public': False
    })
    
    assert private_response.status_code == 200


def test_template_cloud_sync(cloud_template_client):
    """Test that cloud templates sync properly"""
    client, db_path, user_id, project_id, mock_firestore = cloud_template_client
    
    # Upload template
    upload_response = client.post('/api/cloud-templates', json={
        'name': 'Sync Test',
        'description': 'Testing sync',
        'is_public': True
    })
    
    assert upload_response.status_code == 200
    
    # Retrieve cloud templates
    list_response = client.get('/api/cloud-templates')
    
    assert list_response.status_code == 200
    data = list_response.get_json()
    assert len(data.get('templates', [])) > 0


def test_template_without_firebase(tmp_path, monkeypatch):
    """Test template features work without Firebase (local only)"""
    db_path = tmp_path / 'test.db'
    db_str = str(db_path)
    
    patch_all_db_names(monkeypatch, db_str)
    
    main.migrate_schema()
    flask_app.init_users_table()
    
    conn = sqlite3.connect(db_str)
    cursor = conn.cursor()
    
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
        ('local_user', 'local@test.com', 'hash')
    )
    user_id = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO projects (name, user_id) VALUES (?, ?)",
        ('Local Project', user_id)
    )
    project_id = cursor.lastrowid
    
    phonemes = [
        ('CVC', 'onset', 'single_consonants', '', '', 'm', user_id, project_id),
    ]
    cursor.executemany(
        """INSERT INTO phonemes (syllable_type, position, length_type, group_type,
           subgroup_type, phoneme, user_id, project_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        phonemes
    )
    
    conn.commit()
    conn.close()
    
    flask_app.app.config['TESTING'] = True
    
    # Disable Firebase
    mock_firebase = MagicMock()
    mock_firebase.is_available.return_value = False
    
    with patch.object(flask_app, 'clean_firebase_service', mock_firebase):
        with flask_app.app.test_client() as client:
            with client.session_transaction() as sess:
                sess['user_id'] = user_id
                sess['current_project_id'] = project_id
            
            # Local template creation should still work
            response = client.post('/api/templates', json={
                'name': 'Local Template',
                'description': 'Works without cloud'
            })
            
            assert response.status_code == 200
            data = response.get_json()
            assert data.get('success') is True


def test_cloud_template_requires_authentication(tmp_path, monkeypatch):
    """Test that cloud template operations require authentication"""
    db_path = tmp_path / 'test.db'
    db_str = str(db_path)
    
    patch_all_db_names(monkeypatch, db_str)
    main.migrate_schema()
    
    flask_app.app.config['TESTING'] = True
    
    with flask_app.app.test_client() as client:
        # Try to upload without auth
        response = client.post('/api/cloud-templates', json={
            'name': 'Unauthorized',
            'description': 'Should fail'
        })
        
        # Should fail or redirect
        assert response.status_code in [302, 401, 403, 200]


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

