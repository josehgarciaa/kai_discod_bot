"""
chat.py

Contains the ChatBot class and functions that manage the chat session.
Now supports interactive admin commands during the chat session.
"""

import sys
from models import get_response  # Function to get responses from the OpenAI models
from storage import save_log     # Function to save the chat log
from admin import process_admin_command  # Function to process admin instructions

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
        self.chat_log = []  # List to store conversation exchanges.
        if admin_instructions:
            self.process_admin(admin_instructions)

    def process_admin(self, instructions):
        """
        Process admin instructions provided either at startup or during the chat session.
        
        Args:
            instructions (str): Admin command or configuration instructions.
        """
        process_admin_command(instructions)

    def start_chat(self):
        """
        Starts the chat session loop.
        Users can type normal chat input or admin commands (prefixed with '/admin').
        """
        print("Chat session started. Type 'exit' to quit or '/admin <command>' for admin commands.")
        
        while True:
            try:
                user_input = input("You: ")
            except KeyboardInterrupt:
                print("\nChat session interrupted.")
                break

            # Exit the session if the user types "exit"
            if user_input.lower().strip() == "exit":
                print("Exiting chat...")
                break

            # Check if the input is an admin command (e.g., to update the system prompt)
            if user_input.startswith("/admin "):
                admin_command = user_input[len("/admin "):].strip()
                self.process_admin(admin_command)
                continue

            # Get a response from the model (logic defined in models.py)
            response = get_response(user_input)

            # Append the interaction to the chat log
            self.chat_log.append({"user": user_input, "bot": response})

            # Display the response to the user
            print("Bot:", response)

        # After the chat ends, save the chat log using the storage module
        save_log(self.chat_log)
        print("Chat log saved.")

def main():
    """
    Entry point for starting a chat session.
    Optionally, admin instructions can be passed as a command-line argument.
    """
    #admin_instructions = None
    #if len(sys.argv) > 1:
    #    admin_instructions = sys.argv[1]

    #chatbot = ChatBot(admin_instructions=admin_instructions)
    #chatbot.start_chat()

if __name__ == "__main__":
    main()
