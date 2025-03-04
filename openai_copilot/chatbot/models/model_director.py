from models import BaseModel
#from .strategies import MarkdownStrategy, PlainTextStrategy, JSONStrategy



class ModelDirector:
    def __init__(self, xx):
        self.developer="Useful"
        self.model="Useful"
        self.memory="Useful"
        self.output = None
        
    def standardConfig(basemodel):
        return basemodel

#class ModelFactory:
 #   @staticmethod
  #  def create_model(parameters, output_type="plain_text"):
        # Strategy pattern applied here explicitly
 #       strategies = {
 #           "plain_text": PlainTextStrategy(),
 #           "markdown": MarkdownStrategy(),
 #           "json": JSONStrategy(),
  #      }
        
  #      strategy = strategies[output_type]

   #     if parameters['model_name'] == "gpt-4-vision":
   #         # Assuming you have GPTVisionModel defined.
   #         return GPTOmniModel(parameters, strategy)
   #     else:
    #        return GPTReasoningModel(parameters, strategy)