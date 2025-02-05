import json
import boto3
from fetch_meta import fetch_meta_data
from store_s3 import upload_to_s3

def lambda_handler(event, context):
    fetch_meta_data()
    upload_to_s3("../data/processed/meta_cleaned.csv", "processed/meta_cleaned.csv")
    
    return {
        "statusCode": 200,
        "body": json.dumps("ETL Job Completed Successfully!")
    }
