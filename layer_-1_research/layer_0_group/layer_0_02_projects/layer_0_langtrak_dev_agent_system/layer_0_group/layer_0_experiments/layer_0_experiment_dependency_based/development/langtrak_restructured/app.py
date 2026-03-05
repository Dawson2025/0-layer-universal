# resource_id: "a332b3fb-f3c6-48bf-b3f9-865413643acf"
# resource_type: "document"
# resource_name: "app"
"""
LangTrak Application Factory

Dependency-based layer architecture (L2-L8).
Each layer is a Flask Blueprint registered in dependency order.

Layer Dependency Chain:
  L2 Infrastructure (foundation — no deps)
  L3 Users (depends on L2)
  L4 Phoneme System (depends on L2, L3)
  L5 Templates (depends on L2, L3, L4)
  L6 Language Content (depends on L2, L3, L4)
  L7 Projects (depends on L2, L3, L4, L5, L6)
  L8 Teams (depends on L2, L3, L7)
"""

import os
import sqlite3

from flask import Flask

import main

# ── App Factory ──────────────────────────────────────────────────────────────

_app_initialized = False
app = None


def create_app():
    """Create and configure the Flask application.

    Registers all layer blueprints in dependency order.
    Safe to call multiple times — initialization only happens once.
    """
    global app, _app_initialized

    if _app_initialized:
        return app

    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY', 'phoneme_tracker_secret_key_2024')
    app.config['UPLOAD_FOLDER'] = 'videos'

    # ── Initialize Database ──────────────────────────────────────────────
    main.migrate_schema()

    # ── Register Layer Blueprints (dependency order) ─────────────────────

    # L2 Infrastructure — foundation layer (auth, firebase, storage, TTS, db admin)
    from l2_infrastructure import l2_bp
    app.register_blueprint(l2_bp)

    # L3 Users — user model, profiles, sessions (depends on L2)
    from l3_users import l3_bp
    app.register_blueprint(l3_bp)

    # L4 Phoneme System — phoneme groups, types, frequency, display, admin (depends on L2, L3)
    from l4_phoneme_system import l4_bp
    app.register_blueprint(l4_bp)

    # L5 Templates — template core, phoneme selection, application, admin (depends on L2, L3, L4)
    from l5_templates import l5_bp
    app.register_blueprint(l5_bp)

    # L6 Language Content — words, syllables, TTS, suggestions, video (depends on L2, L3, L4)
    from l6_language_content import l6_bp
    app.register_blueprint(l6_bp)

    # L7 Projects — project core, dashboard, navigation, variants (depends on L2, L3, L5, L6)
    from l7_projects import l7_bp
    app.register_blueprint(l7_bp)

    # L8 Teams — team model, membership, invites, project sharing (depends on L2, L3, L7)
    from l8_teams import l8_bp
    app.register_blueprint(l8_bp)

    _app_initialized = True
    return app


# ── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
