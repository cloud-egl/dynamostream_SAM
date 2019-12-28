import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from urllib.parse import unquote_plus
import urllib
import uuid





def lambda_handler(event, context):
    print('Loading function')
    print("Dynamo stream example")
    
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        if record['eventName'] == 'REMOVE':
            print("Delete trigger")
            return 0
        print("Dynamo record", record['dynamodb'])
        json_data = record['dynamodb']
        low_level_data = json_data['NewImage']['Data']
        low_level_data = list(low_level_data.values())[0]
        boto3.resource('dynamodb')
        # To go from low-level format to python
        deserializer = boto3.dynamodb.types.TypeDeserializer()
        python_data = {k: deserializer.deserialize(v) for k,v in low_level_data.items()}
        
        startTime = datetime.now()
        return "End processing"
