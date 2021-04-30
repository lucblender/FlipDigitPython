import serial
import array
from time import sleep
from enum import Enum

number_segments = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]

serial_speed_int = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]

class SerialSpeed(Enum):
    S_1200      = 0x00
    S_2400      = 0x01
    S_4800      = 0x02
    S_9600      = 0x03
    S_19200     = 0x04
    S_38400     = 0x05
    S_57600     = 0x06
    S_115200    = 0x07
    
class SyncMultipleFlipDigits:
    
    def __init__(self, digits):
        self.__digits = digits
        
        for digit in self.__digits:
            digit._FlipDigit__set_in_sync()
        
    def sync_refresh(self):
        data = array.array('B', [0x80, 0x82, 0x8f]).tobytes()
        FlipDigit._FlipDigit__ser .write(data)
        
        
    
class FlipDigit:
    
    __ser = None

    def __init__(self, port, speed=SerialSpeed.S_9600, addr=255):
        self.__port = port
        self.__speed = speed
        self.__addr = addr
        self.__sync = False
        self.open_serial()
        
    def __set_in_sync(self):        
        self.__sync = True
        
    def open_serial(self):    
        if type(self).__ser == None or type(self).__ser.is_open == False:
            type(self).__ser = serial.Serial(self.__port, serial_speed_int[self.__speed.value]) 
        
    def close(self):
        if type(self).__ser != None and type(self).__ser.is_open == True:
            type(self).__ser.close()   

    def set_segments(self, segment_code):
        if self.__sync:
            cmd = 0x8A
        else:
            cmd = 0x89
        data = array.array('B', [0x80, cmd, self.__addr , segment_code, 0x8f]).tobytes()
        self.__ser.write(data)
        
    def set_number(self, number):
        if number > 9 or number < 0:
            return
        self.set_segments(number_segments[number])
        
    def set_serial_speed(self, speed):        
        data = array.array('B', [0x80, 0x8B, self.__addr , speed.value, 0x8f]).tobytes()
        self.__ser.write(data)
        self.__speed = speed
        self.close()
        self.open_serial()
        
    def set_address(self, addr): 
        if addr >= 0xFF  or addr < 0x00:
            return    
        data = array.array('B', [0x80, 0x8C, self.__addr , addr, 0x8f]).tobytes()        
        self.__addr = addr   
        self.__ser.write(data)
