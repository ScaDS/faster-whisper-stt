# source see https://github.com/SYSTRAN/faster-whisper  /1/
# https://huggingface.co/openai/whisper-tiny            /2/

# --- INFO --- # 
'''
This tiny script showcases how easy it is to transcribe audio in realtime (or even faster).
Someday I came across this video: https://youtu.be/Mfbei9I8qQc?feature=shared (btw. a nice channel) when I was looking 
for a starting point regarding state-of-the-art SpeechToText (STT).
The solution was "faster-whisper":
"a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models" /1/

For the setup and required hardware / software see /1/
After setting up, feel free to use the code below to test it.

Beware: models can use some diskspace, so keep an eye on you system-stats!
'''

# --- How it works & what it does --- # 
'''
Before testing: 
- comment/uncomment the function you want to test: 
    # transcribe wav-file
        Beware: change device by commenting/uncommenting in line 54 (CPU) / 55 (GPU)
                set the correct path in line 56 (ger) or 57 (eng)
 
After importing necessary libs, of course, we 
    1. initialize the time-module for time-measurement
    2. init the model (Tiny-Whisper, see /2/) 
    3. feed a audio file (.wav) in "model.transcribe() as well as giving the target language and other inputs (see below)
    4. see the transcript and processing time in terminal-output
'''
# --- Usage --- # 
'''
Beware: tested under Win11; Python3.11.5; pip24.0
- read https://github.com/SYSTRAN/faster-whisper?tab=readme-ov-file#requirements /1/
- create a venv (Win11, e.g.: python -m venv stt-venv)
- activate venv (Win11: stt-venv/scripts/activate)
- pip install -r requirements.txt
- run 'python stt.py'
- have fun :) 
'''

# --- Usability --- #
'''
- feel free to add functionality
- I use it for a STT-LLM-TTS pipeline based on "faster-whisper" (STT); Ollama & API (LLM, Mistral 7b); suno-bark (TTS)
'''

from faster_whisper import WhisperModel
import time                                     # "time" only for seeing how crazy fast this works (on proper hardware) :)

model = WhisperModel("tiny", device="cpu")
# model = WhisperModel("tiny", device="cuda")
# Transcribe wav-file
transcribe_start_time = time.time()
segments, _ = model.transcribe("path/to/your-wav-file.wav", language="de", word_timestamps=True)    # transcribe german
# segments, _ = model.transcribe("path/to/your-wav-file.wav", language="en", word_timestamps=True)              # transcribe english
transcribe_end_time = time.time()
transcribe_duration = transcribe_end_time - transcribe_start_time

segments_list = list(segments)
transcription = " ".join([segment.text for segment in segments_list])
print(transcription)
print(f"transcription time: {transcribe_duration}s")
