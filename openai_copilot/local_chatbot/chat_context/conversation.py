class ConversationManager:
    def __init__(self, role_strategy):
        self.history = []
        self.role_strategy = role_strategy

    def save_state(self):
        return ConversationMemento(self.history, self.role_strategy)

    def restore_state(self, memento):
        self.history = memento.history.copy()
        self.role_strategy = memento.role

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def generate_response(self, prompt, model):
        formatted_prompt = self.role_strategy.format_prompt(prompt)
        response = model.generate_response(formatted_prompt, context=self.history)
        self.add_message("assistant", response)
        return response