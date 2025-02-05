from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient

GA4_PROPERTY_ID = "YOUR_GA4_PROPERTY_ID"

def fetch_ga4_data():
    credentials = service_account.Credentials.from_service_account_file("path/to/your/service-account.json")
    client = BetaAnalyticsDataClient(credentials=credentials)

    request = {
        "property": f"properties/{GA4_PROPERTY_ID}",
        "dateRanges": [{"startDate": "30daysAgo", "endDate": "today"}],
        "metrics": [{"name": "sessions"}],
        "dimensions": [{"name": "country"}]
    }
    response = client.run_report(request)
    print(response)

if __name__ == "__main__":
    fetch_ga4_data()
