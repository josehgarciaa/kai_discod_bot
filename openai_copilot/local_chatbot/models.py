"""
models.py

Interfaces with the OpenAI models.
This module provides the get_response function that sends prompts to OpenAI's API
and returns the generated response.
"""

import openai
from config import API_KEY, MODEL

# Set the API key for openai
openai.api_key = API_KEY

def get_response(prompt):
    """
    Sends the user's prompt to the OpenAI model and returns the generated response.

    Args:
        prompt (str): The user prompt or input text.

    Returns:
        str: The response text from the model.
    """
    try:
        # For chat-based models like gpt-3.5-turbo, we format the prompt into a message list.
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        # Extract and return the assistant's reply
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Return an error message if the API call fails
        return f"Error: {e}"

if __name__ == "__main__":
    # Simple test of the get_response function
    test_prompt = "Hello, how are you today?"
    print("User:", test_prompt)
    print("Bot:", get_response(test_prompt))
