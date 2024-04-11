# faster-whisper-stt
 Simple and basic python function for transcribing audio in realtime based on faster-whisper

# INFO 

This tiny script showcases how easy it is to transcribe audio in realtime (or even faster).

Someday I came across this video: https://youtu.be/Mfbei9I8qQc?feature=shared (btw. a nice channel) when I was looking for a starting point regarding state-of-the-art SpeechToText (STT).

The solution was "faster-whisper":
"a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models" /1/

For the setup and required hardware / software see /1/

After setting up, feel free to use the code provided in the repo.

*Beware*: models can use some diskspace, so keep an eye on your system-stats!

# How it works & what it does
## Transcribe wav-file
**important**: set the correct path in line 53 (ger) or 54 (eng) and choose the target language by commenting/uncommenting one of these lines

After importing necessary libs, of course, we

1. initialize the time-module for time-measurement

2. init the model (Tiny-Whisper, see /2/)

3. feed a audio file (.wav) in "model.transcribe() as well as giving the target language and other inputs (see below)

4. print the transcript and processing-time in terminal-output

# Usage
**important**: tested under Win11; Python3.11.5; pip24.0
- read https://github.com/SYSTRAN/faster-whisper?tab=readme-ov-file#requirements /1/

- create a venv (Win11, e.g.: `python -m venv stt-venv`)

- activate venv (Win11: `stt-venv/scripts/activate`)

- `pip install -r requirements.txt`

- run `python stt.py`

- have *fun* and feel free to share your *use-cases* :) 

# Usability 
- feel free to add functionality
- I use it for a STT-LLM-TTS pipeline based on "faster-whisper" (STT), Ollama & API (LLM, Mistral 7b), suno-bark (TTS)

### sources see:
-  https://github.com/SYSTRAN/faster-whisper /1/
-  https://huggingface.co/openai/whisper-tiny /2/