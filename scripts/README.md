Custom Data Integration Pipeline: Fetching Weather Data from a Public API, Storing in AWS S3, and Automating with Kubernetes CronJob
Overview

This document outlines the implementation of a custom data integration pipeline that:

Fetches data from a public API (e.g., OpenWeatherMap API),

Stores the fetched data in AWS S3,

Automates the process using a Kubernetes CronJob,

Ensures secure storage and retrieval of API keys using AWS Secrets Manager,

Implements error handling and logging to ensure the reliability of the process.

1. Fetch Data from Public API (OpenWeatherMap API)
The first step in the integration pipeline is to retrieve weather data from a public API. For this example, we will use the OpenWeatherMap API to fetch weather data for a given city. The fetched data will be in JSON format, which can then be processed and stored.

We will write a Python script to handle this task. The script will:

Send a request to the API to fetch weather data,

Parse the JSON response,

Store the retrieved data in an AWS S3 bucket.

Python Script (fetch-weather-s3.py)

2. Automate Execution via Kubernetes CronJob
To automate the execution of the data fetching process, we use Kubernetes CronJobs. A CronJob allows us to schedule jobs (in this case, the Python script) to run periodically.

We'll create a Kubernetes CronJob that will execute the Python script at regular intervals (e.g., every hour).

Kubernetes CronJob Configuration (weather-cronjob.yaml)

3. Steps to Deploy the CronJob
Store the Secret for API Key in serets section in wweather-cronjob.yaml

Create ConfigMap for Python Script:
The Python script is stored in a Kubernetes ConfigMap, which can be mounted into the CronJob’s container. You can store the entire Python script in the ConfigMap or mount it from an external source.

Apply CronJob, Secret, and ConfigMap:

Once the YAML files are ready, apply them to your Kubernetes cluster:

bash
Copy
kubectl apply -f weather-cronjob.yaml

Ensure IAM Permissions:
Ensure that the Kubernetes worker nodes or the service account running the CronJob have the necessary IAM permissions to access AWS Secrets Manager and S3. You can attach an appropriate IAM role with the necessary policies.

4. Verification of Integration
To verify that the integration is working as expected, you can perform the following checks:

Check CronJob Logs: Use kubectl to view the logs of the CronJob to verify if the data is being fetched and stored correctly.

kubectl logs <pod-name> -c weather-fetcher

Verify Data in S3: Check if the data is successfully stored in AWS S3. You can list the files in the designated S3 bucket and folder.

aws s3 ls s3://your-s3-bucket-name/weather_data/

Check for Errors: If an error occurs, it will be logged in the pod's logs. You can check for error messages related to fetching data or storing it in S3.

Verify Data Integrity: Manually check the S3 bucket to ensure the files are correctly formatted as JSON and contain the expected weather data.


