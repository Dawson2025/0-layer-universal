import json
import os
import sqlite3
import tempfile
import unittest

os.environ.setdefault('DISABLE_FIREBASE', '1')

import main
import core.database as core_database
from app import app


class AllFieldSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        self._temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self._temp_dir.cleanup)

        self._original_db = main.DB_NAME
        self._original_core_db = core_database.DB_NAME
        self.test_db_path = os.path.join(self._temp_dir.name, 'data/test_phonemes.db')
        main.DB_NAME = self.test_db_path
        core_database.DB_NAME = self.test_db_path

        os.makedirs(os.path.dirname(self.test_db_path), exist_ok=True)
        
        # Initialize schema in correct order
        core_database.init_database()
        main.migrate_schema()

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password_hash, is_active) VALUES (?, ?, ?, 1)",
            ("testuser", "user@example.com", "hash-value"),
        )
        self.user_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO projects (name, user_id) VALUES (?, ?)",
            ("Test Project", self.user_id)
        )
        self.project_id = cursor.lastrowid

        sample_words = [
            ("LangA", json.dumps(["hello", "greeting"]), "talon", "tɑ.lɔn", "TAH-lon"),
            ("LangB", json.dumps(["greet", "welcome"]), "mira", "mi.ra", "MEE-rah"),
        ]

        for entry in sample_words:
            cursor.execute(
                """
                INSERT INTO words (
                    language,
                    english_words,
                    new_language_word,
                    ipa_phonetics,
                    dictionary_phonetics,
                    user_id,
                    project_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (*entry, self.user_id, self.project_id),
            )

        conn.commit()
        conn.close()

    def tearDown(self):
        main.DB_NAME = self._original_db
        core_database.DB_NAME = self._original_core_db

    def _authenticate(self):
        with self.client.session_transaction() as session:
            session['user_id'] = self.user_id
            session['auth_method'] = 'email_password'
            session['current_project_id'] = self.project_id

    def test_all_field_search_matches_constructed_word(self):
        self._authenticate()
        response = self.client.get('/api/lookup-word', query_string={'type': 'all', 'term': 'tal'})

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertTrue(payload['success'])
        self.assertEqual(payload['count'], 1)
        self.assertEqual(payload['results'][0]['new_language_word'], 'talon')

    def test_all_field_search_matches_multiple_fields(self):
        self._authenticate()
        response = self.client.get('/api/lookup-word', query_string={'type': 'all', 'term': 'welcome'})

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertTrue(payload['success'])
        self.assertEqual(payload['count'], 1)
        self.assertEqual(payload['results'][0]['language'], 'LangB')


if __name__ == '__main__':
    unittest.main()
