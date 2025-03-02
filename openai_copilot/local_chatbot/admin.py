"""
admin.py

Handles admin instructions for the chatbot.
Now includes functionality to update the system prompt used in API calls.
"""

# Global variable to store the system prompt.
SYSTEM_PROMPT = "You are a helpful assistant."

def process_admin_command(command):
    """
    Processes an admin command to configure or control the chatbot.
    Now supports setting a new system prompt.

    Args:
        command (str): The admin command string.
    """
    global SYSTEM_PROMPT

    if command.startswith("set_system "):
        # Update the system prompt with the provided value.
        new_system_prompt = command[len("set_system "):].strip()
        SYSTEM_PROMPT = new_system_prompt
        print(f"[ADMIN] System prompt updated to: {SYSTEM_PROMPT}")

    elif command.strip() == "reset_chat":
        print("[ADMIN] Resetting chat log...")
        # TODO: Add logic to reset the chat log

    else:
        print("[ADMIN] Unrecognized command. Available commands:")
        print("  set_system <prompt>  - Update the system prompt used for API calls.")
        print("  reset_chat           - Reset the chat log.")

if __name__ == "__main__":
    # Simple tests when running admin.py directly
    process_admin_command("set_system Welcome to the updated ChatBot system!")
    process_admin_command("reset_chat")
