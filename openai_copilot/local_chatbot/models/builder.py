class ModelBuilder:
    def __init__(self):
        self.parameters = {}
        
    def set_model_name(self, model_name):
        self.parameters["model_name"] = model_name
        return self
        
    def enable_structured_output(self, structured: bool):
        self.parameters["structured"] = structured
        return self
    
    def set_temperature(self, temp: float):
        self.parameters["temperature"] = temp
        return self
    
    def allow_internet_access(self, allow: bool):
        self.parameters["internet_allowed"] = allow
        return self
    
    def build(self):
        if "vision" in self.parameters["model_name"]:
            return GPTVisionModel(self.parameters)
        else:
            return GPTTextModel(self.parameters)