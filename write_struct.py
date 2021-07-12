# -*- coding: utf-8 -*

import serial
import struct
from MachineCmd import MachineCmd

if __name__ == '__main__':

    port = input("arduino serial port: ")
    arduino = serial.Serial(port, 9600)
    machine = MachineCmd()
    while True:
        d1 = int(input("input 1: "))
        d2 = int(input("input 2: "))
        d3 = int(input("input 3: "))
        d4 = int(input("input 4: "))
        d5 = int(input("input 5: "))
        machine.set_values(d1,d2,d3,d4,d5)
        machine.serialize()

        # See what is in packet
        print('sending to arduino...')
        #print(machine.packet.hex())
        # send bytes to arduino
        if arduino.write(machine.packet):
            print('OK')
        else:
            print('fail')
