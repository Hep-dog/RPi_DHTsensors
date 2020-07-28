#!/usr/bin/python

'''
    This script is used to keep the system file size of Raspberry Pi
    The target file is 'syslog' and 'daemon.log' in /var/log/ dir
'''

import os 

CMDs = []

CMDs.append('sudo tail -n 1000 /var/log/syslog > /tmp/temp')
CMDs.append('sudo mv /tmp/temp /var/log/syslog')
CMDs.append('sudo chmod 640 /var/log/syslog')
CMDs.append('sudo chown root:adm /var/log/syslog')
CMDs.append('sudo tail -n 1000 /var/log/daemon.log > /tmp/temp')
CMDs.append('sudo mv /tmp/temp /var/log/daemon.log')
CMDs.append('sudo chmod 640 /var/log/daemon.log')
CMDs.append('sudo chown root:adm /var/log/daemon.log')


for cmd in CMDs:
    #print(cmd)
    os.system(cmd)

