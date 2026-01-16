"""Smoke test that exercises Firestore-backed analytics if credentials are available."""
from __future__ import annotations

import argparse
import sys

from data_science_operations import (
    compute_stats,
    get_firestore_client,
    group_timings,
    normalise_records,
    print_summary,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a handful of Firestore timing documents and run analytics.")
    parser.add_argument(
        "--project",
        default="assignment-time",
        help="Firestore project to smoke-test (default: assignment-time).")
    parser.add_argument(
        "--collection",
        default="assignment_timings",
        help="Collection name that stores timing documents (default: assignment_timings).")
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Number of documents to fetch for the smoke test (default: 20).")
    return parser.parse_args()


def main() -> None:
    try:
        from firebase_admin import _apps  # type: ignore  # noqa: F401 (imported for side-effect check)
    except ModuleNotFoundError:  # pragma: no cover - environment dependent
        print("firebase-admin is not installed. Install it or run the JSON-based smoke test instead.")
        sys.exit(0)

    args = parse_args()

    client = get_firestore_client(args.project)
    print(f"Connected to Firestore project: {args.project}")

    snapshot = client.collection(args.collection).limit(args.limit).stream()
    documents = [doc.to_dict() or {} for doc in snapshot]
    records = normalise_records(documents)
    if not records:
        print("No timing records returned; check that the collection has data.")
        return

    print(f"Fetched {len(records)} records from collection '{args.collection}'.")

    grouped = group_timings(records, "assignmentId")
    print("\n=== Firestore Summary (grouped by assignmentId) ===")
    print_summary(grouped)

    overall = compute_stats(records)
    print("\nOverall stats (seconds):", overall)


if __name__ == "__main__":
    main()

