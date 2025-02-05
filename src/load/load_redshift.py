import psycopg2

REDSHIFT_CREDENTIALS = {
    "dbname": "your_db",
    "user": "your_user",
    "password": "your_password",
    "host": "your_redshift_host",
    "port": 5439
}

def load_to_redshift(file_path, table_name):
    conn = psycopg2.connect(**REDSHIFT_CREDENTIALS)
    cursor = conn.cursor()
    
    with open(file_path, 'r') as f:
        next(f)  # Skip header row
        cursor.copy_from(f, table_name, sep=',')
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Data loaded into Redshift table {table_name}")

if __name__ == "__main__":
    load_to_redshift("../data/processed/meta_enriched.csv", "meta_analytics")
