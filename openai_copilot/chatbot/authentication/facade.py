from authentication import SessionManager
from typing import Optional
from openai import OpenAI
from openai import OpenAI



class AuthenticationFacade:
    def __init__(self):
        self.session_manager = SessionManager()
        self.client = None

    def login(self, api_key: Optional[str] = None):
        
        if api_key is not None:
            self.session_manager.set_api_key(api_key)
        else:
            self.session_manager.load_dotenv()
            
        if not self.session_manager.is_authenticated:
            raise ValueError("Authentication failed: Invalid API key format")
        print("Authentication successful.")
        
        if self.client is None:
            self.client = OpenAI(api_key=self.session_manager.api_key)

    def get_client(self):
        return self.client         


    def logout(self):
        self.session_manager.clear_session()
        print("Logout successful.")

    def is_logged_in(self):
        return self.session_manager.is_authenticated