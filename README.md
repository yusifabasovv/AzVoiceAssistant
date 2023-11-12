# AzVoiceAssistant

## Description
AzVoiceAssistant is a Gradio-based voice assistant application enabling interactions with GPT models using text or voice inputs. Specializing in Azerbaijani language support, it integrates OpenAI's GPT models for processing inputs and generating voice responses.

## Installation
To install AzVoiceAssistant, run the following commands:
```bash
git clone https://github.com/yourusername/AzVoiceAssistant.git
cd AzVoiceAssistant
pip install -r requirements.txt
```

## Configuration
Ensure to set up your API keys in a `.env` file.

## Usage
Start the application with the following command:
```bash
python app.py
```
Navigate to the provided local URL to interact with the assistant.

## Features
- Text and voice input support.
- Azerbaijani language compatibility.
- Integration with OpenAI's GPT models.
- Customizable model parameters through the Gradio interface.

## File Structure
- `app.py`: Contains core application logic.
- `/gradio_app`: Manages the Gradio user interface.
- `/voice`: Includes voice processing functionalities.
- `/chat`: Handles conversation and prompt management.

## Contributing
We welcome contributions. For significant changes, please open an issue first to discuss what you'd like to change.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
- OpenAI for the GPT models.
- Gradio team for their interactive interface toolkit.


## TODO List
Feel free to contribute to any of the following tasks:

- [ ] Language options
- [ ] Chat history
- [ ] UI for credentials
- [ ] Streaming for input voice


