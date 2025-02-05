import requests

def fetch_data(url, headers=None, params=None):
    """ Generic function to fetch data from an API """
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
