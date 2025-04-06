# Kubernetes Deployment: Backend API & Frontend Web Service

## Overview

This deployment focuses on a simple full-stack application running in a Kubernetes cluster and includes the following components:

- Backend API Service: Provides API endpoints (e.g., to fetch weather data).
- Frontend Web Service: Consumes the API and renders data for users.
- Service Objects: 
  - ClusterIP for internal service-to-service communication.
  - LoadBalancer for external/public access to the frontend.
- Configuration Management: Uses ConfigMaps and Secrets for environment configuration and sensitive data.
- Health Checks: Liveness and readiness probes ensure pods are healthy and ready to serve traffic.
- Auto-Scaling: Leverages Horizontal Pod Autoscaler (HPA) based on CPU or memory utilization.

────────────────────────────────────────────

## Docker Images

To build Docker images for both frontend and backend:

### Build frontend image
```sh
cd frontend
docker build -t frontend-image .
```

#### Build backend image
```sh
cd backend
docker build -t backend-image .
```

────────────────────────────────────────────

## Kubernetes Manifest Files

Component:Filename
---------------------------  ------------------------------
- Backend Deployment:backend-deployment.yaml
- Frontend Deployment:frontend-deployment.yaml
- ConfigMap:configmap.yaml
- Secrets:secrets.yaml
- Horizontal Pod Autoscaler:hpa.yaml
- CloudWatch ConfigMap:cloudwatch-configmap.yaml
- Scheduled CronJob (API):weather-cronjob.yaml

────────────────────────────────────────────

## Deployment Instructions

Step 1: Create ConfigMap & Secrets

```sh
kubectl apply -f configmap.yaml
kubectl apply -f secrets.yaml
kubectl apply -f cloudwatch-daemonset.yaml
kubectl apply -f cloudwatch-configmap.yaml
```

Step 2: Deploy Backend & Frontend

```sh
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f weather-cronjob.yaml
```

Step 3: Configure Autoscaling (HPA)

```sh
kubectl apply -f hpa.yaml
```

Step 4: Verify Deployment
```sh
kubectl get pods
kubectl get svc
kubectl get hpa
kubectl get svc frontend-service
```
────────────────────────────────────────────

## High Availability

- Backend Replicas: 3  
- Frontend Replicas: 2  
- Self-healing: Enabled using liveness and readiness probes  
- Routing: Only healthy pods receive traffic  

────────────────────────────────────────────

## Scaling Configuration

- Autoscaling: Backend API scales automatically with HPA based on CPU usage.

────────────────────────────────────────────

## Best Practices Followed

- Use of ConfigMaps and Secrets for clean configuration management.
- Health checks with liveness/readiness probes.
- External monitoring integration via CloudWatch DaemonSet.
- Auto-scaling via HPA for efficient resource utilization.

────────────────────────────────────────────
