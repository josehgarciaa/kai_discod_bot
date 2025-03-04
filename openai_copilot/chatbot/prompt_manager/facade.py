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
from authentication import AuthenticationFacade
from models import Config, Model
from prompt_api import  ChatHistory, MonitoringService


class ChatManager:
    """
    A facade for managing chat interactions, authentication, and monitoring.

    This class does not maintain stateful ModelConfig or Model objects. Instead,
    it expects them to be passed dynamically with each request, ensuring better
    flexibility and avoiding unnecessary state management.
    """

    def __init__(self, auth: AuthenticationFacade, monitoring: MonitoringService, client: Client) -> None:
        """
        Initializes the ChatManager with authentication, monitoring, and API client.

        :param auth: Handles authentication for API requests.
        :param monitoring: Manages chat monitoring and alerts.
        :param client: Handles communication with the language model API.
        """
        self.auth = auth
        self.monitoring = monitoring
        self.client = client
        self.chat_history = ChatHistory()  # Structured message storage

    def send_message(self, message: str, user_id: str, config: Config, model: Model) -> str:
        """
        Processes a user message, stores it in chat history, and retrieves a response.

        :param message: The input message from the user.
        :param user_id: Unique identifier for the user.
        :param config: The configuration settings for the model.
        :param model: The specific model instance to use for the request.
        :return: AI-generated response.
        """
        # Store user message
        self.chat_history.add_message("user", message)

        # Send request to the API using provided configuration
        api_response = self.client.send_request(config)

        # Extract AI response content
        ai_response = api_response["choices"][0]["message"]["content"]

        # Store AI response in history
        self.chat_history.add_message("assistant", ai_response)

        # Notify monitoring system
        #self.monitoring.notify(user_id, message, ai_response)

        # Generate assistant response via authenticated client
        response = self.auth.get_client().chat.completions.create(
            model=model.type,
            messages=[
                {"role": "developer", "content": config.developer},
                {"role": "user", "content": message},
            ]
        )
        # Store AI response in history
        self.chat_history.add_message("assistant", response)

        return response

    #def get_chat_history(self) -> List[dict]:
    #    """
    #    Retrieve the stored chat history in a structured format.

    #    :return: List of chat messages as dictionaries.
    #    """
    #    return self.chat_history.get_history()
