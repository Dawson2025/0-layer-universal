"""
Word lifecycle tests using Firebase Emulator.
"""

import pytest
import uuid
from datetime import datetime, timezone
from services.firebase import firestore_db


@pytest.mark.emulator
class TestWordLifecycle:
    """Test complete word lifecycle with Firebase Emulator"""

    def test_create_and_retrieve_word(self):
        """Create word and verify it's retrievable"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project
        project_data = {
            "name": f"Word Test Project {unique_suffix}",
            "user_id": f"test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        project_id = firestore_db.create_project(project_data)

        # Create word
        word_data = {
            "language": "Test Language",
            "english_words": ["hello", "hi"],
            "new_language_word": f"testhello-{unique_suffix}",
            "ipa_phonetics": "həˈloʊ",
            "user_id": project_data["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }

        word_id = firestore_db.create_word(word_data)
        assert word_id is not None

        # Retrieve words for project
        words = firestore_db.get_project_words(project_id)
        assert len(words) >= 1

        word_ids = [w.get("id") for w in words]
        assert word_id in word_ids

        # Verify word data
        created_word = next(w for w in words if w.get("id") == word_id)
        assert created_word.get("new_language_word") == f"testhello-{unique_suffix}"
        assert "hello" in created_word.get("english_words", [])

    def test_delete_word(self):
        """Verify word deletion works correctly"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project and word
        project_data = {
            "name": f"Delete Word Project {unique_suffix}",
            "user_id": f"test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        project_id = firestore_db.create_project(project_data)

        word_data = {
            "new_language_word": f"deletetest-{unique_suffix}",
            "user_id": project_data["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }
        word_id = firestore_db.create_word(word_data)

        # Verify word exists
        words_before = firestore_db.get_project_words(project_id)
        word_ids_before = [w.get("id") for w in words_before]
        assert word_id in word_ids_before

        # Delete word
        delete_success = firestore_db.delete_word(word_id)
        assert delete_success is True

        # Verify word no longer exists
        words_after = firestore_db.get_project_words(project_id)
        word_ids_after = [w.get("id") for w in words_after]
        assert word_id not in word_ids_after

        # Verify direct fetch returns None
        fetched_word = firestore_db.get_word(word_id)
        assert fetched_word is None
