
# I made 3 classes for DeviceA, DeviceB and DeviceC
# on initialization each device has a dictionary state which looks like this
# {
#     "deviceId": ...
#     "deviceType": ...
#     "name": ...
#     "props": {
#         "enable": ...
#         "reset" : ...
#         "hasError": ...
#         "isReady" : ...
#         "errorId" : ...
#         "initialized": ...
#     }
# }


# first child class (DeviceA)
class DeviceA():
    def __init__(self, dictionary, index):
        self.state = {
            "deviceId": index,
            "deviceType": "A",
            "name": "A" + str(index),
            "props": dictionary
        }

# second child class (DeviceB)
class DeviceB():
    def __init__(self, dictionary, index):
        self.state = {
            "deviceId": index,
            "deviceType": "B",
            "name": "B" + str(index),
            "props": dictionary
        }

# third child class (DeviceC)
class DeviceC():
    def __init__(self, dictionary, index):
        self.state = {
            "deviceId": index,
            "deviceType": "C",
            "name": "C" + str(index),
            "props": dictionary
        }
        
