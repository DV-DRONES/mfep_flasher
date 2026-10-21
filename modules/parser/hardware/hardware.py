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

        self.yaml = yaml.load(config_file, Loader=yaml.FullLoader) or None
        self.cores = self.yaml["cores"] or None
        self.timers = self.yaml["timers"] or None
        self.adcs = self.yaml["adcs"] or None
        self.dacs = self.yaml["dacs"] or None
        self.protocols = self.yaml["protocols"] or None
        self.rom = self.yaml["rom"] or None
        self.ram = self.yaml["ram"] or None


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
#  auxiliaries:
#   auxiliaryX:
#    name: whatever
# connections:
#  connX:
#   from_category: mcu
#   to_category: sensors
#   from_pin: X
#   to_pin: X
# inputs: ["in1"]
# outputs: ["out1"]

class Board:

    def __init__(self, config_file:str):
        if config_file == "":
            return

        self.yaml = yaml.load(config_file, Loader=yaml.FullLoader) or None
        self.devices = self.yaml["devices"] or None
        self.connections = self.yaml["connections"] or None
        self.inputs = self.yaml["inputs"] or None
        self.outputs = self.yaml["outputs"] or None


# Sensor config file architecture
# name: whatever
# status: WIP/FINISHED/PLACEHOLDER
# type: AIR+HUMIDITY/LIGHT/IMU
# protocols: []

class Sensor:

    def __init__(self, config_file:str):
        if config_file == "":
            return

        self.yaml = yaml.load(config_file, Loader=yaml.FullLoader) or None
        self.name = self.yaml["name"] or None
        self.status = self.yaml["status"] or None
        self.type = self.yaml["type"] or None
        self.protocols = self.yaml["protocols"] or None

# auxiliary config file architecture
# name: whatever
# status: WIP/FINISHED/PLACEHOLDER
# type: LED/Mosfet/LED-drivers/motor-driver/switches/potentiometer
# protocols: []
# 

class Auxiliary:

    def __init__(self, config_file:str):
        if config_file == "":
            return

        self.yaml = yaml.load(config_file, Loader=yaml.FullLoader) or None
        self.name = self.yaml["name"] or None
        self.status = self.yaml["status"] or None
        self.type = self.yaml["type"] or None
        self.inputs = self.yaml["inputs"] or None
        self.protocols = self.yaml["protocols"] or None







