#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import re
import subprocess
from datetime import datetime  # Format Example: %d/%m/%Y-%I:%M:%S (%p)

# Version Control
LATEST_VERSION = " 3.3.6 (22/12/2023)"

# CONFIG Values
GPIO_PIN = 11  # Which GPIO Pin will be used
TEMP_MAX = 65  # Treshold for enabling fan
TEMP_LOW = 50  # Treshold for disabling fan
SLEEP_INTERVAL = 5  # (Value in seconds)
STARTDATE = datetime.now().strftime("%d/%m/%Y %I:%M:%S (%p)")
TEMP_DEBUG = subprocess.getstatusoutput(
    'vcgencmd measure_temp')  # Get Temperature

# GPIO
# BOARD / BCM - Board -> Pin Number, BCM - GPIO Number
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.OUT)

# Fetches temperature
def check_CPU_temp():
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)   # a solution with a regex
        try:
            tempstring = float(m.group())
        except ValueError:  # catch only error needed
            pass
    return tempstring, msg


print("\n\n**SCRIPT STARTED**\n")
print("********************************************************************************")
print("[DEBUG] Latest Version:", LATEST_VERSION)
print("[DEBUG] Current Temperature:", TEMP_DEBUG)
print("[DEBUG] Max. Temperature Treshold:", TEMP_MAX, "°C")
print("[DEBUG] Min. Temperature Treshold:", TEMP_LOW, "°C")
print("[DEBUG] GPIO used pin:", GPIO_PIN)
print("[DEBUG] Start Date:", STARTDATE)
print("********************************************************************************\n")

if __name__ == '__main__':
    if TEMP_LOW >= TEMP_MAX:
        raise RuntimeError(
            "Error! Tempmax is lower than Templow (", TEMP_MAX, "<", TEMP_LOW, ")\n\n")
    elif TEMP_MAX > TEMP_LOW:
        print("[DEBUG-CHECK] [SUCCESS] Tempmax is higher than Templow (",
              TEMP_MAX, "°C >", TEMP_LOW, "°C) -> Continuing \n\n")

    # Toggling Fan Check
    while True:
        # Vars
        tempstring, msg = check_CPU_temp()
        CPU_TEMP = tempstring
        date = datetime.now().strftime("[%d/%m/%Y-%I:%M:%S (%p)]")

        if CPU_TEMP >= TEMP_MAX:
            print(date, "Warning! The temperature is above", TEMP_MAX,
                  "(Max. temperature) - **FAN ENABLED**")
            print("[DEBUG] Current Temperature:", CPU_TEMP, "°C\n")
            GPIO.output(GPIO_PIN, GPIO.HIGH)

        if CPU_TEMP <= TEMP_LOW:
            print(date, "The temperature is below", TEMP_LOW,
                  "(Min. temperature) - **FAN DISABLED**")
            print("[DEBUG] Current Temperature:", CPU_TEMP, "°C\n")
            GPIO.output(GPIO_PIN, GPIO.LOW)

        if CPU_TEMP > TEMP_LOW or CPU_TEMP < TEMP_MAX:
            print(date, "Temperature is between", TEMP_LOW,
                  "°C (Min. temperature) and", TEMP_MAX, "°C (Max. temperature) - **Fan will not be toggled**")
            print("[DEBUG] Current Temperature:", CPU_TEMP, "°C\n")

        time.sleep(SLEEP_INTERVAL)

GPIO.cleanup()      # Cleanup pins to prevent error
