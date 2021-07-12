# -*- coding: utf-8 -*

import struct

class MachineCmd(object):
    """
        define the structure of the data, little-endian
        h is for 2 byte integer, see the full list here https://docs.python.org/3/library/struct.html#format-characters
        add as many data types as you want to send to arduino
    """

    def __init__(self):
        self.cmd_struct = struct.Struct('<hhhhh')
        self.packet = ''
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        self.d4 = 0
        self.d5 = 0

    def get_packet_hex(self, data):
        return self.packet.hex()

    def get_packet():
        return self.packet

    def set_values(self, d1=0, d2=0, d3=0, d4=0, d5=0):
        self.d1 = int(d1)
        self.d2 = int(d2)
        self.d3 = int(d3)
        self.d4 = int(d4)
        self.d5 = int(d5)

    def serialize(self):
        self.packet = self.cmd_struct.pack(self.d1, self.d2, self.d3, self.d4, self.d5)
