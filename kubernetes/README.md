Kubernetes Deployment: Backend API and Frontend Web Service

Overview

This task focuses on deploying a simple application on a Kubernetes cluster that includes:

Backend API Service: Provides a simple API (for example, to fetch data).

Frontend Web Service: A web service that consumes the API from the Backend.

Service Objects: ClusterIP for internal communication between services and LoadBalancer for external public access.

Configuration Management: Using ConfigMaps and Secrets for environment variables and sensitive data.

Health Checks: Configuring liveness and readiness probes to ensure that both services are healthy and ready to serve traffic.

Scaling: Using Horizontal Pod Autoscaler (HPA) to ensure auto-scaling based on CPU or memory usage.

1. Kubernetes Deployment Manifest

Backend API Deployment  backend-deployment.yaml

Frontend Web Deployment  frontend-deployment.yaml

Config map  configmap.yaml

serets   secrets.yaml

Horizontal pod autosaler   hpa.yaml

2. Deployment Instructions

Step 1: Create ConfigMap and Secrets
Create the ConfigMap and Secrets before applying the Deployments.

kubectl apply -f configmap.yaml
kubectl apply -f secrets.yaml

Step 2: Apply Deployments
Apply the Deployment and Service for both the Backend API and Frontend Web services.

kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml

Step 3: Set Up Horizontal Pod Autoscaler
Apply the Horizontal Pod Autoscaler (HPA) for the Backend API.

kubectl apply -f hpa.yaml

Step 4: Verify the Deployment
Check the status of the Pods and ensure they are running.

kubectl get pods

kubectl get svc

kubectl get hpa

kubectl get svc frontend-service


High Availability
Multiple replicas (3 for the backend, 2 for the frontend) are specified for redundancy.

Liveness and Readiness probes ensure self-healing and traffic is routed only to healthy pods.

Scaling Configuration
Horizontal Pod Autoscaler (HPA) automatically adjusts the number of backend API Pods based on CPU utilization.

Best Practices
ConfigMaps and Secrets for configuration management.








