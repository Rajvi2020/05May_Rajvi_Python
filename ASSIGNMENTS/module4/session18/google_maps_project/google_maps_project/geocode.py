import os
import requests
from dotenv import load_dotenv


load_dotenv()


def get_coordinates(address):
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": address,
        "key": api_key
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["status"] != "OK":
        print("Error:", data.get("status"))
        return None

    location = data["results"][0]["geometry"]["location"]

    latitude = location["lat"]
    longitude = location["lng"]

    return latitude, longitude


address = input("Enter address: ")

result = get_coordinates(address)

if result:
    latitude, longitude = result

    print("Address:", address)
    print("Latitude:", latitude)
    print("Longitude:", longitude)