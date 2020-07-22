#!/usr/bin/python

import os, sys, commands

################################ Setup for workarea ##################################
'''
        users should set the DHTsensors_workarea in ~/.bashrc file firstly:
            export DHTsensors_workarea=.....
'''
cmd = 'echo $DHTsensors_workarea'
_, workarea = commands.getstatusoutput(cmd)

# set workarea for data collection (in Collection and Display folders)
cmd1 = 'cp ' + workarea + '/Setup/Templates/temp_runCollection.py ' + workarea + 'Collection/runCollection.py'
cmd2 = 'cp ' + workarea + '/Setup/Templates/temp_rundb.py ' + workarea + 'Display/rundb.py'
os.system(cmd1)
os.system(cmd2)

dirFormat = workarea.replace("/", r"\/")
cmd1 = 'sed -i "s:Defaultdir:' + dirFormat + ':g" ' + workarea + '/Collection/runCollection.py'
cmd2 = 'sed -i "s:Defaultdir:' + dirFormat + ':g" ' + workarea + '/Display/rundb.py'
os.system(cmd1)
os.system(cmd2)

# setup workarea for script  to run collection and displaying (in Crontab folder)
cmd1 = 'cp ' + workarea + '/Setup/Templates/collectionTempt.sh ' + workarea +'Crontab/doCollection.sh'
cmd2 = 'cp ' + workarea + '/Setup/Templates/displayTempt.sh '    + workarea +'Crontab/doDisplay.sh'
os.system(cmd1)
os.system(cmd2)

cmd1 = 'sed -i "s:Defaultdir:' + dirFormat + ':g" ' + workarea + '/Crontab/doCollection.sh'
cmd2 = 'sed -i "s:Defaultdir:' + dirFormat + ':g" ' + workarea + '/Crontab/doDisplay.sh'
os.system(cmd1)
os.system(cmd2)


# setup workarea for scripts to synchronize data from clients to host (in Sync folder)
cmd1 = 'cp ' + workarea + '/Setup/Templates/trans.sh ' + workarea +'/Sync/trans.sh'
cmd2 = 'cp ' + workarea + '/Setup/Templates/trans.service ' + workarea +'/Sync/trans.service'
os.system(cmd1)
os.system(cmd2)

cmd1 = 'sed -i "s:Defaultdir:' + dirFormat + ':g" ' + workarea + '/Sync/trans.sh'
cmd2 = 'sed -i "s:Defaultdir:' + dirFormat + ':g" ' + workarea + '/Sync/trans.service'
os.system(cmd1)
os.system(cmd2)

# setup host ip for data synchronizing from clients to host (in Sync folder)
ipHost = '192.168.43.84'
cmd = 'sed -i "s:ipHost:' + ipHost + ':g" ' + workarea + '/Sync/trans.sh'
os.system(cmd)


########################################################################################


########################### Setup for influxdb database ################################
# The default database directory is: $(workarea)/Data/date
cmd = 'date +%y%m%d'
_, day = commands.getstatusoutput(cmd)

newdir = str(workarea) + '/Data/' + str(day)
print 'The new database folder is: ' + newdir


# Set directories for influxdb databases: data, meta, and wal-dir
data_area = str(newdir) + '/data/data'
meta_area = str(newdir) + '/data/meta'
wald_area = str(newdir) + '/data/wal'

# Set the write permission for influxdb
os.system(' mkdir -p ' + data_area)
os.system(' mkdir -p ' + meta_area)
os.system(' mkdir -p ' + wald_area)
os.system(' sudo chown -R influxdb:influxdb ' + data_area)
os.system(' sudo chown -R influxdb:influxdb ' + meta_area)
os.system(' sudo chown -R influxdb:influxdb ' + wald_area)

# Set the influxdb config file, and move it to  /etc/influxdb/
Temp_file = str(workarea) + "/Setup/Templates/temp_influxdb"
conf_file = str(workarea) + "/Setup/Templates/influxdb.conf"
cmd = "cp " + Temp_file + "     " + conf_file
os.system(cmd)

temp = newdir.replace( "/", r"\/")
cmd = 'sed -i "s/Workarea/' + temp + '/g" ' + conf_file
os.system(cmd)

cmd = 'sudo mv ' + conf_file + '    /etc/influxdb/influxdb.conf'
os.system(cmd)

########################################################################################



