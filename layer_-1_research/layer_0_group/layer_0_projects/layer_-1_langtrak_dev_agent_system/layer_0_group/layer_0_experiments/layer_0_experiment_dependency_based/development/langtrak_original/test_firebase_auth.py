import pytest
import json
import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Temporarily disable firebase to prevent actual external calls during basic app testing
os.environ.setdefault('DISABLE_FIREBASE', '1')

# Import the Flask app factory
from app import create_app

@pytest.fixture
def client():
    # Create a test client using the Flask application configured for testing
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_google_auth_endpoint(client):
    """
    Test the /auth/google endpoint using the Flask test client.
    This test simulates the request made by the original test_firebase_auth.py script.
    """
    test_data = {
        'idToken': 'fake_token',
        'user': {
            'uid': 'test123',
            'email': 'test@example.com',
            'displayName': 'Test User'
        }
    }
    response = client.post('/auth/google', json=test_data)

    # Assertions for the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'redirect_url' in data
    assert data['redirect_url'] == '/dashboard'
