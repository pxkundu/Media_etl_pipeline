import boto3

def create_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f"S3 bucket {bucket_name} created successfully!")

if __name__ == "__main__":
    create_s3_bucket("your-s3-bucket-name")
