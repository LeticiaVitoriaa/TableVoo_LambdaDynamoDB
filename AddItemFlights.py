import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    data = client.put_item(
        TableName='flights',
        Item={
            'id': {
                'S': 'AA962'
            },
            'aircraft_prefix': {
                'S': 'N930NN'
            },
            'pilot_name': {
                'S': 'Deep, John'
            },
            'max_load':{
                'N': '136.9'
            },
            'route':{
                'S': 'GRU-DFW'
            }
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully created items!')
    }