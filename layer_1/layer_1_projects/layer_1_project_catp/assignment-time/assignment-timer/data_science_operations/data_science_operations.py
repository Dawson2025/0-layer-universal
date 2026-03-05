# resource_id: "0b283eb3-a45e-4705-b11c-58a0b673ed35"
# resource_type: "document"
# resource_name: "data_science_operations"
﻿# TODO: make features that take care of outliers and any other data anylitics features you deem important

from __future__ import annotations

import argparse
import collections
import json
import importlib.util
import math
import statistics
import sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Mapping, Optional

try:
    import firebase_admin
    from firebase_admin import firestore
    from firebase_admin import credentials
except ModuleNotFoundError:
    # The CLI can operate purely on JSON input, so defer the dependency until Firestore is accessed.
    # When the user sticks to --input-json, firebase_admin stays optional.
    firebase_admin = None
    firestore = None
    credentials = None

try:
    from google.auth.exceptions import DefaultCredentialsError
except ModuleNotFoundError:  # pragma: no cover - present when firebase_admin is absent.
    DefaultCredentialsError = Exception  # type: ignore[assignment]


def _quote_executable(executable: Optional[str]) -> str:
    """Return a shell-safe representation of the running Python executable."""

    if not executable:
        return "python"
    if " " in executable and not executable.startswith("\""):
        return f'"{executable}"'
    return executable


_PYTHON_EXECUTABLE = _quote_executable(sys.executable)
_INSTALL_FIREBASE_COMMAND = f"{_PYTHON_EXECUTABLE} -m pip install firebase-admin"
_VERIFY_FIREBASE_COMMAND = f"{_PYTHON_EXECUTABLE} -m pip show firebase-admin"

_FIRESTORE_AUTH_GUIDANCE = (
    "Install the dependency for this Python interpreter with:\n"
    f"    {_INSTALL_FIREBASE_COMMAND}\n"
    "If the module still cannot be imported, confirm this interpreter owns the install via:\n"
    f"    {_VERIFY_FIREBASE_COMMAND}\n"
    "and rerun the CLI with the same Python executable.\n"
    "Authenticate with Application Default Credentials using:\n"
    "    gcloud auth application-default login\n"
    "or set the GOOGLE_APPLICATION_CREDENTIALS environment variable before retrying Firestore mode.\n"
    "Verify credentials are active with:\n"
    "    gcloud auth application-default print-access-token"
)

MISSING_FIRESTORE_GUIDANCE = (
    "firebase-admin is not installed; Firestore features are unavailable.\n"
    f"{_FIRESTORE_AUTH_GUIDANCE}"
)

MISSING_FIRESTORE_CREDENTIALS_GUIDANCE = (
    "Firestore credentials were not found. The CLI relies on Application Default Credentials.\n"
    f"{_FIRESTORE_AUTH_GUIDANCE}"
)

# ---------------------------------------------------------------------------
# Normalisation helpers
# ---------------------------------------------------------------------------

GroupKey = str


def _format_duration(seconds: float) -> str:
    """Convert a duration in seconds to an HH:MM:SS string suitable for reports."""
    total_seconds = int(round(seconds))
    total_seconds = max(total_seconds, 0)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{secs:02}"


@dataclass
class TimingRecord:
    """Normalised assignment timing entry used by downstream analytics."""

    assignment_id: Optional[int]
    assignment_name: str
    course_id: Optional[int]
    course_name: str
    time_in_seconds: float


def _ensure_app(project_id: Optional[str] = None) -> firebase_admin.App:
    """Initialise (or reuse) a firebase-admin app for the desired project."""
    if project_id:
        try:
            return firebase_admin.get_app(project_id)
        except ValueError:
            return firebase_admin.initialize_app(options={"projectId": project_id}, name=project_id)

    try:
        return firebase_admin.get_app()
    except ValueError:
        return firebase_admin.initialize_app()



def _ensure_firestore_credentials(project_id: Optional[str] = None) -> None:
    """Validate Application Default Credentials before initialising a Firestore client."""

    # If an app already exists we assume callers provided credentials explicitly, so we skip checks
    # to avoid interfering with advanced usage where ADC are intentionally not used.
    try:
        if project_id:
            firebase_admin.get_app(project_id)
        else:
            firebase_admin.get_app()
        return
    except ValueError:
        pass

    if credentials is None:
        raise RuntimeError(MISSING_FIRESTORE_CREDENTIALS_GUIDANCE)

    try:
        credentials.ApplicationDefault()
    except DefaultCredentialsError as exc:
        raise RuntimeError(MISSING_FIRESTORE_CREDENTIALS_GUIDANCE) from exc

def get_firestore_client(project_id: Optional[str] = None) -> firestore.Client:
    """Return a Firestore client using ADC and an optional project override."""
    if firebase_admin is None or firestore is None:
        raise RuntimeError(MISSING_FIRESTORE_GUIDANCE)

    _ensure_firestore_credentials(project_id)

    try:
        app = _ensure_app(project_id)
    except DefaultCredentialsError as exc:
        raise RuntimeError(MISSING_FIRESTORE_CREDENTIALS_GUIDANCE) from exc
    except ValueError as exc:
        if "Application Default Credentials" in str(exc):
            raise RuntimeError(MISSING_FIRESTORE_CREDENTIALS_GUIDANCE) from exc
        raise

    return firestore.client(app)


