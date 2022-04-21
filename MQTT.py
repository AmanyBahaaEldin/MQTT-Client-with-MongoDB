from datetime import datetime
from operator import concat
import random
import json
from xml.etree.ElementTree import tostring
from paho.mqtt import client as mqtt_client
from json_data import string_to_json


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt/sensor"
client_id = f'python-mqtt-{random.randint(0, 100)}'



def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        dataFromMqtt = msg.payload.decode()
        
        string_to_json(dataFromMqtt)
        


    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()