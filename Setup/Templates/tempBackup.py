#!/usr/bin/env python
# coding=utf-8

'''
    Since the rsyns will copy the origin data to server, the data
    in server will be lost if the origin data in clients lost.

    So we backup the data in server every data using this script
'''

import time, os, subprocess

now = time.strftime("%Y-%m-%d", time.localtime())
tar_path = 'Defaultdir/Collection/data'

cmd = 'ls ' + tar_path

dats = []

# Obtain the source data
for root, dirs, files in os.walk(tar_path):
    for file in files:
        if os.path.splitext(file)[1] == '.dat':
            dats.append(file)

# Create the new path for data backup
dst_path = 'Defaultdir/Data/Rawdata/' + now
cmd = 'mkdir -p ' + dst_path
os.system(cmd)

# Data backup
for dat in dats:
    tar_file = tar_path + '/' + dat
    cmd = 'tail -n 1500 ' + tar_file + ' > ' + dst_path + '/' + str(dat)
    os.system(cmd)
    #print(cmd)
