from django.urls import path

from .views import OrderPlaceAPIView


urlpatterns = [
    path(
        'orders/place/',
        OrderPlaceAPIView.as_view(),
        name='order-place'
    ),
]