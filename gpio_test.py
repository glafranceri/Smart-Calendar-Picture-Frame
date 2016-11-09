#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

# Set GPIO pin numbers to Board numbers 
GPIO.setmode(GPIO.BOARD)

# Define PIR to be 10
PIR = 10

# Setup PIR to an input
GPIO.setup(PIR, GPIO.IN)

while 1:
    if GPIO.input(PIR):
        print "Motion Detected"
