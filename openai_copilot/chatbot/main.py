
from authentication import AuthenticationService
from models import Config, ConfigDirector, Model,Director
from chat_manager import ChatManager
from helpers import read_project, write_project
if __name__ == "__main__":

        # Test it:
    import os
    import datetime

    import os

    

    #I got everything to communicate to the API
    manager = AuthenticationService()
    manager.login()

    # User friendly structured model building clearly:
    model_config = ConfigDirector.default_config() #default_config
    model = Director.python_programmer()
    model.set_model_type("gpt-4o")
    


    project_content = read_project(".")

    project_content = write_project("projects/")

#    model.set_tools([translation, write_documents])
    
    manager = ChatManager(authenticator = manager)

   

  #  message = "can you create a file called tes_ai_function.md? with the word dog inside"
  #  if manager.send_message(message):
  #      chatbot = [model_config, model]
  #      response = manager.get_response(chatbot) 
  #      print(response)
  #  else:
  #      print("Problems processing data")   
        
