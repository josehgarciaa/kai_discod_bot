
# A Concrete Model: Text-based GPT model
class GPTTextModel(OpenAIModel):
    def __init__(self, parameters):
        self.parameters = parameters
    
    def generate_response(self, prompt, context):
        # Simplified example
        return openai.ChatCompletion.create(
                model=self.parameters["model_name"],
                messages=context + [{"role": "user", "content": prompt}],
                temperature=self.parameters["temperature"]
        )
        
# Another Concrete Model: Vision-enabled Model
class GPTVisionModel(OpenAIModel):
    def __init__(self, parameters):
        self.parameters = parameters
    
    def generate_response(self, prompt, context, images):
        # Imaginary example (simplified!)
        return openai.ChatCompletion.create(
                model=self.parameters["model_name"],
                messages=context + [{"role": "user", "content": prompt, "images": images}],
                temperature=self.parameters["temperature"]
        )