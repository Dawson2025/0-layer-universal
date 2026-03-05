#!/usr/bin/env python3
# resource_id: "03831eab-af98-4cb9-85a7-2bbee6f7208a"
# resource_type: "document"
# resource_name: "fix_database"
"""
Fix the database by initializing schema and inserting sample data.
"""

import main

def fix_database():
    """Fix the database by recreating it with proper schema and data."""
    print("🔧 Fixing database...")
    
    try:
        # Initialize the database schema
        print("Creating database schema...")
        main.migrate_schema()
        print("✓ Schema created successfully")
        
        # Insert sample data
        print("Inserting sample data...")
        main.insert_sample_data()
        print("✓ Sample data inserted successfully")
        
        # Test the database connection
        print("Testing database connection...")
        phonemes = main.get_sorted_phonemes()
        print(f"✓ Database working! Retrieved {len(phonemes)} phonemes")
        
        print("\n🎉 Database fixed successfully!")
        return True
        
    except Exception as e:
        print(f"✗ Error fixing database: {e}")
        return False

if __name__ == "__main__":
    fix_database()
