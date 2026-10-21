import yaml
import hardware

# config yaml architecture:
# 
class Parser:
    def __init__(self, config_yaml:str, external_files:dict[str]):
        self.config = config_yaml
        self.external_files = external_files

    
    def parse(self):
        pass
