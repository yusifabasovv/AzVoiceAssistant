from voice import utils
from typing import Callable


def speech_to_text(stream, client: Callable, prompt: str, language: str = "az"):
    "Converts speech to text using whisper large-v2 model."

    stream = list(stream)
    name = utils.convert_audio_to_file(stream[1], stream[0])
    file = open(name, "rb")

    transcript = client.audio.transcriptions.create(
        model="whisper-1", file=file, language=language, response_format="text", prompt=prompt
    )
    return transcript
