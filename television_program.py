# PSEUDOCODE
# CREATE A TV PROGRAM THAT WILL PRODUCE THE FOLLOWING OUTPUTS:
# 1. "tv1's channel is 30 and volume level is 3"
# 2. "tv2's channel is 3 and volume level is 2"

# CLASS CREATION
class TV:

# CLASS DEFINITIONS 
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False
    
    def turnOn(self):
        self.on = True
    
    def turnOff(self):
        self.on = False
    
    def getChannel(self):
        return self.channel
    
    def setChannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel
    
    def getVolume(self):
        return self.volume
    
    def setVolume(self, volume):
        if 1 <= volume <= 7:
            self.volume = volume
    
    def channelUp(self):
        if self.channel < 120:
            self.channel += 1
    
    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1
    
    def volumeUp(self):
        if self.volume < 7:
            self.volume += 1
    
    def volumeDown(self):
        if self.volume > 1:
            self.volume -= 1

def TestTV():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)
    
    tv2 = TV()
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)

# FOR THE PRINTING OF THE CODE AND CALLING OF VARIABLES   
    print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
    print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")

# TO TEST THE CLASS
TestTV()





