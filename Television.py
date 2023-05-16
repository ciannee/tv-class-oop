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


    # sets a new volume for this tv


    # increases the channel number by 1


    # decreases the channel number by 1


    # increases the volume level by 1


    # decreases the volume level by 1