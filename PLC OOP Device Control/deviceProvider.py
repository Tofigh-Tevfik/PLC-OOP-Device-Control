from globalDevices import deviceState
from deviceClass import DeviceA, DeviceB, DeviceC

# Device Provider will add the devices
# on initialization it will add the configuration and pass a default state to the devices
# after initialization, it can add devices

class DeviceProvider:

    default = {
        "enable": False,
        "reset" : False,
        "hasError": False,
        "isReady" : False,
        "errorId" : None,
        "initialized": False,
    }

    # on Initialization, it will add the given configuration with a default state, all parameters set to False
    def __init__(self, eConfig, numberOfDevices):
        self.numberOfDevices = numberOfDevices
        for iteration, device in enumerate(eConfig):
            if device.upper() == "A":
                deviceState["deviceA"].append(DeviceA(self.default, iteration))
            elif device.upper() == "B":
                deviceState["deviceB"].append(DeviceB(self.default, iteration))
            elif device.upper() == "C":
                deviceState["deviceC"].append(DeviceC(self.default, iteration))

    def addDevice(self, Config, state = default):
        for iteration, device in enumerate(Config):
            if device.upper() == "A":
                deviceState["deviceA"].append(DeviceA(state, iteration + self.numberOfDevices))
            elif device.upper() == "B":
                deviceState["deviceB"].append(DeviceB(state, iteration + self.numberOfDevices))
            elif device.upper() == "C":
                deviceState["deviceC"].append(DeviceC(state, iteration + self.numberOfDevices))

