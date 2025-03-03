"""
models.py

Interfaces with the OpenAI models. This module provides functions to send prompts to OpenAI's API
and return generated responses. It now includes a function to generate search queries.

https://platform.openai.com/docs/api-reference/chat/create

"""

import json
import openai
from config import API_KEY, MODEL

# Set the API key for OpenAI
from openai import OpenAI
openai_client = OpenAI(api_key=API_KEY)


def get_response(user_prompt, image_url =None, response_format=None, tools=None):
    """
    Sends the user's prompt to the OpenAI model and returns the generated response.

    Args:
        user_prompt (str): The user prompt or input text.
        response_format = defines the structured out, it can be defined using json schema or pydantic obetc
        tools = define the interface with the functions to be called
        image_url = define an url to read images

    Returns:
        str: The response text from the model.
    """
    system_prompt ="You are a knowleadgable software architech with knowledge also on LLM and openai. You will help the user, which is a scientific programmer with no experience in software engeneering but extensive experience about algorithm implementation. You will always answer using markdown format"
    try:
        completion = openai_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return completion.choices[0].message
    except Exception as e:
        return f"Error: {e}"
    
# Example usage (for testing purposes)
if __name__ == "__main__":
    # Initialize the client using the new OpenAI interface

    input = ""
    with open("input.md", "r", encoding="utf-8") as file:
        input = file.read()
    
    response= get_response(input)
    try:
        output = response.content
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(output)
    except:
        print(response)
