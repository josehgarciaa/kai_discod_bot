class OpenAIFacade:
    def __init__(self, auth_facade):
        self.auth_facade = auth_facade

    def send_prompt(self, model, prompt_messages, temperature=0.7):
        if not self.auth_facade.is_logged_in():
            raise PermissionError("User not authenticated. Please log in.")

        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=prompt_messages,
                temperature=temperature
            )
            return response
        except openai.error.RateLimitError:
            print("Rate limit reached! Try back later.")
        except openai.error.OpenAIError as e:
            print(f"API Error: {e}")