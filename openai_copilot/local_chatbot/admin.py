"""
admin.py

Handles admin instructions for the chatbot.
This module manages both the system prompt and a set of OpenAI Chat API configuration options.
"""

# Global system prompt used in API calls.
SYSTEM_PROMPT = "You are a helpful assistant."

# Dictionary to store various API options and configurations.
ADMIN_OPTIONS = {
    "store": False,
    "reasoning_effort": "medium",
    "metadata": {},
    "frequency_penalty": 0,
    "logit_bias": None,
    "logprobs": False,
    "top_logprobs": None,
    "max_completion_tokens": None,
    "n": 1,
    "presence_penalty": 0,
    "seed": None,
    "service_tier": "auto",
    "stop": None,
    "stream": False,
    "stream_options": None,
    "temperature": 1,
    "top_p": 1,
    "tools": None,
    "tool_choice": None,
    "parallel_tool_calls": True,
    "user": None,
    # Deprecated options can be omitted or left commented.
    # "function_call": None,
    # "functions": None,
}

def parse_value(val):
    """
    Attempts to convert a string value to an appropriate Python type.
    
    Args:
        val (str): The string representation of the value.
    
    Returns:
        The value converted to a bool, int, float, or remains as string if conversion isn't possible.
    """
    if val.lower() == "none":
        return None
    elif val.lower() == "true":
        return True
    elif val.lower() == "false":
        return False
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return val

def process_admin_command(command):
    """
    Processes an admin command to configure or control the chatbot.
    
    Supported commands:
      - set_system <prompt>:
            Updates the global system prompt used in API calls.
      - set_option <option_name> <value>:
            Updates an option in ADMIN_OPTIONS. The value is parsed into an appropriate type.
      - show_options:
            Displays all current admin option settings.
      - reset_options:
            Resets all options to their default values.
      - reset_chat:
            Placeholder to reset the chat log (functionality to be implemented elsewhere).
    
    Args:
        command (str): The admin command string.
    """
    global SYSTEM_PROMPT, ADMIN_OPTIONS

    if command.startswith("set_system "):
        new_system_prompt = command[len("set_system "):].strip()
        SYSTEM_PROMPT = new_system_prompt
        print(f"[ADMIN] System prompt updated to: {SYSTEM_PROMPT}")

    elif command.startswith("set_option "):
        # Expected format: set_option <option_name> <value>
        parts = command.split(maxsplit=2)
        if len(parts) < 3:
            print("[ADMIN] Usage: set_option <option_name> <value>")
            return
        option_name = parts[1]
        value_str = parts[2]
        if option_name not in ADMIN_OPTIONS:
            print(f"[ADMIN] Option '{option_name}' not found.")
            return
        value = parse_value(value_str)
        ADMIN_OPTIONS[option_name] = value
        print(f"[ADMIN] Updated option '{option_name}' to: {value}")

    elif command.strip() == "show_options":
        print("[ADMIN] Current options:")
        for key, value in ADMIN_OPTIONS.items():
            print(f"  {key}: {value}")

    elif command.strip() == "reset_options":
        # Reset ADMIN_OPTIONS to the default values.
        ADMIN_OPTIONS.clear()
        ADMIN_OPTIONS.update({
            "store": False,
            "reasoning_effort": "medium",
            "metadata": {},
            "frequency_penalty": 0,
            "logit_bias": None,
            "logprobs": False,
            "top_logprobs": None,
            "max_completion_tokens": None,
            "n": 1,
            "presence_penalty": 0,
            "seed": None,
            "service_tier": "auto",
            "stop": None,
            "stream": False,
            "stream_options": None,
            "temperature": 1,
            "top_p": 1,
            "tools": None,
            "tool_choice": None,
            "parallel_tool_calls": True,
            "user": None,
        })
        print("[ADMIN] Options have been reset to default values.")

    elif command.strip() == "reset_chat":
        print("[ADMIN] Resetting chat log... (This should be implemented in the chat module.)")

    else:
        print("[ADMIN] Unrecognized command. Available commands:")
        print("  set_system <prompt>         - Update the system prompt used for API calls.")
        print("  set_option <name> <value>     - Update an option parameter.")
        print("  show_options                - Display current admin options.")
        print("  reset_options               - Reset admin options to default values.")
        print("  reset_chat                  - Reset chat log (not implemented here).")

if __name__ == "__main__":
    # Test commands for demonstration:
    process_admin_command("set_system Welcome to the updated ChatBot system!")
    process_admin_command("set_option temperature 0.8")
    process_admin_command("set_option max_completion_tokens 200")
    process_admin_command("show_options")