def _coerce_int(value) -> Optional[int]:
    try:
        if value is None:
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def _record_from_dict(data: Mapping[str, object]) -> Optional[TimingRecord]:
    """Convert a raw document mapping into a TimingRecord if possible."""
    # Firestore comes back as dict-like objects; we defensively guard against missing fields
    # so the analytics pipeline stays resilient to partial documents.
    time_value = data.get("timeInSeconds")
    if time_value is None:
        return None

    try:
        seconds = float(time_value)
    except (TypeError, ValueError):
        return None

    return TimingRecord(
        assignment_id=_coerce_int(data.get("assignmentId")),
        assignment_name=str(data.get("assignmentName") or "Unknown Assignment"),
        course_id=_coerce_int(data.get("courseId")),
        course_name=str(data.get("courseName") or "Unknown Course"),
        time_in_seconds=seconds,
    )


def normalise_records(documents: Iterable[Mapping[str, object]]) -> List[TimingRecord]:
    """Normalise iterable Firestore-style documents into TimingRecord objects."""
    records: List[TimingRecord] = []
    for item in documents:
        # Each raw mapping is converted to our dataclass. Invalid entries are quietly skipped.
        timing = _record_from_dict(item)
        if timing:
            records.append(timing)
    return records


def fetch_assignment_timings(client: firestore.Client, collection: str = "assignment_timings") -> List[TimingRecord]:
    """Fetch assignment timing documents and normalise them into TimingRecord objects."""
    snapshot = client.collection(collection).stream()
    documents = [doc.to_dict() or {} for doc in snapshot]
    return normalise_records(documents)


def load_records_from_json(path: str | Path) -> List[TimingRecord]:
    """Load timing records from a JSON file on disk."""
    # Having fixtures in JSON keeps them easy to edit, then we reuse the same normalisation code.
    file_path = Path(path)
    payload = json.loads(file_path.read_text(encoding="utf-8-sig"))
    return normalise_records(payload)


