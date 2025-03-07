from dataclasses import dataclass, field
from typing import List, Optional, Dict
from openai.types.chat import ChatCompletionMessageParam


class APIAction():
    
    def __init__(self):
        self.message = None

    def message(self, external_message):
        self.message =  ChatCompletionMessageParam( external_message)