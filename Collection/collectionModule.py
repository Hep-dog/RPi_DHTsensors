#!/usr/bin/python

import time, sys, datetime, logging, os, commands
import Adafruit_DHT
from influxdb import InfluxDBClient


class Collection():

    def __init__(self, meas, sensor, sensor_gpip, outname):
        self.meas   = meas
        self.sensor = sensor
        self.sensor_gpip = sensor_gpip
        self.outname= outname

    def setup_logger(self):
        # This function is used to set logging

        level=logging.INFO
        formatter = logging.Formatter( '%(message)s')
        handler   = logging.FileHandler(self.outname)
        handler.setFormatter(formatter)
        logger = logging.getLogger(self.meas) 
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

    def run_collection(self):

        # Set the output file
        #logging.basicConfig( filename=self.outname, filemode='a', format='%(message)s', level=logging.INFO)
        logger = self.setup_logger()

        while True:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.sensor_gpip)
            iso = int(round(time.time()*1000000000))
            data = [
                    {
                        "measurement" : self.meas,
                        "time" : iso,
                        "fields" : {
                            "temperature" : temperature,
                            "humidity"    : humidity
                            }
                        }
                    ]
    
            if temperature is not None and humidity is not None:
                if float(humidity)<100:
                    #logging.info('Temp={0:0.1f}C and Humidity={1:0.1f}%'.format(temperature, humidity))
                    logger.info('{0:18d} Temp={1:0.1f}C and Humidity={2:0.1f}%'.format(iso, temperature, humidity))

                    break


def main():

    sensor = Adafruit_DHT.DHT11
    sensor_gpip = 4
    output = "data/test.log"

    Test_dht11 = Collection(host, sensor, sensor_gpip, output)

    Test_dht11.run_collection()

if __name__ == "__main__":
    main()
