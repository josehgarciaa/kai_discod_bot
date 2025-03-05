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

from typing import List
from authentication import AuthenticationService
from models import Config, Model
from chat_manager import  ChatHistory, MonitoringService


class ChatManager:
    """
    A facade for managing chat interactions, authentication, and monitoring.

    This class does not maintain stateful ModelConfig or Model objects. Instead,
    it expects them to be passed dynamically with each request, ensuring better
    flexibility and avoiding unnecessary state management.
    """

    def __init__(self, authenticator: AuthenticationService, monitor: MonitoringService) -> None:
        """
        Initializes the ChatManager with authentication, monitoring, and API client.

        :param auth: Handles authentication for API requests.
        :param monitoring: Manages chat monitoring and alerts.
        :param client: Handles communication with the language model API.
        """
        self.auth = authenticator
        self.monitor = monitor
        self.chat_history = ChatHistory()  # Structured message storage
        self.developer_message = ""

    def send_message(self, message: str, config: Config, model: Model, user: str = "user") -> str:
        """
        Processes a user message, stores it in chat history, and retrieves a response.

        :param message: The input message from the user.
        :param user_id: Unique identifier for the user.
        :param config: The configuration settings for the model.
        :param model: The specific model instance to use for the request.
        :return: AI-generated response.
        """
        # Store user message
        #if self.developer_message != model.developer:
        #    self.chat_history.add_message("developer", model.developer)
        #    self.developer_message = model.developer
        
        self.chat_history.add_message("user", message)
        """
                # Notify monitoring system
                #self.monitoring.notify(user_id, message, ai_response)

                # Generate assistant response via authenticated client
                api_response = self.auth.get_client().chat.completions.create(
                    model=model.type,
                    messages=self.chat_history.get_messages(),
                    tools = model.tools_list.get_all_schemas()
                )
                
                import json
                if api_response.choices[0].message.tool_calls is not None:
                    tool_call = api_response.choices[0].message.tool_calls[0]
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    result = model.tools_list.get_tool_by_name(function_name).call_function(function_args)
                    
                    messages= self.chat_history.get_messages()
                    messages.append(api_response.choices[0].message)
                    messages.append({                               # append result message
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })
                    #self.chat_history.add_message("assistant",result)
                    #self.chat_history.add_message("user","You determine the answer from my question before, but now answer the question as before with the answer you got and not calling any function")
                    
                    # Generate assistant response via authenticated client
                    api_response = self.auth.get_client().chat.completions.create(
                        model=model.type,
                        messages=messages,#self.chat_history.get_messages(),
                        tools = model.tools_list.get_all_schemas()
                    )
                    print(api_response.choices[0].message)
                """#self.chat_history.add_response(api_response.choices[0].message)
                #return self.chat_history

    def clear_history(self):
        self.chat_history.clear_messages()        
        self.developer_message = ""
