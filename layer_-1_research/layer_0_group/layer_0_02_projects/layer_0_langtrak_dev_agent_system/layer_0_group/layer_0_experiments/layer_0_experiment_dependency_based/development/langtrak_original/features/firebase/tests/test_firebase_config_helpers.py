import os
import tempfile
import unittest
from pathlib import Path
from textwrap import dedent
from unittest import mock

from features.firebase import get_firebase_client_config, parse_firebase_config_js


class FirebaseConfigHelperTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

    def _write_config(self, contents: str) -> Path:
        path = Path(self.temp_dir.name) / "config/firebase/firebase-config.js"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8")
        return path

    def test_parse_returns_empty_when_file_missing(self):
        missing_path = Path(self.temp_dir.name) / "missing.js"
        config = parse_firebase_config_js(config_path=missing_path)
        self.assertEqual(config, {})

    def test_get_config_applies_environment_overrides(self):
        sample_file = self._write_config(
            dedent(
                """
                const firebaseConfig = {
                    apiKey: "file-key",
                    projectId: "file-project"
                };
                """
            ).strip()
        )

        env_values = {
            "VITE_FIREBASE_API_KEY": "env-key",
            "VITE_FIREBASE_PROJECT_ID": "env-project",
            "VITE_FIREBASE_MESSAGING_SENDER_ID": "555",
        }

        with mock.patch.dict(os.environ, env_values, clear=True):
            config = get_firebase_client_config(config_path=sample_file)

        self.assertEqual(config["apiKey"], "env-key")
        self.assertEqual(config["projectId"], "env-project")
        self.assertEqual(config["authDomain"], "env-project.firebaseapp.com")
        self.assertEqual(config["storageBucket"], "env-project.firebasestorage.app")
        self.assertEqual(config["messagingSenderId"], "555")
        self.assertEqual(config["appId"], "")

    def test_get_config_defaults_to_empty_strings(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            config = get_firebase_client_config(config_path=Path(self.temp_dir.name) / "config/firebase/firebase-config.js")

        self.assertEqual(
            config,
            {
                "apiKey": "",
                "authDomain": "",
                "projectId": "",
                "storageBucket": "",
                "messagingSenderId": "",
                "appId": "",
            },
        )


if __name__ == "__main__":
    unittest.main()
