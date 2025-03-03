from abc import ABC, abstractmethod

class OutputFormattingStrategy(ABC):
    @abstractmethod
    def format(self, response_content: str):
        pass
    
import json

class PlainTextStrategy(OutputFormattingStrategy):
    def format(self, response_content: str):
        return response_content.strip()

class MarkdownStrategy(OutputFormattingStrategy):
    def format(self, response_content: str):
        # Return Markdown formatted response
        return response_content

class JsonStrategy(OutputFormattingStrategy):
    def format(self, response_content: str):
        try:
            # Attempt to convert from model output (which might be text) into dict
            return json.loads(response_content)
        except json.JSONDecodeError:
            raise ValueError("Response content is not valid JSON")