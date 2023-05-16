# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 6: UML Class Diagram

# Pseudocode:

# create TV class
class TV:
    def __init__(self, channel, volume_level, switch):

    # behavior (instance methods)
    self.channel = channel
    self.volume_level = volume_level
    self.switch = switch

    # turns on this tv
    def turnOn(self):
        self.switch = True

    # turns off this tv
    def turnOff(self):
        self.switch = False

    # returns the channel for this tv
    def getChannel(self):
        return self.channel

    # sets a new channel for this tv
    def setChannel(self):
        if self.channel >= 1:
            self.channel = channel
        elif self.channel <= 120:
            self.channel = channel

    # gets the volume level for this tv
    def getVolume(self):
        return self.volume_level

    # sets a new volume for this tv
    def setVolume(self):
        if self.volume_level >= 1:
            self.volume_level = self.volume_level
        elif self.volume_level <= 1:
            self.volume_level = self.volume_level

    # increases the channel number by 1
    def channelUp(self):
        if self.channel > 120:
            self.channel += 1

    # decreases the channel number by 1
    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1

    # increases the volume level by 1
    def volumeUp(self):
        if self.volume_level < 7:
            self.volume_level += 1

    # decreases the volume level by 1
    def volumeDown(self):
        if self.volume_level > 1:
            self.volume -= 1