#/usr/bin/python
#coding = utf-8

import time, sys, datetime, logging, os, commands
import Adafruit_DHT
from influxdb import InfluxDBClient
import Module

# workarea, which is necessary
workarea = 'Defaultdir'
sys.path.append(workarea)

# import the parameters
from Parameters import paras

def main():

    num_sensors = len( paras.sensor_gpios )

    for n in range( num_sensors ):
        tempt_sensor = Module.Collection(
                paras.host,
                paras.port,
                paras.user, 
                paras.passwd, 
                paras.dbname, 
                paras.measurements[n], 
                paras.sensor, 
                paras.sensor_gpios[n], 
                paras.outputs[n]
                )

        tempt_sensor.check_IP()
        tempt_sensor.sync_localdata_DHT()


main()
