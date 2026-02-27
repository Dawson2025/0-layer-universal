#!/usr/bin/env python3
"""
Check database tables and schema
"""
import sqlite3

def check_database():
    """Check what tables exist in the database"""
    try:
        conn = sqlite3.connect("phonemes.db")
        cursor = conn.cursor()
        
        # List all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print("📋 Tables in phonemes.db:")
        for table in tables:
            print(f"  - {table[0]}")
        
        # Check if users table exists and its schema
        if any('users' in table for table in tables):
            cursor.execute("PRAGMA table_info(users)")
            columns = cursor.fetchall()
            print(f"\n📊 Users table schema:")
            for col in columns:
                print(f"  {col[1]} {col[2]} {'NOT NULL' if col[3] else 'NULL'}")
        else:
            print("\n❌ Users table does not exist")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error checking database: {e}")

if __name__ == "__main__":
    check_database()
