import requests
from openai.types.chat import ChatCompletionMessageParam

class MessageRequest:
    """
    A simple class to encapsulate sending requests to an API endpoint.
    """
    def __init__(self, endpoint, payload=None, headers=None):
        self.message = None

    def send(self, message):
        self.message = ChatCompletionMessageParam(content=message)

        return self


────────────────────────────────────────────────────────
4) main.py (Example Usage)
────────────────────────────────────────────────────────
from message_factory import MessageFactory
from message_request import MessageRequest

def main():
    # 1. PREPARE A REQUEST TO THE API
    request = MessageRequest(
        endpoint="https://example.com/api/chat",  # Replace with your real endpoint
        payload={"user_message": "Hello, can you do X for me?"}
    )

    # 2. SEND THE REQUEST AND GET RAW RESPONSE (E.G., DICT)
    raw_response = request.send()
    # Suppose raw_response is something like:
    # { "type": "function_call", "content": "Need a function call",
    #   "function_name": "do_x_for_user", "args": ["param1", "param2"] }

    # 3. USE THE FACTORY TO CREATE A SPECIFIC MESSAGE OBJECT
    message_obj = MessageFactory.create_message(raw_response)

    # 4. PROCESS THE MESSAGE (RENDER TEXT, EXECUTE FUNCTION, ETC.)
    message_obj.process()

    # 5. MAINTAIN A HISTORY OF MESSAGES IF YOU WANT
    message_history = []
    message_history.append(message_obj)

    # Potentially do additional API calls in a loop or similar, appending to history.


if __name__ == "__main__":
    main()


────────────────────────────────────────────────────────
NOTES & CONSIDERATIONS
────────────────────────────────────────────────────────
• In real-world code, you often separate concerns (API calls vs. message/model objects). Here, the MessageRequest class is a lightweight wrapper around requests.post().  
• If your API can return multiple flavors (text, function calls, data structures), the Factory keeps you from doing endless if-else checks.  
• Each message subclass (TextMessage, FunctionCallMessage, DataStructureMessage) handles its own specialized behavior in process().  
• message_history can just be a simple Python list, or it can be a sophisticated data store if you need database persistence or advanced features.  