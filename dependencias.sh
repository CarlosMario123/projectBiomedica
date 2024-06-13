#!/bin/bash

#USER = "pi"

sudo apt update -y

sudo apt upgrade -y

sudo apt install python3-pip -y

sudo apt install python3-smbus -y

sudo apt install python3-full -y

sudo apt install i2c-tools -y

sudo usermod -aG i2c pi

sudo usermod -aG gpio pi

sudo usermod -aG dialout pi

cd /home/pi/projectBiomedica

#git clone https://github.com/CarlosMario123/projectBiomedica.git

#cd projectBiomedica

#git switch raspberry

# python -m venv ./variable

# source ./variable/bin/activate

#estos son los buenos, los instalables
#pip install mpu6050 --break-system-packages
#pip install mpu6050-raspberrypi --break-system-packages
#pip install RPi.GPIO --break-system-packages
#pip install pyserial --break-system-packages
#pip install tk --break-system-packages
#pip install scipy --break-system-packages
#pip install pillow --break-system-packages

#pip install smbus --break-system-packages
#pip install serial --break-system-packages

#activar i2c
sudo raspi-config
