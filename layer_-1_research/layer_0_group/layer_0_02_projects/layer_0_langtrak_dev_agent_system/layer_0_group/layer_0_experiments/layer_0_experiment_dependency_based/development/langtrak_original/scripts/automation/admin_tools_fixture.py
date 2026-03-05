#!/usr/bin/env python3
# resource_id: "49f0bfc8-248f-4156-af92-dc3f42c385fc"
# resource_type: "document"
# resource_name: "admin_tools_fixture"
"""
Admin Tools Automation Fixture

Provides deterministic setup/teardown helpers for automation suites that cover
database maintenance flows (US-050–US-053). The fixture:
  * Resets the SQLite words/phonemes dataset to a known baseline.
  * Seeds representative words (with and without backing media files).
  * Persists metadata for later cleanup.
  * Removes generated artifacts and restores the baseline on cleanup.

Usage:
    python3 scripts/automation/admin_tools_fixture.py prepare
    python3 scripts/automation/admin_tools_fixture.py cleanup
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable, List


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "phonemes.db"
VIDEOS_DIR = ROOT / "videos"
ARTIFACTS_DIR = ROOT / "artifacts" / "fixtures"
STATE_FILE = ARTIFACTS_DIR / "admin_tools_state.json"

sys.path.insert(0, str(ROOT))

import main  # noqa: E402  # pylint: disable=wrong-import-position
from services.reset import reset_database  # noqa: E402  # pylint: disable=wrong-import-position


@dataclass
class FixtureWord:
    """Represents a seeded word used for admin tool automation."""

    id: int
    language: str
    new_word: str
    video_path: str
    video_created: bool

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "language": self.language,
            "new_language_word": self.new_word,
            "video_path": self.video_path,
            "video_created": self.video_created,
        }


def ensure_directories() -> None:
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


def reset_to_baseline() -> None:
    """
    Reset words/phonemes tables and restore sample phoneme data.

    This yields a deterministic starting point for admin maintenance flows.
    """
    reset_database(str(DB_PATH), insert_sample_data=main.insert_sample_data)


def increment_frequency(cursor: sqlite3.Cursor, syllable_type: str, position: str, length_type: str, phoneme: str) -> None:
    cursor.execute(
        """
        UPDATE phonemes
        SET frequency = frequency + 1
        WHERE syllable_type = ? AND position = ? AND length_type = ? AND phoneme = ?
        """,
        (syllable_type, position, length_type, phoneme),
    )


def seed_words(conn: sqlite3.Connection, timestamp: str) -> List[FixtureWord]:
    """
    Insert representative words to exercise admin maintenance tools.

    Creates:
      * One complete word with existing media (verifies deletion removes file).
      * One word pointing to a missing media file (used for "fix video paths").
      * One word with inconsistent relative path formatting (tests normalization).
    """
    cursor = conn.cursor()
    syllable_type = "CVC"
    onset = ("onset", "single_consonants", "tʃ")
    nucleus = ("nucleus", "diphthongs", "aɪ")
    coda = ("coda", "single_consonants", "v")

    words: List[FixtureWord] = []

    fixtures = [
        {
            "language": "AdminLang-A",
            "english": "Cleanup Canary",
            "constructed": f"fixture_{timestamp}_alpha",
            "video_filename": f"fixture_{timestamp}_alpha.mp4",
            "create_media": True,
            "stored_path": None,
        },
        {
            "language": "AdminLang-B",
            "english": "Broken Video Ref",
            "constructed": f"fixture_{timestamp}_beta",
            "video_filename": f"missing_fixture_{timestamp}_beta.mp4",
            "create_media": False,
            "stored_path": None,
        },
        {
            "language": "AdminLang-C",
            "english": "Path Needs Normalization",
            "constructed": f"fixture_{timestamp}_gamma",
            "video_filename": f"fixture_{timestamp}_gamma.mp4",
            "create_media": True,
            "stored_path": f"./videos/fixture_{timestamp}_gamma.mp4",
        },
    ]

    for entry in fixtures:
        video_path = VIDEOS_DIR / entry["video_filename"]
        if entry["create_media"]:
            video_path.write_bytes(b"")  # Placeholder file to verify deletion behaviour.

        stored_path = entry["stored_path"] or str(video_path)

        cursor.execute(
            """
            INSERT INTO words (
                language,
                english_words,
                new_language_word,
                ipa_phonetics,
                dictionary_phonetics,
                syllable_type,
                onset_phoneme,
                onset_length_type,
                nucleus_phoneme,
                nucleus_length_type,
                coda_phoneme,
                coda_length_type,
                video_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                entry["language"],
                entry["english"],
                entry["constructed"],
                "tʃaɪv",
                "CH-EYE-V",
                syllable_type,
                onset[2],
                onset[1],
                nucleus[2],
                nucleus[1],
                coda[2],
                coda[1],
                stored_path,
            ),
        )
        word_id = cursor.lastrowid

        for position, length_type, phoneme in (onset, nucleus, coda):
            increment_frequency(cursor, syllable_type, position, length_type, phoneme)

        words.append(
            FixtureWord(
                id=word_id,
                language=entry["language"],
                new_word=entry["constructed"],
                video_path=str(video_path if entry["create_media"] else stored_path),
                video_created=entry["create_media"],
            )
        )

    conn.commit()
    return words


def write_state(words: Iterable[FixtureWord], timestamp: str) -> None:
    word_list = list(words)
    payload = {
        "timestamp": timestamp,
        "word_count": len(word_list),
        "words": [word.to_dict() for word in word_list],
    }
    STATE_FILE.write_text(json.dumps(payload, indent=2))


def load_state() -> dict | None:
    if not STATE_FILE.exists():
        return None
    try:
        return json.loads(STATE_FILE.read_text())
    except json.JSONDecodeError:
        return None


def handle_prepare(args: argparse.Namespace) -> None:
    _ = args  # Reserved for future options.
    if STATE_FILE.exists():
        raise SystemExit(f"State file already exists: {STATE_FILE}. Run cleanup before preparing again.")

    ensure_directories()
    reset_to_baseline()

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        words = seed_words(conn, timestamp)

    write_state(words, timestamp)
    print(f"Prepared admin tools fixture with {len(words)} words. State captured at {STATE_FILE}.")


def handle_cleanup(args: argparse.Namespace) -> None:
    _ = args
    state = load_state()

    if state:
        for entry in state.get("words", []):
            video_path = Path(entry.get("video_path", ""))
            if entry.get("video_created") and video_path.exists():
                try:
                    video_path.unlink()
                except OSError as exc:
                    print(f"Warning: failed to remove video file {video_path}: {exc}", file=sys.stderr)
    else:
        print("No state file found; proceeding with baseline reset only.")

    reset_to_baseline()

    if STATE_FILE.exists():
        STATE_FILE.unlink()

    print("Cleaned admin tools fixture and restored baseline dataset.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage admin tools automation fixtures.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Reset baseline and seed fixture data.")
    prepare.set_defaults(func=handle_prepare)

    cleanup = subparsers.add_parser("cleanup", help="Remove fixture data and restore baseline.")
    cleanup.set_defaults(func=handle_cleanup)

    return parser


def main_cli(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except SystemExit as exc:
        raise
    except Exception as exc:  # pragma: no cover - surface unexpected errors
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main_cli())
