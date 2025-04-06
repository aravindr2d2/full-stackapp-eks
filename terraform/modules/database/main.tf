resource "aws_db_instance" "rds" {
  allocated_storage = 20
  engine            = "mysql"
  instance_class    = "db.t3.medium"
#  name              = "onfinance-db"
  username          = var.db_username
  password          = var.db_password
  db_subnet_group_name = aws_db_subnet_group.db_subnet_group.name
  multi_az          = true
  publicly_accessible = false
}

resource "aws_db_subnet_group" "db_subnet_group" {
  name       = "onfinance-db-subnet-group"
  subnet_ids = [module.vpc.subnet_a_id, module.vpc.subnet_b_id]
}
