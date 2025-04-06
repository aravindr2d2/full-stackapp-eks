import json
import requests
import boto3
import os

# Initialize S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Set up the API endpoint and key (ensure the key is stored in AWS Secrets Manager for security)
    api_key = os.environ['API_KEY']  # Assume you store API key in Secrets Manager or environment variables
    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Send GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        weather_data = response.json()
        # For simplicity, let's assume we're interested in the "main" part of the response
        weather_info = {
            "city": city,
            "temperature": weather_data['main']['temp'],
            "humidity": weather_data['main']['humidity'],
            "weather": weather_data['weather'][0]['description']
        }

        # Convert the data to JSON and store it in S3
        s3_key = f"weather-data/{city}_{event['time']}.json"
        s3_client.put_object(
            Bucket=os.environ['S3_BUCKET'],  # Specify the S3 bucket name in environment variables
            Key=s3_key,
            Body=json.dumps(weather_info)
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Weather data for {city} stored successfully!")
        }

    else:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to fetch data from API: {response.status_code}")
        }
