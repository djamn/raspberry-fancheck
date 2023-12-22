#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Version Control
LATEST_VERSION = "1.0.1 (26/09/2021)"

# CONFIG Values
pin = 11

# GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

# Disabling Fan
GPIO.output(pin, GPIO.LOW)
print("[DEBUG] Latest Version:", LATEST_VERSION)
print("[SUCCESS] Successfully disabled fan!")

GPIO.cleanup()