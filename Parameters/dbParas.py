#/usr/bin/python
#coding = utf-8

import os, commands


################# Setup for collecting data and run transfer to influxdb database ######

# IP address for clients, default value is OK
host = "127.0.0.1"
# Port for influxdb, default value is OK
port = 8086
# User and passwd for influxdb and grafana, none is OK
user = ""
passwd = ""

# Name of database for influxdb and input for grafana
dbname = "DHT11"

# Data files for saving the humi and temp values
outputs = [
        "/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_1.dat",
	"/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_2.dat",
	"/home/pi/Work/RPi_DHTsensors/Collection/data/dht11_3.dat"
        ]
    	
# Name of measurements of sensors for influxdb and grafana
measurements = [ "dht11_1", "dht11_2", "dht11_3" ]
########################################################################################


