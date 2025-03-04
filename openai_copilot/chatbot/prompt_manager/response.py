from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class ChatMessage:
    role: str
    content: str
    logprobs: Optional[Dict] = None
    finish_reason: Optional[str] = None
    tokens_used: Optional[int] = None

@dataclass
class ChatHistory:
    messages: List[ChatMessage] = field(default_factory=list)

    def add_message(self, api_response: dict) -> None:
        """
        Parse API response and add structured message.
        """
        choice = api_response.get("choices", [{}])[0]
        message = choice.get("message", {})

        self.messages.append(ChatMessage(
            role=message.get("role"),
            content=message.get("content"),
            logprobs=choice.get("logprobs"),
            finish_reason=choice.get("finish_reason"),
            tokens_used=api_response.get("usage", {}).get("total_tokens")
        ))

    def get_chat_text(self) -> List[Dict[str, str]]:
        """
        Returns only role and content as a list of dicts (simplified history).
        """
        return [{"role": msg.role, "content": msg.content} for msg in self.messages]
