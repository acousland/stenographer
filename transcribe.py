import whisper
from pydub import AudioSegment
import os
import tempfile

def transcribe(video_path, model):
    # Load video into pydub
    video = AudioSegment.from_file(video_path, "mp4")

    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_file_name = temp_file.name

    # Export as wav to the temporary file
    video.export(temp_file_name, format="wav")

    # Load the model
    model = whisper.load_model(model)

    # Transcribe the audio
    result = model.transcribe(temp_file_name)

    # Delete the temporary file
    os.remove(temp_file_name)

    return result["text"]


def transcribe_audio(audio, model):
    # Load the model
    model = whisper.load_model(model)

    # Transcribe the audio
    result = model.transcribe(audio)

    return result["text"]