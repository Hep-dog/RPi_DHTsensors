#!/usr/bin/python
#coding = utf-8

import time, sys, datetime, logging, os, commands
import Adafruit_DHT
from influxdb import InfluxDBClient
import collectionModule

# workarea, which is necessary
workarea = '/home/pi/Work/RPi_DHTsensors'
sys.path.append(workarea)

# import the parameters
from Parameters import Paras_coll

def main():

    num_sensors = len( Paras_coll.sensor_gpios )

    for n in range( num_sensors ):
        tempt_sensor = collectionModule.Collection(
                Paras_coll.measurements[n],
                Paras_coll.sensor, 
                Paras_coll.sensor_gpios[n], 
                Paras_coll.outputs[n]
                )

        tempt_sensor.run_collection()

main()
