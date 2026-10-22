import os
import yaml

# config.yaml structure EXAMPLE
# name: GPASP 
# author: "Marlo3110"
# platform: ESPIDF/ARDUINO/WHATEVER
# dependencies: ["GPASP_PROTOCOL"]
# constants: [["int", "var_name1"]]
# output:
#  outputs: [[rep_name: "protocol_{}_out", cod_name: "out1", size: 100, datatype: "whatever"]] # replacment name, name in the actual plugin code, size(in objects. Will be scaled down proportionally if there is not enough RAM), datatype(from std library)
# input: # also keep in mind to add rep_name or whatever in fron of the values.
#  inputs: [["protocol_{}_in", "in1", 100, "whatever"]] # same principle as "outputs"
# queue:
#  queues: [["protocol_{}_queue", "queue1", 100, "queue_object"]] # same principle again


class Plugin:

    def __init__(self, path:str):
        if path == "":
            return
        if not os.path.isdir(path):
            return

        
        # c
        c_path = path & "/main.h"
        if not os.path.isfile(c_oath):
            print(f"Plugin '{path}' main.h file does not exist. Please check if you've setup the plugin properly.")
            return

        with open(c_path, "r", encoding="utf-8") as f:

            self.code = f.read()

        if self.code == "":
            print("main.h is empty.")
        
        # yaml
        yaml_path = path & "/config.yaml"
        if not os.path.isfile(yaml_path):
            print(f"Plugin '{path}' config.yaml file does not exist. Please check if you've setup the plugin properly.")
            return

        with open(yaml_path, "r", encoding="utf-8") as f:
            self.yaml = f.read()
        
        if self.yaml == "":
            print("config.yaml is empty.")
            return
        
        self.yaml = yaml.load(self.yaml)
        self.name = self.yaml["name"]
        self.author = self.yaml["author"]
        self.dependencies = self.yaml["dependencies"]
        self.platform = self.yaml["platform"]
        self.constants = self.yaml["constants"]
        self.outputs = self.yaml["output"]["outputs"]
        self.inputs = self.yaml["input"]["inputs"]
        self.queue = self.yaml["queue"]["queues"]
