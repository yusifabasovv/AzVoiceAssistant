from openai import OpenAI
from chat.conversation import run_conversation
from chat.prompts import MAIN_PROMPT, STT_PROMPT
from chat.tools import Functions

from voice.stt import speech_to_text
from voice.tts import text_to_speech
import gradio as gr
from dotenv import load_dotenv

load_dotenv()


client = OpenAI()
functions = Functions()


def get_completion(
    text: str,
    voice: gr.Audio,
    chat_model_type: str,
    model_temperature: float,
    voice_model_type: str,
    voice_speed: float,
    voice_type: str,
):
    """
    Processes either text or voice input to generate a voice response using GPT models.

    Args:
        text (str): Text input provided by the user.
        voice (str): Voice input provided by the user.
        chat_model_type (str): Type of the chat model to use.
        model_temperature (float): Temperature setting for the chat model.
        voice_model_type (str): Type of the voice model to use.
        voice_speed (float): Speed of the voice response.
        voice_type (str): Type of voice to use in the response.

    Returns:
        str: Filename of the generated voice response.
    """
    global client

    # Determine the input type (text or voice)
    if text:
        input_ = text
    elif voice:
        input_ = speech_to_text(stream=voice, client=client, prompt=STT_PROMPT)
    else:
        input_ = " "  # Default to a blank string if no input is provided

    # Run the conversation through the GPT model
    response = run_conversation(
        query=input_,
        client=client,
        prompt=MAIN_PROMPT,
        functions=functions,
        chat_model_type=chat_model_type,
        model_temperature=model_temperature,
    )

    # Extract the text content from the response
    try:
        response_text = response.content
    except AttributeError:
        # Fallback if the response structure is different
        response_text = response.choices[0].message.content

    # Convert the response text to speech
    file_name = text_to_speech(
        response_text, client, voice_model_type, voice_speed, voice_type
    )

    return file_name
