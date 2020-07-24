#/usr/bin/python
#coding = utf-8

import os, commands


################# Setup for collecting data and run transfer to influxdb database ######
import Adafruit_DHT

# Sensor type for Adafruit_DHT, should be DHT11, DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

# GPIOs for DHT sensors (BCM mode)
sensor_gpios = [ 4, 18, 23 ]

# Data files for saving the humi and temp values
outputs = [
        "/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_1.dat",
	"/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_2.dat",
	"/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_3.dat"
        ]
    	
# Name of measurements of sensors for influxdb and grafana
measurements = [ "dht11_1", "dht11_2", "dht11_3" ]
########################################################################################


