# PSEUDOCODE
# CREATE A TV PROGRAM THAT WILL PRODUCE THE FOLLOWING OUTPUTS:
# 1. "tv1's channel is 30 and volume level is 3"
# 2. "tv2's channel is 3 and volume level is 2"

class TV:
    def __init__(self, brand, channel=1, volume=50):
        self.brand = brand
        self.channel = channel
        self.volume = volume
        self.is_on = False

