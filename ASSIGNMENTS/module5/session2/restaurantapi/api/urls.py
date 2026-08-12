# from django.urls import path
# from .views import RestaurantListCreateAPIView, RestaurantDetailAPIView


# urlpatterns = [
#     path(
#         'restaurants/',
#         RestaurantListCreateAPIView.as_view()
#     ),

#     path(
#         'restaurants/<int:id>/',
#         RestaurantDetailAPIView.as_view()
#     ),
# ]

from django.urls import path

from .views import (
    RestaurantListCreateAPIView,
    RestaurantDetailAPIView
)


urlpatterns = [
    path(
        'restaurants/',
        RestaurantListCreateAPIView.as_view()
    ),

    path(
        'restaurants/<int:pk>/',
        RestaurantDetailAPIView.as_view()
    ),
]