### Setup

- create venv: python -m venv stt-venv 
- pip install faster-whisper
- pip install -r requirements_stt.txt


### Start

- voila stt-demo-app.ipynb


### Usage

- click start- / stop recording
- when clicking stop the transcript will automatically be show in the textbox
- reset-btn resets textbox
- send-btn sends transcript to ollama-api-endpoint for asking a (opensource-) llm; ask team LL (@autmoate) or set this up on your own (https://ollama.com/download --> team LL is happy to help here and even provides a sophisticated tutorial)
