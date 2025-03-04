
from authentication import AuthenticationFacade
from models import Config, ConfigDirector, Model,Director
from prompt_manager import ConversationManager

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
    model_config = ConfigDirector.default_config()
    model = Director.default_model()

    chat = Chat(model, model_config)

    #reponse = chat.prompt("cosas para el prompt")
    #history = chat.get_history()

    
