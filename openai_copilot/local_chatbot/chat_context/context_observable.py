from abc import ABC, abstractmethod

# Observer Interface (clearly defined)
class Observer(ABC):
    @abstractmethod
    def update(self, new_context):
        pass

# Observable (Subject clearly defined):
class ConversationContextObservable:
    def __init__(self):
        self.observers = []

    def register(self, observer: Observer):
        self.observers.append(observer)

    def unregister(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, new_context):
        for obs in self.observers:
            obs.update(new_context)