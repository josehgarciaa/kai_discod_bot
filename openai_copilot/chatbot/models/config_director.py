from .models import GPTOmniModel, GPTReasoningModel
from .strategies import MarkdownStrategy, PlainTextStrategy, JSONStrategy

class ModelConfigDirector:

    def standardConfig(model_config_builder):
        return model_config_builder

        
