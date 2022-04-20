from http import client
import pymongo

def mqttClient(jsonDocument):
    mqttClient = pymongo.MongoClient('mongodb+srv://mogodbproject:mongo12345678@clusterformqtt.autry.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    # print(mqttClient.list_database_names())
    database = mqttClient['IoT_Database']
    # print(database.list_collection_names())
    collection = database.MQTT
    id = collection.insert_one(jsonDocument).inserted_id 

