from process import Process
from globalDevices import deviceState


# an initial configuration
eConfig = ["a", "b", "b", "a", "c", "b"]

# initializing the process
process = Process(eConfig, len(eConfig))

process.readProps()

process.setCommands({        
        "enable": True,
        "reset" : False,
        "hasError": False,
        "isReady" : False,
        "errorId" : None,
        "initialized": True,
        })

process.setCommands({        
        "enable": True,
        "reset" : False,
        "hasError": True,
        "isReady" : False,
        "errorId" : 444,
        "initialized": True,
        }, 4)

process.addDevice(["A", "B", "C"])
process.readProps()
