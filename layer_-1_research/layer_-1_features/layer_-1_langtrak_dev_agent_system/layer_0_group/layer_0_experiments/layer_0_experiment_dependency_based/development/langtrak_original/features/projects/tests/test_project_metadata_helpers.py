import os
import sqlite3
import tempfile
import unittest
from unittest import mock

import main
from features.projects import fetch_project_metadata, normalize_project_identifier


class ProjectMetadataHelperTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.original_db = main.DB_NAME
        self.test_db_path = os.path.join(self.temp_dir.name, "test_projects.db")
        main.DB_NAME = self.test_db_path

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                cloud_project_id TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        cursor.execute(
            "INSERT INTO projects (name, user_id, cloud_project_id) VALUES (?, ?, ?)",
            ("Sample Project", 5, "cloud-123"),
        )
        self.local_project_id = cursor.lastrowid
        conn.commit()
        conn.close()

    def tearDown(self):
        main.DB_NAME = self.original_db

    def test_normalize_project_identifier_handles_prefix(self):
        self.assertEqual(
            normalize_project_identifier("local:42"),
            ("local", "42", "local:42"),
        )
        self.assertEqual(
            normalize_project_identifier("cloud:abc"),
            ("cloud", "abc", "cloud:abc"),
        )

    def test_normalize_project_identifier_defaults_to_cloud(self):
        self.assertEqual(
            normalize_project_identifier("xyz"),
            ("cloud", "xyz", "cloud:xyz"),
        )

    def test_fetch_project_metadata_local_success(self):
        result = fetch_project_metadata("local", str(self.local_project_id), owner_id="5")
        self.assertIsNotNone(result)
        self.assertEqual(result["project_id"], str(self.local_project_id))
        self.assertEqual(result["owner_user_id"], 5)

    def test_fetch_project_metadata_local_wrong_owner(self):
        result = fetch_project_metadata("local", str(self.local_project_id), owner_id="999")
        self.assertIsNone(result)

    def test_fetch_project_metadata_cloud_calls_services(self):
        with mock.patch("features.projects.metadata.clean_firebase_service.is_available", return_value=True), mock.patch(
            "features.projects.metadata.firestore_db.get_project",
            return_value={"id": "cloud-123", "name": "Cloud Project", "user_id": "15"},
        ):
            result = fetch_project_metadata("cloud", "cloud-123", owner_id="15")

        self.assertIsNotNone(result)
        self.assertEqual(result["cloud_project_id"], "cloud-123")
        self.assertEqual(result["owner_user_id"], "15")

    def test_fetch_project_metadata_cloud_service_unavailable(self):
        with mock.patch("features.projects.metadata.clean_firebase_service.is_available", return_value=False):
            result = fetch_project_metadata("cloud", "cloud-123", owner_id="15")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
