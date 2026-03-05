# resource_id: "7bd173d1-fd5f-4624-88e0-fe75f2486322"
# resource_type: "document"
# resource_name: "routes"
"""
L3 Users Layer Routes

Routes for user search and profile management.
Depends on: L2 Infrastructure (auth, firebase)
"""

from flask import request, jsonify

from . import l3_bp
from l2_infrastructure.auth import require_auth
from l2_infrastructure.firebase import firestore_db


# ── L3.2 User Profiles ──────────────────────────────────────────────────────

@l3_bp.route('/api/users/search', methods=['GET'])
@require_auth
def api_search_users():
    """Search users by username or email"""
    try:
        query = request.args.get('q', '').strip()
        if len(query) < 2:
            return jsonify({'success': False, 'error': 'Search query must be at least 2 characters'})

        users = firestore_db.search_users(query)
        return jsonify({'success': True, 'users': users})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l3_bp.route('/api/users/<user_id>/profile', methods=['GET'])
@require_auth
def api_get_user_profile(user_id):
    """Get user profile information"""
    try:
        profile = firestore_db.get_user_profile(user_id)
        if not profile:
            return jsonify({'success': False, 'error': 'User not found'})

        return jsonify({'success': True, 'user': profile})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
