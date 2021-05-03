from flipdigit import *
from time import sleep


# myDigit = flipdigit.FlipDigit('/dev/tty0') #Linux com port
myDigit = flipdigit.FlipDigit('COM6')

for i in range(0,8):
    myDigit.set_segments(2**i)
    sleep(0.5)
    
myDigit.close()