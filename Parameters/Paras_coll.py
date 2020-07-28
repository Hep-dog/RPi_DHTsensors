#/usr/bin/python
#coding = utf-8

import os, commands


################# Setup for collecting data and run transfer to influxdb database ######
import Adafruit_DHT

# Sensor type for Adafruit_DHT, should be DHT11, DHT22 or AM2302
sensor = Adafruit_DHT.DHT22

# GPIOs for DHT sensors (BCM mode)
sensor_gpios = [ 4, 18, 12 ]

# Data files for saving the humi and temp values
#outputs = [
#        "/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_1.dat",
#	"/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_2.dat",
#	"/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_3.dat"
#        ]
outputs = [
        "/home/pi/Work/RPi_DHTsensors/Collection/data/20200729_20200730/dht11_1_20200729_20200730.dat",
	"/home/pi/Work/RPi_DHTsensors/Collection/data/20200729_20200730/dht11_2_20200729_20200730.dat",
	"/home/pi/Work/RPi_DHTsensors/Collection/data/20200729_20200730/dht11_3_20200729_20200730.dat"
        ]
    	
# Name of measurements of sensors for influxdb and grafana
measurements = [ "dht11_1", "dht11_2", "dht11_3" ]
########################################################################################


