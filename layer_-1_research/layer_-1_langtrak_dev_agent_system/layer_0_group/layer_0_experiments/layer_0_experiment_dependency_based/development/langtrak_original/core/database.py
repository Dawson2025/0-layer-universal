import sqlite3
import os

DB_NAME = "lang_trak.db"

def get_db_connection(db_path=None):
    if db_path is None:
        db_path = DB_NAME
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;") # Ensure foreign keys are enabled
    return conn

def init_database(db_path=None):
    if db_path is None:
        db_path = DB_NAME

    # Ensure the directory for the database exists
    os.makedirs(os.path.dirname(db_path) or '.', exist_ok=True)

    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE,
            is_active INTEGER DEFAULT 1, -- Added is_active column
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            firebase_uid TEXT UNIQUE -- Added for Firebase integration
        )
    """)

    # Projects table - Standardized to use user_id, includes cloud fields
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            user_id INTEGER NOT NULL,
            storage_type TEXT DEFAULT 'local',
            cloud_project_id TEXT,
            cloud_last_sync TIMESTAMP,
            migrated_to_cloud INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Words table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT NOT NULL,
            english_words TEXT NOT NULL,
            ipa TEXT,
            syllables TEXT,
            project_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            video_path TEXT,
            frequency INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Phonemes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phoneme TEXT NOT NULL,
            type TEXT NOT NULL,
            position TEXT NOT NULL,
            length_type TEXT NOT NULL,
            syllable_type TEXT,            -- Added for compatibility with main.migrate_schema()
            group_type TEXT,               -- Added for compatibility with main.migrate_schema()
            subgroup_type TEXT,            -- Added for compatibility with main.migrate_schema()
            sub_subgroup_type TEXT,        -- Added for compatibility with main.migrate_schema()
            sub_sub_subgroup_type TEXT,    -- Added for compatibility with main.migrate_schema()
            frequency INTEGER DEFAULT 0,
            project_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Templates table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            template_data TEXT NOT NULL, -- Stores JSON representation of phonemes
            user_id INTEGER NOT NULL,
            is_public INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Project Groups table - Reverted PK to 'id', added 'group_identifier'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Reverted to id
            group_identifier TEXT UNIQUE,          -- New column for 'local:X' strings
            name TEXT NOT NULL,
            description TEXT,
            user_id INTEGER NOT NULL,                   -- Renamed from owner_id
            invite_code TEXT UNIQUE,
            parent_group_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (parent_group_id) REFERENCES project_groups(id) -- Updated FK
        )
    """)

    # Group Memberships table - References project_groups(id)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS group_memberships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER NOT NULL, -- This group_id is the INTEGER PK from project_groups
            user_id INTEGER NOT NULL,
            role TEXT DEFAULT 'member', -- e.g., 'member', 'admin'
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (group_id) REFERENCES project_groups(id), -- Updated FK
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE (group_id, user_id)
        )
    """)

    # Project Shares table - Consolidated
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_shares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            group_id INTEGER NOT NULL,
            shared_by INTEGER NOT NULL,
            project_identifier TEXT, -- Temporarily removed NOT NULL constraint
            storage_type TEXT NOT NULL DEFAULT 'local',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (group_id) REFERENCES project_groups(id),
            FOREIGN KEY (shared_by) REFERENCES users(id),
            UNIQUE (project_id, group_id) -- Added composite unique constraint
        )
    """)

    # Project Variants Meta table - Consolidated
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_variants_meta (
            variant_identifier TEXT PRIMARY KEY,
            group_id INTEGER, -- Changed from TEXT to INTEGER, now FK to project_groups(id)
            user_id INTEGER,
            storage_type TEXT,
            parent_variant_identifier TEXT,
            branch_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (group_id) REFERENCES project_groups(id) -- Added FK
        )
    """)

    # Cloud Project Mapping - For mapping local projects to cloud projects if needed (from main.py)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cloud_project_map (
            local_project_id INTEGER PRIMARY KEY,
            cloud_project_id TEXT UNIQUE NOT NULL,
            FOREIGN KEY (local_project_id) REFERENCES projects(id)
        )
    """)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # This block is for direct execution to set up the DB
    # In normal app flow, init_database() is called by the app
    db_file = os.path.join(os.path.dirname(__file__), DB_NAME)
    init_database(db_file)
    print(f"Database '{db_file}' initialized with all tables.")