--------------------------------------------------------------------------------
# message_factory.py
--------------------------------------------------------------------------------
class MessageFactory:
    """
    Factory class that creates the appropriate Message subclass
    based on the 'type' field in the raw response data.
    """
    @staticmethod
    def create_message(response_data):
        msg_type = response_data.get("type")

        if msg_type == "text":
            return TextMessage(content=response_data["content"])

        elif msg_type == "function_call":
            return FunctionCallMessage(
                content=response_data.get("content", ""),
                function_name=response_data["function_name"],
                args=response_data.get("args", [])
            )

        elif msg_type == "data_structure":
            return DataStructureMessage(content=response_data["content"])

        else:
            raise ValueError(f"Unknown message type: {msg_type}")
