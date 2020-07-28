#/usr/bin/python
#coding = utf-8

import time, sys, datetime, logging, os, commands
from influxdb import InfluxDBClient
import dbModule

# workarea, which is necessary
workarea = '/home/pi/Work/RPi_DHTsensors'
sys.path.append(workarea)

# import the parameters
from Parameters import Paras_db

def main():

    num_sensors = len( Paras_db.measurements )

    for n in range( num_sensors ):
        tempt_sensor = dbModule.Display(
                Paras_db.host,
                Paras_db.port,
                Paras_db.user, 
                Paras_db.passwd, 
                Paras_db.dbname, 
                Paras_db.measurements[n], 
                Paras_db.outputs[n]
                )

        tempt_sensor.check_IP()
        tempt_sensor.sync_localdata_DHT()


main()
