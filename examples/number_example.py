from flipdigit import *
from time import sleep


# myDigit = FlipDigit('/dev/tty0') #Linux com port
myDigit = FlipDigit('COM6')

for i in range(0,10):
    myDigit.set_number(i)
    sleep(0.5)
    
myDigit.close()