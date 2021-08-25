# MQTT_Python_Example

Install 
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa\
sudo apt-get update\
sudo apt-get install mosquitto\
sudo pip3 install paho-mqtt

在 /etc/mosquitto/mosquitto.conf 中加入\
listener 1883 0.0.0.0\
allow_anonymous true\

