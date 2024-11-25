import json
import uuid
import os
import boto3


def handler(event, context):
  print('received event:')
  print(event)
  userId = event["arguments"]["userId"]
  groupIds = event["arguments"]["groupIds"]
  
  generated_uuid = str(uuid.uuid4())
 
  lambda_client = boto3.client('lambda')
  
  payload = {"id": generated_uuid, "userId": userId, "groupIds": groupIds}

  print(json.dumps(payload))

  invoke_params = {
    'FunctionName': os.environ['FUNCTION_TEAMGETENTITLEMENT_NAME'],  
    'InvocationType': 'Event',
    'Payload': json.dumps(payload)
    }

  lambda_client.invoke(**invoke_params)

  return {
    'id': generated_uuid,
    }