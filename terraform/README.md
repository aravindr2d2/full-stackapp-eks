# Terraform Setup for AWS EKS & RDS

1. Initialize Terraform
```bash
terraform init

Plan the infrastructure


terraform plan

Apply the infrastructure


terraform apply

To destroy the infrastructure


terraform destroy


**Kubernetes**

```markdown
# Kubernetes Setup

1. Deploy the services on EKS
```bash
./scripts/deploy.sh

Monitor the pods


kubectl get pods

To delete the deployments


kubectl delete -f kubernetes
