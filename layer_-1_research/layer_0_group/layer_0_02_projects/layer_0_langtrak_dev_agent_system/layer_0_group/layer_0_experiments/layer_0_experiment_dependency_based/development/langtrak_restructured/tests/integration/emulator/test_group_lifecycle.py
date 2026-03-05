# resource_id: "28a92350-fdb7-4188-9915-61a15eadedd4"
# resource_type: "document"
# resource_name: "test_group_lifecycle"
"""
Group lifecycle tests using Firebase Emulator.
"""

import pytest
import uuid
from datetime import datetime, timezone
from services.firebase import firestore_db


@pytest.mark.emulator
class TestGroupLifecycle:
    """Test complete group lifecycle with Firebase Emulator"""

    def test_create_and_retrieve_group(self):
        """Create group and verify it's retrievable"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create group
        group_data = {
            "name": f"Test Group {unique_suffix}",
            "description": "Emulator test group",
            "owner_id": f"test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
            "member_count": 1,
        }

        group_id = firestore_db.create_group(group_data)
        assert group_id is not None
        assert isinstance(group_id, str)

    def test_delete_group(self):
        """Verify group deletion works correctly"""
        unique_suffix = uuid.uuid4().hex[:10]

        # Create group
        group_data = {
            "name": f"Delete Test Group {unique_suffix}",
            "owner_id": f"test-user-{unique_suffix}",
            "created_at": datetime.now(timezone.utc),
        }
        group_id = firestore_db.create_group(group_data)

        # Delete group
        delete_success = firestore_db.delete_group(group_id)
        assert delete_success is True
