from math import radians, sin, cos, sqrt, atan2


def calculate_distance(user_lat, user_lng, cafe_lat, cafe_lng):
    """
    Calculate distance between two locations
    using the Haversine formula.

    Returns distance in kilometers.
    """

    earth_radius = 6371

    lat1 = radians(user_lat)
    lat2 = radians(cafe_lat)

    lat_difference = radians(cafe_lat - user_lat)
    lng_difference = radians(cafe_lng - user_lng)

    a = (
        sin(lat_difference / 2) ** 2
        + cos(lat1)
        * cos(lat2)
        * sin(lng_difference / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = earth_radius * c

    return distance


def find_nearby_cafes(user_lat, user_lng, cafes):
    """
    Return all cafes within 3 km
    of user's location.
    """

    nearby_cafes = []

    for cafe in cafes:

        distance = calculate_distance(
            user_lat,
            user_lng,
            cafe["lat"],
            cafe["lng"]
        )

        if distance <= 3:

            cafe_with_distance = cafe.copy()

            cafe_with_distance["distance"] = round(
                distance,
                2
            )

            nearby_cafes.append(
                cafe_with_distance
            )

    return nearby_cafes