#!/bin/bash

remote_ip=192.168.43.84

/usr/bin/inotifywait -mrq -e modify,delete,create,attrib,move /home/jiyizi/Work/Coding/Raspberry/RPi_DHTsensors/Collection/data/ | while read events
do
	sudo rsync -av --password-file=/etc/rsyncd.secrets /home/jiyizi/Work/Coding/Raspberry/RPi_DHTsensors/Collection/data/ pi@${remote_ip}::dht11
	sudo echo "`date +'%F %T'` have $events" >> /tmp/rsync.log 2>&1
done
