from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class ChatMessage:
    role: str
    content: str

@dataclass
class ChatHistory:
    messages: List[ChatMessage] = field(default_factory=list)



    def add_message(self, user, message: dict) -> None:
        """
        Parse API response and add structured message.
        """
        self.messages.append(ChatMessage(
            role=user,
            content=message,
        ))
        
    def add_response(self, api_response_message: dict) -> None:
        """
        Parse API response and add structured message.
        """
        self.messages.append(ChatMessage(
            role=api_response_message.role,
            content=api_response_message.content,
        ))


    def get_last_message(self) -> List[Dict[str, str]]:
        """
        Returns only role and content as a list of dicts (simplified history).
        """
        return self.messages[-1].content
        
    def get_messages(self) -> List[Dict[str, str]]:
        """
        Returns only role and content as a list of dicts (simplified history).
        """
        return [{"role": msg.role, "content": msg.content} for msg in self.messages]

    def clear_messages(self) -> List[Dict[str, str]]:
        """
        Returns only role and content as a list of dicts (simplified history).
        """
        self.messages= []


    def __repr__(self) -> str:
        """
        Provide a concise string representation of the model configuration.
        """
        full_chat = ""
        for msg in self.messages:
            full_chat+="_role: "+msg.role+"\n"
            full_chat+=msg.content+"\n"
        return full_chat