from abc import ABC, abstractmethod

class PromptHandler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, prompt, context):
        if self._successor:
            return self._successor.handle(prompt, context)
        return prompt, context