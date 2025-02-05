import schedule
import time
from fetch_meta import fetch_meta_data
from store_s3 import upload_to_s3

def job():
    fetch_meta_data()
    upload_to_s3("../data/processed/meta_cleaned.csv", "processed/meta_cleaned.csv")

schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
