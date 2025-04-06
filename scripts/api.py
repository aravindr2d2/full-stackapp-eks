import json
import requests
import os

def lambda_handler(event, context):
    api_url = "https://api.example.com/data"
    headers = {
        'Authorization': f"Bearer {os.environ['API_KEY']}"
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()
    
    # Save to S3 or DynamoDB (for example)
    print(json.dumps(data))
    return {
        'statusCode': 200,
        'body': json.dumps('Data fetched successfully')
    }
