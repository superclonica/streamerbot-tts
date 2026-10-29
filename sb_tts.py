"""Streamer.bot TTS: voice %rawInput% offline with the free SuperClonica engine.

Run from a Streamer.bot "Run a Program" sub-action with the environment variables
SC_TEXT (the message), SC_VOICE (F1..F5, M1..M5 or a voice JSON file), SC_LANG and SC_OUT.
"""
import os, shutil, subprocess, sys

text = os.environ.get('SC_TEXT', '').strip()[:300]
if not text:
    sys.exit(0)
cli = shutil.which('superclonica') or os.path.join(os.path.dirname(sys.executable), 'Scripts', 'superclonica')
subprocess.run([cli, '--text', text, '--voice', os.environ.get('SC_VOICE', 'F1'),
                '--lang', os.environ.get('SC_LANG', 'en'), '--output', os.environ.get('SC_OUT', 'tts.wav')], check=True)