"""
Development Environment Verification Tests.

These tests verify that the lang-trak-dev Firebase project is correctly configured.
Run with: FIREBASE_TEST_ENV=development RUN_FIREBASE_INTEGRATION_TESTS=1 pytest tests/integration/real_firebase/test_dev_environment.py -v
"""

import pytest
import uuid
from datetime import datetime, timezone
from services.firebase import firebase_config, firestore_db, clean_firebase_service


@pytest.mark.real_firebase
@pytest.mark.dev
@pytest.mark.slow
class TestDevEnvironment:
    """Verify lang-trak-dev Firebase environment is correctly configured"""

    @classmethod
    def setup_class(cls):
        """Verify we're in dev environment"""
        assert firebase_config.environment == "development", \
            f"Expected development environment, got: {firebase_config.environment}"
        assert firebase_config.get_project_id() == "lang-trak-dev", \
            f"Expected lang-trak-dev project, got: {firebase_config.get_project_id()}"

    def test_firestore_connection(self):
        """Verify Firestore is accessible"""
        assert clean_firebase_service.is_available()
        assert firestore_db._service.db is not None

    def test_collections_accessible(self):
        """Verify all required collections are accessible"""
        collections = [
            firestore_db.PROJECTS_COLLECTION,
            firestore_db.WORDS_COLLECTION,
            firestore_db.PHONEMES_COLLECTION,
            firestore_db.GROUPS_COLLECTION,
            firestore_db.USERS_COLLECTION,
        ]

        for collection in collections:
            # Try to query each collection (limit 1 for speed)
            docs = clean_firebase_service.get_documents(collection, limit=1)
            assert isinstance(docs, list), f"Failed to query {collection}"

    def test_project_crud_operations(self, cleanup_test_data):
        """Verify project create, read, delete operations work"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create
        project_data = {
            "name": f"Dev Test Project {unique_suffix}",
            "user_id": f"dev-test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "storage_type": "cloud",
            "integration_test": True,
        }

        project_id = firestore_db.create_project(project_data)
        assert project_id is not None
        cleanup_test_data.add_project(project_id)

        # Read
        project = firestore_db.get_project(project_id)
        assert project is not None
        assert project.get("name") == f"Dev Test Project {unique_suffix}"
        assert project.get("id") == project_id

        # Delete is handled by cleanup_test_data fixture

    def test_word_crud_operations(self, cleanup_test_data):
        """Verify word create, read, delete operations work"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project first
        project_data = {
            "name": f"Word Test Project {unique_suffix}",
            "user_id": f"dev-test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        project_id = firestore_db.create_project(project_data)
        cleanup_test_data.add_project(project_id)

        # Create word
        word_data = {
            "new_language_word": f"devword-{unique_suffix}",
            "english_words": ["dev", "test"],
            "user_id": project_data["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }

        word_id = firestore_db.create_word(word_data)
        assert word_id is not None
        cleanup_test_data.add_word(word_id)

        # Read
        words = firestore_db.get_project_words(project_id)
        assert any(w.get("id") == word_id for w in words)

    def test_phoneme_crud_operations(self, cleanup_test_data):
        """Verify phoneme create, read, delete operations work"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project
        project_data = {
            "name": f"Phoneme Test Project {unique_suffix}",
            "user_id": f"dev-test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        project_id = firestore_db.create_project(project_data)
        cleanup_test_data.add_project(project_id)

        # Create phoneme
        phoneme_data = {
            "phoneme": "p",
            "position": "onset",
            "syllable_type": "CVC",
            "user_id": project_data["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }

        phoneme_id = firestore_db.create_phoneme(phoneme_data)
        assert phoneme_id is not None
        cleanup_test_data.add_phoneme(phoneme_id)

        # Read
        phonemes = firestore_db.get_project_phonemes(project_id)
        assert any(p.get("id") == phoneme_id for p in phonemes)

    def test_group_crud_operations(self, cleanup_test_data):
        """Verify group create, read, delete operations work"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create group
        group_data = {
            "name": f"Dev Test Group {unique_suffix}",
            "description": "Dev environment test",
            "owner_id": f"dev-test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }

        group_id = firestore_db.create_group(group_data)
        assert group_id is not None
        cleanup_test_data.add_group(group_id)

    def test_composite_indexes_work(self, cleanup_test_data):
        """Verify composite indexes are deployed"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project
        project_data = {
            "name": f"Index Test Project {unique_suffix}",
            "user_id": f"dev-test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        project_id = firestore_db.create_project(project_data)
        cleanup_test_data.add_project(project_id)

        # Create multiple phonemes with different positions
        for position in ["onset", "nucleus", "coda"]:
            phoneme_data = {
                "phoneme": "test",
                "position": position,
                "user_id": project_data["user_id"],
                "project_id": project_id,
                "created_at": datetime.now(timezone.utc),
            }
            phoneme_id = firestore_db.create_phoneme(phoneme_data)
            cleanup_test_data.add_phoneme(phoneme_id)

        # Query requiring composite index (project_id + position)
        # If index missing, this would fail
        phonemes = firestore_db.get_project_phonemes(project_id)
        assert len(phonemes) == 3
