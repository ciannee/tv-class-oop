
import time
time.sleep(3)

# import TV from Television file
from Television import TV

# create object of a class
television1 = TV(30, 3, True)
television2 = TV (3, 2, True)

# print output
print("\n")
television1 = print("\033[36mtv1's channel is ", television1.channel, "and volume level is ", television1.volume_level)
television2 = print("\033[95mtv2's channel is ", television2.channel, "and volume level is ", television2.volume_level)
print ("\n")