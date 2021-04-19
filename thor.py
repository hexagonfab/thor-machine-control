"""
 * Debug printer motherboard.
 *
 * Written by Lukas Vasadi in April 2021
"""

import time
import serial

from serial.tools import list_ports
from threading import Thread, Event


def findComPort(description):
    ports = list(list_ports.comports())
    for com in ports:
        if description in com.description:
            return com[0]


def connect(port, baudrate):
    mcu = serial.Serial(port=port, baudrate=250000, timeout=1)
    
    # Reset MCU
    mcu.setDTR(False)
    time.sleep(0.1)
    mcu.reset_input_buffer()
    mcu.reset_output_buffer()
    mcu.setDTR(True)

    return mcu


def transmit(motherboard, command):
    command = command.upper() + '\r\n'
    motherboard.write(command.encode())


def readMotherboard(motherboard):
    message = " "
    while message != "":
        message = motherboard.readline()[0:-1].decode('utf-8', 'ignore')
        print(message.strip())


def actuateSolenoid(arduino, command):
    command = command + '\n'
    arduino.write(command.encode())


def main():
    # Find Thor motherboard
    portMotherboard = findComPort("Marlin USB Device")
    motherboard = connect(portMotherboard, 250000)

    # Find integrated Arduino Leonardo
    portArduinoLeonardo = findComPort("Arduino Leonardo")
    leonardo = connect(portArduinoLeonardo, 9600)

    # threadReadMotherboard = Thread(target=readMotherboard, args=(motherboard,), daemon=True) # Provide the motherboard object as an arg
    # threadReadMotherboard.start()

    transmit(motherboard, "G28 X Y")

    while True:
        command = input("Command: ")
        # Actuate solenoid
        if command == "U" or command == "D":
            actuateSolenoid(leonardo, command)
        elif command == "E":
            actuateSolenoid(leonardo, "U") # Initialize solenoid
            while True:
                transmit(motherboard, "G1 X30 Y150")
                time.sleep(5)
                actuateSolenoid(leonardo, "D")
                time.sleep(2)
                actuateSolenoid(leonardo, "U")
                time.sleep(2)
                transmit(motherboard, "G1 X125 Y80")
                time.sleep(5)
                actuateSolenoid(leonardo, "D")
                time.sleep(2)
                actuateSolenoid(leonardo, "U")
                time.sleep(2)
                transmit(motherboard, "G1 X30 Y80")
                time.sleep(5)
                actuateSolenoid(leonardo, "D")
                time.sleep(2)
                actuateSolenoid(leonardo, "U")
                time.sleep(2)
                transmit(motherboard, "G1 X125 Y150")
                time.sleep(5)
                actuateSolenoid(leonardo, "D")
                time.sleep(2)
                actuateSolenoid(leonardo, "U")
                time.sleep(2)
        else:
            transmit(motherboard, command) 
            readMotherboard(motherboard)

        


if __name__ == "__main__":
    main()
