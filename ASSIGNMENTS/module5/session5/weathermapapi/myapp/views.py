import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def music_weather(request, city):

    api_key = ""

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    if response.status_code != 200:
        return Response({
            "status_code": response.status_code,
            "error": response.text
        }, status=404)

    data = response.json()

    return Response({
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    })

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET'])
def food_location(request):

    restaurant = request.GET.get('restaurant')

    if not restaurant:
        return Response({
            "error": "Restaurant name is required"
        }, status=400)

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": restaurant,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "DjangoDRFAssignment/1.0"
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()

    if not data:
        return Response({
            "error": "Restaurant not found"
        }, status=404)

    location = data[0]

    return Response({
        "restaurant": restaurant,
        "latitude": location["lat"],
        "longitude": location["lon"]
    })
    


@api_view(['GET'])

def country_info(request, country_name):
    API_KEY = ""

    url = f"https://api.restcountries.com/countries/v5/names.common/{country_name}"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return Response({
            "error": "Country not found"
        }, status=404)

    data = response.json()

    country = data["data"]["objects"][0]

    return Response({
        "population": country["population"],
        "capital": country["capitals"][0]["name"]
    })

@api_view(['GET'])
def github_repos(request, username):

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    if response.status_code != 200:
        return Response({
            "error": "GitHub user not found"
        }, status=404)

    data = response.json()

    repo_names = []

    for repo in data:
        repo_names.append(repo["name"])

    return Response({
        "repositories": repo_names
    })