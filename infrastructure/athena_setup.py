import boto3

def setup_athena_database():
    athena = boto3.client('athena')
    query = "CREATE DATABASE IF NOT EXISTS media_analytics"
    athena.start_query_execution(QueryString=query)
    print("Athena database created.")

if __name__ == "__main__":
    setup_athena_database()
