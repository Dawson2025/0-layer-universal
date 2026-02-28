#!/usr/bin/env python3
"""
Azure Speech TTS integration verification.

Enable by exporting RUN_AZURE_TTS_TESTS=1 with valid Azure credentials.
"""

import os
import sys
import pytest

sys.path.append(".")

from src.tts_ipa import IPATTSEngine  # noqa: E402


@pytest.mark.integration
def test_azure_tts_generate_audio():
    """Ensure Azure TTS can synthesize IPA when credentials are configured."""
    if os.getenv("RUN_AZURE_TTS_TESTS") != "1":
        pytest.skip("Set RUN_AZURE_TTS_TESTS=1 to enable Azure Speech integration tests")

    engine = IPATTSEngine()

    assert (
        engine.azure_available
    ), "Azure TTS unavailable; ensure Azure Speech SDK is installed and credentials are set"

    sample = "tʃaɪv"
    audio_base64 = engine.generate_ipa_audio(sample)

    assert audio_base64, "Azure TTS returned no audio data"
    assert len(audio_base64) > 100, "Audio payload too small to be valid"


@pytest.mark.integration
def test_azure_tts_generate_phoneme_with_context():
    """Verify phoneme-specific synthesis produces audio via Azure."""
    if os.getenv("RUN_AZURE_TTS_TESTS") != "1":
        pytest.skip("Set RUN_AZURE_TTS_TESTS=1 to enable Azure Speech integration tests")

    engine = IPATTSEngine()
    assert engine.azure_available, "Azure TTS unavailable; check credentials"

    phoneme_audio = engine.generate_phoneme_audio("tʃ", position="onset")
    assert phoneme_audio, "Azure TTS returned no audio for onset phoneme"
    assert len(phoneme_audio) > 100, "Phoneme audio payload too small"
