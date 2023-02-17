from globalDevices import deviceState

# DeviceControl class is used to set commands to the devices
# or read their properties


class DeviceControl:
    # a method to set command to the devices, when index is set to False,
    # it will send the commands to every device,
    # but when index is specified by an int, it will send the the commands to that index
    # the prop should have the same dictionary structure as of the current prop dictionary of the devices
    def setCommands(self, newProps, index = False):
        if not index and type(index) == bool:
            for deviceType in deviceState:
                if deviceType != "deviceProvider":
                    for device in deviceState[deviceType]:
                        device.state["props"] = newProps
        
        else:
            for deviceType in deviceState:
                if deviceType != "deviceProvider":
                    for device in deviceState[deviceType]:
                        if device.state["deviceId"] == index:
                            device.state["props"] = newProps

    # a method to read the props of devices
    # again when index if false, it will print all devices state
    # but when index is specified by an int, it will print the state of that index
    # currently has a bug :(
    def readProps(self, index = False):
        if not index and type(index) == bool:
            for deviceType in deviceState:
                if deviceType != "deviceProvider":
                    for device in deviceState[deviceType]:
                        print(device.state)
        else:
            for deviceType in deviceState:
                if deviceType != "deviceProvider":
                    for device in deviceState[deviceType]:
                        if device.state["deviceId"] == index:
                            print(device.state)

