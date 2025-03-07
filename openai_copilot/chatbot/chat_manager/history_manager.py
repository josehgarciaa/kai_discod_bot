from dataclasses import dataclass, field
from typing import List, Union, Iterable
from chat_manager import APIResponse, ChatUserMessage, ClientAction


@dataclass
class ChatHistory:
    """
    Stores the history of chat messages, allowing messages to be appended
    and retrieved in an API-compatible format.
    """

    history: List[dict] = field(default_factory=list)

    def append_message(self, message: Union[ChatUserMessage,
                                            APIResponse,
                                            ClientAction]) -> None:
        """
        Appends a single message or multiple messages to the chat history.

        Args:
            message (ChatUserMessage | Iterable[ChatUserMessage]): 
                A single ChatUserMessage or an iterable of ChatUserMessage instances.

        Raises:
            AttributeError: If an object does not have a `get_api_message()` method.
        """                           
        if isinstance(message, (ChatUserMessage,APIResponse)):
            # Single message case
            self.history.append(message.get_api_message())
        elif isinstance(message, ClientAction):
            # Handle multiple messages
            for api_message in message.get_api_message():
                self.history.append(api_message)
        else:
            raise AttributeError(f"Object {message} does not have 'get_api_message()' method.")

    def messages(self) -> List[dict]:
        """
        Retrieves the entire chat history.

        Returns:
            List[dict]: A list of messages formatted as API-compatible dictionaries.
        """
        return self.history
