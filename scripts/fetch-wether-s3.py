import requests
import json
import os
import boto3
from botocore.exceptions import NoCredentialsError
import logging
from datetime import datetime

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Fetch the API key from environment variables or Secrets Manager (handled in the Kubernetes environment)
API_KEY = os.getenv("API_KEY")
CITY = "London"  # Example city, could be dynamically passed
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
S3_BUCKET = "your-s3-bucket-name"  # S3 bucket name
S3_PATH = "weather_data/"  # Folder path in the S3 bucket

def get_weather_data(city, api_key):
    """Fetch weather data from the OpenWeatherMap API."""
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx/5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return None

def store_data_in_s3(data, bucket_name, path):
    """Store data in an AWS S3 bucket."""
    s3_client = boto3.client('s3')
    file_name = f"{path}{CITY}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    try:
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))
        logging.info(f"Data successfully uploaded to S3: {file_name}")
    except NoCredentialsError:
        logging.error("No AWS credentials found. Ensure the environment has proper AWS credentials.")
    except Exception as e:
        logging.error(f"Error storing data in S3: {e}")

def main():
    """Main function to fetch and store weather data."""
    logging.info("Fetching weather data...")
    data = get_weather_data(CITY, API_KEY)
    
    if data:
        logging.info(f"Weather data retrieved for {CITY}")
        store_data_in_s3(data, S3_BUCKET, S3_PATH)

if __name__ == "__main__":
    main()
