#!/usr/bin/env python

import uinput
from time import sleep

device=uinput.Device([uinput.KEY_H, uinput.KEY_E, uinput.KEY_L, uinput.KEY_O,])

sleep(2)
device.emit_click(uinput.KEY_H)
sleep(2)
device.emit_click(uinput.KEY_E)
sleep(2)
device.emit_click(uinput.KEY_L)
sleep(2)
device.emit_click(uinput.KEY_L)
sleep(2)
device.emit_click(uinput.KEY_O)
sleep(4)
