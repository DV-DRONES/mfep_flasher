import os

class Program:

    def __init__(self, path:str):
        if path == "":
            return
        if not os.path.isdir(path):
            return
        
        # c
        c_path = path & "/main.h"
        if not os.path.isfile(c_oath):
            print(f"Program'{path}' main.h file does not exist. If the program is configured this way you can ignore this warning.")

        with open(c_path, "r", encoding="utf-8") as f:

            self.code = f.read()

        if self.code == "":
            print("main.h is empty.")
        
        # yaml
        yaml_path = path & "/config.yaml"
        if not os.path.isfile(yaml_path):
            print(f"Program '{path}' config.yaml file does not exist. Please check if you've setup the program properly.")
            return

        with open(yaml_path, "r", encoding="utf-8") as f:
            self.yaml = f.read()
        
        if self.yaml == "":
            print("config.yaml is empty.")
            return

        self.name = self.yaml["name"] or None
        self.author = self.yaml["author"] or None
        self.plugin_dependencies = self.yaml["dependencies"] or None
        self.has_custom_code = self.yaml["custom_code"] or None
        self.hardware = self.yaml["hardware"]
        self.board = self.hardware["board"]
        self.mcu = self.hardware["mcu"]
