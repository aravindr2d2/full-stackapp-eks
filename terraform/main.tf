provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source = "./modules/vpc"
}

module "eks" {
  source = "./modules/eks"
#  vpc_id = module.vpc.aws_vpc_id
}

module "rds" {
  source = "./modules/rds"
  vpc_id = module.vpc.vpc_id
}
