

class LinearUnitController:
    def __init__(self, start = False, k1 = False, v1 = False):
        self.start = bool(start) # start button
        self.k1 = bool(k1) # proximity sensor
        self.v1 = bool(v1) # linear unit

    def Update(self, start, k1):

        self.start = start
        self.k1 = k1

        if self.k1: # when the sensor is triggered
            self.v1 = False

        elif self.start: # when the sensor is not tirggered and button is pressed
            # I will reverse the output
            # waiting for button release with a while loop
            while self.start:
                pass

            self.v1 = not self.v1


import time


class SpeedupTimer:


    def __init__(self, speedfactor = 1, enable = False, speedup = False):
        # gave the inputs a default value just in case
        self.enable = enable
        self.speedup = speedup
        self.speedfactor = speedfactor
        self.q = False # output
    
    def Update(self, enable, speedup):

        self.enable = enable
        self.speedup = speedup
        
        while self.enable and not self.speedup:
            self.q = True
            print("situation 2, q is on")
            time.sleep(10) # q is turned on for 10 seconds
            self.q = False
            print("situation 2, q is off")
            time.sleep(1) # q is turned off for 1 second

        while self.enable and self.speedup:
            self.q = True
            print("situation 3, q is on")
            time.sleep(10 / self.speedfactor) # turned of for 10/speedfactor seconds
            self.q = False
            print("situation 3, q is off")
            time.sleep(1)

        else:
            print(1)
            self.q = False






class MovingAverage:

    samples = list()

    def __init__(self, sampleCount):
        self.sampleCount = sampleCount
    
    def Update(self, x): # x is the input

        # in case, input is not a real number
        try:
            self.samples.append(float(x))
        except:
            pass

        if len(self.samples) > self.sampleCount:
            self.samples.pop(0) # in case the size of the list
            # exceeds the sample Count, I will pop out the first element

    def avg(self):
        # I will add the samples and divide them by sample count if 
        # sample count is greater than 0, else i will return 0
        return sum(self.samples) / self.sampleCount if self.sampleCount > 0 else 0


