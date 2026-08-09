from maps.distance import find_nearby_cafes


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


nearby_cafes = find_nearby_cafes(
    user_lat,
    user_lng,
    cafes
)


print("Cafes within 3 km:")

for cafe in nearby_cafes:

    print(
        f"{cafe['name']} - "
        f"{cafe['distance']} km"
    )