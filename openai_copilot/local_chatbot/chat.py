"""
chat.py

Contains the ChatBot class and functions that manage the chat session.
"""

import sys
from models import get_response  # function to get responses from the OpenAI models
from storage import save_log   # function to save the chat log
from admin import process_admin_command  # function to process admin instructions


class ChatBot:
    """
    ChatBot class to handle the chat session.
    """

    def __init__(self, admin_instructions=None):
        """
        Initialize the ChatBot with an optional admin instruction.
        
        Args:
            admin_instructions (str, optional): Initial admin commands to configure the chatbot.
        """
        self.chat_log = []  # stores the conversation as a list of dicts: [{'user': <str>, 'bot': <str>}]
        if admin_instructions:
            self.process_admin(admin_instructions)

    def process_admin(self, instructions):
        """
        Process admin instructions provided at startup.
        
        Args:
            instructions (str): Admin command or configuration instructions.
        """
        # Delegate admin instruction processing to admin.py
        process_admin_command(instructions)

    def start_chat(self):
        """
        Starts the chat session loop.
        """
        print("Chat session started. Type 'exit' to quit.")
        
        while True:
            try:
                user_input = input("You: ")
            except KeyboardInterrupt:
                print("\nChat session interrupted.")
                break

            if user_input.lower().strip() == "exit":
                print("Exiting chat...")
                break

            # Get a response from the model (logic is defined in models.py)
            response = get_response(user_input)

            # Save the interaction in the chat log
            self.chat_log.append({"user": user_input, "bot": response})

            # Display the response to the user
            print("Bot:", response)

        # After chat ends, save the chat log using the storage module
        save_log(self.chat_log)
        print("Chat log saved.")


def main():
    """
    Entry point for starting a chat session.
    Optionally, admin instructions can be passed as a command-line argument.
    """
    admin_instructions = None
    if len(sys.argv) > 1:
        admin_instructions = sys.argv[1]

    chatbot = ChatBot(admin_instructions=admin_instructions)
    chatbot.start_chat()


if __name__ == "__main__":
    main()
