#!/usr/bin/env python3
"""
Codex notification hook executed via the `notify` config option.

Receives a single JSON string argument describing the event and triggers
desktop/audio cues using the same environment variables as codex-notify.sh.
"""

from __future__ import annotations

import json
import os
import sys
import subprocess
import shutil
from typing import Optional, Tuple


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def get_env(*names: str, default: str | None = None) -> str | None:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return default


def bell() -> None:
    if os.environ.get("CODEX_NOTIFY_BELL", "1") != "0":
        try:
            sys.stdout.write("\a")
            sys.stdout.flush()
        except Exception:
            pass


def notify(title: str, body: str | None) -> None:
    notifier = get_env("CODEX_NOTIFY_SENDER")
    if not notifier:
        for candidate in ("wsl-notify-send.exe", "wsl-notify-send"):
            if have(candidate):
                notifier = candidate
                break
    if not notifier:
        return
    message = body or title
    try:
        subprocess.Popen(
            [notifier, "--category", title, message],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        pass


def say_text(text: str | None) -> None:
    if not text:
        return
    speaker = get_env("CODEX_NOTIFY_SPEAKER", default="spd-say")
    if speaker and have(speaker):
        try:
            subprocess.Popen(
                [speaker, text],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return
        except FileNotFoundError:
            pass

    # Fall back to native Windows speech when running inside WSL.
    if os.environ.get("WSL_DISTRO_NAME") and have("powershell.exe"):
        speak_cmd = (
            "[console]::beep(900,200); "
            "Add-Type -AssemblyName System.Speech; "
            f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak({json.dumps(text)})"
        )
        try:
            subprocess.Popen(
                ["powershell.exe", "-Command", speak_cmd],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except FileNotFoundError:
            pass


def play_sound(path: str | None) -> None:
    if not path:
        return
    player = get_env("CODEX_NOTIFY_PLAYER", default="ffplay")
    if not player or not have(player):
        return
    if not os.path.exists(path):
        return
    try:
        subprocess.Popen(
            [player, "-autoexit", "-nodisp", path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        pass


def run_custom(command: str | None) -> None:
    if not command:
        return
    try:
        subprocess.Popen(
            ["bash", "-lc", command],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        pass


def summarize(notification: dict) -> Tuple[str, str, Optional[str], Optional[str], Optional[str]]:
    assistant = (notification.get("last-assistant-message") or "").strip()
    inputs = notification.get("input-messages") or []
    prompt = " ".join(s.strip() for s in inputs if s)

    if assistant and prompt:
        body = f"{assistant}\nPrompt: {prompt}"
    elif assistant:
        body = assistant
    elif prompt:
        body = f"Prompt: {prompt}"
    else:
        body = "Codex turn complete."

    title = get_env(
        "CODEX_NOTIFY_TURN_TITLE",
        "CODEX_NOTIFY_TITLE_SUCCESS",
        default="Codex needs input",
    )
    text = get_env(
        "CODEX_NOTIFY_TURN_TEXT",
        "CODEX_NOTIFY_SUCCESS_TEXT",
        default="Codex is ready for your next instruction.",
    )
    sound = get_env("CODEX_NOTIFY_TURN_SOUND", "CODEX_NOTIFY_SUCCESS_SOUND")
    command = get_env(
        "CODEX_NOTIFY_COMMAND_TURN",
        "CODEX_NOTIFY_COMMAND_SUCCESS",
    )
    return title, body, text, sound, command


def handle_notification(notification: dict) -> None:
    ntype = notification.get("type")
    if ntype in {"agent-turn-complete", "approval-requested"}:
        title, body, text, sound, command = summarize(notification)
        bell()
        notify(title, body)
        say_text(text)
        play_sound(sound)
        run_custom(command)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        return 1
    payload = argv[1]
    try:
        notification = json.loads(payload)
    except json.JSONDecodeError:
        return 1
    handle_notification(notification)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
