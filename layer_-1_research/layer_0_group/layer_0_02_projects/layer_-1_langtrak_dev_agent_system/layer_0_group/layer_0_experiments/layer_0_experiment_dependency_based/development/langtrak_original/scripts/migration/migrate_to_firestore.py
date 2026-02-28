#!/usr/bin/env python3
"""
Migration Script: SQLite to Firestore
Migrates all data from the existing SQLite database to Firestore collections
"""
import sqlite3
import json
import sys
import os
from datetime import datetime

# Add the current directory to Python path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.firebase import firebase_service, firestore_db

# Database configuration
DB_NAME = 'data/phonemes.db'

def migrate_users():
    """Migrate users from SQLite to Firestore"""
    print("Migrating users...")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, username, email, password_hash, firebase_uid, created_at, is_active
        FROM users
    """)
    
    users = cursor.fetchall()
    conn.close()
    
    migrated_count = 0
    user_id_mapping = {}  # Old ID -> New ID mapping
    
    for user in users:
        old_id, username, email, password_hash, firebase_uid, created_at, is_active = user
        
        # Check if user already exists in Firestore
        existing_user = None
        if firebase_uid:
            existing_user = firestore_db.get_user_by_firebase_uid(firebase_uid)
        if not existing_user:
            existing_user = firestore_db.get_user_by_email(email)
        
        if existing_user:
            print(f"User {email} already exists in Firestore")
            user_id_mapping[old_id] = existing_user['id']
            continue
        
        user_data = {
            'username': username,
            'email': email,
            'password_hash': password_hash or '',
            'firebase_uid': firebase_uid,
            'created_at': datetime.fromisoformat(created_at) if created_at else datetime.utcnow(),
            'is_active': bool(is_active)
        }
        
        new_user_id = firestore_db.create_user(user_data)
        if new_user_id:
            user_id_mapping[old_id] = new_user_id
            migrated_count += 1
            print(f"Migrated user: {username} ({email})")
        else:
            print(f"Failed to migrate user: {username} ({email})")
    
    print(f"Migrated {migrated_count} users")
    return user_id_mapping

def migrate_projects(user_id_mapping):
    """Migrate projects from SQLite to Firestore"""
    print("Migrating projects...")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, name, user_id, created_at, updated_at
        FROM projects
    """)
    
    projects = cursor.fetchall()
    conn.close()
    
    migrated_count = 0
    project_id_mapping = {}  # Old ID -> New ID mapping
    
    for project in projects:
        old_id, name, user_id, created_at, updated_at = project
        
        # Map old user ID to new user ID
        if user_id not in user_id_mapping:
            print(f"Skipping project {name} - user {user_id} not found in mapping")
            continue
        
        new_user_id = user_id_mapping[user_id]
        
        project_data = {
            'name': name,
            'user_id': new_user_id,
            'created_at': datetime.fromisoformat(created_at) if created_at else datetime.utcnow(),
            'updated_at': datetime.fromisoformat(updated_at) if updated_at else datetime.utcnow()
        }
        
        new_project_id = firestore_db.create_project(project_data)
        if new_project_id:
            project_id_mapping[old_id] = new_project_id
            migrated_count += 1
            print(f"Migrated project: {name}")
        else:
            print(f"Failed to migrate project: {name}")
    
    print(f"Migrated {migrated_count} projects")
    return project_id_mapping

