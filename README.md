# Door opener

Simple Webserver to use RaspberryPi and a Relay to open or activate things.
## Hardware

- Any RaspberryPi
- [USB-Relay](https://www.aliexpress.com/item/LCUS-1-type-USB-Relay-Module-Electronic-Converter-PCB-USB-Intelligent-Control-Switch/32955376837.html?spm=a2g0s.9042311.0.0.122a4c4dZg1vG4)

## Installation

### Setup RaspberryPi

1. [Download Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/)
2. Copy Image to SD-Card

    ```bash
    dd bs=4M if=2018-11-13-raspbian-stretch.img of=/dev/sdX conv=fsync
    ```

3. Hook up your RaspberryPi and login with the default root login
    - user: pi
    - pw: raspberry
4. Open the Config: `sudo raspi-config`
5. Change default password
6. Change hostname
7. Connect to WiFi
8. Enable predictable networknames
9. Change localisation options: Use spacebar to select local
10. Enable SSH for simpler access: `Interfacing options -> ssh enable`
11. Close `raspi-config`
12. Update Package list: `sudo apt-get update`
13. Add a new user `sudo adduser keyman`
14. Add group for usb users: `sudo groupadd usbusers`
15. Add a rule for the usbusers-groupe to access usb devices:

    ```bash
    echo 'SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", MODE="0664", GROUP="usbusers"' | sudo tee -a /etc/udev/rules.d/99-com.rules
    ```

16. Add user to groupe: `sudo usermod -aG usbusers keyman`
17. Change user to new user: `su keyman`

### Test Relay Connection

1. Plug-in your Relay
2. Display and find relay in the usb devices: `lsusb -v`
3. Write down the vendorid and productid. Depending on your Relaymodel you have to change Constants in the code.
4. Test relay connection with this code.The string may vary depending on the type of the relay.

    ```bash
    # On
    echo -e "\\xA0\\x01\\x01\\xA2" > /dev/ttyUSB0
    # Off
    echo -e "\\xA0\\x01\\x00\\xA1" > /dev/ttyUSB0
    ```


### Install Software

1. Install git (as user: pi): `sudo apt-get install git`
2. Clone door-opener (as user: keyman): `git clone https://github.com/develmusa/door-opener.git`
3. Download requirements: `cd door-opener && pip install -r requirements.txt`


### Setup for Connection

- To connect from outside of your network you need a DNS. Take a look at [Duck DNS](https://www.duckdns.org/domains).
- You also need to setup portforwarding on your router.
