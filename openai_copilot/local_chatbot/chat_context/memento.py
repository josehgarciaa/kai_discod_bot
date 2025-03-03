# The Memento (easy-to-store conversation state)
class ConversationMemento:
    def __init__(self, history, role):
        self.history = history.copy()  # conversation history
        self.role = role              # current conversational role and style