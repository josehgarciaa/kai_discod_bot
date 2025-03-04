
from authentication import AuthenticationFacade
from models import Config, ConfigDirector, Model,Director
from prompt_manager import ChatManager, MonitoringService


if __name__ == "__main__":

    #I got everything to communicate to the API
    manager = AuthenticationFacade()
    manager.login()

    # User friendly structured model building clearly:
    model_config = ConfigDirector.default_config()
    model = Director.default_model()

    monitor = MonitoringService()
    chatbot = ChatManager(authenticator = manager, monitor = monitor)

    message = "Mi nombre es Jose, ¿Cuantas letras tiene?"
    response = chatbot.send_message(message, model_config, model)
    message = "¿Cual es mi nombre?"
    response = chatbot.send_message(message, model_config, model)
    model.set_developer_instruction("Ahora responderas solo en ingles")
    message = "Traduce toda la conversacion anterior al ingles"
    response = chatbot.send_message(message, model_config, model)
    
    
    print(response)

    
