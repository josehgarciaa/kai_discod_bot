"""
models.py

Interfaces with the OpenAI models. This module provides functions to send prompts to OpenAI's API
and return generated responses. It now includes a function to generate search queries.
"""

import json
import openai
from config import API_KEY, MODEL

# Set the API key for OpenAI
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
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"


def create_search_queries(openai_client, user_prompt, model="gpt-4o", max_tokens="1000"):
    """
    Generates three search queries optimized for Google based on the provided user prompt.
    
    Args:
        openai_client: An instance of the OpenAI client.
        user_prompt (str): The user prompt which contains the context and requirements.
        model (str, optional): The model to use. Defaults to "gpt-4o".
        max_tokens (str, optional): Maximum tokens for the response. Defaults to "1000".
    
    Returns:
        dict: A dictionary containing three search queries.
    """
    # Define system instructions to guide the query generation
    sys_prompt = (
        "Design three search queries optimized for google. "
        "The first one shall be a query very directed to what the user is requiring in its prompt, "
        "the second one should be more generic and the third one should be a bit more experimental. "
        "Please, when is convenient use google query operators. Avoid at all cost websites that cannot be scrapped with selenium "
        "such as LinkedIn or similar. Use the operator to discard them."
    )
    
    # Request the chat completion using the new interface
    chat = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format="json"  # assuming the response format is set as "json"
    )
    
    # Parse and return the generated search queries
    return json.loads(chat.choices[0].message.content)

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Initialize the client using the new OpenAI interface
    from openai import OpenAI
    client = OpenAI(api_key=API_KEY)
    
    model_name = "gpt-4o"
    user_prompt = (
        "Consider this json "
        '"name": "ONERA", "entity_type": "none", "country": "France", '
        '"contact": "Hakim Amara, Annick Loiseau", "url": "none", '
        '"notes": "Collaborators and Potential customer" '
        " search where this person is working right now"
    )
    
    queries = create_search_queries(client, user_prompt, model=model_name, max_tokens="1000")
    print("Generated Search Queries:", queries)
