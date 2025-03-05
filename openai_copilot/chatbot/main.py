
from authentication import AuthenticationService
from models import Config, ConfigDirector, Model,Director
from chat_manager import ChatManager, MonitoringService

if __name__ == "__main__":

    # Test it:
    def sum_two_numbers(num1: float, num2: float) -> float:
        """
        Sum two numbers.

        Args:
            number1 (float): The first number to sum.
            number2 (float): The second number to sum.

        Returns:
            float: The sum.
        """
        return 20

    # Test it:
    def translation(num1: float, num2: float) -> str:
        """
        Translate both numbers.

        Args:
            number1 (float): The first number to sum.
            number2 (float): The second number to sum.

        Returns:
            str: A string contained the written form of the numebrs.
        """
        return "ONE TOW"

    

    #I got everything to communicate to the API
    manager = AuthenticationService()
    manager.login()

    # User friendly structured model building clearly:
    model_config = ConfigDirector.default_config()
    model = Director.python_programmer()
    

    model.set_tools([translation,sum_two_numbers])

    monitor = MonitoringService()
    
    chatbot = ChatManager(authenticator = manager, monitor = monitor)

    message = "how do you get the values only of a dictionary"
    message = "in openai api have the object ChatCompletionMessage is it possible to initialize it with a user call?"
    response = chatbot.send_message(message, model_config, model)
    print(response)
