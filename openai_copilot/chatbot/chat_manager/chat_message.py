from dataclasses import dataclass, field
from typing import List, Optional, Dict
from openai.types.chat import ChatCompletionMessage

class ChatMessage():
    
    def __init__(self):
        self.message = None

    def user(self, external_message):
        self.message =  ChatCompletionMessage( role="user", content="external_message")

    def developer(self, external_message):
        self.message =  ChatCompletionMessage( role="developer", content="external_message")

    def assistant(self, external_message):
        self.message =  ChatCompletionMessage( external_message )
        
    
        
    

