#!/usr/bin/bash

# update the source.list
sudo apt update

# install the influxdb
sudo wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/os-release
sudo echo "deb https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt update
sudo apt install -y influxdb
pip install influxdb

# install the grafana
sudo wget -qO- https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list

sudo apt update
sudo apt install -y grafana


# run the influxdb and grafana service after booting
sudo systemctl enable influxdb.service
sudo systemctl enable grafana-server

# Install the Adafruit_Python_DHT, only for Raspberry PI clients
cd ../Adafruit_Python_DHT/ 
sudo python setup.py install

# install the postfix for crontab
sudo apt install -y postfix

# install the inotify for synchronizing
sudo apt install -y inotify-tools
