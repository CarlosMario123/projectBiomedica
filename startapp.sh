#!/bin/bash

cd /home/pi/projectBiomedica

#. variable/bin/activate

/usr/bin/python3 app.py >> /home/pi/projectBiomedica/log.txt 2>&1

