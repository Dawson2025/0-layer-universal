# resource_id: "3bf3d229-db15-4d35-a0bc-735945766aa9"
# resource_type: "document"
# resource_name: "registration"
"""User registration functionality."""

from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash
import sqlite3

from core.database import DB_NAME
from . import auth_bp


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registration route"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Validation
        if not username or not email or not password:
            flash('All fields are required', 'error')
            return render_template('register.html')

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')

        if len(password) < 6:
            flash('Password must be at least 6 characters long', 'error')
            return render_template('register.html')

        # Check if user already exists
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ? OR username = ?", (email, username))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email or username already exists', 'error')
            conn.close()
            return render_template('register.html')

        # Create new user
        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        # Log them in automatically
        session['user_id'] = user_id
        session['username'] = username
        flash(f'Account created successfully! Welcome, {username}!', 'success')

        # Check for pending group invite
        if 'pending_group_invite' in session:
            invite_token = session.pop('pending_group_invite')
            return redirect(url_for('groups.join_group_via_invite', invite_token=invite_token))

        return redirect(url_for('index'))

    return render_template('register.html')
