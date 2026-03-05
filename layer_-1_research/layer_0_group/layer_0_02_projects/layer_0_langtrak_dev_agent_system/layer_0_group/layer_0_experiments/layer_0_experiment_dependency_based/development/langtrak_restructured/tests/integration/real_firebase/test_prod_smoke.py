# resource_id: "b5a97eeb-5fe8-4b56-81e4-574680f9a603"
# resource_type: "document"
# resource_name: "test_prod_smoke"
"""
Production Smoke Tests (READ-ONLY!)

CRITICAL: These tests ONLY perform READ operations on production.
NO WRITES, NO DELETES, NO MODIFICATIONS!

Run with:
    FIREBASE_TEST_ENV=production \
    ALLOW_PROD_TESTS=yes_i_know_what_im_doing \
    RUN_FIREBASE_INTEGRATION_TESTS=1 \
    pytest tests/integration/real_firebase/test_prod_smoke.py -v
"""

import pytest
from services.firebase import firebase_config, firestore_db, clean_firebase_service


@pytest.mark.real_firebase
@pytest.mark.production
@pytest.mark.smoke
@pytest.mark.slow
class TestProductionSmoke:
    """
    Minimal smoke tests for production environment.

    IMPORTANT: Only READ operations allowed!
    """

    def test_firestore_accessible(self, firebase_environment):
        """Verify Firestore is accessible (read-only check)"""
        # Verify we're in production environment
        assert firebase_environment == "production"
        firebase_config.refresh()
        assert firebase_config.environment == "production"
        assert firebase_config.get_project_id() == "lang-trak-prod"

        assert clean_firebase_service.is_available()
        assert firestore_db._service.db is not None

    def test_collections_readable(self, firebase_environment):
        """Verify collections are readable"""
        assert firebase_environment == "production"
        firebase_config.refresh()

        collections = [
            firestore_db.PROJECTS_COLLECTION,
            firestore_db.USERS_COLLECTION,
        ]

        for collection in collections:
            # Only read, limit to 1 for minimal impact
            docs = clean_firebase_service.get_documents(collection, limit=1)
            assert isinstance(docs, list)

    def test_project_query_works(self, firebase_environment):
        """Verify project queries work"""
        assert firebase_environment == "production"
        firebase_config.refresh()

        # Simple query to verify production database is responsive
        docs = clean_firebase_service.get_documents(
            firestore_db.PROJECTS_COLLECTION,
            limit=5
        )
        assert isinstance(docs, list)

    # NO WRITE TESTS IN PRODUCTION!
    # NO DELETE TESTS IN PRODUCTION!
    # NO MODIFICATION TESTS IN PRODUCTION!
