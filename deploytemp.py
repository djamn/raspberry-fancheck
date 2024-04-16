#!/usr/bin/env python3
import subprocess
import os
import time
import sys

# VERSION CONTROL
LATEST_VERSION = "2.4.0 (16/04/2024)"

# CONFIG VALUES
SOURCE_PATH = '/home/pi/'
DESTINATION_PATH = '/usr/local/bin/'
TIME_VALUE = 1.2  # Delayvalue in seconds

print("**SCRIPT STARTED**\n\
Specified file will be converted to file without ending, made executable & moved to", DESTINATION_PATH, "\n")
print("[DEBUG] Latest Version:", LATEST_VERSION, "\n")

if len(sys.argv) > 1:
    FILENAME_INPUT = sys.argv[1]
    print("Received filename via argument:", FILENAME_INPUT)
else:
    FILENAME_INPUT = input("Enter the file name with ending:\n") # Prompts user to enter filename

# Processing Values
# Add filename with file extension to Source Path (/home/pi/test.py)
SOURCE_PATH_FULL = os.path.join(SOURCE_PATH, FILENAME_INPUT)
# Add filename with file extension to Destination Path (/other/path/test.py)
DESTINATION_PATH_FULL = os.path.join(DESTINATION_PATH, FILENAME_INPUT)
# Remove file extension from filename (test.py --> test)
FILENAME_WITHOUT_EXTENSION = os.path.splitext(FILENAME_INPUT)[0]
# Add filename without file extension to Source Path (/home/pi/test)
SOURCE_PATH_FULL_WITHOUT_EXTENSION = os.path.join(
    SOURCE_PATH, FILENAME_WITHOUT_EXTENSION)
# Add filename without file extension to Destination Path (other/path/test)
DESTINATION_PATH_FULL_WIHTOUT_EXTENSION = os.path.join(
    DESTINATION_PATH, FILENAME_WITHOUT_EXTENSION)

print("Processing...")
time.sleep(TIME_VALUE)

print("********************************************************************************")
print("[DEBUG] Filename:", FILENAME_INPUT)
print("[DEBUG] Filename without file extension:", FILENAME_WITHOUT_EXTENSION)
print("[DEBUG] Source Path:", SOURCE_PATH)
print("[DEBUG] Full Source Path:", SOURCE_PATH_FULL)
print("[DEBUG] Destination Path:", DESTINATION_PATH)
print("[DEBUG] Full Destination Path:", DESTINATION_PATH_FULL)
print("[DEBUG] Source Path without file extension:",
      SOURCE_PATH_FULL_WITHOUT_EXTENSION)
print("[DEBUG] Destination Path without file extension:",
      DESTINATION_PATH_FULL_WIHTOUT_EXTENSION)
print("********************************************************************************\n")

# Changes Filetype (test.py --> test)
os.rename(SOURCE_PATH_FULL, FILENAME_WITHOUT_EXTENSION)
print("[SUCCESS] Changed filetype")

# Makes file executable (rw-r--r-- --> rwxr-xr-x)
subprocess.check_call(['chmod', '+x', SOURCE_PATH_FULL_WITHOUT_EXTENSION])
print("[SUCCESS] Made file executable")

# Moves changed file to specified path
os.rename(SOURCE_PATH_FULL_WITHOUT_EXTENSION,
          DESTINATION_PATH_FULL_WIHTOUT_EXTENSION)
print("[SUCCESS] Moved file successfully to", DESTINATION_PATH)
print("\n[SUCCESS] **DONE!**")
