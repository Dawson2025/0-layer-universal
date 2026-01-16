#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class SubLayer:
    number: str
    slug: str
    folder_name: str
    folder_path: Path


SUB_LAYER_RE = re.compile(r"^sub_layer_(\d+\.\d+)_([a-z0-9_]+)$")


def repo_root_from_here() -> Path:
    # .../layer_0_universal/0.02_sub_layers/0.00_sub_layer_registry/scripts/sub_layer_registry.py
    return Path(__file__).resolve().parents[5]


def sublayers_root() -> Path:
    # .../layer_0_universal/0.02_sub_layers/
    return Path(__file__).resolve().parents[2]


def registry_dir() -> Path:
    # .../layer_0_universal/0.02_sub_layers/0.00_sub_layer_registry/
    return Path(__file__).resolve().parents[1]


def aliases_dir() -> Path:
    return registry_dir() / "aliases"


def list_sublayers() -> List[SubLayer]:
    root = sublayers_root()
    items: List[SubLayer] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        match = SUB_LAYER_RE.match(child.name)
        if not match:
            continue
        number, slug = match.group(1), match.group(2)
        items.append(
            SubLayer(
                number=number,
                slug=slug,
                folder_name=child.name,
                folder_path=child,
            )
        )
    return items


def relpath(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(str(to_path), start=str(from_path.parent))


def write_registry_yaml(sublayers: Iterable[SubLayer]) -> Path:
    out = registry_dir() / "sub_layer_registry.yaml"
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")

    lines: List[str] = []
    lines.append("# Auto-generated. Do not edit by hand.")
    lines.append(f"generated_at_utc: {now}")
    lines.append("sublayers:")
    for sl in sublayers:
        path = f"layer_0_universal/0.02_sub_layers/{sl.folder_name}"
        lines.append(f"  - slug: {sl.slug}")
        lines.append(f"    number: \"{sl.number}\"")
        lines.append(f"    folder: {sl.folder_name}")
        lines.append(f"    path: {path}")
    lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_alias_md(sl: SubLayer) -> Path:
    aliases_dir().mkdir(parents=True, exist_ok=True)
    out = aliases_dir() / f"{sl.slug}.md"
    target_readme = sl.folder_path / "README.md"

    # Prefer linking to README if it exists, otherwise to folder.
    target = target_readme if target_readme.exists() else sl.folder_path
    link = relpath(out, target)

    out.write_text(
        "\n".join(
            [
                f"# Alias: `{sl.slug}`",
                "",
                "**Purpose**: Stable link to this sub-layer (numeric ordering may change).",
                "",
                f"- Current folder: `{sl.folder_name}`",
                f"- Open: [{sl.folder_name}]({link})",
                "",
                "If you are writing documentation, link to this alias file instead of hard-linking numeric `sub_layer_0.xx_*` paths.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return out


def generate() -> int:
    sublayers = list_sublayers()
    if not sublayers:
        raise SystemExit(f"No sublayers found under: {sublayers_root()}")

    write_registry_yaml(sublayers)
    for sl in sublayers:
        write_alias_md(sl)

    print(f"✅ Registry written: {registry_dir() / 'sub_layer_registry.yaml'}")
    print(f"✅ Aliases written: {aliases_dir()}/")
    return 0


def ripgrep_files(pattern: str, root: Path) -> List[str]:
    try:
        result = subprocess.run(
            ["rg", "-n", pattern, str(root)],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        raise SystemExit("ripgrep (rg) is required for check-hardlinks")

    if result.returncode not in (0, 1):
        raise SystemExit(result.stderr.strip() or "rg failed")
    return [line for line in result.stdout.splitlines() if line.strip()]


def check_hardlinks() -> int:
    root = repo_root_from_here() / "0_context"

    hits = ripgrep_files(r"sub_layer_0\.\d{2}_[a-z0-9_]+", root)
    hits = [h for h in hits if "/0.00_sub_layer_registry/aliases/" not in h]

    print("🔎 Hard-linked numeric sublayer references:")
    if not hits:
        print("✅ None found.")
        return 0

    for line in hits[:200]:
        print(line)
    if len(hits) > 200:
        print(f"... ({len(hits) - 200} more)")

    print()
    print("Fix guidance:")
    print("- Prefer alias links under `layer_0_universal/0.02_sub_layers/0.00_sub_layer_registry/aliases/`")
    print("- Regenerate aliases with: python3 .../sub_layer_registry.py generate")
    return 2


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate a stable sub-layer registry and alias links.",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("generate", help="Generate registry YAML and alias markdown files")
    sub.add_parser("check-hardlinks", help="List docs that still hard-link sub_layer_0.xx_* paths")

    args = parser.parse_args(argv)
    if args.command == "generate":
        return generate()
    if args.command == "check-hardlinks":
        return check_hardlinks()

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
