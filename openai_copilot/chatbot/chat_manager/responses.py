--------------------------------------------------------------------------------
# messages.py
--------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Message(ABC):
    """
    Base abstract class for all message types.
    Subclasses must implement the process() method.
    """
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def process(self):
        pass


class TextMessage(Message):
    """
    Represents a text response from the API.
    """
    def process(self):
        # For a text message, we might just display it or store it as-is.
        print(f"[TextMessage] Content: {self.content}")


class FunctionCallMessage(Message):
    """
    Represents a function call response from the API.
    content: some descriptive text about the call (optional)
    function_name: the name of the function to call
    args: arguments for the function
    """
    def __init__(self, content, function_name, args):
        super().__init__(content)
        self.function_name = function_name
        self.args = args

    def process(self):
        # Stub for actually executing the function. Could do real logic here.
        print(f"[FunctionCallMessage] Executing {self.function_name} with args: {self.args}")


class DataStructureMessage(Message):
    """
    Represents a data-structure-based response, e.g., JSON or Python dict.
    """
    def process(self):
        # Example: we might parse or transform this data structure further.
        print(f"[DataStructureMessage] Handling data structure: {self.content}")


--------------------------------------------------------------------------------
# message_factory.py
--------------------------------------------------------------------------------
class MessageFactory:
    """
    Factory class that creates the appropriate Message subclass
    based on the 'type' field in the raw response data.
    """
    @staticmethod
    def create_message(response_data):
        msg_type = response_data.get("type")

        if msg_type == "text":
            return TextMessage(content=response_data["content"])

        elif msg_type == "function_call":
            return FunctionCallMessage(
                content=response_data.get("content", ""),
                function_name=response_data["function_name"],
                args=response_data.get("args", [])
            )

        elif msg_type == "data_structure":
            return DataStructureMessage(content=response_data["content"])

        else:
            raise ValueError(f"Unknown message type: {msg_type}")


--------------------------------------------------------------------------------
# main.py (Usage Example)
--------------------------------------------------------------------------------
from message_factory import MessageFactory

def main():
    # Simulated raw responses from your API:
    raw_responses = [
        {
            "type": "text",
            "content": "Hello, user!"
        },
        {
            "type": "function_call",
            "content": "Check user details",
            "function_name": "get_user_profile",
            "args": ["some_user_id"]
        },
        {
            "type": "data_structure",
            "content": {"users": ["Alice", "Bob"], "count": 2}
        }
    ]

    # Maintain a history of message objects:
    message_history = []

    for raw in raw_responses:
        # Use the Factory to create the appropriate Message subclass:
        msg_obj = MessageFactory.create_message(raw)
        # Store it in your message history:
        message_history.append(msg_obj)
        # Process the message (render text, execute function, etc.):
        msg_obj.process()

    # Example: do something with the entire message history if desired.
    print("\n----- Full Message History -----")
    for i, m in enumerate(message_history):
        print(f"Message {i+1}: {m.__class__.__name__}, content={m.content}")


if __name__ == "__main__":
    main()

--------------------------------------------------------------------------------
Explanation of Key Points
--------------------------------------------------------------------------------
1. Abstract Base Class (Message):  
   • Enforces that any message type must implement the process() method.  
   • Avoids cluttering one single monolithic “Message” class with all sorts of specialized logic.

2. Specialized Message Subclasses:  
   • TextMessage: for simple text-based responses.  
   • FunctionCallMessage: for responses indicating an action needs to be executed (like a function name + parameters).  
   • DataStructureMessage: for responses carrying structured data (e.g., a dictionary) that you may need to parse or display differently.

3. The Factory (MessageFactory):  
   • Centralizes object creation logic.  
   • Decides which subclass to instantiate based on the type field.  
   • Keeps your code more flexible—if new message “flavors” appear, you add a new subclass and extend the factory, without touching other message types.

4. Message History:  
   • message_history is just a list that stores references to the created message objects.  
   • Each message can be processed immediately (e.g., printed, executed, etc.) and also be saved as part of the conversation history.

This structure keeps things clean: You won’t litter your main logic with if-else checks. Instead, the factory handles creation, and each specialized class handles its own process() method