def migrate_phonemes(user_id_mapping, project_id_mapping):
    """Migrate phonemes from SQLite to Firestore"""
    print("Migrating phonemes...")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, syllable_type, position, length_type, group_type, subgroup_type,
               sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency,
               project_id, user_id
        FROM phonemes
    """)
    
    phonemes = cursor.fetchall()
    conn.close()
    
    migrated_count = 0
    
    for phoneme in phonemes:
        (old_id, syllable_type, position, length_type, group_type, subgroup_type,
         sub_subgroup_type, sub_sub_subgroup_type, phoneme_char, frequency,
         project_id, user_id) = phoneme
        
        # Map IDs if they exist
        new_project_id = project_id_mapping.get(project_id) if project_id else None
        new_user_id = user_id_mapping.get(user_id) if user_id else None
        
        phoneme_data = {
            'syllable_type': syllable_type,
            'position': position,
            'length_type': length_type,
            'group_type': group_type,
            'subgroup_type': subgroup_type,
            'sub_subgroup_type': sub_subgroup_type,
            'sub_sub_subgroup_type': sub_sub_subgroup_type,
            'phoneme': phoneme_char,
            'frequency': frequency or 0,
            'project_id': new_project_id,
            'user_id': new_user_id
        }
        
        new_phoneme_id = firestore_db.create_phoneme(phoneme_data)
        if new_phoneme_id:
            migrated_count += 1
            print(f"Migrated phoneme: {phoneme_char} ({position})")
        else:
            print(f"Failed to migrate phoneme: {phoneme_char}")
    
    print(f"Migrated {migrated_count} phonemes")

def migrate_words(user_id_mapping, project_id_mapping):
    """Migrate words from SQLite to Firestore"""
    print("Migrating words...")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, language, english_words, new_language_word, ipa_phonetics,
               dictionary_phonetics, video_path, syllable_type, onset_phoneme,
               onset_length_type, nucleus_phoneme, nucleus_length_type,
               coda_phoneme, coda_length_type, user_id, project_id
        FROM words
    """)
    
    words = cursor.fetchall()
    conn.close()
    
    migrated_count = 0
    
    for word in words:
        (old_id, language, english_words, new_language_word, ipa_phonetics,
         dictionary_phonetics, video_path, syllable_type, onset_phoneme,
         onset_length_type, nucleus_phoneme, nucleus_length_type,
         coda_phoneme, coda_length_type, user_id, project_id) = word
        
        # Map IDs if they exist
        new_project_id = project_id_mapping.get(project_id) if project_id else None
        new_user_id = user_id_mapping.get(user_id) if user_id else None
        
        word_data = {
            'language': language,
            'english_words': english_words,
            'new_language_word': new_language_word,
            'ipa_phonetics': ipa_phonetics,
            'dictionary_phonetics': dictionary_phonetics,
            'video_path': video_path,
            'syllable_type': syllable_type,
            'onset_phoneme': onset_phoneme,
            'onset_length_type': onset_length_type,
            'nucleus_phoneme': nucleus_phoneme,
            'nucleus_length_type': nucleus_length_type,
            'coda_phoneme': coda_phoneme,
            'coda_length_type': coda_length_type,
            'user_id': new_user_id,
            'project_id': new_project_id
        }
        
        new_word_id = firestore_db.create_word(word_data)
        if new_word_id:
            migrated_count += 1
            print(f"Migrated word: {new_language_word or 'Unnamed'}")
        else:
            print(f"Failed to migrate word: {new_language_word or 'Unnamed'}")
    
    print(f"Migrated {migrated_count} words")

def migrate_groups(user_id_mapping):
    """Migrate groups from SQLite to Firestore"""
    print("Migrating groups...")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Check if groups table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='groups'")
    if not cursor.fetchone():
        print("Groups table doesn't exist, skipping...")
        conn.close()
        return {}
    
    cursor.execute("""
        SELECT id, name, description, admin_user_id, created_at
        FROM groups
    """)
    
    groups = cursor.fetchall()
    conn.close()
    
    migrated_count = 0
    group_id_mapping = {}
    
    for group in groups:
        old_id, name, description, admin_user_id, created_at = group
        
        # Map admin user ID
        new_admin_user_id = user_id_mapping.get(admin_user_id) if admin_user_id else None
        
        group_data = {
            'name': name,
            'description': description,
            'admin_user_id': new_admin_user_id,
            'created_at': datetime.fromisoformat(created_at) if created_at else datetime.utcnow()
        }
        
        new_group_id = firestore_db.create_group(group_data)
        if new_group_id:
            group_id_mapping[old_id] = new_group_id
            migrated_count += 1
            print(f"Migrated group: {name}")
        else:
            print(f"Failed to migrate group: {name}")
    
    print(f"Migrated {migrated_count} groups")
    return group_id_mapping

def main():
    """Main migration function"""
    print("Starting migration from SQLite to Firestore...")
    print("=" * 50)
    
    # Check if Firebase is properly initialized
    if not firebase_service.db:
        print("Error: Firebase/Firestore not properly initialized!")
        print("Make sure you have proper Firebase credentials configured.")
        return False
    
    try:
        # Migrate in order of dependencies
        user_id_mapping = migrate_users()
        project_id_mapping = migrate_projects(user_id_mapping)
        group_id_mapping = migrate_groups(user_id_mapping)
        migrate_phonemes(user_id_mapping, project_id_mapping)
        migrate_words(user_id_mapping, project_id_mapping)
        
        print("=" * 50)
        print("Migration completed successfully!")
        print(f"Migrated {len(user_id_mapping)} users")
        print(f"Migrated {len(project_id_mapping)} projects")
        print(f"Migrated {len(group_id_mapping)} groups")
        
        return True
        
    except Exception as e:
        print(f"Migration failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = main()
    if not success:
        sys.exit(1)