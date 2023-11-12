from chat import tools
import json
from typing import Callable


def run_conversation(
    query: str,
    prompt: str,
    client: Callable,
    functions: tools.Functions,
    chat_model_type: str = "gpt-3.5-turbo",
    model_temperature: int = 0.5,
):
    # Step 1: send the conversation and available functions to the model

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": query},
    ]

    tools = json.load(open("chat/tools.json"))

    response = client.chat.completions.create(
        model=chat_model_type,
        messages=messages,
        tools=tools,
        temperature=model_temperature,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message

    if response_message.content is None:
        response_message.content = ""
    if response_message.function_call is None:
        del response_message.function_call

    tool_calls = response_message.tool_calls
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            # "get_current_weather": get_current_weather,
            "get_current_date_and_time": functions.get_current_date_and_time,
            "google_search": functions.search_google,
        }  # only one function in this example, but you can have multiple
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            print(function_args)
            try:
                function_response = function_to_call(**function_args)
            except:
                function_response = function_to_call()
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response

        second_response = client.chat.completions.create(
            model=chat_model_type, messages=messages, temperature=model_temperature
        )  # get a new response from the model where it can see the function response

        return second_response

    else:
        return response_message
