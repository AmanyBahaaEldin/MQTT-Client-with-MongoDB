from datetime import datetime
import json
from xml.etree.ElementTree import tostring
from Mongo_Altls import mqttClient
def string_to_json(string):
    
    
    json_object = json.loads(string)
    date = datetime.now()
    time = date.strftime("%H:%M:%S")
    
    json_object.update({"date":time})
    print(type(json_object)) 
    print(json_object)
    mqttClient(json_object)

    
