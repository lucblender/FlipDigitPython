from flipdigit import *
from time import sleep

# myDigit = flipdigit.FlipDigit('/dev/tty0') #Linux com port
myDigit1 = flipdigit.FlipDigit('COM6',SerialSpeed.S_115200,0x01)
myDigit2 = flipdigit.FlipDigit('COM6',SerialSpeed.S_115200,0x02)

mySyncDigits = SyncMultipleFlipDigits([myDigit1, myDigit2])

#---------------------------------------------------------
#
# The FlipDigit class use a static serial port attribute! 
# The first baudrate and serial port configurated will be taken in account and not the others!!
#
#---------------------------------------------------------
for i in range(0,10):
    myDigit1.set_number(i)
    myDigit2.set_number((i+1)%10)
    mySyncDigits.sync_refresh()
    sleep(0.5)
    
myDigit1.close()

#---------------------------------------------------------
#
# When you close one digit serial port, all will be closed since it's a static attribute
#
#---------------------------------------------------------