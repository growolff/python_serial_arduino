# -*- coding: utf-8 -*

import serial
import struct
from array import array
from io import BytesIO

class machineCmd(object):

    # define the structure of the data, little-endian
    # h is for 2 byte intenger, see the full list here https://docs.python.org/3/library/struct.html#format-characters
    # add as many data types as you want to send to arduino
    _struct = struct.Struct('<hhhh')

    def __init__(self):
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        self.d4 = 0

    def serialize(self, buff):
        #try
        buff.write(self._struct.pack(self.d1, self.d2, self.d3, self.d4))
        #except struct.error as se:
        #    raise SerializationError('Error in serialization %s' % (self.__str__))

    def to_hex(self, data):
        return ":".join("{:02x}".format(c) for c in data)


if __name__ == '__main__':

    port = input("arduino serial port: ")
    arduino = serial.Serial(port, 9600)
    cmd = machineCmd()
    buff = BytesIO()

    while True:
        cmd.d1 = int(input("input 1: "))
        cmd.d2 = int(input("input 2: "))
        cmd.d3 = int(input("input 3: "))
        cmd.d4 = int(input("input 4: "))
        print('sending to arduino...')
        cmd.serialize(buff)
        base_cmd = bytearray(buff.getvalue())

        # send bytes to arduino
        if arduino.write(base_cmd):
            print('OK')
        else:
            print('fail')
