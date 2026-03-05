# resource_id: "3ce1191a-a4ca-4842-b178-b33140fb76c1"
# resource_type: "document"
# resource_name: "main"
# main.py
import sqlite3
import os
import json
import subprocess
import shutil
import glob
import platform
import webbrowser
from collections import defaultdict
from scripts.legacy.flattened_dataset import flattened_dataset
from src.phonotactics import PhonotacticRules
from services.reset import get_database_snapshot, reset_database as perform_database_reset

DB_NAME = "data/phonemes.db"
# ---------- Schema & Data ----------

def migrate_schema():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    def ensure_column(table: str, column: str, definition: str) -> None:
        cursor.execute(f"PRAGMA table_info({table})")
        existing_columns = {row[1] for row in cursor.fetchall()}
        if column not in existing_columns:
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {definition}")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS phonemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            syllable_type TEXT,
            position TEXT,
            length_type TEXT,
            group_type TEXT,
            subgroup_type TEXT,
            phoneme TEXT,
            frequency INTEGER DEFAULT 0
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT,
            english_words TEXT,
            new_language_word TEXT,
            ipa_phonetics TEXT,
            dictionary_phonetics TEXT,
            syllable_type TEXT,
            onset_phoneme TEXT,
            onset_length_type TEXT,
            nucleus_phoneme TEXT,
            nucleus_length_type TEXT,
            coda_phoneme TEXT,
            coda_length_type TEXT,
            video_path TEXT
        )
        """
    )

    ensure_column("phonemes", "project_id", "project_id INTEGER")
    ensure_column("phonemes", "user_id", "user_id INTEGER")
    ensure_column("phonemes", "sub_subgroup_type", "sub_subgroup_type TEXT")
    ensure_column("phonemes", "sub_sub_subgroup_type", "sub_sub_subgroup_type TEXT")

    ensure_column("words", "user_id", "user_id INTEGER")
    ensure_column("words", "project_id", "project_id INTEGER")
    ensure_column("words", "syllable_type", "syllable_type TEXT")
    ensure_column("words", "onset_phoneme", "onset_phoneme TEXT")
    ensure_column("words", "onset_length_type", "onset_length_type TEXT")
    ensure_column("words", "nucleus_phoneme", "nucleus_phoneme TEXT")
    ensure_column("words", "nucleus_length_type", "nucleus_length_type TEXT")
    ensure_column("words", "coda_phoneme", "coda_phoneme TEXT")
    ensure_column("words", "coda_length_type", "coda_length_type TEXT")
    ensure_column("words", "syllables_data", "syllables_data TEXT")
    ensure_column("words", "image_path", "image_path TEXT")
    ensure_column("words", "created_at", "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            user_id INTEGER,
            cloud_project_id TEXT,
            cloud_last_sync TIMESTAMP,
            migrated_to_cloud INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS project_shares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            group_id INTEGER,
            shared_by INTEGER,
            shared_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            project_identifier TEXT,
            cloud_project_id TEXT,
            storage_type TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS project_variants_meta (
            variant_identifier TEXT PRIMARY KEY,
            group_id TEXT,
            user_id INTEGER,
            storage_type TEXT,
            parent_variant_identifier TEXT,
            branch_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    ensure_column("words", "video_path", "video_path TEXT")

    # Ensure projects table columns for cloud sync
    ensure_column("projects", "cloud_project_id", "cloud_project_id TEXT")
    ensure_column("projects", "cloud_last_sync", "cloud_last_sync TIMESTAMP")
    ensure_column("projects", "migrated_to_cloud", "migrated_to_cloud INTEGER DEFAULT 0")

    # Ensure project_shares table columns
    ensure_column("project_shares", "project_identifier", "project_identifier TEXT")
    ensure_column("project_shares", "storage_type", "storage_type TEXT")

    # Ensure uniqueness per project (allow same symbol combos in different projects)
    try:
        cursor.execute("DROP INDEX IF EXISTS idx_unique_phoneme")
    except sqlite3.OperationalError:
        pass
    cursor.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_phoneme_project
        ON phonemes (project_id, syllable_type, position, length_type, group_type, subgroup_type, phoneme)
        """
    )
    conn.commit()
    conn.close()

    os.makedirs("videos", exist_ok=True)

def migrate_existing_words_to_structured():
    """
    Migrate existing words in the database to include structured phoneme data.
    This will attempt to parse existing words and populate the new fields.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get all words that don't have structured data
    cursor.execute("""
        SELECT id, ipa_phonetics FROM words 
        WHERE syllable_type IS NULL OR onset_phoneme IS NULL OR nucleus_phoneme IS NULL
    """)
    words_to_migrate = cursor.fetchall()

    if not words_to_migrate:
        print("No words need migration. All words already have structured data.")
        conn.close()
        return

    print(f"Found {len(words_to_migrate)} words that need migration.")
    print("Note: This migration requires manual intervention as automatic IPA parsing is complex.")
    print("Consider manually editing these words using the edit function to add structured data.")

    for word_id, ipa in words_to_migrate:
        cursor.execute("SELECT new_language_word FROM words WHERE id = ?", (word_id,))
        word_name = cursor.fetchone()[0]
        print(f"- Word '{word_name}' (ID: {word_id}) with IPA: {ipa}")

    conn.close()
    input("Press Enter to continue...")

def insert_sample_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    for entry in flattened_dataset:
        cursor.execute("""
            INSERT OR IGNORE INTO phonemes
            (syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            entry.get("syllable_type"),
            entry.get("position"),
            entry.get("length_type"),
            entry.get("group_type"),
            entry.get("subgroup_type"),
            entry.get("phoneme"),
            entry.get("frequency", 0),
        ))
    conn.commit()
    conn.close()

# ---------- Video Processing Functions ----------

def find_ffmpeg():
    """Find FFmpeg executable on the system"""

    # First try to find ffmpeg in PATH
    ffmpeg_path = shutil.which('ffmpeg')
    if ffmpeg_path:
        return ffmpeg_path

    # If not found, try common Windows installation locations
    possible_paths = [
        r"C:\Program Files\FFmpeg\bin\ffmpeg.exe",
        r"C:\ffmpeg\bin\ffmpeg.exe",
    ]

    # Check winget installation location
    import os
    username = os.environ.get('USERNAME', 'Dawson')
    winget_pattern = f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg*\\ffmpeg-*\\bin\\ffmpeg.exe"
    winget_paths = glob.glob(winget_pattern)
    possible_paths.extend(winget_paths)

    for path in possible_paths:
        if os.path.exists(path):
            return path

    return None

def convert_video_to_mp4(input_path, output_path):
    """
    Convert a video file to MP4 format using FFmpeg.
    Returns True if successful, False otherwise.
    """
    try:
        # Strip quotes from input path if present
        input_path = input_path.strip().strip('"').strip("'").strip()

        # Check if input file exists
        if not os.path.exists(input_path):
            print(f"Error: Input video file '{input_path}' not found.")
            return False

        # Find FFmpeg executable
        ffmpeg_exe = find_ffmpeg()
        if not ffmpeg_exe:
            print("Error: FFmpeg not found. Please install FFmpeg.")
            print("Install with: winget install FFmpeg")
            return False

        print(f"Using FFmpeg at: {ffmpeg_exe}")

        # Check if output already exists and remove it
        if os.path.exists(output_path):
            os.remove(output_path)

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Run FFmpeg conversion
        cmd = [
            ffmpeg_exe, '-i', input_path,
            '-c:v', 'libx264',  # Video codec
            '-c:a', 'aac',      # Audio codec
            '-movflags', '+faststart',  # Optimize for streaming
            '-y',  # Overwrite output file if it exists
            output_path
        ]

        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✓ Video converted successfully to: {output_path}")
            return True
        else:
            print(f"Error converting video: {result.stderr}")
            return False

    except Exception as e:
        print(f"Error during video conversion: {e}")
        return False

def handle_video_upload(new_language_word):
    """
    Handle video upload for a word. Returns the path to the converted video or None.
    """
    video_input = input("Enter path to video file (or press Enter to skip): ").strip()
    if not video_input:
        return None

    # Strip quotes if user included them
    video_input = video_input.strip().strip('"').strip("'").strip()

    if not os.path.exists(video_input):
        print(f"Warning: Video file '{video_input}' not found. Skipping video.")
        return None

    # Create a safe filename for the video
    safe_word = "".join(c for c in new_language_word if c.isalnum() or c in (' ', '-', '_')).rstrip()
    video_filename = f"{safe_word}.mp4"
    video_output_path = os.path.join("videos", video_filename)

    print(f"Converting video to MP4 format...")
    if convert_video_to_mp4(video_input, video_output_path):
        return video_output_path
    else:
        print("Video conversion failed. Word will be saved without video.")
        return None

def play_video(video_path):
    """
    Play a video file using the system's default video player.
    Cross-platform compatible.
    """
    if not video_path or not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return False

    try:
        system = platform.system()

        if system == "Windows":
            # Use Windows default video player
            os.startfile(video_path)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", video_path])
        elif system == "Linux":
            subprocess.run(["xdg-open", video_path])
        else:
            # Fallback: try to open with default browser
            webbrowser.open(f"file://{os.path.abspath(video_path)}")

        print(f"🎬 Opening video: {video_path}")
        return True

    except Exception as e:
        print(f"Error opening video: {e}")
        print(f"Try opening manually: {os.path.abspath(video_path)}")
        return False

def show_video_options(video_path):
    """Show video options and handle user choice"""
    if not video_path:
        return

    print(f"\n🎬 Video available: {video_path}")
    print("Video options:")
    print("1. Play video")
    print("2. Show video file location")
    print("3. Continue without video")

    choice = input("Select option (1-3): ").strip()

    if choice == "1":
        play_video(video_path)
        input("Press Enter when done watching...")
    elif choice == "2":
        abs_path = os.path.abspath(video_path)
        print(f"Video location: {abs_path}")
        if platform.system() == "Windows":
            # Option to open file location in Explorer
            open_location = input("Open file location in Explorer? (y/n): ").strip().lower()
            if open_location == 'y':
                subprocess.run(["explorer", "/select,", abs_path])
    # Option 3 or any other input just continues

def get_existing_languages():
    """
    Get list of existing languages from the database.
    Returns a list of unique language names.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT language FROM words WHERE language IS NOT NULL AND language != '' ORDER BY language")
    languages = [row[0] for row in cursor.fetchall()]
    conn.close()
    return languages

def select_or_input_language():
    """
    Allow user to select from existing languages or input a new one.
    Returns the selected/entered language name.
    """
    existing_languages = get_existing_languages()

    if existing_languages:
        print("\nExisting languages in database:")
        for i, lang in enumerate(existing_languages, 1):
            print(f"  {i}. {lang}")
        print(f"  {len(existing_languages) + 1}. Enter a new language")

        while True:
            choice = input(f"\nSelect language (1-{len(existing_languages) + 1}): ").strip()

            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(existing_languages):
                    selected_lang = existing_languages[choice_num - 1]
                    print(f"Selected: {selected_lang}")
                    return selected_lang
                elif choice_num == len(existing_languages) + 1:
                    break
                else:
                    print(f"Please enter a number between 1 and {len(existing_languages) + 1}")
            else:
                print("Please enter a valid number")

    # Input new language
    while True:
        new_lang = input("Enter new language name: ").strip()
        if new_lang:
            return new_lang
        print("Language name cannot be empty.")


def lookup_word():
    """Simple CLI lookup that delegates to the words display functions."""
    search_term = input("Enter the constructed word to look up: ").strip()
    if not search_term:
        print("No word entered. Returning to menu.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT language, english_words, new_language_word, ipa_phonetics, video_path
        FROM words
        WHERE LOWER(new_language_word) = LOWER(?)
        ORDER BY id DESC
        """,
        (search_term,)
    )
    results = cursor.fetchall()
    conn.close()

    if not results:
        print(f"No entries found for '{search_term}'.")
        return

    print(f"\nResults for '{search_term}':")
    for language, english_words, new_word, ipa, video in results:
        try:
            english_list = json.loads(english_words) if english_words else []
            if isinstance(english_list, list):
                english_display = ', '.join(english_list)
            else:
                english_display = str(english_list)
        except (json.JSONDecodeError, TypeError):
            english_display = english_words or ''

        print(f"- Language: {language or 'Unknown'}")
        print(f"  English: {english_display or '—'}")
        print(f"  Constructed: {new_word}")
        print(f"  IPA: {ipa or '—'}")
        if video:
            print(f"  Video: {video}")
        print()

# ---------- Ordering & Queries ----------

def get_sorted_phonemes():
    """
    Enforce fixed order for:
      syllable_type: CVC -> CV
      position:      onset -> nucleus -> coda
      length_type:   if position in (onset, coda): single_consonants -> cluster2 -> cluster3
                     if position == nucleus:        monophthongs -> diphthongs
    Inside those, sort by aggregated frequency:
      group_freq (sum per group), subgroup_freq (sum per subgroup), then phoneme freq ascending.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            syllable_type,
            position,
            length_type,
            group_type,
            subgroup_type,
            phoneme,
            frequency,
            /* aggregate: group sum for sorting/labels */
            SUM(frequency) OVER (
                PARTITION BY syllable_type, position, length_type, group_type
            ) AS group_freq,
            /* aggregate: subgroup sum (nullable) */
            CASE
                WHEN subgroup_type IS NULL OR subgroup_type = '' THEN NULL
                ELSE SUM(frequency) OVER (
                    PARTITION BY syllable_type, position, length_type, group_type, subgroup_type
                )
            END AS subgroup_freq
        FROM phonemes
        ORDER BY
            /* fixed outer order */
            CASE syllable_type WHEN 'CVC' THEN 0 WHEN 'CV' THEN 1 ELSE 2 END,
            CASE position WHEN 'onset' THEN 0 WHEN 'nucleus' THEN 1 WHEN 'coda' THEN 2 ELSE 3 END,
            CASE
                WHEN position IN ('onset','coda') THEN
                    CASE length_type
                        WHEN 'single_consonants' THEN 0
                        WHEN 'cluster2'         THEN 1
                        WHEN 'cluster3'         THEN 2
                        ELSE 3
                    END
                WHEN position = 'nucleus' THEN
                    CASE length_type
                        WHEN 'monophthongs' THEN 0
                        WHEN 'diphthongs'   THEN 1
                        ELSE 2
                    END
                ELSE 3
            END,
            /* by aggregates/freq ascending within each section */
            group_freq ASC,
            CASE WHEN subgroup_freq IS NULL THEN -1 ELSE subgroup_freq END ASC,
            frequency ASC,
            phoneme
    """)
    result = cursor.fetchall()
    conn.close()
    return result

# ---------- Displays ----------


