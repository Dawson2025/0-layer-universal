#!/usr/bin/env python3
"""
Validate feature directory isolation and optional tests.

Scans `features/` for expected files/directories, reports gaps, and can run
feature-specific pytest suites when requested.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).resolve().parents[2]
FEATURES_DIR = PROJECT_ROOT / "features"
ARTIFACT_ROOT = PROJECT_ROOT / "artifacts" / "parallel-workflow"

RECOMMENDED_FILES = ["README.md"]
OPTIONAL_FILES = ["routes.py"]
RECOMMENDED_DIRS = ["tests"]
OPTIONAL_DIRS = ["templates"]


@dataclass
class FeatureReport:
    name: str
    path: str
    has_init: bool
    present_files: Dict[str, bool]
    present_dirs: Dict[str, bool]
    pytest_ran: bool = False
    pytest_exit_code: Optional[int] = None
    pytest_command: Optional[List[str]] = None
    pytest_output: Optional[str] = None

    @property
    def issues(self) -> List[str]:
        problems: List[str] = []
        if not self.has_init:
            problems.append("__init__.py missing")
        if not self.present_dirs.get("tests", False):
            problems.append("tests/ missing")
        if self.pytest_ran and self.pytest_exit_code not in (0, None):
            problems.append("pytest failed")
        return problems

    @property
    def warnings(self) -> List[str]:
        notes: List[str] = []
        if not self.present_dirs.get("templates", False):
            notes.append("templates/ missing")
        if not self.present_files.get("README.md", False):
            notes.append("README.md missing")
        if not self.present_files.get("routes.py", False):
            notes.append("routes.py missing")
        return notes

    def to_dict(self) -> Dict[str, object]:
        result = asdict(self)
        result["issues"] = self.issues
        result["warnings"] = self.warnings
        return result


def collect_features() -> List[Path]:
    if not FEATURES_DIR.exists():
        raise SystemExit(f"Features directory not found: {FEATURES_DIR}")
    return sorted(
        [
            path
            for path in FEATURES_DIR.iterdir()
            if path.is_dir() and not path.name.startswith("__")
        ],
        key=lambda p: p.name,
    )


def run_pytest(feature_path: Path) -> FeatureReport:
    tests_dir = feature_path / "tests"
    report = FeatureReport(
        name=feature_path.name,
        path=str(feature_path.relative_to(PROJECT_ROOT)),
        has_init=(feature_path / "__init__.py").exists(),
        present_files={
            fname: (feature_path / fname).exists()
            for fname in RECOMMENDED_FILES + OPTIONAL_FILES
        },
        present_dirs={
            dirname: (feature_path / dirname).exists()
            for dirname in RECOMMENDED_DIRS + OPTIONAL_DIRS
        },
    )

    if tests_dir.exists():
        report.pytest_ran = True
        cmd = ["python", "-m", "pytest", str(tests_dir)]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(PROJECT_ROOT)
        process = subprocess.run(
            cmd,
            cwd=PROJECT_ROOT,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        report.pytest_command = cmd
        report.pytest_exit_code = process.returncode
        report.pytest_output = process.stdout
    return report


def build_report(run_pytest_flag: bool) -> Dict[str, object]:
    features = collect_features()
    reports: List[FeatureReport] = []
    for feature_path in features:
        if run_pytest_flag:
            report = run_pytest(feature_path)
        else:
            report = FeatureReport(
                name=feature_path.name,
                path=str(feature_path.relative_to(PROJECT_ROOT)),
                has_init=(feature_path / "__init__.py").exists(),
                present_files={
                    fname: (feature_path / fname).exists()
                    for fname in RECOMMENDED_FILES + OPTIONAL_FILES
                },
                present_dirs={
                    dirname: (feature_path / dirname).exists()
                    for dirname in RECOMMENDED_DIRS + OPTIONAL_DIRS
                },
            )
        reports.append(report)

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "project_root": str(PROJECT_ROOT),
        "run_pytest": run_pytest_flag,
        "features_analyzed": len(reports),
        "reports": [r.to_dict() for r in reports],
    }


def save_report(report: Dict[str, object], output: Optional[Path]) -> Path:
    if output is None:
        ARTIFACT_ROOT.mkdir(parents=True, exist_ok=True)
        default = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        output_path = ARTIFACT_ROOT / f"{default}.json"
    else:
        output_path = output
        output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(json.dumps(report, indent=2))
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate parallel feature structure.")
    parser.add_argument(
        "--pytest",
        action="store_true",
        help="Run pytest for each feature's tests directory (if present).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write JSON summary (default: artifacts/parallel-workflow/<timestamp>.json)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with non-zero status when issues or pytest failures are detected.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(run_pytest_flag=args.pytest)
    output_path = save_report(report, args.output)

    print(json.dumps(report, indent=2))
    print(f"\nReport written to {output_path}")

    if not args.strict:
        return 0

    total_issues = sum(len(entry["issues"]) for entry in report["reports"])
    pytest_failures = any(entry.get("pytest_exit_code") not in (0, None) for entry in report["reports"])
    return 0 if total_issues == 0 and not pytest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
