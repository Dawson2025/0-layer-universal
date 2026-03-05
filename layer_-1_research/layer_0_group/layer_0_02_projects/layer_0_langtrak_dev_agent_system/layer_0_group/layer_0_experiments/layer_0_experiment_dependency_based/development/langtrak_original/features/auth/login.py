# resource_id: "fe2eff87-5cb1-437e-9972-56c86686a394"
# resource_type: "document"
# resource_name: "login"
"""User login functionality."""

from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash
import sqlite3

from core.database import DB_NAME
from features.firebase import get_firebase_client_config
from . import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login route - supports both Firebase and legacy authentication"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        if not email or not password:
            flash('Email and password are required', 'error')
            return render_template('login.html')

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, password_hash FROM users WHERE email = ? AND is_active = 1", (email,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data and check_password_hash(user_data[2], password):
            session['user_id'] = user_data[0]
            session['username'] = user_data[1]
            flash(f'Welcome back, {user_data[1]}!', 'success')

            # Check for pending group invite
            if 'pending_group_invite' in session:
                invite_token = session.pop('pending_group_invite')
                return redirect(url_for('groups.join_group_via_invite', invite_token=invite_token))

            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')

    # Inject Firebase configuration for the template
    firebase_config = get_firebase_client_config()
    if not firebase_config.get('apiKey') or not firebase_config.get('appId'):
        print("Warning: Firebase client config missing apiKey/appId. "
              "Set VITE_FIREBASE_* environment variables or update firebase-config.js.")

    return render_template('login.html', firebase_config=firebase_config)


@auth_bp.route('/logout')
def logout():
    """Logout route"""
    session.clear()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('index'))
