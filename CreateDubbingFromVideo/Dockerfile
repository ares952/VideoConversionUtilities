FROM python:3.11-bookworm

WORKDIR /app

#following prerequisities are needed:
#ffmpeg - audio/video conversion tool
#jq - json manipulation tool

RUN apt-get update && apt-get install -y ffmpeg jq && apt-get clean

# whisper is needed to convert audio file to subtitles
RUN pip install --no-cache-dir setuptools-rust
#+5.6G:
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git
RUN pip install --no-cache-dir pysrt
RUN pip install --no-cache-dir srt

# download whisper models in advance - large and turbo are needed, tiny/base/small/medium are not goot enough
#+6.9G:
RUN python -c "import whisper; whisper.load_model('large')" && \
    python -c "import whisper; whisper.load_model('turbo')"

# there is a possibility to translate the files using google translator (gTTS) or coqui TTS AI tool
RUN pip install --no-cache-dir googletrans
RUN pip install --no-cache-dir TTS






#TTS models which might be used:
#paid for commercial use:
#tts_models/multilingual/multi-dataset/xtts_v1.1
#tts_models/multilingual/multi-dataset/xtts_v2

#free for commercial use:
#tts_models/en/ljspeech/tacotron2-DDC
#tts_models/cs/cv/vits"
#tts_models/cs/cv/vits"
#tts_models/sk/cv/vits"
#tts_models/es/css10/vits"
#tts_models/de/thorsten/vits


#RUN pip install --no-cache-dir transformers sentencepiece
#RUN pip install --no-cache-dir sacremoses


CMD ["bash", "-c", "while true; do sleep 1; done"]
