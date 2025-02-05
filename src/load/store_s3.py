import boto3

BUCKET_NAME = "your-s3-bucket-name"

def upload_to_s3(file_path, s3_key):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, BUCKET_NAME, s3_key)
    print(f"Uploaded {file_path} to S3 bucket {BUCKET_NAME} as {s3_key}")

if __name__ == "__main__":
    upload_to_s3("../data/processed/meta_cleaned.csv", "processed/meta_cleaned.csv")
