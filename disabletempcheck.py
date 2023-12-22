#!/usr/bin/env python3
# Description:
# Disables Maintenance mode
import subprocess
import time

# VERSION CONTROL
LATEST_VERSION = "1.0.2 (28/10/2021)"
TIME_VALUE = 1.2 # Delayvalue in seconds



# CONFIG VALUES
# -/-

print("**SCRIPT STARTED**\n")
print("[DEBUG] Latest Version:", LATEST_VERSION, "\n")

INPUT_TYPE = input(
    "\nDo you really want to disable the temperature check? (y/n):\n**NOTE** You need to reenable it via a full reboot!\n")

if INPUT_TYPE == "y" or INPUT_TYPE == "yes":
    print("[DEBUG] Disabling temperature check...\n")
    time.sleep(TIME_VALUE)
    subprocess.call(['sh','/etc/init.d/temp.sh','stop'])
    print("\n[SUCCESS] Successfully disabled temp check!\n**Note** Temperature may increase now!")

elif INPUT_TYPE != "y" or INPUT_TYPE != "yes":
    print("[SUCCESS] Alright!")
    exit
