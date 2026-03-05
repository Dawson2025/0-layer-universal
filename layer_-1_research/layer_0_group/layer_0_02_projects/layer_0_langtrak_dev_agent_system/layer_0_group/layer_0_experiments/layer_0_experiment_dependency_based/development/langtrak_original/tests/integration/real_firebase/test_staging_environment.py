# resource_id: "d5a1a908-af3f-4d2e-8803-e450699cbfe4"
# resource_type: "document"
# resource_name: "test_staging_environment"
"""
Staging Environment Verification Tests.

These tests verify that the staging Firebase project is correctly configured.
Run with: FIREBASE_TEST_ENV=staging RUN_FIREBASE_INTEGRATION_TESTS=1 pytest tests/integration/real_firebase/test_staging_environment.py -v
"""

import pytest
import uuid
from datetime import datetime, timezone
from services.firebase import firebase_config, firestore_db, clean_firebase_service


@pytest.mark.real_firebase
@pytest.mark.staging
@pytest.mark.slow
class TestStagingEnvironment:
    """Verify staging Firebase environment is correctly configured"""

    @classmethod
    def setup_class(cls):
        """Verify we're in staging environment"""
        # Note: Adjust this based on your actual staging environment name
        # assert firebase_config.environment == "staging"
        # assert firebase_config.get_project_id() == "lang-trak-staging"
        pass  # Implement when staging environment is ready

    def test_firestore_connection(self):
        """Verify Firestore is accessible in staging"""
        assert clean_firebase_service.is_available()
        assert firestore_db._service.db is not None

    def test_collections_accessible(self):
        """Verify all required collections are accessible"""
        collections = [
            firestore_db.PROJECTS_COLLECTION,
            firestore_db.WORDS_COLLECTION,
            firestore_db.PHONEMES_COLLECTION,
            firestore_db.GROUPS_COLLECTION,
        ]

        for collection in collections:
            docs = clean_firebase_service.get_documents(collection, limit=1)
            assert isinstance(docs, list)

    def test_basic_crud_operations(self, cleanup_test_data):
        """Verify basic CRUD operations work in staging"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project
        project_data = {
            "name": f"Staging Test {unique_suffix}",
            "user_id": f"staging-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "integration_test": True,
        }

        project_id = firestore_db.create_project(project_data)
        assert project_id is not None
        cleanup_test_data.add_project(project_id)

        # Verify can read
        project = firestore_db.get_project(project_id)
        assert project is not None
