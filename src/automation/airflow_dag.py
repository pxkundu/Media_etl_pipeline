from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from fetch_meta import fetch_meta_data
from store_s3 import upload_to_s3

default_args = {"owner": "airflow", "start_date": datetime(2024, 1, 1)}
dag = DAG("media_etl_pipeline", default_args=default_args, schedule_interval="@daily")

task_fetch_meta = PythonOperator(task_id="fetch_meta", python_callable=fetch_meta_data, dag=dag)
task_upload_s3 = PythonOperator(task_id="upload_s3", python_callable=upload_to_s3, dag=dag)

task_fetch_meta >> task_upload_s3
