from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionMessageParam



class ChatUserMessage:
    """
    Handles user messages before sending them to the chat controller.
    Performs preprocessing before storing and sending the message.

    Attributes:
        processed_message (ChatCompletionMessageParam): The processed message
        before being sent to the chat server.
    """

    def __init__(self):
        """
        Initializes an empty processed message object.
        """
        self.api_compatible_message = None    
        self.readable_content =None     

    def handle(self, content: str) -> None:
        """
        Processes the input message content and stores it in `processed_message`.

        Args:
            content (str): The raw text message from the user.
        """
        # More preprocessing can be added in future implementations
        self.api_compatible_message = ChatCompletionUserMessageParam(role="user", content=content)

        return self

    def get_api_message(self):
        return self.api_compatible_message

    
    def readable(self):
        message = self.api_compatible_message
        self.readable_content = "role:"+message.get("role")+"\n"+message.get("content")
        return self.readable_content         

