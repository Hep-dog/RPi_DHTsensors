#!/bin/bash

remote_ip=ipHost

/usr/bin/inotifywait -mrq -e modify,delete,create,attrib,move Defaultdir/Collection/data/ | while read events
do
	sudo rsync -av --password-file=/etc/rsyncd.secrets Defaultdir/Collection/data/ pi@${remote_ip}::dht11
	sudo echo "`date +'%F %T'` have $events" >> /tmp/rsync.log 2>&1
done
