# Terraform setup for AWS EKS & RDS

## Terraform Setup 

1. Run following Terraform commands:
```sh
terraform init

terraform plan

terraform apply

```

2. To destroy the infrastructure:

```sh
terraform destroy

```

## Kubernetes Setup


1. Deploy the services on EKS
```sh
./scripts/deploy.sh

```

2. Monitor the pods
```sh
kubectl get pods
```

3. To delete the deployments

```sh
kubectl delete -f kubernetes/

```