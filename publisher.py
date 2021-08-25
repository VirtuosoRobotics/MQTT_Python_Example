#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

# This is the Publisher

client = mqtt.Client()
# client.connect("127.0.0.1",1883,60)
client.connect("192.168.31.2",1883,60)

while True:
    client.publish("topic/test", time.time());
    time.sleep(0.05)

# client.disconnect();