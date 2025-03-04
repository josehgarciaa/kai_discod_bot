import os
from dotenv import load_dotenv

class SessionManager:
    __instance = None
    
    def __new__(cls):
        if SessionManager.__instance is None:
            SessionManager.__instance = object.__new__(cls)
            SessionManager.__instance.api_key = None
            SessionManager.__instance.is_authenticated = False
        return SessionManager.__instance

    def set_api_key(self, api_key:str):
        self.api_key = api_key
        self.is_authenticated = self.validate_api_key(api_key)

    def load_dotenv(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.is_authenticated = self.validate_api_key(self.api_key)
        
    def validate_api_key(self, api_key:str)->bool:
        # Add actual validation logic, possibly checking on OpenAI's side.
        # For demonstration, we check basic provisions:
        return api_key.startswith("sk-") and len(api_key) > 20

    def clear_session(self):
        self.api_key = None
        self.is_authenticated = False