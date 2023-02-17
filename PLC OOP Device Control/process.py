from deviceControl import DeviceControl
from globalDevices import deviceState
from deviceProvider import DeviceProvider


# I made a class called process. On initialization it adds a deviceProvider object
# to the globalState, which will add the configuration
# It has methods for setting and reading props commands to devices, to one or all of them, by a deviceController object
# It has another method for adding devices.
class Process:
    initialize = bool()

    def __init__(self, eConfig, numberOfDevices):
        deviceState["deviceProvider"] = DeviceProvider(eConfig, numberOfDevices)
        self.deviceControl = DeviceControl()

    # When index is set to False it will set the commands for every Device
    # It calls a method from deviceControl object that sets the props for devices
    # the command must be a dictionary with this structure
    # {
    #      "enable": ...
    #       "reset" : ...
    #       "hasError": ...
    #       "isReady" : ...
    #       "errorId" : ...
    #       "initialized": ...
    # }
    def setCommands(self, props, index = False):
        self.deviceControl.setCommands(props, index)

    # Again when index is set to false it will print out the props of all devices
    # it calls a method from deviceControl object
    def readProps(self, index = False):
        self.deviceControl.readProps(index)
    # adds devices by a given configuration
    # Config is a list of strings with device names like ["A", "B", "C"]
    def addDevice(self, Config):
        deviceState["deviceProvider"].addDevice(Config)
