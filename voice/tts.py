import time
from typing import Callable


def text_to_speech(text, client: Callable, voice_model_type, voice_speed, voice_type):
    "Converts text to speech using openai's tts model."

    response = client.audio.speech.create(
        model=voice_model_type, voice=voice_type, input=text, speed=voice_speed
    )

    file_name = f"{time.time()}.mp3"
    response.stream_to_file(file_name)

    return file_name
