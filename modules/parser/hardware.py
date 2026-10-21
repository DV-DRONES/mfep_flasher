# in this file, classes will be defined for storing information about Boards, MCUs, Sensors and other devices!


# Microcontroller config file architecture
# name: whatever
# status: WIP/FINISHED/PLACEHOLDER
# cores:
#  coreX:
#   frequency: X Mhz
#   bits: X bits
#   priority: X
# timers:
#  TIM1:
#   Ch1:
#    bits: X

class Microcontroller:

    def __init__(self, config_file:str):
        if config_file == "":
            return

        self.yaml = yaml.load(config_file, Loader=yaml.FullLoader)
        self.cores = self.yaml["cores"] or None
        self.timers = self.yaml["timers"] or None


# Board config file architecture
# name: whatever
# status: WIP/FINISHED/PLACEHOLDER
# devices:
#  microcontrollers:
#   mcuX:
#    name: whatever
#  sensors:
#   sensorX:
#    name: whatever
#  auxillaries:
#   auxillaryX:
#    name: whatever
# connections:
#  conn1:
#   from_category: mcu
#   to_category: sensors
#   from_pin: X
#   to_pin: X


class Board:

    def __init__(self, config_file:str):
        if config_file == "":
            return

        self.yaml = yaml.load(config_file, Loader=yaml.FullLoader)
        self.devices = self.yaml["devices"]
        self.connections = self.yaml["connections"]


# Sensor config file architecture



class Sensor:

    def __init__(self, config_file:str):
        pass


# auxillary config file architecture

class Auxillary:

    def __init__(self, config_file:str):
        pass
