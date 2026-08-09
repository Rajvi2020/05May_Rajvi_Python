from django.contrib import admin
from django.urls import path
from maps.views import (
    geocode_address,
    show_restaurant_location,
    nearby_cafes,
)
from maps.views import (
    geocode_address,
    show_restaurant_location,
)
from maps.views import (
    geocode_address,
    show_restaurant_location,
    nearby_cafes,
    search_by_distance,
)


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),
path(
    "search-by-distance/",
    search_by_distance,
    name="search_by_distance"
),
    path(
        "geocode/",
        geocode_address,
        name="geocode_address"
    ),

    path(
        "restaurant-location/",
        show_restaurant_location,
        name="show_restaurant_location"
    ),
    path(
    "nearby-cafes/",
    nearby_cafes,
    name="nearby_cafes"
),

]