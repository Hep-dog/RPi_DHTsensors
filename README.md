### This project is used to read the temperature and humidity values using the DHT11/DHT22 sensor for Raspberry. The core package is the Adafruit_DHT (https://github.com/adafruit/Adafruit_Python_DHT)
### If you have any problem, please contact: shenpx91@gmail.com
### Note: the python version should be python2.+ ( less then python3 )

Two methods listed in this repository, to transfer the data to influxdb and display it using the grafana:

1. Using the InfluxDBCilent to transfer data the databases. (master branch)
2. Using the telegraf to do the data transmission           (telegraf branch) 

The first one is easy for configuration and modularizing for multi and different sensors,
so we take it as the official method in the this repository work.

================================ Global layout ===========================================

0. ----------------------------- Installation  -------------------------------------------

	The scripts in this dir is used to install the necessary packages:

		a. Adafruit_Python_DHT, using its "setup.py" file to install (Only for raspberry pi);
		b. influxdb, which is the database
		c. grafana, used for the data display
		d. rsync
		e. inotify, used to synchronize data from clients to host, together with rsync
	
	This packages can be installed with the "autoInstalling.sh" script. Often, the rsync has
	already been installed in Linux system. So its installation has not been included.
	

1. --------------------------------- Setup ------------------------------------------------

	The scripts in this dir are used for the software config. The main file is the "Config.py" file
	for the global environment, influxdb and so on.

		a. To keep this package working, you should define the variable "DHTsensors_workarea" and add it in ~/.bashrc. You can set it by:
			$ echo DHTsensors_workarea=... (top dir of this package)

		b: Using the workarea to set the absolute directories for many other script templates:
			date collection script (Collection dir), data transmission script (Display dir), crontab script (Crontab dir) and data synchronizing (Sync dir).

		c: Copy the templates files to their target directories

		d: SET THE HOST IP, THE DEFAULT VALUE IS 192.168.43.84. THE VALUE IS USED FOR THE DATA TRANSMISSION FORM CLIENTS TO HOST, WHICH MUST BE CHANGED WITH YOUR HOST MACHINE IP!!!


2. --------------------------------- Parameters ---------------------------------------------

	The file in this dir holds the key parameters for DHTsensors data collection and transferring to data basebase:

		a. For data collection, we use the class named "collectionModule" in Collection dir, to read and save the raw data. There are several parameters should be set firstly, which is defined in the "Paras_coll.py" file in Parameters dir.

			sensor = sensor	   // Name of sensor for AdafruitDHT, should be DHT11, DHT22 or AM2302
			sensor_gpios = [ ] // the gpio BCM number of the sensor
			meas = meas[ ]     // Name for measurement in influxdb
			outputs = [ ]	   // Data files for saving the humi and temp values

		b. For data transmission from raw data to influxdb database, and for displaying later. We use the class named "Display" to transfer the raw data to infludb. Serveral parameters should be set firstly, which the default values are defined in the "Para_db.py" file in Parameters dir.

			host = host	 // The IP address for influxdb. The default value is ok, which can be obtained with the function "Check_IP"
			port = port	 // Port for influxdb, default is ok
			user = user      // User for influxdb, could be null
			passwd = passwd  // Password for User in influxdb, could be null
			dbname = dbname  // Name of the database
			meas = meas[ ]   // Name for measurement in influxdb
			outputs = [ ]	 // Data files for saving the humi and temp values
	
		Notes: Multi sensors can be used simultanously. For this case the number of measurements , sensor_gpios and outputs need to keep same!


3. --------------------------------- Collection and Display ---------------------------------

	The scripts in these dirs are used to collect DHTsensor (RPi) and Display data (RPi and Host server).
	To keep the collection and displaying processes independent with each other, we just use two main functions,
	which are in Collection and Display dirs. They are just defined in the save class, Collection in "Module.py".
	The run parameters are defined in the "Parameter.py". So users can just run them without additional changes and settings:

		$ python runCollection.py ( Only the RPi clients can do, because the Adafruit_DHT is just installed on clients )
		$ python rundb.py ( Bothe clients and host server can run )


	The crontab is used to continue with the data collection and displaying. During the crontab running, the environment always not same as shell. We should use the absolute dir for each file and command. In addition, we use the bash scripts to run the python ones, which are in the Crontab dir. We source the "/etc/profile" firstly, to get the shell environment, and then run the data collection and displaying processes. Adding the following schedules in crontal:

		$ crontab -e
		Adding "* * * * * /bin/bash workarea/Crontab/doCollection.sh";
		Adding "* * * * * /bin/bash workarea/Crontab/doDisplay.sh";
	
	Additionally, the crontab shell environment is not same as user environment usually. So we should ad the following commands at tbe beginning of crontab, which also can be found in the "templateCrontab" file in Crontab dir.
		$ SEHLL=/bin/bash
		$ BASH_ENV=~/.bashrc
		$ PATH=/sbin:/bin:/usr:/sbin:/usr/bin
		$ ...
		$ ...

4. --------------------------------- Synchronizing data  ---------------------------------

	We use rsync + inotify to synchronize data from RPi clients to Ubuntu host. More detailed descriptions can be found in the Sync directory.
	After the data transmission from clients to host, we transfer the data to influxdb database in host server, and then display it with grafana. Just like what we do in clients, except the data collection with DHT sensors.

	Note: Since we use the rsync to synchronize data from RPi clients to host server, the later will be lost if those in clients are lost. So we add the script in directory "Backup" to backup data day by day. In this way, the origin data could be keey the size for latest few days to save storage, because all data are backup in server. One should add the running of the backup script to crontab with per day schedule.


5. --------------------------------- Raw data backup ---------------------------------

	Since we use the rsync to synchronize data from RPi clients to Ubuntu server, the data in server will be lost if those in clients are lost. 
	So we add the script in directory "Backup" to backup data day by day. In this way, the origin data could be keey the size for latest few days 
	to save storage, because all data are backup in server. One should add the running of the backup script to crontab with per day schedule.
		
		Adding the following command to crontab, just like the data collection and displaying:
			$ * * * * * /bin/bash workarea/Crontab/doBackup.sh


6. --------------------------------- Useful information  ---------------------------------

	a. The frequency of DHT sensors data reading, cited from other people familar with Adafruit_DHT_reader (Link:	www.sopwith.ismellsmoke.net/?p=400) 

		The Adafruit_DHT.read_retry( sensor, pin ) function call will attempt to read data from the sensor 15 times in 2 second intervals. It returns as soon as is
		has valid data. This means the function call can take up to 30 seconds to return results. After 15 reties it gives up and return None values for the temp and
		humidity.... If you need a temp/humi reading more than once or twice a minute, this device is not for you.


	b. About the system logs: 

		Since there will be large log files in the /var/log directory during the influxdb and telegraf running, and the Raspberry Pi system may be stuck due to this
		reason. So the regular cleaning of these files is available by running the script named "Clean_log.py" in Setup dir, and it will be executed day by day with
		the crontab.

	c. The influxdb database:
		




