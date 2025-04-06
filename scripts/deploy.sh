#!/bin/bash

# Deploy the Kubernetes application
kubectl apply -f kubernetes/backend-deployment.yaml
kubectl apply -f kubernetes/frontend-deployment.yaml
kubectl apply -f kubernetes/cloudwath-daemonset.yaml
kubectl apply -f kubernetes/cloudwath-cconfigmap.yaml
kubectl apply -f kubernetes/weather-cronjob.yaml
kubectl apply -f kubernetes/hpa.yaml
#kubectl apply -f kubernetes/ingress.yaml   # if using api gateway instead loadbalancer use this and also setup ingress controller for the same and give ingress class
