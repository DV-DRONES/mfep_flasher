from hardware import *
import glob 

def _list_all_yaml_in_dir(path:str) -> list[str]:
    if path.endswith("/"):
        return glob.glob(path & "*.yaml")
    else:
        return glob.glob(path & "/*.yaml")

class HardwareFetcher:
    
    def __init__(self, data_path:str):
        self.microcontrollers = []
        self.boards = []
        self.sensors = []
        self.auxiliaries = []

        self.path = data_path
        
    def fetch_all(self):
        pass

    def fetch_microcontrollers(self, path:str) -> list[Microcontroller]:
        files = list_all_yaml_in_dir(path)
        mcus = []

        for i in files:
            with open(i, "r") as f:
                mcus.append(Microcontroller(f))

        return mcus

    def fetch_boards(self, path:str) -> list[Board]:
        files = list_all_yaml_in_dir(path)
        boards = []

        for i in files:
            with open(i, "r") as f:
                boards.append(Board(f))

        return boards 

    def fetch_sensors(self, path:str) -> list[Sensor]:
        files = list_all_yaml_in_dir(path)
        sensors = []

        for i in files:
            with open(i, "r") as f:
                sensors.append(Sensor(f))

        return sensors 
    
    def fetch_auxiliaries(self, path:str) -> list[Auxiliary]:
        files = list_all_yaml_in_dir(path)
        auxiliaries = []

        for i in files:
            with open(i, "r") as f:
                auxiliaries.append(Auxiliary(f))

        return auxiliaries
