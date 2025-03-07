# chat_manager.py
# -*- coding: utf-8 -*-

"""
ChatManager serves as the facade for handling chat interactions.
It processes user messages, stores conversation history using dataclasses,
and integrates authentication and monitoring services.

PEP 8 Compliance:
- Function names are lowercase with underscores.
- Uses @dataclass for structured data management.
"""

from authentication import AuthenticationService
from chat_manager import ChatUserMessage, APIResponse

class ChatManager:
    """
    A facade for managing chat interactions, authentication, and monitoring.

    This class does not maintain stateful ModelConfig or Model objects. Instead,
    it expects them to be passed dynamically with each request, ensuring better
    flexibility and avoiding unnecessary state management.
    """

    def __init__(self, authenticator: AuthenticationService) -> None:
        """
        Initializes the ChatManager with authentication, monitoring, and API client.

        :param auth: Handles authentication for API requests.
        :param monitoring: Manages chat monitoring and alerts.
        :param client: Handles communication with the language model API.
        """
        self.auth = authenticator
        #self.monitor = monitor
        #self.chat_history = ChatHistory()  # Structured message storage
        self.developer_message = ""


    def send_message(self, user_text: str) -> bool:
        """
        Processes the user's message, stores it internally, and returns a status message.

        Args:
            user_text (str): The text input from the user.

        Returns:
            trhe: is process else no
            
        """
        try:
            user_message = ChatUserMessage().handle(user_text)
            self.chat_history.append(user_message)
            return True
        except:
            print("The user message could not be processed")
            return False

    def get_response(self, chatbot) -> APIResponse:
        """
        Process an incoming ChatMessage and determine an appropriate response.
        This method decides which type of ChatResponse to return.
        """
        model_config, model = chatbot  

        #Check if more responses are necessary
        while response.call_api():
            #Determine the actions to take based on the API response
            raw_api_response =  self.auth.get_client().chat.completions.create(
                                model=model.type,
                                messages=self.chat_history.messages(),
                                tools = model.tools_list.get_all_schemas()
                                )
            #handle the response
            api_response = APIResponse().handle(raw_api_response)
            self.chat_history.append(api_response)
    
        return api_response.readable()

    def clear_history(self):
        #self.chat_history.clear_messages()        
        self.developer_message = ""
