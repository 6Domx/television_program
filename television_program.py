# PSEUDOCODE
# CREATE A TV PROGRAM THAT WILL PRODUCE THE FOLLOWING OUTPUTS:
# 1. "tv1's channel is 30 and volume level is 3"
# 2. "tv2's channel is 3 and volume level is 2"


class TV:
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







