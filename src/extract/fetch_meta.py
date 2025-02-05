import json
from api_utils import fetch_data

META_API_URL = "https://graph.facebook.com/v16.0/me/adaccounts"
TOKEN = "YOUR_ACCESS_TOKEN"

def fetch_meta_data():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    params = {"fields": "name,account_id"}
    data = fetch_data(META_API_URL, headers=headers, params=params)
    with open("../data/raw/meta_data.json", "w") as f:
        json.dump(data, f)
    print("Meta data fetched successfully!")

if __name__ == "__main__":
    fetch_meta_data()
