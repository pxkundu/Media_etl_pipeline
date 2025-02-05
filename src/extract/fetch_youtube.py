import json
from googleapiclient.discovery import build

API_KEY = "YOUR_YOUTUBE_API_KEY"

def fetch_youtube_data():
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.channels().list(part="statistics", id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
    response = request.execute()
    
    with open("../data/raw/youtube_data.json", "w") as f:
        json.dump(response, f)
    print("YouTube data fetched successfully!")

if __name__ == "__main__":
    fetch_youtube_data()
