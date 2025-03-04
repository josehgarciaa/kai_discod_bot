"""
storage.py

Manages the chat register. This file handles saving and loading chat logs.
"""

import json
import os

# Define the file where chat logs will be stored.
CHAT_LOG_FILE = "chat_log.json"

def save_log(chat_log):
    """
    Saves the chat log to a JSON file.

    Args:
        chat_log (list): List of chat exchanges. Each exchange is a dictionary,
                         for example: {'user': 'Hello', 'bot': 'Hi there!'}.
    """
    try:
        with open(CHAT_LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(chat_log, file, indent=4)
        print(f"Chat log saved to {CHAT_LOG_FILE}.")
    except Exception as e:
        print(f"Error saving chat log: {e}")

def load_log():
    """
    Loads the chat log from the JSON file.

    Returns:
        list: A list of chat exchanges if the file exists,
              otherwise returns an empty list.
    """
    if not os.path.exists(CHAT_LOG_FILE):
        return []
    
    try:
        with open(CHAT_LOG_FILE, "r", encoding="utf-8") as file:
            chat_log = json.load(file)
        return chat_log
    except Exception as e:
        print(f"Error loading chat log: {e}")
        return []

if __name__ == "__main__":
    # Basic tests for saving and loading the chat log.
    test_log = [
        {"user": "Hello", "bot": "Hi there!"},
        {"user": "How are you?", "bot": "I'm just a bot, but thanks for asking!"}
    ]
    save_log(test_log)
    
    loaded_log = load_log()
    print("Loaded chat log:", loaded_log)
