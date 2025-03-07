from dataclasses import dataclass, field
from typing import List, Optional, Dict
from openai.types.chat import ChatCompletionMessageParam


class APIResponse():
    
    def __init__(self):
        self.message = None
        self.call_api_value = True 

    def call_api(self):
        if self.call_api_value:
            self.call_api_value =False
            return True
        return False
        
        

    def handle(self, raw_api_response):
        return raw_api_response
                
        """        if raw_api_response.choices[0].message.tool_calls is not None:
                    tool_call = api_response.choices[0].message.tool_calls[0]
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    #result = model.tools_list.get_tool_by_name(function_name).call_function(function_args)
                    
                    response_list = [raw_api_response]
                    response_list.append(api_response.choices[0].message)
                                    messages.append({                               # append result message
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": str(result)
                        })
                            #self.chat_history.add_message("assistant",result)
                            #self.chat_history.add_message("user","You determine the answer from my question before, but now answer the question as before with the answer you got and not calling any function")
                            
                            # Generate assistant response via authenticated client
                            api_response = self.auth.get_client().chat.completions.create(
                                model=model.type,
                                messages=messages,#self.chat_history.get_messages(),
                                tools = model.tools_list.get_all_schemas()
                            )
                            print(api_response.choices[0].message)
                    else 
                        return raw_api_response"""
                        
        

