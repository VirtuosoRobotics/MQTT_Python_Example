#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time,threading

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
    # print(msg.payload.decode())
    # if msg.payload.decode() == "Hello world!":
    #     print("Yes!")
    # client.disconnect()
    print(time.time() - float(msg.payload.decode()))
    
client = mqtt.Client()
client.connect("192.168.31.2",1883,60)
# client.connect("127.0.0.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

t = threading.Thread(target=client.loop_forever)
t.daemon = True
t.start()
time.sleep(10)
print('time up!')
# client.loop_forever()
