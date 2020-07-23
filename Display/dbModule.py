#!/usr/bin/python

import time, sys, datetime, logging, os, commands
from influxdb import InfluxDBClient

class Display():

    def __init__(self, host, port, user, passwd, dbname, meas, outname):
        self.host = host
        self.port = port
        self.meas = meas
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.outname= outname

    def check_IP(self):
        cmd = 'ifconfig  |grep broadcast | awk -F \'netmask\' {\'system("echo " $1)\'} | awk -F \'inet\'  {\'system("echo " $2)\'}'
        status, output = commands.getstatusoutput(cmd)
        self.host = str(output)


    # This function is used to synchronize the local DHT data the influxdb
    def sync_localdata_DHT(self):
        file = open(self.outname, "r")
        
        while True:
            lines = file.readlines()
            if not lines:
                break
            for line in lines:
                iso  = int(line.split(" ")[0])
                temp = float(((line.split(" ")[1]).split("Temp=")[1]).split("C")[0])
                humi = float(((line.split(" ")[3]).split("dity=")[1]).split("%")[0])
                #print(iso, temp, humi)

                data = [
                        {
                            "measurement" : self.meas,
                            "time" : iso,
                            "fields" : {
                                "temperature" : temp,
                                "humidity"    : humi
                                }
                            }
                        ]
                if temp is not None and humi is not None:
                    if float(humi)<100:
                        # Create the InfluxDB client object
                        client = InfluxDBClient( self.host, self.port, self.user, self.passwd, self.dbname)
                        client.write_points(data)
                        #print("[%s] Temp: %s, Humidity: %s" % (iso ,temp, humi))
        
        file.close()


def main():

    host = "127.0.0.1"
    port = 8086
    user = ""
    passwd = ""
    dbname = "sync"
    output = "/home/pi/Work/dht22/Collect/data/test.log"
    measurement = "dht11"

    # Create class to read and write dht11 data
    Test_dht11 = Collection(host, port, user, passwd, dbname, measurement, sensor, sensor_gpip, output)

    Test_dht11.check_IP()
    print(Test_dht11.host)
    Test_dht11.run_collection()
    Test_dht11.sync_localdata_DHT()

if __name__ == "__main__":
    main()
