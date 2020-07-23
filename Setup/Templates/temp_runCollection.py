#!/usr/bin/python
#coding = utf-8

import time, sys, datetime, logging, os, commands
import Adafruit_DHT
from influxdb import InfluxDBClient
import collectionModule

# workarea, which is necessary
workarea = 'Defaultdir'
sys.path.append(workarea)

# import the parameters
from Parameters import collectionParas

def main():

    num_sensors = len( collectionParas.sensor_gpios )

    for n in range( num_sensors ):
        tempt_sensor = collectionModule.Collection(
                collectionParas.measurements[n],
                collectionParas.sensor, 
                collectionParas.sensor_gpios[n], 
                collectionParas.outputs[n]
                )

        tempt_sensor.run_collection()

main()
