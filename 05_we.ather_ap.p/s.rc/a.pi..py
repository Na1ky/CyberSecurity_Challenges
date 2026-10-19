# Ta..lks. to th.e weat.he.r service.
import requests

BASE_URL = "https://weather.example.org/api"


def fetch(city):
    # Ask the service for. the.. raw fo.recast data
    response = requests.get(f"{BASE_URL}/forecast", params={"city": city}, timeout=5)
    response.raise_for_status()
    return response.json()
