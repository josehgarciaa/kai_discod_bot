
handler_chain = ContextLengthHandler(
    max_length=4000,
    successor=FormatHandler()
)

class ContextLengthHandler(PromptHandler):
    def __init__(self, max_length, successor=None):
        super().__init__(successor)
        self.max_length = max_length

    def handle(self, prompt, context):
        # Simplified length check/reduction logic
        total_content = ''.join([msg['content'] for msg in context]) + prompt
        if len(total_content) > self.max_length:
            print("Truncating context due to max length")
            context = context[-3:]  # keep last 3 messages for example
        return super().handle(prompt, context)

class FormatHandler(PromptHandler):
    def handle(self, prompt, context):
        # Ensure prompt is correctly formatted (adding possible system prompt)
        prompt = prompt.strip()
        return super().handle(prompt, context)