from chat_manager import APIResponse
import json

class ClientAction():
    
    def __init__(self):
        self.api_messages = []

    def get_api_message(self):
        return self.api_messages
                    
    def required(self, api_response):
        return api_response.required_action()
    
    def execute(self, model, api_response):
        
        for tool_call in api_response.raw_api_response.choices[0].message.tool_calls:
            api_message = {"role": "tool", "tool_call_id": tool_call.id, "content": ""}
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            api_message["content"] = str(model.tools_list.get_tool_by_name(function_name).call_function(function_args))
            self.api_messages.append(api_message)
        return True 
        
        
    
    
    