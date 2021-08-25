#!/usr/bin/env python3

from threading import Thread
import paho.mqtt.client as mqtt
import time

class MQTT_subscriber:

    def __init__(self,ip,port,topic_name,on_message):
        self.client = mqtt.Client()
        self.client.connect(ip,port,60)
        self.topic = topic_name
        self.client.on_connect = self.on_connect
        self.client.on_message = on_message
        self.run()

    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe(self.topic)

    def run(self):
        print('start listening')
        t = Thread(target=self.client.loop_forever)
        t.daemon = True
        t.start()


if __name__ == "__main__":

    def transfer_time(client, userdata, msg):
        print(time.time() - float(msg.payload.decode()))

    def pub_time(client, userdata,msg):
        print(msg.payload.decode())

    sub = MQTT_subscriber("192.168.31.2",1883,"topic/test",transfer_time)
    sub2 = MQTT_subscriber("192.168.31.2",1883,"topic/test",pub_time)
    time.sleep(10)
    print('time up')
