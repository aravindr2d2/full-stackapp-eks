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
