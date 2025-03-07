

from chat_manager import ChatMessage, ChatResponse


class ChatController:
    """
    Core chat service controller that processes messages and maintains history.
    Currently supports a single session.
    """
    def __init__(self):
        # Initialize an empty history list to store ChatMessage and ChatResponse objects
        self.history = []

    def process_message(self, message: ChatMessage) -> ChatResponse:
        """
        Process an incoming ChatMessage and determine an appropriate response.
        This method decides which type of ChatResponse to return.
        """
        # Store the incoming message in history
        self.history.append(message)

        #Query the API and chat ChatResponse
        
        if ChatResponse.is_text() :
            return ChatTextResponse("Chat history cleared.")
        elif ChatResponse.is_toolcall():
            # exectute tool
            return ChatActionRequest(command)
        else:
            # Default behavior: echo the message or provide a generic response
            # (In a real system, this is where NLP or other logic would generate a response)
            reply_text = f"Echo: {content}"
            response = ChatTextResponse(reply_text)
            # Store response in history as well
            self.history.append(response)
            return response

    def clear_history(self):
        """Clear the chat history for this session."""
        self.history.clear()
