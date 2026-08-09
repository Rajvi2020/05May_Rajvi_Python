from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from .geocoding import get_coordinates


def geocode_address(request):
    address = request.GET.get(
        "address",
        "IIM Ahmedabad, Gujarat"
    )

    try:
        latitude, longitude = get_coordinates(address)

        return JsonResponse({
            "address": address,
            "latitude": latitude,
            "longitude": longitude
        })

    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=400)


def show_restaurant_location(request):

    latitude = None
    longitude = None
    address = ""

    if request.method == "POST":

        address = request.POST.get("address")

        try:
            latitude, longitude = get_coordinates(address)

        except Exception as e:

            return render(
                request,
                "maps/restaurant_location.html",
                {
                    "error": str(e),
                    "address": address,
                }
            )

    return render(
        request,
        "maps/restaurant_location.html",
        {
            "latitude": latitude,
            "longitude": longitude,
            "address": address,
            "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        }
    )

from .distance import find_nearby_cafes


def nearby_cafes(request):

    user_lat = 23.0225
    user_lng = 72.5714

    cafes = [
        {
            "name": "Cafe A",
            "lat": 23.0230,
            "lng": 72.5720
        },

        {
            "name": "Cafe B",
            "lat": 23.0300,
            "lng": 72.5800
        },

        {
            "name": "Cafe C",
            "lat": 23.1000,
            "lng": 72.6500
        },

        {
            "name": "Cafe D",
            "lat": 23.0210,
            "lng": 72.5700
        },

        {
            "name": "Cafe E",
            "lat": 23.1500,
            "lng": 72.7000
        }
    ]

    nearby = find_nearby_cafes(
        user_lat,
        user_lng,
        cafes
    )

    return render(
        request,
        "maps/nearby_cafes.html",
        {
            "cafes": nearby
        }
    )

from .distance import calculate_distance
from .geocoding import get_coordinates


def search_by_distance(request):

    pickup_points = [
        {
            "name": "Flipkart Pickup Point - Rajkot Central",
            "address": "Kalawad Road, Rajkot, Gujarat",
            "lat": 22.3039,
            "lng": 70.8022,
        },
        {
            "name": "Flipkart Pickup Point - Raiya Road",
            "address": "Raiya Road, Rajkot, Gujarat",
            "lat": 22.2852,
            "lng": 70.7577,
        },
        {
            "name": "Flipkart Pickup Point - University Road",
            "address": "University Road, Rajkot, Gujarat",
            "lat": 22.2932,
            "lng": 70.7385,
        },
        {
            "name": "Flipkart Pickup Point - Gondal Road",
            "address": "Gondal Road, Rajkot, Gujarat",
            "lat": 22.2736,
            "lng": 70.8001,
        },
        {
            "name": "Flipkart Pickup Point - 150 Feet Ring Road",
            "address": "150 Feet Ring Road, Rajkot, Gujarat",
            "lat": 22.2956,
            "lng": 70.7887,
        },
    ]

    results = []
    address = ""
    error = None

    if request.method == "POST":

        address = request.POST.get("address", "").strip()

        if address:

            try:
                user_lat, user_lng = get_coordinates(address)

                for point in pickup_points:

                    distance = calculate_distance(
                        user_lat,
                        user_lng,
                        point["lat"],
                        point["lng"]
                    )

                    point_copy = point.copy()

                    point_copy["distance"] = round(
                        distance,
                        2
                    )

                    results.append(point_copy)

                # Nearest first
                results.sort(
                    key=lambda x: x["distance"]
                )

            except Exception as e:

                error = str(e)

    return render(
        request,
        "maps/search_by_distance.html",
        {
            "results": results,
            "address": address,
            "error": error,
        }
    )