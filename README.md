# Raspberry Fan-Check
This repository contains an explanation to implement a simple fan check system that toggles a fan on **RaspberryPI 4** via GPIO Pins

## Getting Started
- **Needed:** **Transistor** (to connect power when GPIO Pin sends signal), **Board**, **LED** (optional), **Resistor** (see image below)
- Click here for [conversion table](https://learn.sparkfun.com/tutorials/resistors/decoding-resistor-markings)
- The red cable is connected to the 5V (+) (also 3.3V possible for slower speed) and the blue cable to the Ground (-)
- In this script, **GPIO PIN 11** is used. When the pin is enabled, it sends a signal (brown cable) to the LED which gets forwarded to the Transistor.
- The Transistor then receives the signal and forwards the power through the black cable to the fan which toggles it
- **Software:** Python3 & pip


## Execution of temp check on every boot
- ``python3 temp.py`` is the main script -> Remove file ending, it is executable without python3 command due to ``#!/usr/bin/env/python3``
- Script must be moved to **/usr/local/bin** to be executable by simply writing the **filename** in the terminal.

### How to
  - ``sudo chmod +x /usr/local/bin/<FILENAME>.py`` - Add execution permission
  - ``sudo mv <FILENAME>.py /usr/local/bin/<FILENAME>``  
  > :warning: **Hint:** You can also just move the ``deploytemp.py`` script with this instruction, then execute it by typing ``deploytemp`` and insert the name (one at a time) of the files you want to move. (Check if files are encoded in **LF**!)

- **To start the script on boot of Raspberry Pi:**
  - Create ``temp.sh`` script from repo
  - Move it to **/etc/init.d** and make it executable
    - ``sudo mv temp.sh /etc/init.d/``
    - ``sudo chmod +x /etc/init.d/temp.sh``
  - Register script to be executed on boot:
    -  ``sudo update-rc.d temp.sh defaults``
  - Reboot RaspberryPi or manuelly start the script:
    - ``sudo /etc/init.d/temp.sh start``

> :warning: Files that are moved to **/usr/local/bin** must be encoded in **LF**, not CRLF, otherwise they are not executable.
> **Fix (VSCode):** At the bottom right, change CRLF to LF
> **Fix (Terminal):** ``sudo sed -i -e 's/\r$//' /PATH/FILENAME``

### Scripts explanations
- ``deploytemp.py`` - Automatically changes the file ending of the inserted script, moves it to /usr/local/bin and makes it executable
  - Firstly move the file to /usr/local/bin, remove the file ending, check if LF is used and add +x permission
  - Then execute it with ``deploytemp`` (The files to move must be in the same directory)
- ``disablefan.py`` & ``enablefan.py`` - Toggles fan (e.g. for debugging purposes)
- ``temp.py`` - Main Script -> Fan-Check
- ``temp.sh`` - Bootscript of **temp.py**
- ``disabletempcheck.py`` - Fully disables temperature check. Can only be reenabled by rebooting
- ``checktemp.py`` - Displays temperature every few seconds (stop with ctrl + c) [Needs: ``apt install python3-colorama``]
- ``test_led.py`` - Tests the LED of the board. The GPIO-PIN must be correct

#### How To
![Build 1](/assets/build_1.jpg)  
![Build 2](/assets/build_2.jpg)  
![Build 3](/assets/build_3.jpg)
![Components](/assets/build_4.jpg)
![Build 5](/assets/build_5.jpg)
![GPIO Pins](/assets/raspberry-pi-gpio.png)
(https://www.elektronik-kompendium.de/sites/raspberry-pi/bilder/raspberry-pi-gpio.png)
