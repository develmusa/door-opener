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

1. Install git: `sudo apt-get install git`
2. Install python3-pip: `sudo apt-get install python3-pip`
3. Change rigths for python packages: `sudo chmod -R 775 /usr/local/lib/python3.X/dist-packages/`
2. Clone door-opener: `git clone https://github.com/develmusa/door-opener.git`
3. Download requirements: `cd door-opener && sudo pip3 install -r requirements.txt`
4. Start door-opener: `python3 dooropener/dooropener.py`
5. Test door-opener: Access Endpoint to activate the relay for 5 seconds `http://192.168.0.17:1666/sesame-open` or `http://192.168.0.17:1666/sesame-open/x` for x seconds.
6. Add door-opener to autostart: 
    - open `/etc/rc.local`
    - add `nohup python3 /home/keyman/door-opener/dooropener/dooropener.py &` before exit 0
7. Check autostart:
    - reload deamon: `sudo systemctl daemon-reload`
    - check status: `sudo systemctl status rc-local`

### Setup for Connection

To connect from outside of your network without your IP you need a DNS. Also you need to setup port forwarding on your router.

1. Setup DNS: [Duck DNS](https://www.duckdns.org/) is a free Dynamic DNS provider
    1. Sing up for Duck DNS
    2. Add your domain
    3. Keep your Duck DNS domain updated on your Raspberry Pi: Follow the steps on [Install Duck DNS](https://www.duckdns.org/install.jsp)
2. Forward Port to your Raspberry Pi
    1. Check IP of your Raspberry Pi 
    2. Login into your router and forward port 1666 to the ip of your Raspberry Pi
