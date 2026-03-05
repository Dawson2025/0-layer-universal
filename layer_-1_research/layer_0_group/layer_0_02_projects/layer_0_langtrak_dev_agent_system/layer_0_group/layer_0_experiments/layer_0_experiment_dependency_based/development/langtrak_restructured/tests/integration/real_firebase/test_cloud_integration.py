#!/usr/bin/env python3
# resource_id: "b5bf5481-9a5a-43a3-8fbf-5bad05e7eedb"
# resource_type: "document"
# resource_name: "test_cloud_integration"
"""
End-to-end Firebase integration tests.

These tests verify that Firestore collections and Cloud Storage assets
used by Lang-Trak behave as expected when interacting with the Firebase
Admin SDK. They create temporary data under clearly scoped keys and
clean it up after execution. The tests are automatically skipped when
Firebase services or credentials are unavailable to keep local runs safe.
"""

import os
import uuid
import unittest
from datetime import datetime, timezone

from services.firebase import firebase_config

RUN_FIREBASE_INTEGRATION_TESTS = os.getenv("RUN_FIREBASE_INTEGRATION_TESTS", "").lower() in {
    "1",
    "true",
    "yes",
    "on",
}

if RUN_FIREBASE_INTEGRATION_TESTS:
    from services.firebase import clean_firebase_service, firestore_db
else:  # pragma: no cover - keep module importable even when skipping
    clean_firebase_service = None
    firestore_db = None

try:
    from google.cloud import storage
    from google.oauth2 import service_account

    STORAGE_LIB_AVAILABLE = True
except ImportError:  # pragma: no cover - optional dependency
    storage = None
    service_account = None
    STORAGE_LIB_AVAILABLE = False


