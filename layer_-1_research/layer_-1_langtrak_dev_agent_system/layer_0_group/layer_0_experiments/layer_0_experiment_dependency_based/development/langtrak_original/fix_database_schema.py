#!/usr/bin/env python3
"""
Fix database schema to allow NULL password_hash for Google OAuth users
"""
import sqlite3
import os

def fix_database_schema():
    """Make password_hash nullable for Google OAuth users"""
    db_path = "data/phonemes.db"
    
    if not os.path.exists(db_path):
        print(f"❌ Database file {db_path} not found")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check current schema
        cursor.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        print("Current users table schema:")
        for col in columns:
            print(f"  {col[1]} {col[2]} {'NOT NULL' if col[3] else 'NULL'}")
        
        # SQLite doesn't support ALTER COLUMN, so we need to recreate the table
        print("\n🔧 Recreating users table with nullable password_hash...")
        
        # Create new table with nullable password_hash
        cursor.execute("""
            CREATE TABLE users_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT,  -- Made nullable for Google OAuth
                firebase_uid TEXT UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        """)
        
        # Copy data from old table to new table
        cursor.execute("""
            INSERT INTO users_new (id, username, email, password_hash, firebase_uid, created_at, is_active)
            SELECT id, username, email, password_hash, firebase_uid, created_at, is_active
            FROM users
        """)
        
        # Drop old table and rename new table
        cursor.execute("DROP TABLE users")
        cursor.execute("ALTER TABLE users_new RENAME TO users")
        
        conn.commit()
        print("✅ Database schema updated successfully!")
        
        # Verify the new schema
        cursor.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        print("\nNew users table schema:")
        for col in columns:
            print(f"  {col[1]} {col[2]} {'NOT NULL' if col[3] else 'NULL'}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error updating database schema: {e}")
        return False

if __name__ == "__main__":
    success = fix_database_schema()
    if success:
        print("\n🎉 Database schema fix completed!")
    else:
        print("\n💥 Database schema fix failed!")
