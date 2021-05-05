![licence](https://img.shields.io/pypi/l/flipdigit?color=brightgreen)![latest version](https://img.shields.io/pypi/v/flipdigit?color=brightgreen)
# FlipDigitPython

## Description

This library has for goal to control the [Small 7-segment displays](https://flipdots.com/en/products-services/small-7-segment-displays/) by alfazeta.

## Install

The module is available on pip:
```
pip install flipdigit
```

## Requirement

If you install the library with pip, the required parckage are installed automatically. If you use the library from sources, the only library needed for this to work is pyserial. Basic installation can be made like so:

```pip3 install pyserial```

or by using the provided requirments.txt file:

```pip3 install -r requirments.txt```

## How to use

### Simple digit

You can simply declare a FlipDigit like so:

```python
from flipdigit import *

# myDigit = FlipDigit('/dev/tty0') 	# Linux com port
myDigit = FlipDigit('COM6') 		# Windows com port
``` 

This use the default configuration of a digit: 9600 baud with adress set as 0xFF.

Then you can either send the data code to enable or not a segment following the pattern shown there:

<img src="https://raw.githubusercontent.com/lucblender/FlipDigitPython/master/examples/7-segments.png" height="100">

The code is then going from _a_ for the lsb to _g_ for the msb

As example, a 0 is 0b111111 or 0x3F:

```python
myDigit.set_segments(0x3F)
``` 

or  you can directly send the number you want like so:

```python
myDigit.set_number(0)
``` 

Examples:
- [segment_example.py](https://github.com/lucblender/FlipDigitPython/blob/master/examples/segment_example.py)
- [number_example.py](https://github.com/lucblender/FlipDigitPython/blob/master/examples/number_example.py)

### Configuration

You can easily change the configuration of a digit like so:

```python
myDigit = FlipDigit('COM6')	#we use a digit with default configuration

myDigit.set_serial_speed(SerialSpeed.S_115200)
myDigit.set_address(0x01)
``` 

The digit has now the address '1' and the baudrate is set to 115200 bauds.

Now the digit need to be used like so:

```python
myDigit1 = FlipDigit('COM6',SerialSpeed.S_115200,0x01)
``` 

Examples:
- [config_example.py](https://github.com/lucblender/FlipDigitPython/blob/master/examples/config_example.py)

### Multiple digit

You can easily use multiple digit since they share a static serial attribute. Be careful, only the first digit serial configuration will be taken in account!

```python
myDigit1 = FlipDigit('COM6',SerialSpeed.S_115200,0x01)
myDigit2 = FlipDigit('COM6',SerialSpeed.S_115200,0x02)

myDigit1.set_number(1)
myDigit2.set_number(2)
```

Examples:
- [multiple_digits.py](https://github.com/lucblender/FlipDigitPython/blob/master/examples/multiple_digits.py)

### Multiple digit in sync

In the previous example, the set_number is not made in sync. It is possible to send the set_number or set_segments and then have all the digit refreshed at the same time using the SyncMultipleFlipDigits object like so: 

```python
myDigit1 = FlipDigit('COM6',SerialSpeed.S_115200,0x01)
myDigit2 = FlipDigit('COM6',SerialSpeed.S_115200,0x02)

mySyncDigits = SyncMultipleFlipDigits([myDigit1, myDigit2])
# now that the digits are part of a SyncMultipleFlipDigits, they won't be refreshed automatically


myDigit1.set_number(i)	 		
sleep(1)
myDigit2.set_number((i+1)%10)
sleep(1)

mySyncDigits.sync_refresh() # myDigit1 and myDigit2 are refreshed only here!

```

Examples:
- [multiple_sync_digits.py](https://github.com/lucblender/FlipDigitPython/blob/master/examples/multiple_sync_digits.py)


## License

Under MIT license. Please see [License File](https://github.com/lucblender/FlipDigitPython/blob/master/LICENSE) for more information.