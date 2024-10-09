import spacy
import re

class Mask:
    def __init__(self) -> None:
        self.patterns = {
            'phone': r'(?:\+\d{1,3}[-\s]?)?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'ipv6': r'\b(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\b',
            'ipv4': r'\b((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}\b'
        }

    def mask_text(self,text:str) -> str:

        for category,pattern in self.patterns.items():
            text = re.sub(pattern, f'[REDACTED {category.upper()}]', text)

        text = self.mask_nlp(text)

        return text
    
    def mask_nlp(self,text:str) -> str:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)

        for ent in doc.ents:
            print(f'Label: {ent.label_}: Value: {ent.text}')
            text = re.sub(ent.text,f'[REDACTED {ent.label_}]',text)
        return text
    
    def mask_file(self,file_name:str) -> str:
        print('File Name: ' + file_name)
        with open(file_name,'r') as file:
            file_text = file.read()
        return self.mask_text(file_text)