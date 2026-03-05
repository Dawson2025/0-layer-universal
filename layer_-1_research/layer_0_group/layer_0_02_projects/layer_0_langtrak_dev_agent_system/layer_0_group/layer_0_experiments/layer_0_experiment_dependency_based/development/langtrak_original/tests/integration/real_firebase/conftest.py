# resource_id: "d5e35903-fc96-4a7c-9f95-205d9e755933"
# resource_type: "document"
# resource_name: "conftest"
"""
Configuration for real Firebase environment tests.

These tests run against actual Firebase projects (dev, staging, production).
"""

import pytest
import os


def pytest_configure(config):
    """Register custom markers for real Firebase tests"""
    config.addinivalue_line(
        "markers", "real_firebase: mark test as requiring real Firebase connection"
    )
    config.addinivalue_line(
        "markers", "dev: mark test for development environment"
    )
    config.addinivalue_line(
        "markers", "staging: mark test for staging environment"
    )
    config.addinivalue_line(
        "markers", "production: mark test for production environment (DANGEROUS!)"
    )
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test (minimal, safe)"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow-running"
    )


@pytest.fixture(scope="session")
def firebase_environment():
    """
    Configure Firebase environment for testing.

    Determines which Firebase project to use based on:
    1. FIREBASE_TEST_ENV environment variable
    2. Validates proper credentials are set
    3. Applies safety checks for production
    """
    # Get environment from env var (default to development)
    env = os.getenv("FIREBASE_TEST_ENV", "development")

    # Ensure RUN_FIREBASE_INTEGRATION_TESTS is set
    if not os.getenv("RUN_FIREBASE_INTEGRATION_TESTS"):
        pytest.skip("Real Firebase tests disabled. Set RUN_FIREBASE_INTEGRATION_TESTS=1 to enable")

    # Ensure emulator variables are NOT set
    if os.getenv("FIRESTORE_EMULATOR_HOST"):
        del os.environ["FIRESTORE_EMULATOR_HOST"]
    if os.getenv("FIREBASE_AUTH_EMULATOR_HOST"):
        del os.environ["FIREBASE_AUTH_EMULATOR_HOST"]
    if os.getenv("FIREBASE_STORAGE_EMULATOR_HOST"):
        del os.environ["FIREBASE_STORAGE_EMULATOR_HOST"]

    # Set appropriate configuration based on environment
    # Set FIREBASE_ENV so firebase_config picks up the right environment
    os.environ["FIREBASE_ENV"] = env

    if env == "development":
        # Use dev project
        os.environ["FIREBASE_PROJECT"] = "lang-trak-dev"
        # Credentials should be in firebase-admin-config.json or environment

    elif env == "staging":
        # Use staging project
        os.environ["FIREBASE_PROJECT"] = "lang-trak-staging"
        # Would use staging credentials

    elif env == "production":
        # EXTRA SAFETY CHECKS for production
        if os.getenv("ALLOW_PROD_TESTS") != "yes_i_know_what_im_doing":
            pytest.skip(
                "Production tests require explicit confirmation. "
                "Set ALLOW_PROD_TESTS=yes_i_know_what_im_doing"
            )
        os.environ["FIREBASE_PROJECT"] = "lang-trak-prod"
        # Would use production credentials (READ-ONLY!)

    else:
        pytest.fail(f"Unknown FIREBASE_TEST_ENV: {env}. Use: development, staging, or production")

    # Import Firebase to ensure it initializes with correct environment
    from services.firebase import clean_firebase_service, firebase_config

    # IMPORTANT: Refresh firebase_config to pick up the environment variable we just set
    firebase_config.refresh()

    # Verify Firebase is available
    if not clean_firebase_service.is_available():
        pytest.skip(f"Firebase service not available for {env} environment")

    # Verify we're not accidentally in production when we shouldn't be
    actual_env = firebase_config.environment
    if env == "production" and actual_env != "production":
        pytest.fail(f"Expected production environment but got: {actual_env}")

    print(f"\n🔥 Using Firebase environment: {env}")
    print(f"   Project: {firebase_config.get_project_id()}")

    yield env

    print(f"\n✅ Completed tests for {env} environment")


@pytest.fixture
def cleanup_test_data():
    """
    Track and cleanup test data created during tests.

    Usage:
        def test_something(cleanup_test_data):
            project_id = create_project(...)
            cleanup_test_data.add_project(project_id)
            # Test will automatically clean up project after completion
    """
    from services.firebase import clean_firebase_service, firestore_db

    class TestDataCleaner:
        def __init__(self):
            self.projects = []
            self.words = []
            self.phonemes = []
            self.groups = []

        def add_project(self, project_id):
            self.projects.append(project_id)

        def add_word(self, word_id):
            self.words.append(word_id)

        def add_phoneme(self, phoneme_id):
            self.phonemes.append(phoneme_id)

        def add_group(self, group_id):
            self.groups.append(group_id)

        def cleanup(self):
            """Clean up all tracked test data"""
            # Clean up in reverse order of dependencies
            for phoneme_id in self.phonemes:
                try:
                    clean_firebase_service.delete_document(firestore_db.PHONEMES_COLLECTION, phoneme_id)
                except Exception as e:
                    print(f"Warning: Failed to cleanup phoneme {phoneme_id}: {e}")

            for word_id in self.words:
                try:
                    clean_firebase_service.delete_document(firestore_db.WORDS_COLLECTION, word_id)
                except Exception as e:
                    print(f"Warning: Failed to cleanup word {word_id}: {e}")

            for group_id in self.groups:
                try:
                    clean_firebase_service.delete_document(firestore_db.GROUPS_COLLECTION, group_id)
                except Exception as e:
                    print(f"Warning: Failed to cleanup group {group_id}: {e}")

            for project_id in self.projects:
                try:
                    clean_firebase_service.delete_document(firestore_db.PROJECTS_COLLECTION, project_id)
                except Exception as e:
                    print(f"Warning: Failed to cleanup project {project_id}: {e}")

    cleaner = TestDataCleaner()
    yield cleaner

    # Cleanup after test completes
    cleaner.cleanup()
