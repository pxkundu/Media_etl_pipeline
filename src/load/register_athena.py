import boto3

ATHENA_DATABASE = "media_analytics"
TABLE_NAME = "meta_data"
S3_PATH = "s3://your-s3-bucket-name/processed/"

def create_athena_table():
    athena = boto3.client("athena")
    query = f"""
    CREATE EXTERNAL TABLE IF NOT EXISTS {ATHENA_DATABASE}.{TABLE_NAME} (
        name STRING,
        account_id STRING
    ) 
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
    LOCATION '{S3_PATH}'
    """
    athena.start_query_execution(QueryString=query, QueryExecutionContext={"Database": ATHENA_DATABASE})
    print("Athena table registered.")

if __name__ == "__main__":
    create_athena_table()