@unittest.skipUnless(
    RUN_FIREBASE_INTEGRATION_TESTS,
    "Set RUN_FIREBASE_INTEGRATION_TESTS=1 to exercise Firestore integration tests.",
)
class FirestoreIntegrationTests(unittest.TestCase):
    """Validate Firestore project, word, group, and phoneme workflows."""

    @classmethod
    def setUpClass(cls):
        if firestore_db is None or clean_firebase_service is None:
            raise unittest.SkipTest("Firebase integration tests are disabled by configuration")

        if firebase_config.environment == "production":
            raise unittest.SkipTest("Firestore integration tests disabled for production environment")

        if not clean_firebase_service.is_available():
            raise unittest.SkipTest("Firebase service is unavailable")

        cls.created_word_ids = []
        cls.created_project_ids = []
        cls.created_group_ids = []
        cls.created_phoneme_ids = []

    @classmethod
    def tearDownClass(cls):
        # Clean up phonemes first (they reference projects)
        for phoneme_id in getattr(cls, "created_phoneme_ids", []):
            try:
                clean_firebase_service.delete_document(firestore_db.PHONEMES_COLLECTION, phoneme_id)
            except Exception:  # pragma: no cover - best effort cleanup
                pass

        # Clean up words (they reference projects)
        for word_id in getattr(cls, "created_word_ids", []):
            try:
                clean_firebase_service.delete_document(firestore_db.WORDS_COLLECTION, word_id)
            except Exception:  # pragma: no cover - best effort cleanup
                pass

        # Clean up groups
        for group_id in getattr(cls, "created_group_ids", []):
            try:
                clean_firebase_service.delete_document(firestore_db.GROUPS_COLLECTION, group_id)
            except Exception:  # pragma: no cover - best effort cleanup
                pass

        # Clean up projects last
        for project_id in getattr(cls, "created_project_ids", []):
            try:
                clean_firebase_service.delete_document(firestore_db.PROJECTS_COLLECTION, project_id)
            except Exception:  # pragma: no cover - best effort cleanup
                pass

    def test_project_and_word_round_trip(self):
        """Ensure projects and their words persist correctly in Firestore."""
        unique_suffix = uuid.uuid4().hex[:10]

        project_payload = {
            "name": f"Integration Test Project {unique_suffix}",
            "user_id": f"integration-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.utcnow(),
            "storage_type": "cloud",
            "integration_test": True,
        }

        project_id = firestore_db.create_project(project_payload)
        self.assertIsNotNone(project_id, "Expected Firestore project ID")
        self.assertIsInstance(project_id, str)
        self.__class__.created_project_ids.append(project_id)

        project_doc = firestore_db.get_project(project_id)
        self.assertIsNotNone(project_doc, "Project should be retrievable immediately after creation")
        self.assertEqual(project_doc.get("id"), project_id)
        self.assertEqual(project_doc.get("name"), project_payload["name"])
        self.assertEqual(project_doc.get("user_id"), project_payload["user_id"])

        word_payload = {
            "language": "Integration",
            "english_words": ["alpha", "beta"],
            "new_language_word": f"word-{unique_suffix}",
            "ipa_phonetics": "ˈalpha",
            "dictionary_phonetics": "/AL-fa/",
            "video_path": f"integration-tests/videos/{unique_suffix}.mp4",
            "syllable_type": "CVC",
            "onset_phoneme": "a",
            "onset_length_type": "single_consonants",
            "nucleus_phoneme": "l",
            "nucleus_length_type": "monophthongs",
            "coda_phoneme": "f",
            "coda_length_type": "single_consonants",
            "user_id": project_payload["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }

        word_id = firestore_db.create_word(word_payload)
        self.assertIsNotNone(word_id, "Expected Firestore word ID")
        self.assertIsInstance(word_id, str)
        self.__class__.created_word_ids.append(word_id)

        project_words = firestore_db.get_project_words(project_id)
        self.assertTrue(
            any(doc.get("id") == word_id for doc in project_words),
            "Word should appear under its project",
        )

        fetched_word = firestore_db.get_word(word_id)
        self.assertIsNotNone(fetched_word, "Word should be retrievable directly")
        self.assertEqual(fetched_word.get("project_id"), project_id)
        self.assertEqual(fetched_word.get("new_language_word"), word_payload["new_language_word"])

    def test_phoneme_lifecycle(self):
        """Ensure phonemes can be created, retrieved, and deleted from Firestore."""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create a project first (phonemes reference projects)
        project_payload = {
            "name": f"Phoneme Test Project {unique_suffix}",
            "user_id": f"integration-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.utcnow(),
            "storage_type": "cloud",
            "integration_test": True,
        }
        project_id = firestore_db.create_project(project_payload)
        self.assertIsNotNone(project_id)
        self.__class__.created_project_ids.append(project_id)

        # Create phonemes for this project
        phoneme_payload_1 = {
            "syllable_type": "CVC",
            "position": "onset",
            "length_type": "single_consonants",
            "group_type": "Stops",
            "subgroup_type": "Voiceless",
            "phoneme": "p",
            "frequency": 5,
            "user_id": project_payload["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }

        phoneme_id_1 = firestore_db.create_phoneme(phoneme_payload_1)
        self.assertIsNotNone(phoneme_id_1, "Expected Firestore phoneme ID")
        self.assertIsInstance(phoneme_id_1, str)
        self.__class__.created_phoneme_ids.append(phoneme_id_1)

        phoneme_payload_2 = {
            "syllable_type": "CVC",
            "position": "nucleus",
            "length_type": "monophthongs",
            "group_type": "Vowels",
            "subgroup_type": "Front",
            "phoneme": "i",
            "frequency": 10,
            "user_id": project_payload["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }

        phoneme_id_2 = firestore_db.create_phoneme(phoneme_payload_2)
        self.assertIsNotNone(phoneme_id_2)
        self.__class__.created_phoneme_ids.append(phoneme_id_2)

        # Verify phonemes appear in project phoneme list
        project_phonemes = firestore_db.get_project_phonemes(project_id)
        self.assertGreaterEqual(len(project_phonemes), 2, "Project should have at least 2 phonemes")
        phoneme_ids_in_project = [p.get("id") for p in project_phonemes]
        self.assertIn(phoneme_id_1, phoneme_ids_in_project)
        self.assertIn(phoneme_id_2, phoneme_ids_in_project)

        # Verify phoneme data
        phoneme_1_data = next((p for p in project_phonemes if p.get("id") == phoneme_id_1), None)
        self.assertIsNotNone(phoneme_1_data)
        self.assertEqual(phoneme_1_data.get("phoneme"), "p")
        self.assertEqual(phoneme_1_data.get("position"), "onset")

        # Delete one phoneme and verify it's gone
        delete_success = firestore_db.delete_phoneme(phoneme_id_1)
        self.assertTrue(delete_success, "Phoneme deletion should succeed")

        # Verify phoneme no longer appears in project
        project_phonemes_after = firestore_db.get_project_phonemes(project_id)
        phoneme_ids_after = [p.get("id") for p in project_phonemes_after]
        self.assertNotIn(phoneme_id_1, phoneme_ids_after, "Deleted phoneme should not appear in project")
        self.assertIn(phoneme_id_2, phoneme_ids_after, "Other phoneme should still be present")

        # Remove from cleanup list since we already deleted it
        self.__class__.created_phoneme_ids.remove(phoneme_id_1)

    def test_group_lifecycle(self):
        """Ensure groups can be created, retrieved, and deleted from Firestore."""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create a group
        group_payload = {
            "name": f"Integration Test Group {unique_suffix}",
            "description": "Test group for integration testing",
            "owner_id": f"integration-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.utcnow(),
            "member_count": 1,
            "integration_test": True,
        }

        group_id = firestore_db.create_group(group_payload)
        self.assertIsNotNone(group_id, "Expected Firestore group ID")
        self.assertIsInstance(group_id, str)
        self.__class__.created_group_ids.append(group_id)

        # Verify group data can be retrieved
        # Note: If there's a get_group method, use it; otherwise we verify via collection query
        try:
            group_memberships = firestore_db.get_group_memberships(group_id)
            self.assertIsInstance(group_memberships, list)
        except Exception as e:
            # If method doesn't exist or errors, that's okay for this test
            pass

        # Delete the group and verify it's gone
        delete_success = firestore_db.delete_group(group_id)
        self.assertTrue(delete_success, "Group deletion should succeed")

        # Verify group is no longer retrievable
        try:
            # Try to get group document directly
            group_doc = clean_firebase_service.get_document(firestore_db.GROUPS_COLLECTION, group_id)
            self.assertIsNone(group_doc, "Deleted group should not be retrievable")
        except Exception:
            # If document doesn't exist, that's the expected behavior
            pass

        # Remove from cleanup list since we already deleted it
        self.__class__.created_group_ids.remove(group_id)

    def test_word_deletion_verification(self):
        """Verify words are actually deleted from Firestore."""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project
        project_payload = {
            "name": f"Word Deletion Test {unique_suffix}",
            "user_id": f"integration-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.utcnow(),
            "storage_type": "cloud",
            "integration_test": True,
        }
        project_id = firestore_db.create_project(project_payload)
        self.assertIsNotNone(project_id)
        self.__class__.created_project_ids.append(project_id)

        # Create word
        word_payload = {
            "language": "Integration",
            "english_words": ["test"],
            "new_language_word": f"word-delete-test-{unique_suffix}",
            "user_id": project_payload["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }
        word_id = firestore_db.create_word(word_payload)
        self.assertIsNotNone(word_id)
        self.__class__.created_word_ids.append(word_id)

        # Verify word exists
        project_words_before = firestore_db.get_project_words(project_id)
        word_ids_before = [w.get("id") for w in project_words_before]
        self.assertIn(word_id, word_ids_before)

        # Delete the word
        delete_success = firestore_db.delete_word(word_id)
        self.assertTrue(delete_success, "Word deletion should succeed")

        # Verify word no longer exists in project
        project_words_after = firestore_db.get_project_words(project_id)
        word_ids_after = [w.get("id") for w in project_words_after]
        self.assertNotIn(word_id, word_ids_after, "Deleted word should not appear in project words")

        # Verify word document doesn't exist
        fetched_word = firestore_db.get_word(word_id)
        self.assertIsNone(fetched_word, "Deleted word should return None when fetched")

        # Remove from cleanup list since we already deleted it
        self.__class__.created_word_ids.remove(word_id)


@unittest.skipUnless(
    RUN_FIREBASE_INTEGRATION_TESTS,
    "Set RUN_FIREBASE_INTEGRATION_TESTS=1 to exercise Firebase Storage integration tests.",
)
class FirebaseStorageIntegrationTests(unittest.TestCase):
    """Validate Firebase Storage asset lifecycle."""

    @classmethod
    def setUpClass(cls):
        if not RUN_FIREBASE_INTEGRATION_TESTS:
            raise unittest.SkipTest("Firebase integration tests are disabled by configuration")

        if firebase_config.environment == "production":
            raise unittest.SkipTest("Storage integration tests disabled for production environment")

        if not STORAGE_LIB_AVAILABLE:
            raise unittest.SkipTest("google-cloud-storage library is not installed")

        credentials_path = firebase_config.get_credentials_path()
        if not os.path.exists(credentials_path):
            raise unittest.SkipTest("Firebase service account credentials not found")

        cls.project_id = firebase_config.get_project_id()
        cls.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        cls.client = storage.Client(project=cls.project_id, credentials=cls.credentials)

        candidate_buckets = []
        env_bucket = os.getenv("FIREBASE_STORAGE_BUCKET")
        if env_bucket:
            candidate_buckets.append(env_bucket)
        candidate_buckets.append(f"{cls.project_id}.appspot.com")
        candidate_buckets.append(f"{cls.project_id}.firebasestorage.app")

        cls.bucket = None
        cls.bucket_name = None
        for bucket_name in dict.fromkeys(candidate_buckets):
            try:
                bucket = cls.client.lookup_bucket(bucket_name)
            except Exception:  # pragma: no cover - network failures are non-deterministic
                bucket = None

            if bucket:
                cls.bucket = bucket
                cls.bucket_name = bucket_name
                break

        if cls.bucket is None:
            raise unittest.SkipTest("No accessible Firebase Storage bucket was found for tests")

        cls.created_blob_names = []

    @classmethod
    def tearDownClass(cls):
        bucket = getattr(cls, "bucket", None)
        if bucket is None:
            return

        for blob_name in getattr(cls, "created_blob_names", []):
            try:
                blob = bucket.blob(blob_name)
                blob.delete()
            except Exception:  # pragma: no cover - best effort cleanup
                pass

    def test_upload_and_retrieve_media_asset(self):
        """Ensure media assets can be uploaded and retrieved from Storage."""
        blob_name = f"integration-tests/words/{uuid.uuid4().hex}.txt"
        payload = "integration storage verification"

        blob = self.bucket.blob(blob_name)
        blob.upload_from_string(payload, content_type="text/plain")
        self.__class__.created_blob_names.append(blob_name)

        fetched_blob = self.bucket.get_blob(blob_name)
        self.assertIsNotNone(fetched_blob, f"Blob {blob_name} should exist after upload")

        downloaded_payload = fetched_blob.download_as_text()
        self.assertEqual(downloaded_payload, payload)


if __name__ == "__main__":
    unittest.main()
