import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    data = client.get_item(
        TableName='flights',
        Key={
            'id': {
                'S': 'id'
            }
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }