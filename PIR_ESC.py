#!/usr/bin/env python
# PIR_ESC.py

# url: https://gist.github.com/glafranceri/5df7db9b64ed1a27a1f8cc8f46b772d2
# written by glafranceri@gmail.com
# This script is licensed under GNU GPL version 2.0 or above
# PIR_ESC.py needs uninput and RPi.GPIO to work

# Script needs to be run as root from the command line using sudo
# Press [Ctrl] + [C] to exit script 

# Import modules in script
import uinput
import RPi.GPIO as GPIO
from time import sleep

# Map Esc key to device
device=uinput.Device([uinput.KEY_ESC])

# Set GPIO pin numbers to Board numbers 
GPIO.setmode(GPIO.BOARD)

# Define PIR to be 10
PIR = 10

# Setup GPIO to look for input on Board pin number PIR (10)
GPIO.setup(PIR, GPIO.IN)

while 1: # Begin Loop
    try:
        if GPIO.input(PIR): # If there is voltage
            device.emit_click(uinput.KEY_ESC) # Press the ESC key
            sleep(60) # Sleep 60 seconds
    except KeyboardInterrupt:
        exit()
GPIO.cleanup()
    
