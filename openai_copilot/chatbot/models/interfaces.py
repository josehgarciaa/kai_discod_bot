

from abc import ABC, abstractmethod

# General abstract interface for models:
class OpenAIModel(ABC):
    @abstractmethod
    def generate_response(self, prompt, context):
        pass
    