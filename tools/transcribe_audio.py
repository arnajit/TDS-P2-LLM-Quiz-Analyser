from langchain.tools import tool
import speech_recognition as sr
import ffmpeg
import os
import tempfile

@tool
def transcribe_audio(file_path: str) -> str:
    """
    If any tool returns the field "audio_url", you MUST:

1. Call download_file with this audio_url.
2. Then call transcribe_audio with the downloaded file path.
3. Use ONLY the transcript as the answer.

NEVER ignore audio_url.
NEVER try to transcribe directly from the URL.
ALWAYS follow the chain: get_rendered_html → download_file → transcribe_audio.
    """
    try:
        if not file_path.startswith("LLMFiles"):
            full_path = os.path.join("LLMFiles", file_path)
        else:
            full_path = file_path

        # Convert MP3 to WAV using ffmpeg-python
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            wav_path = tmp.name

        (
            ffmpeg
            .input(full_path)
            .output(wav_path, format="wav", acodec="pcm_s16le")
            .run(quiet=True, overwrite_output=True)
        )

        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)

        os.remove(wav_path)

        return text or "Error: Empty transcript"

    except Exception as e:
        return f"Error: {e}"
