# Infrastructure Deployment on AWS using Terraform and Kubernetes (EKS)

This document outlines the architecture and deployment strategy for provisioning and running a Kubernetes-based application on AWS using **Terraform** and **EKS (Elastic Kubernetes Service)**. The goal is to ensure a highly available, scalable, and secure deployment leveraging AWS services.

---

## Architecture Overview

### Core Components

- **Terraform**: Used to provision and manage AWS infrastructure resources (VPC, EKS, IAM, S3, etc.).
- **AWS EKS**: Managed Kubernetes service to deploy and manage the application in a scalable and fault-tolerant manner.
- **Kubernetes Manifests**: Deployment, services, and autoscaling configurations to manage application lifecycle and exposure.
- **AWS Services**:
  - **VPC**: For network isolation.
  - **IAM Roles**: For secure access to AWS resources.
  - **S3**: For application data storage.
  - **CloudWatch**: For logging and monitoring of resources.

---

## Architecture Flow

The architecture follows a clear, logical flow to automate infrastructure provisioning and application deployment.

### 1. Code Repository and Workflow Trigger

- **Developers** commit code changes to a **GitHub repository**, which contains:
  - **Terraform** configuration files for provisioning infrastructure.
  - **Kubernetes manifests** (Deployment, Service, ConfigMap, etc.) for application deployment.
  - **Application code**.

### 2. Terraform Infrastructure Provisioning

- **Terraform** provisions AWS infrastructure:
  - **VPC** with both **public and private subnets**.
  - **EKS Cluster** for running the Kubernetes-based application.
  - **IAM Roles and Policies** for Kubernetes worker nodes and other AWS services.
  - **S3 Bucket** for storing application data.

### 3. Kubernetes Deployment

- **Kubernetes (EKS)** is used to manage and scale application containers.
- **kubectl** is employed to apply Kubernetes manifests to the EKS cluster for deployment:
  - **Deployment** ensures the application is deployed with **multiple replicas**.
  - **Service** exposes the application via a **LoadBalancer** for public access.
  - **Horizontal Pod Autoscaler (HPA)** automatically scales the application based on resource usage.

---

## Architecture Diagram

```plaintext
+----------------------------------------------------------+
|                  GitHub Repository                       |
|  - Terraform Configuration                              |
|  - Kubernetes Manifests                                  |
|  - Application Code                                      |
+----------------------------------------------------------+
            |                       
    Code Commit / Push Changes  
            |                       
            v
+----------------------------------------------------------+
|               Terraform Infrastructure Provisioning      |
|  - VPC with Public/Private Subnets                        |
|  - EKS Cluster (Elastic Kubernetes Service)               |
|  - IAM Roles/Policies                                     |
|  - S3 Bucket                                              |
|  - Security Groups                                        |
+----------------------------------------------------------+
            |                       
            v
+----------------------------------------------------------+
|                  Kubernetes (EKS) Deployment             |
|  - Application deployed as Pods on Kubernetes             |
|  - LoadBalancer exposed for public access                |
|  - Horizontal Pod Autoscaler for scaling                 |
+----------------------------------------------------------+
            |                       
            v
+----------------------------------------------------------+
|                      AWS Services                        |
|  - CloudWatch for logging and monitoring                  |
|  - S3 Bucket for application data                        |
+----------------------------------------------------------+
