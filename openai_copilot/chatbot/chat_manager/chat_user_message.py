from openai.types.chat import ChatCompletionUserMessageParam



class ChatUserMessage:
    """
    Handles user messages before sending them to the chat controller.
    Performs preprocessing before storing and sending the message.

    Attributes:
        processed_message (ChatCompletionMessageParam): The processed message
        before being sent to the chat server.
    """

    def __init__(self, user_content):
        """
        Initializes an empty processed message object.
        """
        self.processed_message = self.process(user_content)
        

    def process(self, content: str) -> None:
        """
        Processes the input message content and stores it in `processed_message`.

        Args:
            content (str): The raw text message from the user.
        """
        # More preprocessing can be added in future implementations
        self.processed_message = ChatCompletionUserMessageParam(content=content)
        return self.processed_message
        

