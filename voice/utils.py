import time
import soundfile as sf
import os


def convert_audio_to_file(audio_array, rate):
    name = f"{time.time()}.mp3"
    sf.write(name, audio_array, rate)
    return name


def delete_mp3_files():
    # Iterate over all files in the directory
    directory = os.getcwd()
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
