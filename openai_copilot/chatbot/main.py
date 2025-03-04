
from authentication import AuthenticationFacade
from models import ModelConfigBuilder,ModelConfigDirector, BaseModel,ModelDirector


def main():
    """
    Entry point for starting a chat session.
    Optionally, admin instructions can be passed as a command-line argument.
    """
    #admin_instructions = None
    #if len(sys.argv) > 1:
    #    admin_instructions = sys.argv[1]

    #chatbot = ChatBot(admin_instructions=admin_instructions)
    #chatbot.start_chat()

if __name__ == "__main__":

    #I got everything to communicate to the API
    manager = AuthenticationFacade()
    #manager.login()
#    client = manager.get_client()

    # User friendly structured model building clearly:
    model_config = ModelConfigDirector(ModelConfigBuilder()).standardConfig()
    model = ModelDirector(BaseModel()).standardConfig()


    # Client engaging clearly with created model:
    #conversation_history = []
    #response = model.generate_response("Explain strategy pattern clearly", conversation_history)
    #print(response)

    #print( manager.is_logged_in())
    
    
