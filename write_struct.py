# -*- coding: utf-8 -*

import serial
import struct
from MachineCmd import MachineCmd

if __name__ == '__main__':

    port = input("arduino serial port: ") # COM4 windows, /dev/ttyUSB0 or /dev/ttyUSB0 linux
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
        print('sending to arduino...' + machine.get_packet_hex())
        #print(machine.packet.hex())
        # send bytes to arduino
        if arduino.write(machine.packet):
            print('OK')
            try:
                packet = arduino.read(10)
                print("original packet: ", packet.hex())
            except serial.SerialException as e:
                print(e)
        else:
            print('fail')