def _load_sample_fixture() -> tuple[list[Mapping[str, object]], str]:
    """Load the bundled Python fixture that mirrors Firestore documents."""
    sample_module_path = Path(__file__).resolve().parent / 'sample_data' / 'same_as_google_firebase' / 'sample_data.py'
    spec = importlib.util.spec_from_file_location('data_science_operations_sample', sample_module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Unable to load bundled sample data module')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    records = getattr(module, 'SAMPLE_TIMINGS', [])
    project_id = getattr(module, 'SAMPLE_PROJECT_ID', 'sample-data')
    return records, project_id


def _choose_runtime_mode(args: argparse.Namespace) -> tuple[str, Optional[object]]:
    """Determine whether to use Firestore, JSON, or the bundled fixture."""
    base_dir = Path(__file__).resolve().parent
    default_json = base_dir / 'sample_data' / 'json' / 'assignment_timings_sample.json'
    firebase_available = firebase_admin is not None and firestore is not None

    if args.input_json:
        return 'json', Path(args.input_json)
    if args.project:
        return 'firestore', args.project

    print('Select data source:')
    print('  1. Firestore (requires firebase-admin)')
    print('  2. Bundled sample fixture (default)')
    print('  3. JSON file on disk')
    choice = input('Enter choice [2]: ').strip() or '2'

    if choice == '1':
        if not firebase_available:
            print(MISSING_FIRESTORE_GUIDANCE)
            print('Falling back to sample fixture.')
        else:
            try:
                _ensure_firestore_credentials()
            except RuntimeError as exc:
                print(exc)
                print('Falling back to sample fixture.')
            else:
                project = input('Firestore project ID [assignment-time]: ').strip() or 'assignment-time'
                return 'firestore', project

    if choice == '3':
        path_input = input(f'Path to JSON file [{default_json}]: ').strip() or str(default_json)
        return 'json', Path(path_input)

    return 'sample', None




@dataclass
class Stats:
    """Container for aggregate timing metrics computed from records."""
    count: int
    mean: float
    median: float
    std_dev: Optional[float]
    min_value: float
    max_value: float

def remove_outliers(values):
    q1 = np.percentile(values, 25)
    q3 = np.percentile(values, 75)
    iqr = q3-q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    for value in values:
        if value < lower_bound or value > upper_bound:
            values.remove(value)

def compute_stats(records: Iterable[TimingRecord]) -> Stats:

    values = [rec.time_in_seconds for rec in records]
    remove_outliers(values)
    count = len(values)
    mean = statistics.fmean(values)
    median = statistics.median(values)
    std_dev = statistics.stdev(values) if count > 1 else None
    return Stats(
        count=count,
        mean=mean,
        median=median,
        std_dev=std_dev,
        min_value=min(values),
        max_value=max(values),
    )


def _stats_to_dict(stats: Stats) -> Dict[str, float]:
    return asdict(stats)


def export_json(records: Iterable[TimingRecord], grouped: Dict[GroupKey, List[TimingRecord]], project_id: str, output_path: str) -> None:
    """Write a JSON snapshot bundling raw records and per-group statistics."""
    payload = {
        "projectId": project_id,
        "totalCount": len(records),
        "summary": (_stats_to_dict(compute_stats(records)) if records else None),
        "groups": {
            key: {
                "count": len(group_records),
                "stats": _stats_to_dict(compute_stats(group_records))
            }
            for key, group_records in grouped.items()
        },
        "records": [asdict(rec) for rec in records],
    }

    destination = Path(output_path)
    if destination.parent and not destination.parent.exists():
        destination.parent.mkdir(parents=True, exist_ok=True)

    destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def group_timings(records: Iterable[TimingRecord], key: str) -> Dict[GroupKey, List[TimingRecord]]:
    """Partition timing records by assignmentId or courseAssignment."""
    groups: Dict[GroupKey, List[TimingRecord]] = collections.defaultdict(list)

    for rec in records:
        if key == "assignmentId" and rec.assignment_id is not None:
            group_key = f"assignmentId:{rec.assignment_id}"
        elif key == "courseAssignment":
            group_key = f"course:{rec.course_id or 'unknown'}|assignment:{rec.assignment_name}"
        else:
            group_key = f"assignment:{rec.assignment_name}"
        groups[group_key].append(rec)

    return groups


def print_summary(grouped: Dict[GroupKey, List[TimingRecord]]) -> None:
    headers = ["Group", "Count", "Mean (hh:mm:ss)", "Median (hh:mm:ss)", "Std Dev", "Min", "Max"]
    # Table output stays human-readable while JSON exports keep raw seconds for further analysis.
    print(" | ".join(headers))
    print("-" * (len(" | ".join(headers)) + 10))
    for group_key, records in grouped.items():
        stats = compute_stats(records)
        std_dev = _format_duration(stats.std_dev) if stats.std_dev is not None else "n/a"
        line = " | ".join(
            [
                group_key,
                str(stats.count),
                _format_duration(stats.mean),
                _format_duration(stats.median),
                std_dev,
                _format_duration(stats.min_value),
                _format_duration(stats.max_value),
            ]
        )
        print(line)


def plot_distribution(records: Iterable[TimingRecord], output_path: str) -> None:
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError("matplotlib is required for plotting; install it with `pip install matplotlib`.") from exc

    values = np.array([rec.time_in_seconds for rec in records], dtype=float)
    if values.size == 0:
        raise ValueError("No timing data available to plot")

    mean = values.mean()
    std = values.std(ddof=0)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(values, bins=min(20, max(5, int(math.sqrt(values.size)))), density=True, color="#4C72B0", alpha=0.6, label="Histogram")

    if std > 0:
        xmin, xmax = values.min(), values.max()
        x = np.linspace(xmin, xmax, 200)
        pdf = (1 / (std * math.sqrt(2 * math.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
        ax.plot(x, pdf, color="#DD8452", label="Normal PDF")

    ax.set_title("Assignment Timing Distribution")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Density")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aggregate assignment timing statistics from Firestore.")
    # CLI flags mirror the analytics helpers so the tool can run in scripts or interactively.
    parser.add_argument(
        "--project",
        help="Firestore project ID. Defaults to the project tied to your credentials.",
    )
    parser.add_argument(
        "--group-by",
        choices=["assignmentId", "courseAssignment"],
        default="assignmentId",
        help="Grouping strategy for the aggregation.",
    )
    parser.add_argument(
        "--plot",
        metavar="PATH",
        help="Optional path to save a bell-curve style histogram of all timings.",
    )
    parser.add_argument(
        "--export-json",
        metavar="PATH",
        help="Write fetched timing data and summary statistics to JSON.",
    )
    parser.add_argument(
        "--input-json",
        metavar="PATH",
        help="Use a local JSON file instead of querying Firestore.",
    )
    parser.add_argument(
        "--collection",
        default="assignment_timings",
        help="Firestore collection that stores timing documents (default: assignment_timings).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    mode, source = _choose_runtime_mode(args)
    records: List[TimingRecord]
    project_id: Optional[str]
    client = None

    if mode == 'sample':
        fixture_records, fixture_project = _load_sample_fixture()
        records = normalise_records(fixture_records)
        project_id = fixture_project
    elif mode == 'json':
        json_path = Path(source)  # type: ignore[arg-type]
        records = load_records_from_json(json_path)
        project_id = args.project or 'sample-data'
    else:  # Firestore mode
        project = str(source)
        client = get_firestore_client(project)
        records = fetch_assignment_timings(client, collection=args.collection)
        project_id = project

    if not records:
        print("No timing records found.")
        return

    # Always print a summary so the tool is useful in shell pipelines.
    grouped = group_timings(records, args.group_by)
    print_summary(grouped)

    if args.export_json:
        export_json(records, grouped, project_id or 'unknown', args.export_json)
        print(f"Exported {len(records)} records to {args.export_json}")

    if args.plot:
        plot_distribution(records, args.plot)
        print(f"Saved distribution plot to {args.plot}")


if __name__ == "__main__":
    main()
