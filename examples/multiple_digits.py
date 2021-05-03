from flipdigit import *
from time import sleep

# myDigit = FlipDigit('/dev/tty0') #Linux com port
myDigit1 = FlipDigit('COM6',SerialSpeed.S_115200,0x01)
myDigit2 = FlipDigit('COM6',SerialSpeed.S_115200,0x02)

#---------------------------------------------------------
#
# The FlipDigit class use a static serial port attribute! 
# The first baudrate and serial port configurated will be taken in account and not the others!!
#
#---------------------------------------------------------
for i in range(0,10):
    myDigit1.set_number(i)
    myDigit2.set_number((i+1)%10)
    sleep(0.5)
    
myDigit1.close()

#---------------------------------------------------------
#
# When you close one digit serial port, all will be closed since it's a static attribute
#
#---------------------------------------------------------