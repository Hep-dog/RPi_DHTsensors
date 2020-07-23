#/usr/bin/python
#coding = utf-8

import time, sys, datetime, logging, os, commands
from influxdb import InfluxDBClient
import dbModule

# workarea, which is necessary
workarea = 'Defaultdir'
sys.path.append(workarea)

# import the parameters
from Parameters import dbParas

def main():

    num_sensors = len( dbParas.measurements )

    for n in range( num_sensors ):
        tempt_sensor = dbModule.Display(
                dbParas.host,
                dbParas.port,
                dbParas.user, 
                dbParas.passwd, 
                dbParas.dbname, 
                dbParas.measurements[n], 
                dbParas.outputs[n]
                )

        tempt_sensor.check_IP()
        tempt_sensor.sync_localdata_DHT()


main()
