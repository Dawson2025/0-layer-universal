#!/usr/bin/env bash
# resource_id: "07ae2db8-20ca-4ee0-bb86-171d06639855"
# resource_type: "script"
# resource_name: "checkpoint-all"
set -euo pipefail

ROOT_DEFAULT="/home/dawson/dawson-workspace/code/0_layer_universal"
ROOT="$ROOT_DEFAULT"
DRY_RUN=0
MSG_PREFIX="checkpoint"

usage() {
  cat <<USAGE
Usage: $(basename "$0") [--root <path>] [--message <prefix>] [--dry-run]

Performs bottom-up checkpoint (git add/commit/push) for all git repos under root.
Repos are processed deepest-first so submodule pointers can be committed in parents.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT="$2"
      shift 2
      ;;
    --message)
      MSG_PREFIX="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ ! -d "$ROOT" ]]; then
  echo "Root does not exist: $ROOT" >&2
  exit 1
fi

mapfile -t REPOS < <(
  find "$ROOT" \( -name .git -type d -o -name .git -type f \) 2>/dev/null |
  sed 's#/.git$##' |
  awk '{ print length, $0 }' |
  sort -rn |
  cut -d' ' -f2- |
  awk '!seen[$0]++'
)

if [[ ${#REPOS[@]} -eq 0 ]]; then
  echo "No git repos found under $ROOT"
  exit 0
fi

STAMP="$(date +%Y-%m-%dT%H:%M:%S%z)"

echo "Root: $ROOT"
echo "Repos found: ${#REPOS[@]}"
echo "Mode: $([[ $DRY_RUN -eq 1 ]] && echo DRY-RUN || echo EXECUTE)"
echo

for repo in "${REPOS[@]}"; do
  rel="${repo#$ROOT/}"
  [[ "$repo" == "$ROOT" ]] && rel="."

  if ! git -C "$repo" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "[SKIP] $rel (not a work tree)"
    continue
  fi

  branch="$(git -C "$repo" branch --show-current || true)"
  status="$(git -C "$repo" status --porcelain)"

  if [[ -z "$status" ]]; then
    echo "[CLEAN] $rel"
    continue
  fi

  commit_msg="$MSG_PREFIX: auto checkpoint $STAMP ($rel)"

  echo "[DIRTY] $rel"
  echo "        branch: ${branch:-detached}"

  if [[ $DRY_RUN -eq 1 ]]; then
    echo "        would run: git add -A"
    echo "        would run: git commit -m \"$commit_msg\""
    if [[ -n "$branch" ]]; then
      echo "        would run: git push origin $branch"
    else
      echo "        would run: git push (detached HEAD)"
    fi
    continue
  fi

  git -C "$repo" add -A

  # commit can be empty if only ignored/untracked patterns changed after add; handle gracefully
  if git -C "$repo" diff --cached --quiet; then
    echo "        nothing staged after add; skipping commit"
    continue
  fi

  git -C "$repo" commit -m "$commit_msg"

  if [[ -n "$branch" ]]; then
    git -C "$repo" push origin "$branch"
  else
    # Detached HEAD cannot be safely pushed without explicit ref.
    echo "        WARNING: detached HEAD; skipping push for safety"
  fi

  echo "        pushed"
done

echo
echo "Checkpoint pass complete."
