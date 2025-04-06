#!/bin/bash

# Deploy the Kubernetes application
kubectl apply -f kubernetes/manifests/backend-deployment.yaml
kubectl apply -f kubernetes/manifests/frontend-deployment.yaml
kubectl apply -f kubernetes/manifests/service-backend.yaml
kubectl apply -f kubernetes/manifests/service-frontend.yaml
kubectl apply -f kubernetes/manifests/hpa.yaml
kubectl apply -f kubernetes/manifests/ingress.yaml
