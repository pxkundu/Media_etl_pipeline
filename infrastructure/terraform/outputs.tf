output "s3_bucket_name" {
  description = "The name of the S3 bucket"
  value       = aws_s3_bucket.media_data_bucket.id
}

output "lambda_function_arn" {
  description = "ARN of the deployed Lambda function"
  value       = aws_lambda_function.etl_lambda.arn
}

output "redshift_cluster_id" {
  description = "ID of the Redshift cluster"
  value       = aws_redshift_cluster.media_redshift.id
}
