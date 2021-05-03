from flipdigit import *
from time import sleep

#---------------------------------------------------------
#
# We start with basic config: addr = 0xff and speed 9600 
#
#---------------------------------------------------------


# myDigit = flipdigit.FlipDigit('/dev/tty0') #Linux com port
myDigit = flipdigit.FlipDigit('COM6')

myDigit.set_serial_speed(SerialSpeed.S_115200)
myDigit.set_address(0x01)

for i in range(0,10):
    myDigit.set_number(i)
    sleep(0.5)
    
myDigit.close()


#---------------------------------------------------------
#
# Config is now: addr = 0x01 and speed 115200
# 
# You should use now:
# myDigit = FlipDigit('COM6',SerialSpeed.S_115200,0x01)
#
#---------------------------------------------------------

