import requests
from django.conf import settings


def get_coordinates(address):
    """
    Convert an address into latitude and longitude
    using Google Geocoding API.
    """

    api_key = settings.GOOGLE_MAPS_API_KEY

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": address,
        "key": api_key
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["status"] != "OK":
        raise Exception(
            f"Geocoding failed: {data.get('status')}"
        )

    location = data["results"][0]["geometry"]["location"]

    latitude = location["lat"]
    longitude = location["lng"]

    return latitude, longitude