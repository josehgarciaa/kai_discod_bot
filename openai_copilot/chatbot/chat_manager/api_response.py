from dataclasses import dataclass, field
from typing import List, Optional, Dict
from openai.types.chat import ChatCompletionMessageParam
import json

class APIResponse():
    
    def __init__(self):
        self.message = None
        self.call_api_value = True 
        self.processed_content = None
        self.raw_api_response = None
        self.call_tool_value = False 

    def call_api(self):
        return self.call_api_value

    def get_api_message(self):
        return self.raw_api_response.choices[0].message       
        
    def readable(self):
        message = self.raw_api_response.choices[0].message
        self.processed_content = "role: "+message.role+"\n"+message.content
        return self.processed_content

    def required_action(self):
        return self.call_tool_value
             
     
    def handle(self, raw_api_response):
        self.raw_api_response = raw_api_response
        
        if self.raw_api_response.choices[0].message.tool_calls is not None:
            self.call_tool_value = True                
            self.call_api_value =True
            return raw_api_response                                    

                            #self.chat_history.add_message("assistant",result)
                            #self.chat_history.add_message("user","You determine the answer from my question before, but now answer the question as before with the answer you got and not calling any function")


        self.call_tool_value = False                
        self.call_api_value =False
        self.raw_api_response = raw_api_response        
        return self
                

