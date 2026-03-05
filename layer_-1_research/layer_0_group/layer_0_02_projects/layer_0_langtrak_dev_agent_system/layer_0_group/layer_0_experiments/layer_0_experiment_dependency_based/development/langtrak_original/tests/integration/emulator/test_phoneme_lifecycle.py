# resource_id: "fe8f9ab3-9dfa-46db-9dac-220400598649"
# resource_type: "document"
# resource_name: "test_phoneme_lifecycle"
"""
Phoneme lifecycle tests using Firebase Emulator.

These tests run fast (locally) and verify phoneme CRUD operations.
"""

import pytest
import uuid
from datetime import datetime, timezone
from services.firebase import firestore_db


@pytest.mark.emulator
class TestPhonemeLifecycle:
    """Test complete phoneme lifecycle with Firebase Emulator"""

    def test_create_and_retrieve_phoneme(self):
        """Create phoneme in emulator and verify it's retrievable"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project first
        project_data = {
            "name": f"Emulator Test Project {unique_suffix}",
            "user_id": f"test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "storage_type": "cloud",
        }
        project_id = firestore_db.create_project(project_data)
        assert project_id is not None

        # Create phoneme
        phoneme_data = {
            "syllable_type": "CVC",
            "position": "onset",
            "length_type": "single_consonants",
            "group_type": "Stops",
            "subgroup_type": "Voiceless",
            "phoneme": "p",
            "frequency": 5,
            "user_id": project_data["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }

        phoneme_id = firestore_db.create_phoneme(phoneme_data)
        assert phoneme_id is not None
        assert isinstance(phoneme_id, str)

        # Retrieve phonemes for project
        phonemes = firestore_db.get_project_phonemes(project_id)
        assert len(phonemes) >= 1

        # Verify our phoneme is in the list
        phoneme_ids = [p.get("id") for p in phonemes]
        assert phoneme_id in phoneme_ids

        # Verify phoneme data
        created_phoneme = next(p for p in phonemes if p.get("id") == phoneme_id)
        assert created_phoneme.get("phoneme") == "p"
        assert created_phoneme.get("position") == "onset"
        assert created_phoneme.get("syllable_type") == "CVC"

    def test_delete_phoneme(self):
        """Verify phoneme deletion works correctly"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project
        project_data = {
            "name": f"Delete Test Project {unique_suffix}",
            "user_id": f"test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        project_id = firestore_db.create_project(project_data)

        # Create phoneme
        phoneme_data = {
            "phoneme": "t",
            "position": "coda",
            "user_id": project_data["user_id"],
            "project_id": project_id,
            "created_at": datetime.now(timezone.utc),
        }
        phoneme_id = firestore_db.create_phoneme(phoneme_data)

        # Verify phoneme exists
        phonemes_before = firestore_db.get_project_phonemes(project_id)
        phoneme_ids_before = [p.get("id") for p in phonemes_before]
        assert phoneme_id in phoneme_ids_before

        # Delete phoneme
        delete_success = firestore_db.delete_phoneme(phoneme_id)
        assert delete_success is True

        # Verify phoneme no longer exists
        phonemes_after = firestore_db.get_project_phonemes(project_id)
        phoneme_ids_after = [p.get("id") for p in phonemes_after]
        assert phoneme_id not in phoneme_ids_after

    def test_multiple_phonemes_per_project(self):
        """Verify multiple phonemes can be created for one project"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create project
        project_data = {
            "name": f"Multi-Phoneme Project {unique_suffix}",
            "user_id": f"test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        project_id = firestore_db.create_project(project_data)

        # Create multiple phonemes
        phonemes_to_create = [
            {"phoneme": "p", "position": "onset"},
            {"phoneme": "a", "position": "nucleus"},
            {"phoneme": "t", "position": "coda"},
        ]

        created_ids = []
        for phoneme_info in phonemes_to_create:
            phoneme_data = {
                **phoneme_info,
                "user_id": project_data["user_id"],
                "project_id": project_id,
                "created_at": datetime.now(timezone.utc),
            }
            phoneme_id = firestore_db.create_phoneme(phoneme_data)
            created_ids.append(phoneme_id)

        # Verify all phonemes exist
        phonemes = firestore_db.get_project_phonemes(project_id)
        assert len(phonemes) == 3

        phoneme_ids = [p.get("id") for p in phonemes]
        for created_id in created_ids:
            assert created_id in phoneme_ids
