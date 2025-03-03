from abc import ABC, abstractmethod

# Abstract strategy interface for different conversation styles or roles
class RoleStrategy(ABC):
    @abstractmethod
    def format_prompt(self, prompt):
        pass

# Concrete strategies clearly defined:
class CasualFriendRole(RoleStrategy):
    def format_prompt(self, prompt):
        return f"🙌 {prompt}, buddy!"

class FormalAssistantRole(RoleStrategy):
    def format_prompt(self, prompt):
        return f"📋 Assistant, please provide assistance clearly regarding: {prompt}"

class TechnicalAdvisorRole(RoleStrategy):
    def format_prompt(self, prompt):
        return f"🛠️ Technical Detail Request: {prompt}"