def display_nested_phonemes():
    # Check if phonemes table is empty
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM phonemes")
    count = cursor.fetchone()[0]
    conn.close()

    if count == 0:
        choice = input("Database is empty. Would you like to insert sample data? (y/n): ").strip().lower()
        if choice == "y":
            insert_sample_data()
        else:
            print("Database is empty. No data to display.")
            input("\nPress Enter to return to the main menu...")
            return

    # Fixed options for syllable types and positions
    syllable_types = ["CVC", "CV"]
    print("\nAvailable syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    positions_dict = {
        "CVC": ["onset", "nucleus", "coda"],
        "CV": ["onset", "nucleus"]
    }
    positions = positions_dict[syllable_type]
    print("\nAvailable positions:")
    for i, p in enumerate(positions, 1):
        print(f"{i}: {p}")
    p_choice = input("Select a position by number: ").strip()
    try:
        position = positions[int(p_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    # Fixed length types based on position
    length_types_dict = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "coda": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    length_types = length_types_dict[position]
    print("\nAvailable length types:")
    for i, l in enumerate(length_types, 1):
        print(f"{i}: {l}")
    l_choice = input("Select a length type by number: ").strip()
    try:
        length_type = length_types[int(l_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    # Filtered query
    data = [
        row for row in get_sorted_phonemes()
        if row[0] == syllable_type and row[1] == position and row[2] == length_type
    ]
    print(f"\nPhoneme Hierarchy for {syllable_type} > {position} > {length_type}")
    print("(Fixed order for group/subgroup; frequency order within groups)\n")

    grouped = defaultdict(list)
    for row in data:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (g, sub, gfreq, subfreq)
        grouped[key].append((ph, f))

    current = ["", ""]
    for key, phonemes in grouped.items():
        g, sub, gfreq, subfreq = key
        new_keys = [g or "", sub or ""]

        for i in range(len(new_keys)):
            if current[i] != new_keys[i]:
                indent = "  " * i
                if i == 0:
                    label = f"- {new_keys[i]} (group freq: {gfreq})"
                elif i == 1 and new_keys[i] != "" and new_keys[i] != "none":
                    label = f"- {new_keys[i]} (subgroup freq: {subfreq})"
                else:
                    label = f"- {new_keys[i]}"
                print(f"{indent}{label}")
                current[i:] = new_keys[i:]
                for j in range(i + 1, len(current)):
                    current[j] = ""

        for ph, f in phonemes:
            print("  " * 3 + f"- {ph}: {f}")

    input("\nPress Enter to return to the main menu...")

def display_full():
    """
    Display the entire nested phoneme hierarchy for all syllable types, positions, and length types.
    """
    data = get_sorted_phonemes()
    print("\nFull Phoneme Hierarchy")
    print("(Fixed order for syllable_type/position/length/group/subgroup; frequency order within groups)\n")

    grouped = defaultdict(list)
    for row in data:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (s, p, l, g, sub, gfreq, subfreq)
        grouped[key].append((ph, f))

    current = ["", "", "", "", ""]
    for key, phonemes in grouped.items():
        s, p, l, g, sub, gfreq, subfreq = key
        new_keys = [s or "", p or "", l or "", g or "", sub or ""]

        for i in range(len(new_keys)):
            if current[i] != new_keys[i]:
                indent = "  " * i
                if i == 3:
                    label = f"- {new_keys[i]} (group freq: {gfreq})"
                elif i == 4 and new_keys[i] != "" and new_keys[i] != "none":
                    label = f"- {new_keys[i]} (subgroup freq: {subfreq})"
                else:
                    label = f"- {new_keys[i]}"
                print(f"{indent}{label}")
                current[i:] = new_keys[i:]
                for j in range(i + 1, len(current)):
                    current[j] = ""

        for ph, f in phonemes:
            print("  " * 5 + f"- {ph}: {f}")

    input("\nPress Enter to return to the main menu...")

# ---------- Utilities ----------

def reset_database():
    """Reset the database with proper warnings and double confirmation."""
    print("\n⚠️  WARNING: DATABASE RESET ⚠️")
    print("=" * 40)
    print("This action will PERMANENTLY DELETE:")
    print("• All phonemes and their frequencies")
    print("• All words in your language database")
    print("• All language data and relationships")
    print("NOTE: Phoneme templates will be preserved!")
    print("Everything will be lost forever.")
    print("=" * 40)

    # First confirmation
    first_confirm = input("\nAre you ABSOLUTELY SURE you want to reset the database? (yes/no): ").strip().lower()

    if first_confirm not in ['yes', 'y']:
        print("Database reset cancelled.")
        input("Press Enter to return to the main menu...")
        return

    # Show current database contents using service snapshot
    snapshot = get_database_snapshot(DB_NAME)
    if os.path.exists(DB_NAME):
        print("\n📊 Current Database Contents:")
        print(f"   • {snapshot.get('phonemes', 0)} phonemes")
        print(f"   • {snapshot.get('words', 0)} words")
    else:
        print("\n📊 Database file doesn't exist yet.")

    # Second confirmation with typing verification
    print(f"\n🔄 FINAL CONFIRMATION")
    print("To proceed with the reset, type exactly: DELETE EVERYTHING")
    verification = input("Type here: ").strip()

    if verification != "DELETE EVERYTHING":
        print("❌ Verification failed. Database reset cancelled.")
        print("(You must type exactly: DELETE EVERYTHING)")
        input("Press Enter to return to the main menu...")
        return

    # Perform the reset via service
    try:
        result = perform_database_reset(DB_NAME, insert_sample_data=insert_sample_data)

        print("\n✅ Database successfully reset!")
        print("All words and phonemes have been deleted.")
        print("Phonemes reset to default configuration.")
        if result.templates_preserved:
            print(f"Preserved {result.templates_preserved} phoneme templates.")
        else:
            print("No templates found to preserve.")

    except RuntimeError as exc:
        print(f"\n❌ Error during database reset: {exc}")
        print("The database may be in an inconsistent state.")
        print("The database may be in an inconsistent state.")

    input("Press Enter to return to the main menu...")

def select_and_modify_frequency(increment=1):
    # Display nested hierarchy as usual, but number the phonemes
    syllable_types = ["CVC", "CV"]
    print("\nAvailable syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    positions_dict = {
        "CVC": ["onset", "nucleus", "coda"],
        "CV": ["onset", "nucleus"]
    }
    positions = positions_dict[syllable_type]
    print("\nAvailable positions:")
    for i, p in enumerate(positions, 1):
        print(f"{i}: {p}")
    p_choice = input("Select a position by number: ").strip()
    try:
        position = positions[int(p_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    length_types_dict = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "coda": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    length_types = length_types_dict[position]
    print("\nAvailable length types:")
    for i, l in enumerate(length_types, 1):
        print(f"{i}: {l}")
    l_choice = input("Select a length type by number: ").strip()
    try:
        length_type = length_types[int(l_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    # Filtered query
    data = [
        row for row in get_sorted_phonemes()
        if row[0] == syllable_type and row[1] == position and row[2] == length_type
    ]
    print(f"\nPhoneme Hierarchy for {syllable_type} > {position} > {length_type}")
    print("(Numbered phonemes for selection)\n")

    # Group and number phonemes
    grouped = defaultdict(list)
    for row in data:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (g, sub, gfreq, subfreq)
        grouped[key].append((ph, f))

    current = ["", ""]
    phoneme_list = []
    idx = 1
    for key, phonemes in grouped.items():
        g, sub, gfreq, subfreq = key
        new_keys = [g or "", sub or ""]
        for i in range(len(new_keys)):
            if current[i] != new_keys[i]:
                indent = "  " * i
                if i == 0:
                    label = f"- {new_keys[i]} (group freq: {gfreq})"
                elif i == 1 and new_keys[i] != "" and new_keys[i] != "none":
                    label = f"- {new_keys[i]} (subgroup freq: {subfreq})"
                else:
                    label = f"- {new_keys[i]}"
                print(f"{indent}{label}")
                current[i:] = new_keys[i:]
                for j in range(i + 1, len(current)):
                    current[j] = ""
        for ph, f in phonemes:
            print("  " * 3 + f"{idx}: {ph} (freq: {f})")
            phoneme_list.append((syllable_type, position, length_type, g, sub, ph))
            idx += 1

    # Select phoneme to modify
    selection = input("\nEnter the number of the phoneme to modify: ").strip()
    try:
        selection_idx = int(selection) - 1
        selected = phoneme_list[selection_idx]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return

    # Update frequency in database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE phonemes
        SET frequency = frequency + ?
        WHERE syllable_type=? AND position=? AND length_type=? AND group_type=? AND subgroup_type=? AND phoneme=?
    """, (increment, *selected))
    conn.commit()
    conn.close()
    print("Frequency updated.")
    input("Press Enter to return to the main menu...")

# In your menu:
# For increase frequency:
def increase_frequency():
    select_and_modify_frequency(increment=1)

# For decrease frequency:
def decrease_frequency():
    select_and_modify_frequency(increment=-1)

# --- Add new word ---
def create_word_from_phonemes():
    print("\n--- Word Creation Methods ---")
    print("1. Traditional method (updates frequencies immediately)")
    print("2. Enhanced method (updates frequencies after completion)")
    print("3. Table-based method (shows phoneme tables side by side)")
    print("4. Suggestion-based method (provides optimized word suggestions)")

    choice = input("Select a method (1-4): ").strip()

    if choice == "1":
        create_word_traditional()
    elif choice == "2":
        create_word_enhanced()
    elif choice == "3":
        create_word_table_based()
    elif choice == "4":
        create_word_suggestion_based()
    else:
        print("Invalid choice. Using traditional method.")
        create_word_traditional()

def create_word_traditional():
    """Original word creation method that updates frequencies immediately."""
    # Get basic word info first - use new language selection
    language = select_or_input_language()
    english_input = input("Enter the English word(s) (separate multiple meanings with commas): ").strip()

    # Parse multiple English words
    english_words = [word.strip() for word in english_input.split(',') if word.strip()]

    # Choose syllable type
    syllable_types = ["CVC", "CV"]
    print("\nAvailable syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    # Build IPA from selected phonemes and capture structured data
    ipa_parts = []
    phoneme_data = {
        'syllable_type': syllable_type,
        'onset_phoneme': None,
        'onset_length_type': None,
        'nucleus_phoneme': None,
        'nucleus_length_type': None,
        'coda_phoneme': None,
        'coda_length_type': None
    }

    # Determine positions based on syllable type
    if syllable_type == "CVC":
        positions = ["onset", "nucleus", "coda"]
    else:  # CV
        positions = ["onset", "nucleus"]

    # Select phoneme for each position
    for position in positions:
        print(f"\nSelecting phoneme for {position}:")
        selected_data = select_phoneme_for_position_with_data(syllable_type, position)
        if selected_data:
            phoneme, length_type = selected_data
            ipa_parts.append(phoneme)
            print(f"Selected {position}: {phoneme}")

            # Store structured data
            phoneme_data[f'{position}_phoneme'] = phoneme
            phoneme_data[f'{position}_length_type'] = length_type
        else:
            print(f"No phoneme selected for {position}.")
            return

    # Build final IPA string
    ipa_phonetics = "".join(ipa_parts)
    print(f"\nBuilt IPA phonetics: {ipa_phonetics}")

    # Now get the remaining word info
    new_language_word = input("Enter the word in your language: ").strip()
    dictionary_phonetics = ipa_phonetics  # Auto-sync with IPA
    print(f"Dictionary phonetics set to: {dictionary_phonetics}")

    # Handle video upload
    video_path = handle_video_upload(new_language_word)

    # Save to database using the new function with structured data
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    add_new_word_with_structure(cursor, conn, language, english_words, new_language_word, 
                               ipa_phonetics, dictionary_phonetics, phoneme_data, video_path)
    conn.close()

    input("Press Enter to return to the main menu...")

def add_new_word(cursor, conn, language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics, video_path=None):
    # Check if this new language word already exists
    cursor.execute("SELECT english_words FROM words WHERE LOWER(new_language_word) = LOWER(?)", (new_language_word,))
    existing_row = cursor.fetchone()

def create_word_enhanced():
    """Enhanced word creation method that doesn't update frequencies until completion."""
    # Get basic word info first
    language = select_or_input_language()
    english_input = input("Enter the English word(s) (separate multiple meanings with commas): ").strip()

    # Parse multiple English words
    english_words = [word.strip() for word in english_input.split(',') if word.strip()]

    # Choose syllable type
    syllable_types = ["CVC", "CV"]
    print("\nAvailable syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    # Build IPA from selected phonemes and capture structured data
    ipa_parts = []
    phoneme_data = {
        'syllable_type': syllable_type,
        'onset_phoneme': None,
        'onset_length_type': None,
        'nucleus_phoneme': None,
        'nucleus_length_type': None,
        'coda_phoneme': None,
        'coda_length_type': None
    }

    # Determine positions based on syllable type
    if syllable_type == "CVC":
        positions = ["onset", "nucleus", "coda"]
    else:  # CV
        positions = ["onset", "nucleus"]

    # Select phoneme for each position (without updating frequencies)
    for position in positions:
        print(f"\nSelecting phoneme for {position}:")
        selected_data = select_phoneme_for_position_without_frequency_update(syllable_type, position)
        if selected_data:
            phoneme, length_type = selected_data
            ipa_parts.append(phoneme)
            print(f"Selected {position}: {phoneme}")

            # Store structured data
            phoneme_data[f'{position}_phoneme'] = phoneme
            phoneme_data[f'{position}_length_type'] = length_type
        else:
            print(f"No phoneme selected for {position}.")
            return

    # Build final IPA string
    ipa_phonetics = "".join(ipa_parts)
    print(f"\nBuilt IPA phonetics: {ipa_phonetics}")

    # Now get the remaining word info
    new_language_word = input("Enter the word in your language: ").strip()
    dictionary_phonetics = ipa_phonetics  # Auto-sync with IPA
    print(f"Dictionary phonetics set to: {dictionary_phonetics}")

    # Confirm before saving and updating frequencies
    print(f"\n--- Word Summary ---")
    print(f"Language: {language}")
    print(f"English: {', '.join(english_words)}")
    print(f"New Language: {new_language_word}")
    print(f"IPA: {ipa_phonetics}")
    print(f"Dictionary: {dictionary_phonetics}")
    print(f"Syllable Type: {syllable_type}")
    print(f"Onset: {phoneme_data['onset_phoneme']} ({phoneme_data['onset_length_type']})")
    print(f"Nucleus: {phoneme_data['nucleus_phoneme']} ({phoneme_data['nucleus_length_type']})")
    if phoneme_data['coda_phoneme']:
        print(f"Coda: {phoneme_data['coda_phoneme']} ({phoneme_data['coda_length_type']})")

    confirm = input("\nSave this word and update phoneme frequencies? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Word creation cancelled.")
        return

    # Save to database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    add_new_word_with_structure(cursor, conn, language, english_words, new_language_word, 
                               ipa_phonetics, dictionary_phonetics, phoneme_data)

    # Now update all phoneme frequencies
    print("\nUpdating phoneme frequencies...")
    for position in positions:
        phoneme = phoneme_data[f'{position}_phoneme']
        length_type = phoneme_data[f'{position}_length_type']
        update_phoneme_frequency(cursor, conn, syllable_type, position, length_type, phoneme)

    conn.commit()
    conn.close()

    print("✓ Word saved and phoneme frequencies updated!")
    input("Press Enter to return to the main menu...")

def create_word_table_based():
    """Table-based word creation method showing onset, nucleus, and coda tables side by side."""
    # Get basic word info first
    language = input("Enter the name of your language: ").strip()
    english_input = input("Enter the English word(s) (separate multiple meanings with commas): ").strip()

    # Parse multiple English words
    english_words = [word.strip() for word in english_input.split(',') if word.strip()]

    # Choose syllable type
    syllable_types = ["CVC", "CV"]
    print("\nAvailable syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    # Choose length type
    print("\nLength type options:")
    print("1: Solo phonemes (single consonants, monophthongs)")
    print("2: Multiple types (consonant clusters, diphthongs)")
    l_choice = input("Select length type (1-2): ").strip()
    try:
        length_type_choice = int(l_choice)
        if length_type_choice == 1:
            length_types = {
                "onset": ["single_consonants"],
                "nucleus": ["monophthongs"],
                "coda": ["single_consonants"]
            }
        elif length_type_choice == 2:
            length_types = {
                "onset": ["single_consonants", "cluster2", "cluster3"],
                "nucleus": ["monophthongs", "diphthongs"],
                "coda": ["single_consonants", "cluster2", "cluster3"]
            }
        else:
            print("Invalid choice.")
            return
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    # Determine positions based on syllable type
    if syllable_type == "CVC":
        positions = ["onset", "nucleus", "coda"]
    else:  # CV
        positions = ["onset", "nucleus"]

    # Display phoneme tables side by side with numbers and get mapping
    position_mappings = display_phoneme_tables_side_by_side_with_numbers(syllable_type, positions, length_types)

    # Select phonemes using the new number-based method or filters
    result = select_phonemes_by_numbers_or_filters(position_mappings, positions, syllable_type, length_types)
    if not result:
        print("Phoneme selection failed. Returning to main menu.")
        return

    phoneme_data, ipa_phonetics = result

    # Set the syllable type in the phoneme data
    phoneme_data['syllable_type'] = syllable_type

    # Now get the remaining word info
    new_language_word = input("Enter the word in your language: ").strip()
    dictionary_phonetics = ipa_phonetics  # Auto-sync with IPA
    print(f"Dictionary phonetics set to: {dictionary_phonetics}")

    # Confirm before saving and updating frequencies
    print(f"\n--- Word Summary ---")
    print(f"Language: {language}")
    print(f"English: {', '.join(english_words)}")
    print(f"New Language: {new_language_word}")
    print(f"IPA: {ipa_phonetics}")
    print(f"Dictionary: {dictionary_phonetics}")
    print(f"Syllable Type: {syllable_type}")
    print(f"Onset: {phoneme_data['onset_phoneme']} ({phoneme_data['onset_length_type']})")
    print(f"Nucleus: {phoneme_data['nucleus_phoneme']} ({phoneme_data['nucleus_length_type']})")
    if phoneme_data['coda_phoneme']:
        print(f"Coda: {phoneme_data['coda_phoneme']} ({phoneme_data['coda_length_type']})")

    confirm = input("\nSave this word and update phoneme frequencies? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Word creation cancelled.")
        return

    # Save to database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    add_new_word_with_structure(cursor, conn, language, english_words, new_language_word, 
                               ipa_phonetics, dictionary_phonetics, phoneme_data)

    # Now update all phoneme frequencies
    print("\nUpdating phoneme frequencies...")
    for position in positions:
        phoneme = phoneme_data[f'{position}_phoneme']
        length_type = phoneme_data[f'{position}_length_type']
        update_phoneme_frequency(cursor, conn, syllable_type, position, length_type, phoneme)

    conn.commit()
    conn.close()

    print("✓ Word saved and phoneme frequencies updated!")
    input("Press Enter to return to the main menu...")

def create_word_suggestion_based():
    """Suggestion-based word creation method that provides optimized phoneme combinations."""
    # Get basic word info first (same as table-based method)
    language = input("Enter the name of your language: ").strip()
    english_input = input("Enter the English word(s) (separate multiple meanings with commas): ").strip()

    # Parse multiple English words
    english_words = [word.strip() for word in english_input.split(',') if word.strip()]

    # Choose syllable type
    syllable_types = ["CVC", "CV"]
    print("\nAvailable syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return

    # Choose length type
    print("\nLength type options:")
    print("1: Solo phonemes (single consonants, monophthongs)")
    print("2: Multiple types (consonant clusters, diphthongs)")
    l_choice = input("Select length type (1-2): ").strip()
    try:
        length_type_choice = int(l_choice)
        if length_type_choice == 1:
            length_types = {
                "onset": ["single_consonants"],
                "nucleus": ["monophthongs"],
                "coda": ["single_consonants"]
            }
        elif length_type_choice == 2:
            length_types = {
                "onset": ["single_consonants", "cluster2", "cluster3"],
                "nucleus": ["monophthongs", "diphthongs"],
                "coda": ["single_consonants", "cluster2", "cluster3"]
            }
        else:
            print("Invalid choice.")
            return
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    # Determine positions based on syllable type
    if syllable_type == "CVC":
        positions = ["onset", "nucleus", "coda"]
    else:  # CV
        positions = ["onset", "nucleus"]

    # Display phoneme tables side by side with numbers and get mapping
    position_mappings = display_phoneme_tables_side_by_side_with_numbers(syllable_type, positions, length_types)

    # Generate and display suggestions, then allow selection
    result = select_phonemes_with_suggestions(position_mappings, positions, syllable_type, length_types)
    if not result:
        print("Phoneme selection failed. Returning to main menu.")
        return

    phoneme_data, ipa_phonetics = result

    # Set the syllable type in the phoneme data
    phoneme_data['syllable_type'] = syllable_type

    # Now get the remaining word info
    new_language_word = input("Enter the word in your language: ").strip()
    dictionary_phonetics = ipa_phonetics  # Auto-sync with IPA
    print(f"Dictionary phonetics set to: {dictionary_phonetics}")

    # Confirm before saving and updating frequencies
    print(f"\n--- Word Summary ---")
    print(f"Language: {language}")
    print(f"English: {', '.join(english_words)}")
    print(f"New Language: {new_language_word}")
    print(f"IPA: {ipa_phonetics}")
    print(f"Dictionary: {dictionary_phonetics}")
    print(f"Syllable Type: {syllable_type}")
    print(f"Onset: {phoneme_data['onset_phoneme']} ({phoneme_data['onset_length_type']})")
    print(f"Nucleus: {phoneme_data['nucleus_phoneme']} ({phoneme_data['nucleus_length_type']})")
    if phoneme_data['coda_phoneme']:
        print(f"Coda: {phoneme_data['coda_phoneme']} ({phoneme_data['coda_length_type']})")

    confirm = input("\nSave this word and update phoneme frequencies? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Word creation cancelled.")
        return

    # Save to database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    add_new_word_with_structure(cursor, conn, language, english_words, new_language_word, 
                               ipa_phonetics, dictionary_phonetics, phoneme_data)

    # Now update all phoneme frequencies
    print("\nUpdating phoneme frequencies...")
    for position in positions:
        phoneme = phoneme_data[f'{position}_phoneme']
        length_type = phoneme_data[f'{position}_length_type']
        update_phoneme_frequency(cursor, conn, syllable_type, position, length_type, phoneme)

    conn.commit()
    conn.close()

    print("✓ Word saved and phoneme frequencies updated!")
    input("Press Enter to return to the main menu...")


def get_existing_ipa_pronunciations():
    """Get all existing IPA pronunciations from the database to avoid conflicts."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get all IPA pronunciations from existing words
        cursor.execute("SELECT DISTINCT ipa_phonetics FROM words WHERE ipa_phonetics IS NOT NULL AND ipa_phonetics != ''")
        rows = cursor.fetchall()
        conn.close()

        # Return set of existing IPA pronunciations
        return {row[0].strip() for row in rows if row[0] and row[0].strip()}
    except Exception:
        # If there's any database error, return empty set (fail safely)
        return set()


def get_english_word_database():
    """Get the comprehensive database of English words mapping IPA to English spelling."""
    return {
        # === ULTRA-HIGH FREQUENCY FUNCTION WORDS ===
        "ðə": "the", "ʌv": "of", "ænd": "and", "tu": "to", "ə": "a", "ɪn": "in", "ɪt": "it", "ɪz": "is", "fɔr": "for", "æz": "as",
        "wɪð": "with", "hɪz": "his", "ɔn": "on", "bi": "be", "æt": "at", "baɪ": "by", "ðɪs": "this", "hæv": "have", "frʌm": "from", "ðeɪ": "they",
        "aɪ": "I", "nɑt": "not", "ɔr": "or", "wʌt": "what", "wi": "we", "kæn": "can", "aʊt": "out", "ʌðər": "other",
        "wɝ": "were", "wɪtʃ": "which", "du": "do", "ðɛr": "their", "taɪm": "time", "ɪf": "if", "wɪl": "will", "haʊ": "how", "sɛd": "said", "æn": "an",
        "itʃ": "each", "ʃi": "she", "meɪ": "may", "juz": "use", "hər": "her", "θæn": "than", "naʊ": "now", "weɪ": "way", "faɪnd": "find", "loŋ": "long",

        # === CVC PATTERNS - SHORT VOWELS ===
        # Short 'a' /æ/ words
        "pæt": "pat", "bæt": "bat", "kæt": "cat", "hæt": "hat", "mæt": "mat", "ræt": "rat", "fæt": "fat", "sæt": "sat", "væt": "vat", "tæp": "tap",
        "kæp": "cap", "gæp": "gap", "læp": "lap", "mæp": "map", "næp": "nap", "ræp": "rap", "sæp": "sap", "zæp": "zap", "bæg": "bag", "tæg": "tag",
        "ræg": "rag", "læg": "lag", "jæg": "jag", "sæg": "sag", "wæg": "wag", "fæg": "fag", "gæg": "gag", "hæg": "hag", "mæn": "man", "kæn": "can",
        "fæn": "fan", "ræn": "ran", "tæn": "tan", "væn": "van", "bæn": "ban", "pæn": "pan", "dæm": "dam", "hæm": "ham", "jæm": "jam", "ræm": "ram",

        # Short 'i' /ɪ/ words
        "pɪt": "pit", "bɪt": "bit", "kɪt": "kit", "hɪt": "hit", "fɪt": "fit", "sɪt": "sit", "wɪt": "wit", "lɪt": "lit", "gɪt": "git", "nɪt": "knit",
        "tɪp": "tip", "rɪp": "rip", "sɪp": "sip", "dɪp": "dip", "nɪp": "nip", "hɪp": "hip", "lɪp": "lip", "zɪp": "zip", "ʃɪp": "ship", "tʃɪp": "chip",
        "bɪg": "big", "fɪg": "fig", "dɪg": "dig", "pɪg": "pig", "wɪg": "wig", "jɪg": "jig", "rɪg": "rig", "mɪx": "mix", "fɪx": "fix", "sɪx": "six",
        "kɪd": "kid", "lɪd": "lid", "bɪd": "bid", "hɪd": "hid", "dɪd": "did", "rɪd": "rid", "skɪd": "skid", "wɪn": "win", "pɪn": "pin", "bɪn": "bin",

        # Short 'u' /ʌ/ words
        "bʌt": "but", "kʌt": "cut", "gʌt": "gut", "hʌt": "hut", "nʌt": "nut", "rʌt": "rut", "ʃʌt": "shut", "pʌt": "put", "jʌt": "jut", "slʌt": "slut",
        "rʌn": "run", "sʌn": "sun", "fʌn": "fun", "gʌn": "gun", "bʌn": "bun", "nʌn": "nun", "pʌn": "pun", "wʌn": "one", "dʌn": "done", "hʌg": "hug",
        "bʌg": "bug", "rʌg": "rug", "jʌg": "jug", "dʌg": "dug", "mʌg": "mug", "pʌg": "pug", "tʌg": "tug", "kʌp": "cup", "pʌp": "pup", "bʌs": "bus",
        "mʌst": "must", "jʌst": "just", "lʌst": "lust", "rʌst": "rust", "dʌst": "dust", "trʌst": "trust", "fʌd": "flood", "bʌd": "bud", "spʌd": "spud", "θʌd": "thud",
        "lʌv": "love", "glʌv": "glove", "dʌv": "dove", "ʃʌv": "shove", "dʌk": "duck",

        # Short 'o' /ɑ/ words
        "pɑt": "pot", "hɑt": "hot", "kɑt": "cot", "bɑt": "bot", "nɑt": "not", "gɑt": "got", "dɑt": "dot", "lɑt": "lot", "wɑt": "what", "tɑp": "top",
        "kɑp": "cop", "mɑp": "mop", "lɑp": "lop", "sɑp": "sop", "dɑg": "dog", "lɑg": "log", "fɑg": "fog", "rɑk": "rock", "sɑk": "sock", "dɑk": "dock",
        "lɑk": "lock", "mɑk": "mock", "pɑk": "pack", "tɑk": "talk", "wɑk": "walk", "ʧɑk": "chalk", "blɑk": "block",

        # Short 'e' /ɛ/ words
        "bɛt": "bet", "gɛt": "get", "sɛt": "set", "lɛt": "let", "mɛt": "met", "nɛt": "net", "pɛt": "pet", "wɛt": "wet", "jɛt": "jet", "vɛt": "vet",
        "rɛd": "red", "bɛd": "bed", "lɛd": "led", "fɛd": "fed", "wɛd": "wed", "dɛd": "dead", "ʃɛd": "shed", "slɛd": "sled", "brɛd": "bread", "θrɛd": "thread",
        "mɛn": "men", "tɛn": "ten", "pɛn": "pen", "hɛn": "hen", "dɛn": "den", "ðɛn": "then", "wɛn": "when", "ɛn": "end", "bɛnd": "bend", "lɛnd": "lend",
        "sɛnd": "send", "mɛnd": "mend", "tɛnd": "tend", "spɛnd": "spend", "blɛnd": "blend", "trɛnd": "trend", "frɛnd": "friend", "hɛlp": "help", "jɛlp": "yelp", "kɛlp": "kelp",

        # 'oo' /ʊ/ words
        "pʊt": "put", "fʊt": "foot", "gʊd": "good", "wʊd": "would", "kʊd": "could", "ʃʊd": "should", "wʊd": "wood", "bʊk": "book", "lʊk": "look", "tʊk": "took",
        "kʊk": "cook", "hʊk": "hook", "ʃʊk": "shook", "nʊk": "nook", "krʊk": "crook",

        # === CV PATTERNS - LONG VOWELS & DIPHTHONGS ===
        # Long 'e' /i/ sounds
        "bi": "be", "si": "see", "fi": "fee", "hi": "he", "ki": "key", "mi": "me", "ni": "knee", "ʃi": "she", "wi": "we", "θri": "three",
        "fri": "free", "tri": "tree", "fli": "flee", "spi": "spree", "ti": "tea", "θi": "thee", "gli": "glee", "ski": "ski",

        # Long 'a' /eɪ/ sounds
        "beɪ": "bay", "deɪ": "day", "heɪ": "hey", "keɪ": "key", "leɪ": "lay", "meɪ": "may", "peɪ": "pay", "reɪ": "ray", "seɪ": "say", "weɪ": "way",
        "pleɪ": "play", "steɪ": "stay", "preɪ": "pray", "spreɪ": "spray", "streɪ": "stray", "sweɪ": "sway", "θeɪ": "they", "speɪ": "spay", "neɪ": "neigh", "geɪ": "gay",
        "greɪ": "gray", "treɪ": "tray", "kleɪ": "clay", "sleɪ": "slay", "fleɪ": "flay",

        # Long 'i' /aɪ/ sounds
        "baɪ": "buy", "daɪ": "die", "faɪ": "fly", "gaɪ": "guy", "haɪ": "high", "laɪ": "lie", "maɪ": "my", "paɪ": "pie", "saɪ": "sigh",
        "taɪ": "tie", "traɪ": "try", "waɪ": "why", "draɪ": "dry", "kraɪ": "cry", "flaɪ": "fly", "spaɪ": "spy", "skaɪ": "sky", "fraɪ": "fry", "θaɪ": "thigh",
        "braɪt": "bright", "flaɪt": "flight", "maɪt": "might", "naɪt": "night", "raɪt": "right", "saɪt": "sight", "taɪt": "tight", "waɪt": "white", "slaɪ": "sly",

        # Long 'o' /oʊ/ sounds
        "goʊ": "go", "noʊ": "no", "soʊ": "so", "loʊ": "low", "roʊ": "row", "hoʊ": "hoe", "boʊ": "bow", "doʊ": "dough", "floʊ": "flow", "groʊ": "grow",
        "ʃoʊ": "show", "θroʊ": "throw", "bloʊ": "blow", "gloʊ": "glow", "sloʊ": "slow", "snoʊ": "snow", "toʊ": "toe", "moʊ": "mow", "foʊ": "foe", "woʊ": "woe",
        "kroʊ": "crow", "broʊ": "brow", "proʊ": "pro", "stroʊ": "straw", "θoʊ": "though",

        # Long 'u' /u/ sounds
        "du": "do", "nu": "new", "tu": "two", "blu": "blue", "tru": "true", "θru": "through", "flu": "flew", "glu": "glue", "ʧu": "chew", "bru": "brew",
        "dru": "drew", "gru": "grew", "kru": "crew", "skru": "screw", "θru": "threw", "stu": "stew", "ju": "you", "hu": "who", "mu": "moo", "su": "sue",

        # 'oi' /ɔɪ/ sounds
        "bɔɪ": "boy", "tɔɪ": "toy", "jɔɪ": "joy", "rɔɪ": "Roy", "sɔɪ": "soy", "kɔɪ": "coy", "lɔɪ": "loy", "nɔɪ": "annoy", "plɔɪ": "ploy", "klɔɪ": "cloy",
        "frɔɪd": "Freud", "vɔɪd": "void", "ævɔɪd": "avoid", "ɔɪl": "oil", "bɔɪl": "boil",

        # 'ow' /aʊ/ sounds
        "haʊ": "how", "naʊ": "now", "kaʊ": "cow", "baʊ": "bow", "waʊ": "wow", "taʊn": "town", "daʊn": "down", "braʊn": "brown", "kraʊn": "crown", "fraʊn": "frown",
        "draʊn": "drown", "klaʊn": "clown", "glaʊn": "gown", "paʊ": "pow", "ʃaʊ": "show", "θaʊ": "thou", "plaʊ": "plow", "baʊt": "bout", "ʃaʊt": "shout", "kraʊd": "crowd",

        # ===BODY PARTS===
        "hɛd": "head", "feɪs": "face", "aɪ": "eye", "noʊz": "nose", "maʊθ": "mouth", "tʌŋ": "tongue", "tɛθ": "teeth", "tʃin": "chin", "nɛk": "neck", "ɑrm": "arm",
        "hænd": "hand", "fɪst": "fist", "lɛg": "leg", "fut": "foot", "toʊ": "toe", "bæk": "back", "tʃɛst": "chest", "hɑrt": "heart", "braɪn": "brain", "boʊn": "bone",

        # ===ANIMALS===
        "dɔg": "dog", "bɝrd": "bird", "fɪʃ": "fish", "biːr": "bear", "kaʊ": "cow", "pɪg": "pig", "ʃip": "sheep", "goʊt": "goat", "hɔrs": "horse",
        "laɪən": "lion", "taɪgər": "tiger", "mɔŋki": "monkey", "snæk": "snake", "fɹɔg": "frog", "ðək": "duck", "ʃɑrk": "shark", "wæl": "whale", "si": "seal", "bi": "bee",
        "bæt": "bat", "mæws": "mouse", "ræt": "rat", "fɑks": "fox", "wʊlf": "wolf", "ðɪr": "deer", "ɛlk": "elk", "moʊs": "moose", "ɔks": "ox", "jæk": "yak",

        # ===COLORS===
        "blu": "blue", "grin": "green", "jɛloʊ": "yellow", "ɔrənʤ": "orange", "pɝrpəl": "purple", "pɪ pink": "pink", "braʊn": "brown", "blæk": "black", "waɪt": "white",
        "greɪ": "gray", "tæn": "tan", "goʊld": "gold", "sɪlvər": "silver", "vart": "violet",

        # ===NUMBERS===
        "tu": "two", "θri": "three", "fɔr": "four", "faɪv": "five", "sɪks": "six", "sɛvən": "seven", "æt": "eight", "naɪn": "nine", "tɛn": "ten",
        "fɝrst": "first", "sɛkənd": "second", "θɝrd": "third", "fɔrθ": "fourth", "fɪfθ": "fifth", "sɪksθ": "sixth", "twɛlf": "twelfth", "twɛnti": "twenty", "hʌndrəd": "hundred", "θaʊzənd": "thousand",

        # ===COMMON VERBS===
        "wɔk": "walk", "ʤʌmp": "jump", "sɪt": "sit", "stænd": "stand", "laɪ": "lie", "slip": "sleep", "wek": "wake", "it": "eat", "drɪŋk": "drink",
        "lʊk": "look", "hir": "hear", "tʌʧ": "touch", "fil": "feel", "smel": "smell", "test": "taste", "θɪŋk": "think", "noʊ": "know", "læf": "laugh",
        "kraɪ": "cry", "smaɪl": "smile", "tɔk": "talk", "sɪŋ": "sing", "dæns": "dance", "pleɪ": "play", "wɝrk": "work", "stu": "study", "rid": "read", "raɪt": "write",
        "mek": "make", "brɛk": "break", "fɪks": "fix", "oʊpən": "open", "kloʊz": "close", "pʊʃ": "push", "pʊl": "pull", "θroʊ": "throw", "kæʧ": "catch", "hoʊld": "hold",
        "gɪv": "give", "tek": "take", "baɪ": "buy", "sɛl": "sell", "kʌm": "come", "stɑrt": "start", "stɑp": "stop", "fæl": "fall", "raɪz": "rise",

        # ===COMMON ADJECTIVES===
        "smɔl": "small", "lɑrʤ": "large", "taɪni": "tiny", "ʃɔrt": "short", "waɪd": "wide", "θɪn": "thin", "θɪk": "thick", "haɪ": "high",
        "loʊ": "low", "dip": "deep", "fæst": "fast", "sloʊ": "slow", "hɑt": "hot", "koʊld": "cold", "wɔrm": "warm", "kul": "cool", "wɛt": "wet", "draɪ": "dry",
        "gud": "good", "bæd": "bad", "naɪs": "nice", "min": "mean", "kaɪnd": "kind", "hærd": "hard", "sɔft": "soft", "laɪt": "light", "dɑrk": "dark", "braɪt": "bright",

        # ===HOUSEHOLDITEMS===
        "haʊs": "house", "bɛd": "bed", "ʧɛr": "chair", "tebəl": "table", "dɔr": "door", "wɪndoʊ": "window", "wɔl": "wall", "flɔr": "floor", "ruf": "roof", "bæθ": "bath",
        "læmp": "lamp", "klɑk": "clock", "mɪrər": "mirror", "bʊk": "book", "pɛn": "pen", "pɛnsəl": "pencil", "peɪpər": "paper", "kʌp": "cup", "pleɪt": "plate", "naɪf": "knife",
        "fɔrk": "fork", "spun": "spoon", "boʊl": "bowl", "pɑt": "pot", "pæn": "pan", "stʌv": "stove", "sɪŋk": "sink", "soʊp": "soap", "taʊəl": "towel",

        # ===NATURE & WEATHER===
        "mun": "moon", "stɑr": "star", "skaɪ": "sky", "klaʊd": "cloud", "reɪn": "rain", "snoʊ": "snow", "wɪnd": "wind", "stɔrm": "storm", "θʌndər": "thunder",
        "tri": "tree", "flæʊər": "flower", "græs": "grass", "rɑk": "rock", "stoʊn": "stone", "wɔtər": "water", "lek": "lake", "rɪvər": "river", "hɪl": "hill",
        "maʊntən": "mountain", "fild": "field", "fɔrəst": "forest", "dɛzərt": "desert", "ɑɪs": "ice",

        # ===TIME WORDS===
        "deɪ": "day", "naɪt": "night", "mɔrnɪŋ": "morning", "nun": "noon", "ivnɪŋ": "evening", "jir": "year", "mʌnθ": "month", "wik": "week", "aʊər": "hour", "mɪnət": "minute",
        "klɑk": "clock", "wɔʧ": "watch", "ɛrli": "early", "let": "late", "sun": "soon", "nɛkst": "next", "læst": "last", "fɝrst": "first", "pæst": "past",

        # ===ADDITIONAL COMMON WORDS===
        "rul": "rule", "lɔ": "law", "raɪt": "right", "rɔŋ": "wrong", "tru": "true", "fols": "false", "ʃur": "sure",
        "jæŋ": "young", "oʊld": "old", "nu": "new", "frɛʃ": "fresh", "klin": "clean", "dɝrti": "dirty", "ful": "full", "ɛmpti": "empty", "hɛvi": "heavy",
        "fri": "free", "bɪzi": "busy", "rɛdi": "ready", "bɝrθ": "birth", "dɛθ": "death", "laɪf": "life", "hoʊm": "home", "skul": "school", "pleɪs": "place",
        "fin": "find", "sɪŋ": "sing", "sɔŋ": "song", "mjuzɪk": "music", "dæns": "dance",
        "ɛnd": "end", "stɑrt": "start", "help": "help", "kɛr": "care", "lʌv": "love", "het": "hate", "hoʊp": "hope", "fir": "fear",
        "prəʊd": "proud", "ʃeɪm": "shame", "hæpi": "happy", "sæd": "sad", "æŋgri": "angry", "kæm": "calm", "ɛkstætɪk": "excited", "skɛrd": "scared", "breɪv": "brave", "wɑrɪd": "worried",
    }

def get_common_english_words_ipa():
    """Get a set of common English word IPA pronunciations for conflict detection."""
    return set(get_english_word_database().keys())


def get_conflict_word_info(ipa, existing_ipa, english_ipa):
    """Get information about what word this IPA conflicts with."""
    if ipa in english_ipa:
        # Use the consolidated English word database
        english_word_map = get_english_word_database()
        if ipa in english_word_map:
            return f"English word '{english_word_map[ipa]}'"
        else:
            # Fallback for any IPA that might be in the set but not the map
            return f"common English word (IPA: {ipa})"
    elif ipa in existing_ipa:
        return "existing word in your language"
    else:
        return None


def build_ipa_from_suggestion(suggestion, positions, position_mappings):
    """Build IPA pronunciation from a suggestion (list of numbers) and position mappings."""
    try:
        ipa_parts = []
        for i, position in enumerate(positions):
            number = suggestion[i]
            if number in position_mappings[position]:
                data = position_mappings[position][number]
                ipa_parts.append(data['phoneme'])
            else:
                return None
        return "".join(ipa_parts)
    except Exception:
        return None


def filter_suggestions_for_conflicts(suggestions, positions, position_mappings):
    """Filter out suggestions that would create IPA pronunciations conflicting with existing English words.
    Returns both filtered suggestions and the conflicting ones for user review."""

    # Get existing pronunciations to avoid
    existing_ipa = get_existing_ipa_pronunciations()
    english_ipa = get_common_english_words_ipa()

    # Combine both sets
    conflicting_ipa = existing_ipa.union(english_ipa)

    if not conflicting_ipa:
        return suggestions, []  # Return all suggestions, no conflicts

    # Separate suggestions into filtered and conflicting
    filtered_suggestions = []
    conflicting_suggestions = []

    for suggestion in suggestions:
        ipa = build_ipa_from_suggestion(suggestion, positions, position_mappings)
        if ipa is None:
            continue

        if ipa in conflicting_ipa:
            # This suggestion conflicts - add to conflicting list with details
            conflict_word_info = get_conflict_word_info(ipa, existing_ipa, english_ipa)
            conflict_info = {
                'suggestion': suggestion,
                'ipa': ipa,
                'conflict_type': 'english' if ipa in english_ipa else 'existing',
                'conflict_word': conflict_word_info,
                'conflict_info': conflict_word_info  # Ensure both fields are set
            }
            conflicting_suggestions.append(conflict_info)
        else:
            # No conflict, add to filtered list
            filtered_suggestions.append(suggestion)

    return filtered_suggestions, conflicting_suggestions


def display_conflicting_suggestions(conflicting_suggestions, positions, position_mappings):
    """Display the filtered out suggestions with conflict information."""
    if not conflicting_suggestions:
        print("No suggestions were filtered out.")
        return

    print(f"\n--- Filtered Suggestions ({len(conflicting_suggestions)} conflicts found) ---")
    for i, conflict in enumerate(conflicting_suggestions, 1):
        suggestion = conflict['suggestion']
        ipa = conflict['ipa']
        conflict_word = conflict['conflict_word']

        combo_str = ",".join(map(str, suggestion))
        print(f"f{i}: [{combo_str}] → {ipa} (conflicts with {conflict_word})")

    print("\nThese suggestions were filtered out to avoid sounding like existing words.")
    print("You can still select them using 'f' + number (e.g., 'f1', 'f2') if desired.")


def generate_phoneme_suggestions(position_mappings, positions, max_suggestions=500):
    """Generate phoneme combination suggestions optimized for least frequent phoneme usage."""

    # Get the maximum number available for each position
    max_nums = {pos: max(position_mappings[pos].keys()) for pos in positions}

    # Generate all possible combinations within the available range
    all_combinations = []

    if len(positions) == 2:  # CV
        for onset in range(1, max_nums['onset'] + 1):
            for nucleus in range(1, max_nums['nucleus'] + 1):
                all_combinations.append([onset, nucleus])

    elif len(positions) == 3:  # CVC
        for onset in range(1, max_nums['onset'] + 1):
            for nucleus in range(1, max_nums['nucleus'] + 1):
                for coda in range(1, max_nums['coda'] + 1):
                    all_combinations.append([onset, nucleus, coda])

    # Sort combinations by optimal frequency usage:
    # 1. Primary: total frequency sum (lower = better, uses less frequent phonemes)
    # 2. Secondary: lexicographic order (for consistency in tie-breaking)
    optimal_combinations = sorted(all_combinations, key=lambda x: (sum(x), x))

    # Return the requested number of suggestions
    return optimal_combinations[:max_suggestions]


def select_phonemes_with_suggestions(position_mappings, positions, syllable_type, length_types):
    """Select phonemes using suggestions or manual number input with filter support."""

    # Initialize default filters (all positions start with single phonemes)
    current_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }

    # Position mapping
    position_map = {'a': 'onset', 'b': 'nucleus', 'c': 'coda'}

    # Length type mapping
    length_type_map = {
        'a': 'single',  # single consonants, monophthongs
        'b': 'cluster', # cluster2, diphthongs
        'c': 'complex', # cluster3
        'd': 'all'      # all types
    }

    # Track how many suggestions to display (starts with 15, can be extended by 15 more)
    suggestions_to_show = 15

    while True:
        # Generate suggestions based on current position_mappings
        all_suggestions = generate_phoneme_suggestions(position_mappings, positions, max_suggestions=500)

        # Filter out suggestions that conflict with English words
        suggestions, conflicting_suggestions = filter_suggestions_for_conflicts(all_suggestions, positions, position_mappings)

        print(f"\n--- Word Suggestions (optimized for least frequent phonemes) ---")
        displayed_count = 0
        for i, suggestion in enumerate(suggestions, 1):
            if displayed_count >= suggestions_to_show:
                break

            # Build preview of what this suggestion would create
            preview_parts = []
            suggestion_valid = True

            for j, position in enumerate(positions):
                if suggestion[j] in position_mappings[position]:
                    data = position_mappings[position][suggestion[j]]
                    preview_parts.append(data['phoneme'])
                else:
                    suggestion_valid = False
                    break

            if suggestion_valid:
                preview_ipa = "".join(preview_parts)
                combo_str = ",".join(map(str, suggestion))
                print(f"s{i}: [{combo_str}] → {preview_ipa}")
                displayed_count += 1

        # Show extend option if there are more suggestions available
        more_available = len(suggestions) > suggestions_to_show
        if more_available:
            remaining = len(suggestions) - suggestions_to_show
            print(f"\n({remaining} more suggestions available)")

        # Show conflict information if any suggestions were filtered
        if conflicting_suggestions:
            conflicts_found = len(conflicting_suggestions)
            print(f"({conflicts_found} suggestions filtered out to avoid English word conflicts)")

        print(f"\n--- Selection Options ---")
        print("• Enter 's' + number to select a suggestion (e.g., 's1', 's3')")
        if more_available:
            print("• Enter 'extend' to show 15 more suggestions")
        print("• Enter 'conflicts' to see filtered suggestions")
        if conflicting_suggestions:
            print("• Enter 'f' + number to select a filtered suggestion (e.g., 'f1', 'f2')")
        print("• Enter phoneme numbers directly (e.g., '1,2,3' for manual selection)")
        print("• Use letter-based filters to change the display:")
        print("  Position: a=onset, b=nucleus, c=coda")
        print("  Length Type: a=single, b=cluster/diphthong, c=complex cluster, d=all types")
        print("  Examples: 'aa' (onset single), 'bb' (nucleus diphthongs), 'ad,bc,cd' (all positions all types)")

        try:
            input_str = input("Your choice: ").strip()
            if not input_str:
                print("Please enter a selection.")
                continue

            # Check for extend command
            if input_str.lower() == 'extend':
                if more_available:
                    suggestions_to_show += 15
                    print(f"Extended to show {suggestions_to_show} suggestions.")
                    continue
                else:
                    print("No more suggestions available to show.")
                    continue

            # Check for conflicts command
            elif input_str.lower() == 'conflicts':
                display_conflicting_suggestions(conflicting_suggestions, positions, position_mappings)
                continue

            # Check if input is a filtered suggestion selection (starts with 'f')
            elif input_str.lower().startswith('f'):
                if not conflicting_suggestions:
                    print("No filtered suggestions available.")
                    continue

                try:
                    conflict_num = int(input_str[1:])
                    if 1 <= conflict_num <= len(conflicting_suggestions):
                        conflict = conflicting_suggestions[conflict_num - 1]
                        numbers = conflict['suggestion']
                        ipa = conflict['ipa']
                        conflict_word = conflict['conflict_word']

                        print(f"Selected filtered suggestion {conflict_num}: {','.join(map(str, numbers))}")
                        print(f"⚠️  Warning: This creates '{ipa}' which conflicts with {conflict_word}")

                        confirm = input("Do you want to use this suggestion anyway? (y/n): ").strip().lower()
                        if confirm == 'y':
                            return process_phoneme_selection(numbers, positions, position_mappings)
                        else:
                            print("Selection cancelled.")
                            continue
                    else:
                        print(f"Invalid filtered suggestion number. Please enter f1 to f{len(conflicting_suggestions)}.")
                        continue
                except ValueError:
                    print("Invalid filtered suggestion format. Use 'f' followed by a number (e.g., 'f1').")
                    continue

            # Check if input is a suggestion selection (starts with 's')
            elif input_str.lower().startswith('s'):
                try:
                    suggestion_num = int(input_str[1:])
                    if 1 <= suggestion_num <= len(suggestions):
                        numbers = suggestions[suggestion_num - 1]
                        print(f"Selected suggestion {suggestion_num}: {','.join(map(str, numbers))}")

                        # Validate that all numbers exist in their respective position mappings
                        invalid_selections = []
                        for i, position in enumerate(positions):
                            number = numbers[i]
                            if number not in position_mappings[position]:
                                invalid_selections.append(f"{position}: {number}")

                        if invalid_selections:
                            print(f"Invalid selections: {', '.join(invalid_selections)}. Please try again.")
                            continue

                        # Process the suggestion as if it were manual input
                        return process_phoneme_selection(numbers, positions, position_mappings)
                    else:
                        print(f"Invalid suggestion number. Please enter s1 to s{len(suggestions)}.")
                        continue
                except ValueError:
                    print("Invalid suggestion format. Use 's' followed by a number (e.g., 's1').")
                    continue

            # Check if input contains letters (filtering commands)
            elif any(c.isalpha() for c in input_str):
                # Handle filtering commands
                filter_commands = [cmd.strip() for cmd in input_str.split(',')]

                for cmd in filter_commands:
                    if len(cmd) == 2 and cmd[0].isalpha() and cmd[1].isalpha():
                        position_letter = cmd[0].lower()
                        length_letter = cmd[1].lower()

                        if position_letter in position_map and length_letter in length_type_map:
                            position = position_map[position_letter]
                            length_type = length_type_map[length_letter]

                            # Map length type to actual length type names
                            if position in ['onset', 'coda']:
                                if length_type == 'single':
                                    current_filters[position] = 'single_consonants'
                                elif length_type == 'cluster':
                                    current_filters[position] = 'cluster2'
                                elif length_type == 'complex':
                                    current_filters[position] = 'cluster3'
                                elif length_type == 'all':
                                    current_filters[position] = 'all'
                            elif position == 'nucleus':
                                if length_type == 'single':
                                    current_filters[position] = 'monophthongs'
                                elif length_type in ['cluster', 'complex']:  # bc for nucleus all types
                                    current_filters[position] = 'all'
                                elif length_type == 'all':
                                    current_filters[position] = 'all'
                        else:
                            print(f"Invalid filter command: {cmd}")
                            continue

                # Reset suggestion count when filters change
                suggestions_to_show = 15

                # Re-display tables with new filters and update position mappings
                position_mappings = display_phoneme_tables_side_by_side_with_filters(
                    syllable_type, positions, length_types, current_filters
                )

                # Update the position mappings for selection
                continue

            # Handle number-based selection
            else:
                try:
                    numbers = [int(x.strip()) for x in input_str.split(',')]

                    # Validate the number of inputs
                    if len(numbers) != len(positions):
                        print(f"Expected {len(positions)} numbers, got {len(numbers)}. Please try again.")
                        continue

                    # Validate that all numbers exist in their respective position mappings
                    invalid_selections = []
                    for i, position in enumerate(positions):
                        number = numbers[i]
                        if number not in position_mappings[position]:
                            invalid_selections.append(f"{position}: {number}")

                    if invalid_selections:
                        print(f"Invalid selections: {', '.join(invalid_selections)}. Please use numbers from the table.")
                        continue

                    # Process the manual selection
                    return process_phoneme_selection(numbers, positions, position_mappings)

                except ValueError:
                    print("Invalid input. Please enter numbers separated by commas (e.g., '1, 4, 7') or valid filter commands.")
                    continue

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def process_phoneme_selection(numbers, positions, position_mappings):
    """Process the selected phoneme numbers and return phoneme data and IPA."""
    # Create the phoneme data structure
    phoneme_data = {
        'syllable_type': None,  # Will be set by caller
        'onset_phoneme': None,
        'onset_length_type': None,
        'nucleus_phoneme': None,
        'nucleus_length_type': None,
        'coda_phoneme': None,
        'coda_length_type': None
    }

    ipa_parts = []

    # Map numbers to positions and build phoneme data
    for i, position in enumerate(positions):
        number = numbers[i]
        data = position_mappings[position][number]

        # Store the phoneme data
        phoneme_data[f'{position}_phoneme'] = data['phoneme']
        phoneme_data[f'{position}_length_type'] = data['length_type']

        ipa_parts.append(data['phoneme'])
        print(f"Selected {position}: {data['phoneme']} ({data['length_type']})")

    # Build final IPA string
    ipa_phonetics = "".join(ipa_parts)
    print(f"\nBuilt IPA phonetics: {ipa_phonetics}")

    return phoneme_data, ipa_phonetics


def select_phoneme_for_position_without_frequency_update(syllable_type, position):
    """
    Let user select a phoneme from the hierarchy for a specific position.
    Returns a tuple of (selected_phoneme, length_type) or None if cancelled.
    Does NOT update frequencies.
    """
    # Get length types for this position
    length_types_dict = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "coda": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    length_types = length_types_dict[position]

    print(f"\nAvailable length types for {position}:")
    for i, l in enumerate(length_types, 1):
        print(f"{i}: {l}")
    l_choice = input("Select a length type by number: ").strip()
    try:
        length_type = length_types[int(l_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return None

    # Get phonemes for this syllable_type/position/length_type
    data = [
        row for row in get_sorted_phonemes()
        if row[0] == syllable_type and row[1] == position and row[2] == length_type
    ]

    if not data:
        print("No phonemes found for this combination.")
        return None

    print(f"\nPhonemes for {syllable_type} > {position} > {length_type}:")
    print("(Select a phoneme - frequency will be updated after word completion)\n")

    # Group and number phonemes (similar to select_and_modify_frequency)
    grouped = defaultdict(list)
    for row in data:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (g, sub, gfreq, subfreq)
        grouped[key].append((ph, f))

    current = ["", ""]
    phoneme_list = []
    idx = 1
    for key, phonemes in grouped.items():
        g, sub, gfreq, subfreq = key
        new_keys = [g or "", sub or ""]
        for i in range(len(new_keys)):
            if current[i] != new_keys[i]:
                indent = "  " * i
                if i == 0:
                    label = f"- {new_keys[i]} (group freq: {gfreq})"
                elif i == 1 and new_keys[i] != "" and new_keys[i] != "none":
                    label = f"- {new_keys[i]} (subgroup freq: {subfreq})"
                else:
                    label = f"- {new_keys[i]}"
                print(f"{indent}{label}")
                current[i:] = new_keys[i:]
                for j in range(i + 1, len(current)):
                    current[j] = ""
        for ph, f in phonemes:
            print("  " * 3 + f"{idx}: {ph} (freq: {f})")
            phoneme_list.append((syllable_type, position, length_type, g, sub, ph))
            idx += 1

    # Select phoneme
    selection = input(f"\nEnter the number of the phoneme for {position}: ").strip()
    try:
        selection_idx = int(selection) - 1
        selected = phoneme_list[selection_idx]
        selected_phoneme = selected[5]  # phoneme is at index 5

        return (selected_phoneme, length_type)
    except (IndexError, ValueError):
        print("Invalid selection.")
        return None

def update_phoneme_frequency(cursor, conn, syllable_type, position, length_type, phoneme):
    """Update the frequency of a specific phoneme."""
    cursor.execute("""
        UPDATE phonemes
        SET frequency = frequency + 1
        WHERE syllable_type=? AND position=? AND length_type=? AND phoneme=?
    """, (syllable_type, position, length_type, phoneme))
    print(f"  Updated frequency for {position} '{phoneme}'")

def display_phoneme_tables_side_by_side_with_numbers(syllable_type, positions, length_types):
    """Display onset, nucleus, and coda tables side by side with position-based numbering."""
    # Initialize default filters (all positions start with single phonemes)
    default_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }

    return display_phoneme_tables_side_by_side_with_filters(syllable_type, positions, length_types, default_filters)

def display_phoneme_tables_side_by_side_with_filters(syllable_type, positions, length_types, filters):
    """Display onset, nucleus, and coda tables side by side with position-based numbering and filtering."""
    print(f"\n{'='*80}")
    print(f"Phoneme Tables for {syllable_type} Syllable Type")
    print(f"{'='*80}")

    # Get all phoneme data for the tables
    all_phonemes = get_sorted_phonemes()

    # Prepare data for each position and create separate mappings for each position
    position_data = {}
    position_mappings = {}  # Separate mapping for each position

    # First pass: collect all phonemes and create position-based mappings
    for position in positions:
        position_data[position] = {}
        position_mappings[position] = {}  # Each position gets its own mapping starting from 1
        position_number = 1

        # Determine which length types to show for this position based on filters
        if filters[position] == 'all':
            # Show all length types for this position
            target_length_types = length_types[position]
        else:
            # Show only the filtered length type
            target_length_types = [filters[position]]

        # Collect all phonemes for this position
        all_position_phonemes = []
        for length_type in target_length_types:
            for row in all_phonemes:
                if (row[0] == syllable_type and row[1] == position and row[2] == length_type):
                    all_position_phonemes.append(row)

        # Group phonemes by group_type and subgroup_type for hierarchy display
        grouped = defaultdict(list)
        for row in all_position_phonemes:
            s, p, l, g, sub, ph, f, gfreq, subfreq = row
            key = (g, sub, gfreq, subfreq)
            grouped[key].append((ph, f))

        # Sort groups by aggregate frequency (ascending), then subgroups, then phonemes
        sorted_groups = sorted(grouped.items(), key=lambda x: (x[0][2], x[0][3] if x[0][3] is not None else -1))

        # Create mapping for all phonemes in this position (after hierarchy sorting)
        for key, phonemes in sorted_groups:
            g, sub, gfreq, subfreq = key
            # Sort phonemes within this group/subgroup by frequency (ascending)
            sorted_phonemes = sorted(phonemes, key=lambda x: x[1])

            for phoneme, freq in sorted_phonemes:
                position_mappings[position][position_number] = {
                    'position': position,
                    'phoneme': phoneme,
                    'length_type': next(row[2] for row in all_position_phonemes if row[5] == phoneme),
                    'group_type': g,
                    'subgroup_type': sub,
                    'group_freq': gfreq,
                    'subgroup_freq': subfreq,
                    'frequency': freq,
                    'row_data': next(row for row in all_position_phonemes if row[5] == phoneme)
                }
                position_number += 1

        # Also store the data by length type for display purposes
        for length_type in target_length_types:
            position_data[position][length_type] = [row for row in all_position_phonemes if row[2] == length_type]

    # Calculate table widths (now accounting for position-based numbers)
    # Create reverse mapping for phoneme lookup
    reverse_mappings = {}
    for position in positions:
        reverse_mappings[position] = {}
        counter = 1
        for length_type in position_data[position]:
            for row in position_data[position][length_type]:
                phoneme = row[5]
                key = (phoneme, length_type)
                if key not in reverse_mappings[position]:
                    reverse_mappings[position][key] = counter
                    counter += 1

    max_widths = {}
    for position in positions:
        # Set minimum width for each position to prevent cramped display
        min_width = 30  # Minimum 30 characters per position
        max_widths[position] = min_width
        for length_type in position_data[position]:
            if position_data[position][length_type]:
                # Add filter info to header
                if filters[position] == 'all':
                    header = f"{position.upper()} (All Types)"
                else:
                    header = f"{position.upper()} ({filters[position]})"
                max_widths[position] = max(max_widths[position], len(header))

                for row in position_data[position][length_type]:
                    phoneme = row[5]
                    freq = row[6]
                    # Use reverse mapping for efficient lookup
                    key = (phoneme, length_type)
                    if key in reverse_mappings[position]:
                        num = reverse_mappings[position][key]
                        max_widths[position] = max(max_widths[position], len(f"{num}: {phoneme} ({freq})"))

    # Display tables side by side
    for i, position in enumerate(positions):
        if i > 0:
            print("  ", end="")
        if filters[position] == 'all':
            header = f"{position.upper()} (All Types)"
        else:
            header = f"{position.upper()} ({filters[position]})"
        print(f"{header:<{max_widths[position]}}", end="")
    print()

    for i, position in enumerate(positions):
        if i > 0:
            print("  ", end="")
        print("-" * max_widths[position], end="")
    print()

    # Prepare display data for each position with hierarchy information
    position_display_data = {}
    for position in positions:
        position_display_data[position] = []

        if filters[position] == 'all':
            # For 'all' types, show hierarchy with clean group/subgroup separators
            display_groups = defaultdict(list)
            for num, data in position_mappings[position].items():
                key = (data['group_type'], data['subgroup_type'], data['group_freq'], data['subgroup_freq'])
                display_groups[key].append((num, data))

            # Helper function to get length type priority for tie-breaking
            def get_length_type_priority(data_list):
                """Get the length type priority for a group (shorter length types have higher priority)"""
                if not data_list:
                    return 999  # Default high priority for empty groups

                # Get the length type from the first phoneme in the group
                length_type = data_list[0][1]['length_type']

                # Define priority mapping (lower number = higher priority)
                if position in ['onset', 'coda']:
                    priority_map = {
                        'single_consonants': 0,  # Highest priority (shortest)
                        'cluster2': 1,
                        'cluster3': 2
                    }
                elif position == 'nucleus':
                    priority_map = {
                        'monophthongs': 0,  # Highest priority (shortest)
                        'diphthongs': 1
                    }
                else:
                    return 999

                return priority_map.get(length_type, 999)

            # Sort by frequency first, then by length type priority for ties
            sorted_display_groups = sorted(display_groups.items(), 
                key=lambda x: (x[0][2], get_length_type_priority(x[1]), x[0][3] if x[0][3] is not None else -1))

            current_group = ""
            current_subgroup = ""

            for i, (key, phoneme_data_list) in enumerate(sorted_display_groups):
                g, sub, gfreq, subfreq = key

                # Add group header if new
                if g != current_group:
                    # Add blank line before new group (except for first group)
                    if current_group != "":
                        position_display_data[position].append("")

                    # Add group name and frequency
                    position_display_data[position].append(f"{g} ({gfreq})")
                    # Add separator line under group name
                    separator_length = len(f"{g} ({gfreq})")
                    position_display_data[position].append("-" * separator_length)

                    current_group = g
                    current_subgroup = ""

                # Add subgroup header if new
                if sub and sub != "none" and sub != current_subgroup:
                    position_display_data[position].append(f"{sub} ({subfreq})")
                    current_subgroup = sub

                # Add phonemes within this group/subgroup
                for num, data in phoneme_data_list:
                    position_display_data[position].append(f"{num}: {data['phoneme']} ({data['frequency']})")
        else:
            # For single length types, show hierarchy with clean group/subgroup separators
            display_groups = defaultdict(list)
            for num, data in position_mappings[position].items():
                key = (data['group_type'], data['subgroup_type'], data['group_freq'], data['subgroup_freq'])
                display_groups[key].append((num, data))

            # Helper function to get length type priority for tie-breaking
            def get_length_type_priority(data_list):
                """Get the length type priority for a group (shorter length types have higher priority)"""
                if not data_list:
                    return 999  # Default high priority for empty groups

                # Get the length type from the first phoneme in the group
                length_type = data_list[0][1]['length_type']

                # Define priority mapping (lower number = higher priority)
                if position in ['onset', 'coda']:
                    priority_map = {
                        'single_consonants': 0,  # Highest priority (shortest)
                        'cluster2': 1,
                        'cluster3': 2
                    }
                elif position == 'nucleus':
                    priority_map = {
                        'monophthongs': 0,  # Highest priority (shortest)
                        'diphthongs': 1
                    }
                else:
                    return 999

                return priority_map.get(length_type, 999)

            # Sort by frequency first, then by length type priority for ties
            sorted_display_groups = sorted(display_groups.items(), 
                key=lambda x: (x[0][2], get_length_type_priority(x[1]), x[0][3] if x[0][3] is not None else -1))

            current_group = ""
            current_subgroup = ""

            for i, (key, phoneme_data_list) in enumerate(sorted_display_groups):
                g, sub, gfreq, subfreq = key

                # Add group header if new
                if g != current_group:
                    # Add blank line before new group (except for first group)
                    if current_group != "":
                        position_display_data[position].append("")

                    # Add group name and frequency
                    position_display_data[position].append(f"{g} ({gfreq})")
                    # Add separator line under group name
                    separator_length = len(f"{g} ({gfreq})")
                    position_display_data[position].append("-" * separator_length)

                    current_group = g
                    current_subgroup = ""

                # Add subgroup header if new
                if sub and sub != "none" and sub != current_subgroup:
                    position_display_data[position].append(f"{sub} ({subfreq})")
                    current_subgroup = sub

                # Add phonemes within this group/subgroup
                for num, data in phoneme_data_list:
                    position_display_data[position].append(f"{num}: {data['phoneme']} ({data['frequency']})")

    # Calculate maximum number of display rows
    max_display_rows = max(len(position_display_data[pos]) for pos in positions)

    # Display phonemes row by row side by side with hierarchy
    for row_idx in range(max_display_rows):
        for i, position in enumerate(positions):
            if i > 0:
                print("  ", end="")

            # Get the display string for this row
            display_str = ""
            if row_idx < len(position_display_data[position]):
                display_str = position_display_data[position][row_idx]

            print(f"{display_str:<{max_widths[position]}}", end="")
        print()

    print(f"\n{'='*80}")

    return position_mappings

def select_phonemes_by_numbers_or_filters(position_mappings, positions, syllable_type, length_types):
    """Select phonemes using numbers or letter-based filters with position-based numbering."""
    print(f"\nEnter phoneme numbers for each position in order: {', '.join(positions)}")
    print("Example: For CVC, enter '1, 4, 7' to select the 1st onset, 4th nucleus, and 7th coda")
    print("Note: Each position starts numbering from 1 independently")
    print("\nOr use letter-based filters:")
    print("Position: a=onset, b=nucleus, c=coda")
    print("Length Type: a=single, b=cluster/diphthong, c=complex cluster, d=all types")
    print("Examples: 'aa' (onset single), 'bb' (nucleus diphthongs), 'bc' (nucleus all types), 'ad,bc,cd' (all positions all types)")

    # Initialize default filters (all positions start with single phonemes)
    current_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }

    # Position mapping
    position_map = {'a': 'onset', 'b': 'nucleus', 'c': 'coda'}

    # Length type mapping
    length_type_map = {
        'a': 'single',  # single consonants, monophthongs
        'b': 'cluster', # cluster2, diphthongs
        'c': 'complex', # cluster3
        'd': 'all'      # all types
    }

    while True:
        try:
            input_str = input("Enter phoneme numbers or filters: ").strip()
            if not input_str:
                print("Please enter phoneme numbers or filters.")
                continue

            # Check if input contains letters (filtering commands)
            if any(c.isalpha() for c in input_str):
                # Handle filtering commands
                filter_commands = [cmd.strip() for cmd in input_str.split(',')]

                for cmd in filter_commands:
                    if len(cmd) == 2 and cmd[0].isalpha() and cmd[1].isalpha():
                        position_letter = cmd[0].lower()
                        length_letter = cmd[1].lower()

                        if position_letter in position_map and length_letter in length_type_map:
                            position = position_map[position_letter]
                            length_type = length_type_map[length_letter]

                            # Apply the filter
                            if length_type == 'all':
                                # Show all length types for this position
                                current_filters[position] = 'all'
                                print(f"Filtering {position} to show all phoneme types...")
                            else:
                                # Map to specific length types
                                if position == 'nucleus':
                                    if length_type == 'single':
                                        current_filters[position] = 'monophthongs'
                                    elif length_type == 'cluster':
                                        current_filters[position] = 'diphthongs'
                                    elif length_type == 'complex':
                                        # For nucleus, 'c' means show all types (monophthongs + diphthongs)
                                        current_filters[position] = 'all'
                                        print(f"Filtering {position} to show all phoneme types...")
                                    else:
                                        print(f"Invalid length type '{length_type}' for nucleus position")
                                        continue
                                else:  # onset or coda
                                    if length_type == 'single':
                                        current_filters[position] = 'single_consonants'
                                    elif length_type == 'cluster':
                                        current_filters[position] = 'cluster2'
                                    elif length_type == 'complex':
                                        current_filters[position] = 'cluster3'
                                    else:
                                        print(f"Invalid length type '{length_type}' for {position} position")
                                        continue

                                print(f"Filtering {position} to {current_filters[position]}...")
                        else:
                            print(f"Invalid filter command: {cmd}")
                            continue

                # Re-display tables with new filters
                print("\nRe-displaying tables with updated filters...")
                new_position_mappings = display_phoneme_tables_side_by_side_with_filters(
                    syllable_type, positions, length_types, current_filters
                )

                # Update the position mappings for selection
                position_mappings.update(new_position_mappings)

                continue

            # Handle number-based selection
            try:
                numbers = [int(x.strip()) for x in input_str.split(',')]

                # Validate the number of inputs
                if len(numbers) != len(positions):
                    print(f"Expected {len(positions)} numbers, got {len(numbers)}. Please try again.")
                    continue

                # Validate that all numbers exist in their respective position mappings
                invalid_selections = []
                for i, position in enumerate(positions):
                    number = numbers[i]
                    if number not in position_mappings[position]:
                        invalid_selections.append(f"{position}: {number}")

                if invalid_selections:
                    print(f"Invalid selections: {', '.join(invalid_selections)}. Please use numbers from the table.")
                    continue

                # Process the manual selection
                return process_phoneme_selection(numbers, positions, position_mappings)

            except ValueError:
                print("Invalid input. Please enter numbers separated by commas (e.g., '1, 4, 7') or valid filter commands.")
                continue

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def add_new_word_with_structure(cursor, conn, language, english_words, new_language_word, 
                               ipa_phonetics, dictionary_phonetics, phoneme_data, video_path=None, syllables_data=None):
    """
    Add a new word to the database with structured phoneme data.
    phoneme_data should contain: syllable_type, onset_phoneme, onset_length_type, 
    nucleus_phoneme, nucleus_length_type, coda_phoneme, coda_length_type
    """
    # Ensure english_words is a list
    if isinstance(english_words, str):
        # Handle both comma-separated and space-separated words
        if ',' in english_words:
            english_words = [word.strip() for word in english_words.split(',') if word.strip()]
        else:
            # Split by spaces if no commas
            english_words = [word.strip() for word in english_words.split() if word.strip()]
    elif not isinstance(english_words, list):
        english_words = []  # Ensure it's a list
    
    # Filter out empty strings and single characters that might be artifacts
    english_words = [word for word in english_words if word and len(word) > 0 and word not in ['[', ']', '"', ',', ' ']]
    
    # Check if this new language word already exists
    cursor.execute("SELECT english_words FROM words WHERE LOWER(new_language_word) = LOWER(?)", (new_language_word,))
    existing_row = cursor.fetchone()

    if existing_row:
        # Word exists - add new English translations to existing list
        try:
            existing_english_data = json.loads(existing_row[0])
            if isinstance(existing_english_data, list):
                existing_english_list = existing_english_data
            else:
                # If it's a string, convert it to a list
                existing_english_list = [str(existing_english_data)] if existing_english_data else []
        except (json.JSONDecodeError, TypeError):
            # Handle legacy data that might not be JSON
            existing_english_list = [existing_row[0]] if existing_row[0] else []

        # Add new English words that aren't already in the list
        added_words = []
        for word in english_words:
            if word.lower() not in [existing.lower() for existing in existing_english_list]:
                existing_english_list.append(word)
                added_words.append(word)

        if added_words:
            print(f"\n--- Adding to Existing Word ---")
            print(f"'{new_language_word}' already exists. Adding new meanings:")
            for word in added_words:
                print(f"  + {word}")

            # Update the existing record (optionally update video if provided)
            if video_path:
                cursor.execute("""
                    UPDATE words SET english_words = ?, video_path = ? 
                    WHERE LOWER(new_language_word) = LOWER(?)
                """, (json.dumps(existing_english_list), video_path, new_language_word))
                print(f"✓ Video updated for existing word")
            else:
                cursor.execute("""
                    UPDATE words SET english_words = ? 
                    WHERE LOWER(new_language_word) = LOWER(?)
                """, (json.dumps(existing_english_list), new_language_word))
            conn.commit()

            print(f"\n'{new_language_word}' now has these English meanings:")
            for translation in existing_english_list:
                print(f"  • {translation}")
        else:
            print(f"\nAll English meanings for '{new_language_word}' already exist in database.")
    else:
        # New word - create new record with structured phoneme data
        cursor.execute("""
            INSERT INTO words (language, english_words, new_language_word, ipa_phonetics, 
                             dictionary_phonetics, syllable_type, onset_phoneme, onset_length_type,
                             nucleus_phoneme, nucleus_length_type, coda_phoneme, coda_length_type, video_path, syllables_data) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            language, 
            json.dumps(english_words), 
            new_language_word, 
            ipa_phonetics, 
            dictionary_phonetics,
            phoneme_data.get('syllable_type', 'CVC'),
            phoneme_data.get('onset_phoneme'),
            phoneme_data.get('onset_length_type', ''),
            phoneme_data.get('nucleus_phoneme'),
            phoneme_data.get('nucleus_length_type', ''),
            phoneme_data.get('coda_phoneme'),
            phoneme_data.get('coda_length_type', ''),
            video_path,
            syllables_data
        ))
        conn.commit()
        video_msg = f" with video: {video_path}" if video_path else ""
        print(f"✓ Added new word '{new_language_word}' with English meaning(s): {', '.join(english_words)}{video_msg}")

        # Display the structured phoneme data for confirmation
        print(f"  Syllable Type: {phoneme_data.get('syllable_type', 'CVC')}")
        if phoneme_data.get('onset_phoneme'):
            print(f"  Onset: {phoneme_data.get('onset_phoneme')} ({phoneme_data.get('onset_length_type', '')})")
        if phoneme_data.get('nucleus_phoneme'):
            print(f"  Nucleus: {phoneme_data.get('nucleus_phoneme')} ({phoneme_data.get('nucleus_length_type', '')})")
        if phoneme_data.get('coda_phoneme'):
            print(f"  Coda: {phoneme_data.get('coda_phoneme')} ({phoneme_data.get('coda_length_type', '')})")

        return cursor.lastrowid

    return None

def add_new_word(cursor, conn, language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics):
    # Ensure english_words is a list
    if isinstance(english_words, str):
        # Handle both comma-separated and space-separated words
        if ',' in english_words:
            english_words = [word.strip() for word in english_words.split(',') if word.strip()]
        else:
            # Split by spaces if no commas
            english_words = [word.strip() for word in english_words.split() if word.strip()]
    elif not isinstance(english_words, list):
        english_words = []  # Ensure it's a list
    
    # Filter out empty strings and single characters that might be artifacts
    english_words = [word for word in english_words if word and len(word) > 0 and word not in ['[', ']', '"', ',', ' ']]
    
    # Check if this new language word already exists
    cursor.execute("SELECT english_words FROM words WHERE LOWER(new_language_word) = LOWER(?)", (new_language_word,))
    existing_row = cursor.fetchone()

    if existing_row:
        # Word exists - add new English translations to existing list
        existing_english_list = json.loads(existing_row[0])

        # Add new English words that aren't already in the list
        added_words = []
        for word in english_words:
            if word.lower() not in [existing.lower() for existing in existing_english_list]:
                existing_english_list.append(word)
                added_words.append(word)

        if added_words:
            print(f"\n--- Adding to Existing Word ---")
            print(f"'{new_language_word}' already exists. Adding new meanings:")
            for word in added_words:
                print(f"  + {word}")

            # Update the existing record
            cursor.execute("""
                UPDATE words SET english_words = ? 
                WHERE LOWER(new_language_word) = LOWER(?)
            """, (json.dumps(existing_english_list), new_language_word))
            conn.commit()

            print(f"\n'{new_language_word}' now has these English meanings:")
            for translation in existing_english_list:
                print(f"  • {translation}")
        else:
            print(f"\nAll English meanings for '{new_language_word}' already exist in database.")
    else:
        # New word - create new record
        cursor.execute("""
            INSERT INTO words (language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics) 
            VALUES (?, ?, ?, ?, ?)
        """, (language, json.dumps(english_words), new_language_word, ipa_phonetics, dictionary_phonetics))
        conn.commit()
        print(f"✓ Added new word '{new_language_word}' with English meaning(s): {', '.join(english_words)}")

    return True

def select_phoneme_for_position(syllable_type, position):
    """
    Let user select a phoneme from the hierarchy for a specific position.
    Returns the selected phoneme string or None if cancelled.
    """
    # Get length types for this position
    length_types_dict = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "coda": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    length_types = length_types_dict[position]

    print(f"\nAvailable length types for {position}:")
    for i, l in enumerate(length_types, 1):
        print(f"{i}: {l}")
    l_choice = input("Select a length type by number: ").strip()
    try:
        length_type = length_types[int(l_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return None

    # Get phonemes for this syllable_type/position/length_type
    data = [
        row for row in get_sorted_phonemes()
        if row[0] == syllable_type and row[1] == position and row[2] == length_type
    ]

    if not data:
        print("No phonemes found for this combination.")
        return None

    print(f"\nPhonemes for {syllable_type} > {position} > {length_type}:")
    print("(Select a phoneme and increase its frequency)\n")

    # Group and number phonemes (similar to select_and_modify_frequency)
    grouped = defaultdict(list)
    for row in data:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (g, sub, gfreq, subfreq)
        grouped[key].append((ph, f))

    current = ["", ""]
    phoneme_list = []
    idx = 1
    for key, phonemes in grouped.items():
        g, sub, gfreq, subfreq = key
        new_keys = [g or "", sub or ""]
        for i in range(len(new_keys)):
            if current[i] != new_keys[i]:
                indent = "  " * i
                if i == 0:
                    label = f"- {new_keys[i]} (group freq: {gfreq})"
                elif i == 1 and new_keys[i] != "" and new_keys[i] != "none":
                    label = f"- {new_keys[i]} (subgroup freq: {subfreq})"
                else:
                    label = f"- {new_keys[i]}"
                print(f"{indent}{label}")
                current[i:] = new_keys[i:]
                for j in range(i + 1, len(current)):
                    current[j] = ""
        for ph, f in phonemes:
            print("  " * 3 + f"{idx}: {ph} (freq: {f})")
            phoneme_list.append((syllable_type, position, length_type, g, sub, ph))
            idx += 1

    # Select phoneme
    selection = input(f"\nEnter the number of the phoneme for {position}: ").strip()
    try:
        selection_idx = int(selection) - 1
        selected = phoneme_list[selection_idx]
        selected_phoneme = selected[5]  # phoneme is at index 5

        # Increase frequency of selected phoneme
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE phonemes
            SET frequency = frequency + 1
            WHERE syllable_type=? AND position=? AND length_type=? AND group_type=? AND subgroup_type=? AND phoneme=?
        """, selected)
        conn.commit()
        conn.close()

        return selected_phoneme
    except (IndexError, ValueError):
        print("Invalid selection.")
        return None

def select_phoneme_for_position_with_data(syllable_type, position):
    """
    Let user select a phoneme from the hierarchy for a specific position.
    Returns a tuple of (selected_phoneme, length_type) or None if cancelled.
    """
    # Get length types for this position
    length_types_dict = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "coda": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    length_types = length_types_dict[position]

    print(f"\nAvailable length types for {position}:")
    for i, l in enumerate(length_types, 1):
        print(f"{i}: {l}")
    l_choice = input("Select a length type by number: ").strip()
    try:
        length_type = length_types[int(l_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return None

    # Get phonemes for this syllable_type/position/length_type
    data = [
        row for row in get_sorted_phonemes()
        if row[0] == syllable_type and row[1] == position and row[2] == length_type
    ]

    if not data:
        print("No phonemes found for this combination.")
        return None

    print(f"\nPhonemes for {syllable_type} > {position} > {length_type}:")
    print("(Select a phoneme and increase its frequency)\n")

    # Group and number phonemes (similar to select_and_modify_frequency)
    grouped = defaultdict(list)
    for row in data:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (g, sub, gfreq, subfreq)
        grouped[key].append((ph, f))

    current = ["", ""]
    phoneme_list = []
    idx = 1
    for key, phonemes in grouped.items():
        g, sub, gfreq, subfreq = key
        new_keys = [g or "", sub or ""]
        for i in range(len(new_keys)):
            if current[i] != new_keys[i]:
                indent = "  " * i
                if i == 0:
                    label = f"- {new_keys[i]} (group freq: {gfreq})"
                elif i == 1 and new_keys[i] != "" and new_keys[i] != "none":
                    label = f"- {new_keys[i]} (subgroup freq: {subfreq})"
                else:
                    label = f"- {new_keys[i]}"
                print(f"{indent}{label}")
                current[i:] = new_keys[i:]
                for j in range(i + 1, len(current)):
                    current[j] = ""
        for ph, f in phonemes:
            print("  " * 3 + f"{idx}: {ph} (freq: {f})")
            phoneme_list.append((syllable_type, position, length_type, g, sub, ph))
            idx += 1

    # Select phoneme
    selection = input(f"\nEnter the number of the phoneme for {position}: ").strip()
    try:
        selection_idx = int(selection) - 1
        selected = phoneme_list[selection_idx]
        selected_phoneme = selected[5]  # phoneme is at index 5

        # Increase frequency of selected phoneme
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE phonemes
            SET frequency = frequency + 1
            WHERE syllable_type=? AND position=? AND length_type=? AND group_type=? AND subgroup_type=? AND phoneme=?
        """, selected)
        conn.commit()
        conn.close()

        return (selected_phoneme, length_type)
    except (IndexError, ValueError):
        print("Invalid selection.")
        return None

# --- Display all words ---
def display_words():
    """Display all words in the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics,
               syllable_type, onset_phoneme, onset_length_type, nucleus_phoneme, nucleus_length_type,
               coda_phoneme, coda_length_type, video_path
        FROM words ORDER BY new_language_word
    """)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No words found in database.")
    else:
        print(f"\n--- All Words ({len(rows)} entries) ---")
        for (lang, eng_json, new, ipa, dict_ph, 
             syllable_type, onset_phoneme, onset_length_type, 
             nucleus_phoneme, nucleus_length_type, coda_phoneme, coda_length_type, video_path) in rows:
            english_list = json.loads(eng_json)
            print(f"\nLanguage: {lang}")
            print(f"English: {', '.join(english_list)}")
            print(f"New Language: {new}")
            print(f"IPA: {ipa}")
            print(f"Dictionary: {dict_ph}")
            if video_path:
                print(f"Video: {video_path}")
            else:
                print(f"Video: None")

            # Display structured phoneme data if available
            if syllable_type and onset_phoneme and nucleus_phoneme:
                print(f"Structure: {syllable_type}")
                print(f"  Onset: {onset_phoneme} ({onset_length_type})")
                print(f"  Nucleus: {nucleus_phoneme} ({nucleus_length_type})")
                if coda_phoneme:
                    print(f"  Coda: {coda_phoneme} ({coda_length_type})")

    input("Press Enter to return to the main menu...")
# --- Add new phoneme ---
def add_new_phoneme():
    """Add a new phoneme to the database with its classification data."""
    print("\n--- Add New Phoneme ---")

    # Get syllable type
    syllable_types = ["CVC", "CV"]
    print("Available syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        input("Press Enter to return to the main menu...")
        return

    # Get position
    positions_dict = {
        "CVC": ["onset", "nucleus", "coda"],
        "CV": ["onset", "nucleus"]
    }
    positions = positions_dict[syllable_type]
    print(f"\nAvailable positions for {syllable_type}:")
    for i, p in enumerate(positions, 1):
        print(f"{i}: {p}")
    p_choice = input("Select a position by number: ").strip()
    try:
        position = positions[int(p_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        input("Press Enter to return to the main menu...")
        return

    # Get length type
    length_types_dict = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "coda": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    length_types = length_types_dict[position]
    print(f"\nAvailable length types for {position}:")
    for i, l in enumerate(length_types, 1):
        print(f"{i}: {l}")
    l_choice = input("Select a length type by number: ").strip()
    try:
        length_type = length_types[int(l_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        input("Press Enter to return to the main menu...")
        return

    # Connect to database before using cursor
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get existing group types for this category
    cursor.execute("""
        SELECT DISTINCT group_type FROM phonemes 
        WHERE syllable_type = ? AND position = ? AND length_type = ?
        ORDER BY group_type
    """, (syllable_type, position, length_type))
    existing_groups = [row[0] for row in cursor.fetchall()]

    # Display existing group types
    print(f"\nExisting group types for {syllable_type} > {position} > {length_type}:")
    if existing_groups:
        for i, group in enumerate(existing_groups, 1):
            print(f"  {i}: {group}")
        print("  Or enter a new group type:")
    else:
        print("  No existing groups found. You'll be creating the first group in this category.")

    # Get group type
    group_input = input(f"Enter group type number or new group name (e.g., 'plosives', 'fricatives', 'vowels'): ").strip()

    # Check if input is a number (selecting existing group)
    if group_input.isdigit() and existing_groups:
        try:
            group_idx = int(group_input) - 1
            if 0 <= group_idx < len(existing_groups):
                group_type = existing_groups[group_idx]
                print(f"Selected existing group: {group_type}")
            else:
                print("Invalid group number. Please enter the group name instead.")
                group_type = input(f"Enter group type: ").strip()
        except (ValueError, IndexError):
            group_type = group_input
    else:
        group_type = group_input

    if not group_type:
        print("Group type is required.")
        input("Press Enter to return to the main menu...")
        return

    # Get existing subgroup types for this group
    cursor.execute("""
        SELECT DISTINCT subgroup_type FROM phonemes 
        WHERE syllable_type = ? AND position = ? AND length_type = ? AND group_type = ?
        AND subgroup_type IS NOT NULL
        ORDER BY subgroup_type
    """, (syllable_type, position, length_type, group_type))
    existing_subgroups = [row[0] for row in cursor.fetchall()]

    # Display existing subgroup types
    print(f"\nExisting subgroup types for {group_type}:")
    if existing_subgroups:
        print("  0: No subgroup")
        for i, subgroup in enumerate(existing_subgroups, 1):
            print(f"  {i}: {subgroup}")
        print("  Or enter a new subgroup type:")
    else:
        print("  No existing subgroups found.")

    # Get subgroup type (optional)
    subgroup_input = input("Enter subgroup number or new subgroup name (press Enter for no subgroup): ").strip()

    if not subgroup_input:
        subgroup_type = None
    elif subgroup_input == "0":
        subgroup_type = None
    elif subgroup_input.isdigit() and existing_subgroups:
        try:
            subgroup_idx = int(subgroup_input) - 1
            if 0 <= subgroup_idx < len(existing_subgroups):
                subgroup_type = existing_subgroups[subgroup_idx]
                print(f"Selected existing subgroup: {subgroup_type}")
            else:
                subgroup_type = subgroup_input if subgroup_input != "0" else None
        except (ValueError, IndexError):
            subgroup_type = subgroup_input if subgroup_input != "0" else None
    else:
        subgroup_type = subgroup_input if subgroup_input != "0" else None

    # Get phoneme
    phoneme = input("Enter the phoneme symbol (e.g., 'p', 'b', 'ɑ'): ").strip()
    if not phoneme:
        print("Phoneme symbol is required.")
        input("Press Enter to return to the main menu...")
        return

    # Get initial frequency
    try:
        frequency = int(input("Enter initial frequency (default 0): ").strip() or "0")
        if frequency < 0:
            frequency = 0
    except ValueError:
        frequency = 0

    # Add to database (connection already established above)
    try:
        cursor.execute("""
            INSERT INTO phonemes 
            (syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency))
        conn.commit()

        print(f"\n✓ Successfully added phoneme:")
        print(f"  Syllable Type: {syllable_type}")
        print(f"  Position: {position}")
        print(f"  Length Type: {length_type}")
        print(f"  Group: {group_type}")
        print(f"  Subgroup: {subgroup_type or 'None'}")
        print(f"  Phoneme: {phoneme}")
        print(f"  Initial Frequency: {frequency}")

    except sqlite3.IntegrityError:
        print(f"\n✗ Error: This phoneme classification already exists in the database.")
        print(f"Phoneme '{phoneme}' with the same classification parameters is already present.")
    except Exception as e:
        print(f"\n✗ Error adding phoneme: {e}")

    conn.close()
    input("Press Enter to return to the main menu...")

# --- Delete phoneme ---
def delete_phoneme():
    """Delete a phoneme from the database."""
    print("\n--- Delete Phoneme ---")

    # Check if phonemes table is empty
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM phonemes")
    count = cursor.fetchone()[0]

    if count == 0:
        print("No phonemes found in database.")
        conn.close()
        input("Press Enter to return to the main menu...")
        return

    # Get syllable type
    syllable_types = ["CVC", "CV"]
    print("Available syllable types:")
    print("1: CVC")
    print("2: CV")
    s_choice = input("Select a syllable type by number: ").strip()
    try:
        syllable_type = syllable_types[int(s_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        conn.close()
        input("Press Enter to return to the main menu...")
        return

    # Get position
    positions_dict = {
        "CVC": ["onset", "nucleus", "coda"],
        "CV": ["onset", "nucleus"]
    }
    positions = positions_dict[syllable_type]
    print(f"\nAvailable positions for {syllable_type}:")
    for i, p in enumerate(positions, 1):
        print(f"{i}: {p}")
    p_choice = input("Select a position by number: ").strip()
    try:
        position = positions[int(p_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        conn.close()
        input("Press Enter to return to the main menu...")
        return

    # Get length type
    length_types_dict = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "coda": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    length_types = length_types_dict[position]
    print(f"\nAvailable length types for {position}:")
    for i, l in enumerate(length_types, 1):
        print(f"{i}: {l}")
    l_choice = input("Select a length type by number: ").strip()
    try:
        length_type = length_types[int(l_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        conn.close()
        input("Press Enter to return to the main menu...")
        return

    # Get phonemes for this category in hierarchical order
    data = [
        row for row in get_sorted_phonemes()
        if row[0] == syllable_type and row[1] == position and row[2] == length_type
    ]

    if not data:
        print(f"No phonemes found for {syllable_type} > {position} > {length_type}")
        conn.close()
        input("Press Enter to return to the main menu...")
        return

    # Display phonemes in hierarchical structure with numbers for selection
    print(f"\nPhonemes in {syllable_type} > {position} > {length_type}:")
    print("(Hierarchical order - select by number)\n")

    # Group phonemes hierarchically
    grouped = defaultdict(list)
    for row in data:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (g, sub, gfreq, subfreq)
        grouped[key].append((ph, f, row))  # Include full row data for database operations

    current = ["", ""]
    phoneme_list = []
    idx = 1

    for key, phonemes in grouped.items():
        g, sub, gfreq, subfreq = key
        new_keys = [g or "", sub or ""]

        # Display group/subgroup headers
        for i in range(len(new_keys)):
            if current[i] != new_keys[i]:
                indent = "  " * i
                if i == 0:
                    label = f"- {new_keys[i]} (group freq: {gfreq})"
                elif i == 1 and new_keys[i] != "" and new_keys[i] != "none":
                    label = f"- {new_keys[i]} (subgroup freq: {subfreq})"
                else:
                    label = f"- {new_keys[i]}"
                print(f"{indent}{label}")
                current[i:] = new_keys[i:]
                for j in range(i + 1, len(current)):
                    current[j] = ""

        # Display numbered phonemes
        for ph, f, row_data in phonemes:
            print("  " * 3 + f"{idx}: {ph} (freq: {f})")
            # Store the row data for database deletion
            s, p, l, g, sub, phoneme_symbol, freq, gfreq, subfreq = row_data
            phoneme_list.append((s, p, l, g, sub, phoneme_symbol))
            idx += 1

    # Select phoneme to delete
    selection = input(f"\nEnter the number of the phoneme to delete (1-{len(phoneme_list)}): ").strip()
    try:
        selection_idx = int(selection) - 1
        if 0 <= selection_idx < len(phoneme_list):
            selected_data = phoneme_list[selection_idx]
            s, p, l, g, sub, phoneme_symbol = selected_data

            # Get the actual database ID and frequency for this phoneme
            cursor.execute("""
                SELECT id, frequency FROM phonemes 
                WHERE syllable_type=? AND position=? AND length_type=? 
                AND group_type=? AND (subgroup_type=? OR (subgroup_type IS NULL AND ? IS NULL)) AND phoneme=?
            """, (s, p, l, g, sub, sub, phoneme_symbol))

            result = cursor.fetchone()
            if result:
                phoneme_id, freq = result

                # Confirm deletion with full hierarchy path
                subgroup_display = f" > {sub}" if sub else ""
                print(f"\nSelected phoneme to delete:")
                print(f"  {s} > {p} > {l} > {g}{subgroup_display} :: {phoneme_symbol} (freq: {freq})")

                if freq > 0:
                    print(f"\n⚠️  Warning: This phoneme has a frequency of {freq}.")
                    print("Deleting it will remove all frequency data for this phoneme.")

                confirm = input("\nAre you sure you want to delete this phoneme? (y/n): ").strip().lower()

                if confirm == "y":
                    cursor.execute("DELETE FROM phonemes WHERE id = ?", (phoneme_id,))
                    conn.commit()
                    print(f"\n✓ Successfully deleted phoneme '{phoneme_symbol}'")
                else:
                    print("Deletion cancelled.")
            else:
                print("Error: Phoneme not found in database.")
        else:
            print("Invalid selection.")
    except (ValueError, IndexError):
        print("Invalid selection.")

    conn.close()
    input("Press Enter to return to the main menu...")

# ---------- Admin Functions ----------

def admin_login():
    """Check admin password for protected functions."""
    ADMIN_PASSWORD = "20251010"
    password = input("Enter admin password: ").strip()
    if password == ADMIN_PASSWORD:
        print("✓ Admin access granted.")
        return True
    else:
        print("✗ Incorrect password. Access denied.")
        input("Press Enter to return to the main menu...")
        return False

def export_phonemes_as_template():
    """Export current phonemes as a template with frequency set to 0."""
    print("\n--- Export Phonemes as Template ---")

    # Check if phonemes exist
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM phonemes")
    count = cursor.fetchone()[0]

    if count == 0:
        print("No phonemes found in database. Cannot create template.")
        conn.close()
        input("Press Enter to return to the admin menu...")
        return

    # Get template name from user
    template_name = input("Enter template name (e.g., 'english_phonemes'): ").strip()
    if not template_name:
        print("Template name is required.")
        conn.close()
        input("Press Enter to return to the admin menu...")
        return

    # Create templates directory if it doesn't exist
    template_dir = "data/phoneme_templates"
    os.makedirs(template_dir, exist_ok=True)

    # Get all current phonemes
    cursor.execute("""
        SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme
        FROM phonemes
        ORDER BY 
            CASE syllable_type WHEN 'CVC' THEN 0 WHEN 'CV' THEN 1 ELSE 2 END,
            CASE position WHEN 'onset' THEN 0 WHEN 'nucleus' THEN 1 WHEN 'coda' THEN 2 ELSE 3 END,
            CASE
                WHEN position IN ('onset','coda') THEN
                    CASE length_type
                        WHEN 'single_consonants' THEN 0
                        WHEN 'cluster2'         THEN 1
                        WHEN 'cluster3'         THEN 2
                        ELSE 3
                    END
                WHEN position = 'nucleus' THEN
                    CASE length_type
                        WHEN 'monophthongs' THEN 0
                        WHEN 'diphthongs'   THEN 1
                        ELSE 2
                    END
                ELSE 3
            END,
            group_type, subgroup_type, phoneme
    """)
    phonemes = cursor.fetchall()
    conn.close()

    # Create template data structure
    template_data = []
    for row in phonemes:
        syllable_type, position, length_type, group_type, subgroup_type, phoneme = row
        template_entry = {
            'syllable_type': syllable_type,
            'position': position,
            'length_type': length_type,
            'group_type': group_type,
            'subgroup_type': subgroup_type,
            'phoneme': phoneme,
            'frequency': 0  # Set frequency to 0 for template
        }
        template_data.append(template_entry)

    # Save template to file
    template_filename = f"{template_name}.py"
    template_path = os.path.join(template_dir, template_filename)

    try:
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(f"# Phoneme template: {template_name}\n")
            f.write(f"# Generated from existing phonemes with frequency set to 0\n")
            f.write(f"# Total phonemes: {len(template_data)}\n\n")
            f.write(f"{template_name}_template = [\n")

            for entry in template_data:
                f.write("    {")
                f.write(f"'syllable_type': '{entry['syllable_type']}', ")
                f.write(f"'position': '{entry['position']}', ")
                f.write(f"'length_type': '{entry['length_type']}', ")
                f.write(f"'group_type': '{entry['group_type']}', ")
                subgroup = entry['subgroup_type']
                if subgroup:
                    f.write(f"'subgroup_type': '{subgroup}', ")
                else:
                    f.write("'subgroup_type': None, ")
                f.write(f"'phoneme': '{entry['phoneme']}', ")
                f.write(f"'frequency': {entry['frequency']}")
                f.write("},\n")

            f.write("]\n")

        print(f"\n✓ Template successfully exported!")
        print(f"  Template name: {template_name}")
        print(f"  File location: {template_path}")
        print(f"  Total phonemes: {len(template_data)}")
        print(f"  All frequencies set to: 0")

    except Exception as e:
        print(f"\n✗ Error creating template file: {e}")

    input("Press Enter to return to the admin menu...")

def import_phonemes_from_template():
    """Import phonemes from a template file."""
    print("\n--- Import Phonemes from Template ---")

    # Check for templates directory
    template_dir = "data/phoneme_templates"
    if not os.path.exists(template_dir):
        print("No templates directory found. Create a template first.")
        input("Press Enter to return to the admin menu...")
        return

    # List available templates
    template_files = [f for f in os.listdir(template_dir) if f.endswith('.py')]
    if not template_files:
        print("No template files found in templates directory.")
        input("Press Enter to return to the admin menu...")
        return

    print("Available templates:")
    for i, template_file in enumerate(template_files, 1):
        template_name = template_file[:-3]  # Remove .py extension
        print(f"  {i}: {template_name}")

    # Get user choice
    try:
        choice = int(input(f"Select template (1-{len(template_files)}): ").strip())
        if 1 <= choice <= len(template_files):
            selected_file = template_files[choice - 1]
            template_name = selected_file[:-3]
        else:
            print("Invalid choice.")
            input("Press Enter to return to the admin menu...")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Enter to return to the admin menu...")
        return

    # Load template file
    template_path = os.path.join(template_dir, selected_file)
    try:
        # Read the template file
        template_data = None
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Execute the template file to get the data
        local_vars = {}
        exec(content, {}, local_vars)

        # Find the template data variable
        template_var_name = f"{template_name}_template"
        if template_var_name in local_vars:
            template_data = local_vars[template_var_name]
        else:
            print(f"Template variable '{template_var_name}' not found in file.")
            input("Press Enter to return to the admin menu...")
            return

    except Exception as e:
        print(f"Error loading template file: {e}")
        input("Press Enter to return to the admin menu...")
        return

    # Confirm import
    print(f"\nTemplate '{template_name}' contains {len(template_data)} phonemes.")
    confirm = input("Import these phonemes? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Import cancelled.")
        input("Press Enter to return to the admin menu...")
        return

    # Import phonemes
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    imported_count = 0
    duplicate_count = 0

    for entry in template_data:
        try:
            cursor.execute("""
                INSERT INTO phonemes
                (syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                entry.get("syllable_type"),
                entry.get("position"),
                entry.get("length_type"),
                entry.get("group_type"),
                entry.get("subgroup_type"),
                entry.get("phoneme"),
                entry.get("frequency", 0),
            ))
            imported_count += 1
        except sqlite3.IntegrityError:
            # Phoneme already exists
            duplicate_count += 1

    conn.commit()
    conn.close()

    print(f"\n✓ Import completed!")
    print(f"  Template: {template_name}")
    print(f"  Total phonemes in template: {len(template_data)}")
    print(f"  Successfully imported: {imported_count}")
    print(f"  Duplicates skipped: {duplicate_count}")

    input("Press Enter to return to the admin menu...")

def list_phoneme_templates():
    """List available phoneme templates."""
    print("\n--- Available Phoneme Templates ---")

    template_dir = "data/phoneme_templates"
    if not os.path.exists(template_dir):
        print("No templates directory found.")
        input("Press Enter to return to the admin menu...")
        return

    template_files = [f for f in os.listdir(template_dir) if f.endswith('.py')]
    if not template_files:
        print("No template files found.")
        input("Press Enter to return to the admin menu...")
        return

    print("Available templates:")
    for i, template_file in enumerate(template_files, 1):
        template_name = template_file[:-3]  # Remove .py extension
        template_path = os.path.join(template_dir, template_file)

        # Try to get template info
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Execute to get template data
            local_vars = {}
            exec(content, {}, local_vars)
            template_var_name = f"{template_name}_template"

            if template_var_name in local_vars:
                template_data = local_vars[template_var_name]
                phoneme_count = len(template_data)
                print(f"  {i}: {template_name} ({phoneme_count} phonemes)")
            else:
                print(f"  {i}: {template_name} (unable to read)")
        except:
            print(f"  {i}: {template_name} (error reading file)")

    input("Press Enter to return to the admin menu...")

def admin_menu():
    """Display and handle admin commands menu."""
    if not admin_login():
        return

    while True:
        print("\n--- Admin Commands ---")
        print("1. Add new phoneme")
        print("2. Delete phoneme")
        print("3. Increase frequency")
        print("4. Decrease frequency")
        print("5. Reset database")
        print("6. Export phonemes as template")
        print("7. Import phonemes from template")
        print("8. List available templates")
        print("9. Back to main menu")
        choice = input("Select an admin option (1-9): ").strip()

        if choice == "1":
            add_new_phoneme()
        elif choice == "2":
            delete_phoneme()
        elif choice == "3":
            increase_frequency()
        elif choice == "4":
            decrease_frequency()
        elif choice == "5":
            reset_database()
        elif choice == "6":
            export_phonemes_as_template()
        elif choice == "7":
            import_phonemes_from_template()
        elif choice == "8":
            list_phoneme_templates()
        elif choice == "9":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

# ---------- Menu / App ----------

def run():
    migrate_schema()
    while True:
        print("\n--- Phoneme Frequency Tracker ---")
        print("1. Admin Commands")
        print("2. View all phonemes (flat)")
        print("3. Display nested phoneme hierarchy")
        print("4. Display full hierarchy")
        print("5. Add new word")
        print("6. Display all words")
        print("7. Lookup word")
        print("8. Delete last word entry")
        print("9. Delete word by lookup")
        print("10. Edit existing word")
        print("11. Exit")
        choice = input("Select an option (1–11): ").strip()

        if choice == "1":
            admin_menu()
        elif choice == "2":
            display_flat()
        elif choice == "3":
            display_nested_phonemes()
        elif choice == "4":
            display_full()
        elif choice == "5":
            create_word_from_phonemes()
        elif choice == "6":
            display_words()
        elif choice == "7":
            lookup_word()
        elif choice == "8":
            delete_last_word()
        elif choice == "9":
            delete_word_by_lookup()
        elif choice == "10":
            edit_existing_word()
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()
