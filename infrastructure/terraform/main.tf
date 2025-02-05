provider "aws" {
  region = "us-east-1"
}

# Create S3 Bucket for Data Storage
resource "aws_s3_bucket" "media_data_bucket" {
  bucket = "media-etl-data-bucket"
  force_destroy = true
}

# Create IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "media_etl_lambda_role"

  assume_role_policy = jsonencode({
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
    Version = "2012-10-17"
  })
}

# Attach Policy to IAM Role
resource "aws_iam_policy_attachment" "lambda_s3_policy" {
  name       = "lambda_s3_policy_attachment"
  roles      = [aws_iam_role.lambda_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

# Deploy Lambda Function
resource "aws_lambda_function" "etl_lambda" {
  function_name = "MediaETLPipeline"
  runtime       = "python3.8"
  handler       = "lambda_handler.lambda_handler"
  role          = aws_iam_role.lambda_role.arn

  filename      = "lambda_function.zip"
}

# Create Redshift Cluster
resource "aws_redshift_cluster" "media_redshift" {
  cluster_identifier = "media-cluster"
  node_type          = "dc2.large"
  master_username    = var.redshift_username
  master_password    = var.redshift_password
  cluster_type       = "single-node"
}
