from authentication import SessionManager


class AuthenticationFacade:
    def __init__(self):
        self.session_manager = SessionManager()

    def login(self, api_key: str):
        self.session_manager.set_api_key(api_key)
        if not self.session_manager.is_authenticated:
            raise ValueError("Authentication failed: Invalid API key format")
        print("Authentication successful.")

    def logout(self):
        self.session_manager.clear_session()
        print("Logout successful.")

    def is_logged_in(self):
        return self.session_manager.is_authenticated