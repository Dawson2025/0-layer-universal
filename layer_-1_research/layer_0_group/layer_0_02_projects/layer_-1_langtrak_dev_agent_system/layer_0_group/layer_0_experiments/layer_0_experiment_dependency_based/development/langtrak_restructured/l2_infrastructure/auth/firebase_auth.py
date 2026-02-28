"""Firebase authentication integration."""

from flask import jsonify, request, session
import sqlite3

from core.database import DB_NAME
from . import auth_bp


@auth_bp.route('/api/auth/firebase-login', methods=['POST'])
def firebase_login():
    """Handle Firebase authentication login"""
    try:
        data = request.get_json()
        firebase_uid = data.get('uid')
        email = data.get('email')
        display_name = data.get('displayName')
        photo_url = data.get('photoURL')

        if not firebase_uid or not email:
            return jsonify({'success': False, 'error': 'Missing required data'}), 400

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check if user exists with this Firebase UID
        cursor.execute("SELECT id, username, email FROM users WHERE firebase_uid = ?", (firebase_uid,))
        user_data = cursor.fetchone()

        if user_data:
            # User exists, log them in
            user_id = user_data[0]
            username = user_data[1]
        else:
            # Check if user exists with this email (legacy user)
            cursor.execute("SELECT id, username FROM users WHERE email = ?", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                # Update existing user with Firebase UID
                user_id = existing_user[0]
                username = existing_user[1]
                cursor.execute("UPDATE users SET firebase_uid = ? WHERE id = ?", (firebase_uid, user_id))
            else:
                # Create new user
                username = display_name or email.split('@')[0]

                # Ensure username is unique
                base_username = username
                counter = 1
                while True:
                    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
                    if not cursor.fetchone():
                        break
                    username = f"{base_username}_{counter}"
                    counter += 1

                cursor.execute("""
                    INSERT INTO users (username, email, password_hash, firebase_uid)
                    VALUES (?, ?, ?, ?)
                """, (username, email, 'firebase_user', firebase_uid))

                user_id = cursor.lastrowid

        conn.commit()
        conn.close()

        # Set session
        session['firebase_uid'] = firebase_uid
        session['user_id'] = user_id  # Keep for compatibility
        session['username'] = username

        return jsonify({'success': True, 'message': f'Welcome, {username}!'})

    except Exception as e:
        print(f"Firebase login error: {e}")
        return jsonify({'success': False, 'error': 'Authentication failed'}), 500


@auth_bp.route('/api/auth/logout', methods=['POST'])
def api_logout():
    """API logout route for Firebase"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})
