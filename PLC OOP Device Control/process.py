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

    def setCommands(self, props, index = False):
        self.deviceControl.setCommands(props, index)

    def readProps(self, index = False):
        self.deviceControl.readProps(index)

    def addDevice(self, Config):
        deviceState["deviceProvider"].addDevice(Config)