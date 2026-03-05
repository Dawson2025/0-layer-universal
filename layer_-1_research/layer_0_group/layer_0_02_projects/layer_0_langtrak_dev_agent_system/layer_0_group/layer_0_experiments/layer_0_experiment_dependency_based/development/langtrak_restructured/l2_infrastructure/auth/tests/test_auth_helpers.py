# resource_id: "be31fdba-5746-49eb-a9c5-d58896ebe6bb"
# resource_type: "document"
# resource_name: "test_auth_helpers"
import os
import sqlite3
import tempfile
import unittest
from unittest import mock

try:
    from flask import Flask, session
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    Flask = None
    session = None

if Flask is not None:
    import main
    from features.auth import get_user_info, is_project_owner, require_auth, require_project_admin
else:  # pragma: no cover - skip path
    main = None
    get_user_info = is_project_owner = require_auth = require_project_admin = None


@unittest.skipIf(Flask is None, "Flask is not installed")
class AuthHelperTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.secret_key = "testing-secret"
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.original_db = main.DB_NAME
        self.test_db_path = os.path.join(self.temp_dir.name, "auth_tests.db")
        main.DB_NAME = self.test_db_path

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT,
                firebase_uid TEXT,
                is_active INTEGER DEFAULT 1
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                user_id INTEGER,
                cloud_project_id TEXT,
                cloud_last_sync TEXT,
                migrated_to_cloud INTEGER DEFAULT 0
            )
            """
        )
        cursor.execute(
            "INSERT INTO users (username, email, firebase_uid, is_active) VALUES (?, ?, ?, 1)",
            ("legacy_user", "legacy@example.com", None),
        )
        cursor.execute(
            "INSERT INTO projects (name, user_id) VALUES (?, ?)",
            ("Local Project", 1),
        )
        conn.commit()
        conn.close()

    def tearDown(self):
        main.DB_NAME = self.original_db

    def test_get_user_info_without_session(self):
        with self.app.test_request_context("/"):
            info = get_user_info()
            self.assertFalse(info["is_authenticated"])

    def test_get_user_info_with_legacy_user(self):
        with self.app.test_request_context("/"):
            session["user_id"] = 1
            info = get_user_info()
            self.assertTrue(info["is_authenticated"])
            self.assertEqual(info["name"], "legacy_user")
            self.assertIsNone(info["current_project"])

    def test_is_project_owner_true(self):
        result = is_project_owner(1, 1)
        self.assertTrue(result)

    def test_is_project_owner_false(self):
        result = is_project_owner(1, 999)
        self.assertFalse(result)

    def test_require_auth_redirects_when_not_authenticated(self):
        self.app.add_url_rule("/login", "login", lambda: "login page")

        @require_auth
        def protected():
            return "ok"

        with self.app.test_request_context("/protected"):
            response = protected()
            self.assertEqual(response.status_code, 302)
            self.assertIn("/login", response.location)

    def test_require_project_admin_redirects_when_no_project(self):
        self.app.add_url_rule("/login", "login", lambda: "login")
        self.app.add_url_rule("/dashboard", "dashboard", lambda: "dashboard")

        with mock.patch("features.auth.helpers.get_user_info", return_value={"is_authenticated": True, "current_project": None}):

            @require_project_admin
            def admin_view():
                return "admin"

            with self.app.test_request_context("/admin"):
                response = admin_view()
                self.assertEqual(response.status_code, 302)
                self.assertIn("/dashboard", response.location)

    def test_require_project_admin_allows_owner(self):
        self.app.add_url_rule("/login", "login", lambda: "login")
        self.app.add_url_rule("/dashboard", "dashboard", lambda: "dashboard")
        self.app.add_url_rule("/main-menu", "main_menu", lambda: "main")

        user_payload = {
            "is_authenticated": True,
            "current_project": {"id": 1},
            "id": 1,
        }

        with mock.patch("features.auth.helpers.get_user_info", return_value=user_payload):

            @require_project_admin
            def admin_view():
                return "allowed"

            with self.app.test_request_context("/admin"):
                response = admin_view()
                self.assertEqual(response, "allowed")


if __name__ == "__main__":
    unittest.main()
