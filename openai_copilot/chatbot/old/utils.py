"""
utils.py

Contains utility functions that support tasks like formatting messages,
error handling, and other helper operations used across the project.
"""

def format_message(role, content):
    """
    Formats a chat message into a standardized dictionary.

    Args:
        role (str): The role of the message sender (e.g., 'user' or 'bot').
        content (str): The message content.

    Returns:
        dict: A dictionary with keys 'role' and 'content' representing the message.
    """
    return {"role": role, "content": content}


def sanitize_input(input_str):
    """
    Sanitizes the user input by trimming whitespace and handling any additional
    normalization if needed.

    Args:
        input_str (str): The raw input string from the user.

    Returns:
        str: The sanitized input string.
    """
    return input_str.strip()


def handle_error(e):
    """
    Handles errors by printing a formatted error message.
    In a more complex system, you might want to log these errors.

    Args:
        e (Exception): The exception to handle.

    Returns:
        str: The formatted error message.
    """
    error_message = f"An error occurred: {str(e)}"
    print(error_message)
    return error_message


if __name__ == "__main__":
    # Basic tests for the utility functions
    test_msg = format_message("user", "Hello, ChatBot!")
    print("Formatted message:", test_msg)
    
    test_input = "   Hello, world!   "
    print("Sanitized input:", sanitize_input(test_input))
    
    try:
        1 / 0  # Generate an error for testing
    except Exception as err:
        handle_error(err)
    