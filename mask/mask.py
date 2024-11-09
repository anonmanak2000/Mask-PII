import spacy
import re
from typing import Union
import json

class Mask:
    __patterns = {
            'phone': r'(?:\+\d{1,3}[-\s]?)?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'ipv6': r'\b(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\b',
            'ipv4': r'\b((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}\b'
    }

    def mask_text(self,text:str) -> str:
        for category,pattern in self.__patterns.items():
            text = re.sub(pattern, f'[MASKED {category.upper()}]', text)

        text = self.mask_nlp(text)

        return text
    
    def mask_nlp(self,text:str) -> str:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)

        for ent in doc.ents:
            # print(f'Label: {ent.label_}: Value: {ent.text}')
            text = re.sub(ent.text,f'[MASKED {ent.label_}]',text)
        return text
    
    def mask_dict(self, input_data: dict) -> dict:
        for key,value in input_data.items():
           
           if isinstance(value,dict):
               input_data[key] = self.mask_dict(value)
           elif isinstance(value,list):
               input_data[key] = [self.mask_dict(sub_val) if isinstance(sub_val,dict) else sub_val for sub_val in value]
           elif isinstance(value,str):
               input_data[key] = self.mask_text(value) 
        return input_data
    
    def mask(self, input_data: Union[str,dict], format: str = "txt") -> Union[str,dict]:
        if format == "txt":
            masked_data = self.mask_text(input_data)
        elif format == "json":
            masked_data = json.loads(input_data)
            masked_data = json.dumps(self.mask_dict(masked_data),separators=(",",":"))
        return masked_data