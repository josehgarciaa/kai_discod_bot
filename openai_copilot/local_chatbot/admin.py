"""
admin.py

Handles admin instructions for the chatbot.
"""

def process_admin_command(command):
    """
    Processes an admin command to configure or control the chatbot.

    This function acts as a placeholder to demonstrate how admin commands can be handled.
    You can expand it to support more complex actions (e.g., setting system prompts, resetting chat logs, etc.).

    Args:
        command (str): The admin command string.
    """
    print(f"[ADMIN] Processing command: {command}")

    # Example command handling:
    if command.startswith("set_prompt "):
        # Extract and set the system prompt for the chatbot
        prompt = command[len("set_prompt "):].strip()
        print(f"[ADMIN] Setting system prompt to: {prompt}")
        # TODO: Add logic to actually update the chatbot's system prompt

    elif command.strip() == "reset_chat":
        print("[ADMIN] Resetting chat log...")
        # TODO: Add logic to reset the chat log

    else:
        print("[ADMIN] Unrecognized command. Available commands: set_prompt <prompt>, reset_chat")


if __name__ == "__main__":
    # Simple tests when running admin.py directly
    process_admin_command("set_prompt Welcome to the ChatBot!")
    process_admin_command("reset_chat")
