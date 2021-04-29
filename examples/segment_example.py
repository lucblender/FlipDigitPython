from FlipDigit import *
from time import sleep


# myDigit = FlipDigit('/dev/tty0') #Linux com port
myDigit = FlipDigit('COM6')

for i in range(0,8):
    myDigit.set_segments(2**i)
    sleep(0.5)
    
myDigit.close()