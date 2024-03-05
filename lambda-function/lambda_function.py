import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resume-api')

def lambda_handler(event, context):
    try:
        response = table.get_item(
            Key={
                'id': '1'  # Assuming you want to fetch the resume with id '1'
            }
        )
        
        # Check if the item was found
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'message': 'Resume not found'})
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': (response['Item']['resume'])
        }

    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': e.response['Error']['Message']})
        }