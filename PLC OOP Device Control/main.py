from process import Process
from globalDevices import deviceState


# an initial configuration
eConfig = ["a", "b", "b", "a", "c", "b"]

# initializing the process
process = Process(eConfig, len(eConfig))

# reading the props of all devices
process.readProps()

# setting commands to all devices
process.setCommands({        
        "enable": True,
        "reset" : False,
        "hasError": False,
        "isReady" : False,
        "errorId" : None,
        "initialized": True,
        })

# setting commands to device with ID 4
process.setCommands({        
        "enable": True,
        "reset" : False,
        "hasError": True,
        "isReady" : False,
        "errorId" : 444,
        "initialized": True,
        }, 4)

# adding another 3 devices
process.addDevice(["A", "B", "C"])
process.readProps()
