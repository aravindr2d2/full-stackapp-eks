variable "aws_region" {
  description = "AWS region"
  default     = "us-west-2"
}

variable "eks_cluster_name" {
  description = "EKS Cluster Name"
  default     = "onfinance-eks-cluster"
}

variable "instance_type" {
  description = "Instance type for EKS worker nodes"
  default     = "t3.medium"
}

variable "db_username" {
  description = "RDS database master username"
}

variable "db_password" {
  description = "RDS database master password"
  sensitive   = true
}
