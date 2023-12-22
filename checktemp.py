#!/usr/bin/env python3
import time
import re
import subprocess
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime  # Format Example: %d/%m/%Y-%I:%M:%S (%p)

# Version Control
LATEST_VERSION = "2.1.4 (24/04/2023)"

# CONFIG Values
SLEEP_INTERVAL = 2  # (Value in seconds)
DATEFORMAT = "%d/%m/%Y %H:%M:%S"
STARTDATE = datetime.now().strftime(DATEFORMAT)


def check_CPU_temp():
    temp = None
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
print("[DEBUG] Start Date:", STARTDATE)
print("********************************************************************************\n")

if __name__ == '__main__':
    while True:
        tempstring, msg = check_CPU_temp()
        CPU_TEMP = tempstring
        date = datetime.now().strftime("[" + DATEFORMAT + "] ")

        if CPU_TEMP > 60:
            print(date + "Current Temperature: " + Fore.RED + str(CPU_TEMP) + Fore.RESET + " °C")    
        elif CPU_TEMP > 50 and CPU_TEMP <= 60:
            print(date + "Current Temperature: " + Fore.YELLOW + str(CPU_TEMP) + Fore.RESET + " °C")
        else:
            print(date + "Current Temperature: " + Fore.GREEN + str(CPU_TEMP) + Fore.RESET + " °C")

        time.sleep(SLEEP_INTERVAL)
