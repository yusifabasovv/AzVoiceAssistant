import gradio as gr
from voice.utils import delete_mp3_files
from typing import Callable

def run_gradio(get_completion: Callable):
    delete_mp3_files()

    with gr.Blocks(
        gr.themes.Default(
            primary_hue="green",
        )
    ) as demo:
        title = ("Voice Assistant",)

        with gr.Row():
            with gr.Accordion(label="Chat Model's parameters.", open=True):
                temperature = (
                    gr.Slider(
                        minimum=0,
                        maximum=1,
                        value=0.5,
                        step=0.05,
                        label="Model temperature",
                        info="Temperature is a parameter of the OpenAI (ChatGPT, GPT-3, and GPT-4) models that influence the variability and consequently the creativity of responses",
                        interactive=True,
                    ),
                )
                chat_model = (
                    gr.Dropdown(
                        choices=[
                            "gpt-3.5-turbo",
                            "gpt-3.5-turbo-1106",
                            "gpt-4",
                            "gpt-4-1106-preview",
                        ],
                        value="gpt-3.5-turbo",
                        label="Model type",
                        interactive=True,
                    ),
                )
            with gr.Accordion(label="Voice Model's parameters.", open=True):
                voice_speed = (
                    gr.Slider(
                        minimum=0.25,
                        maximum=4,
                        value=1,
                        step=0.1,
                        label="Voice speed",
                        interactive=True,
                    ),
                )
                voice_model = (
                    gr.Dropdown(
                        choices=["tts-1", "tts-1-hd"],
                        value="tts-1",
                        label="Model type",
                        interactive=True,
                    ),
                )
                voice_type = (
                    gr.Dropdown(
                        choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
                        value="nova",
                        label="Voice type",
                        interactive=True,
                    ),
                )

        with gr.Row(variant="compact"):
            with gr.Group():
                input_text = gr.Text(
                    interactive=True,
                    autofocus=True,
                    label="Ask your question by text",
                    info="Press enter to submit",
                )
                with gr.Group():
                    input_voice = gr.Audio(
                        label="Ask your question by voice",
                        min_width=80,
                        sources="microphone",
                    )
                    input_voice_run = gr.Button("Run")

            output_ = [
                gr.Audio(
                    format="mp3", label="Voice output", min_width=80, autoplay=True
                )
            ]

        input_text.submit(
            get_completion,
            inputs=[
                input_text,
                input_voice,
                list(chat_model)[0],
                list(temperature)[0],
                list(voice_model)[0],
                list(voice_speed)[0],
                list(voice_type)[0],
            ],
            outputs=output_,
        )
        input_voice_run.click(
            get_completion,
            inputs=[
                input_text,
                input_voice,
                list(chat_model)[0],
                list(temperature)[0],
                list(voice_model)[0],
                list(voice_speed)[0],
                list(voice_type)[0],
            ],
            outputs=output_,
        )
        # input_voice.stop_recording(get_completion, inputs=[input_text, input_voice, list(chat_model)[0], list(temperature)[0], list(voice_model)[0], list(voice_speed)[0], list(voice_type)[0]], outputs=output_)
        # input_voice.start_recording(# implement text clearinh here)
    demo.launch()
    delete_mp3_files()


if __name__ == "__main__":
    run_gradio()
