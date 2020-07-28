#!/bin/bash

remote_ip=192.168.0.119

scp -r pi@${remote_ip}:/home/pi/Work/RPi_DHTsensors/Collection/data /home/atlas-itk/Work/RPi_DHTsensors/Collection
