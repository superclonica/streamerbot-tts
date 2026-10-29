# Streamer.bot TTS with custom AI voices

Make a Streamer.bot channel point redeem speak in any voice you like: an announcer, a villain, a cartoon character
or your own trained voice. The text is voiced **offline on your PC** by the free
[SuperClonica engine](https://pypi.org/project/superclonica-cpu/) (Supertonic 3, 31 languages, runs on an ordinary CPU),
and Streamer.bot plays the file on stream.

Full walkthrough: [Streamer.bot TTS with custom AI voices](https://superclonica.com/en/guides/streamer-bot-text-to-speech).

## 1. Install

```sh
python -m pip install superclonica-cpu
```

Copy [`sb_tts.py`](sb_tts.py) to a folder such as `C:\stream`.

Voices: the ten stock voices `M1`–`M5` and `F1`–`F5` come with the engine and may be used on monetized streams
(OpenRAIL-M). Any voice from the [SuperClonica catalog](https://superclonica.com/en/explore) can be bought once and
downloaded as a small JSON file; put it next to the script, e.g. `C:\stream\voice.json`.

## 2. The Streamer.bot action

1. Create a channel point reward that requires the viewer to enter text.
2. Add an action with the trigger **Twitch → Channel Reward → Reward Redemption** for that reward.
3. Sub-action **Core → System → Run a Program**:
   - Command: `python`
   - Arguments: `C:\stream\sb_tts.py`
   - Working Directory: `C:\stream`
   - Wait for Exit: `30`
   - Environment Variables:

     | Name | Value |
     |---|---|
     | `SC_TEXT` | `%rawInput%` |
     | `SC_VOICE` | `C:\stream\voice.json` (or `F1`) |
     | `SC_LANG` | `en` |
     | `SC_OUT` | `C:\stream\tts.wav` |

4. Sub-action **Core → Sounds → Play Sound** with `C:\stream\tts.wav`, "Finish playing before continuing" on.

The viewer's text goes through an environment variable, not the command line, so quotes and symbols in a message
cannot break the command. The script cuts messages to 300 characters and ignores empty ones.

## Speed

On our test PC a five-second line took about eleven seconds from start to file, most of it loading the model on each
run. For near-instant replies keep the engine loaded in a local server, or call the
[SuperClonica speech API](https://github.com/superclonica/free-tts-api) (free key: 3 minutes of audio a day).

## Fair use

Give the reward a price and a cooldown, and moderate it like chat. Fan-made character voices are for parody and fan
content; never use a voice to make it sound as if a real person said something.

## License

MIT for the script in this repository. The engine is Apache-2.0; the Supertonic 3 model is OpenRAIL-M.
