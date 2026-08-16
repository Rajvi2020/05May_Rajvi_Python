from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryListAPIView,
    MenuItemListCreateAPIView,
    MenuItemDetailAPIView,
    OrderViewSet,
    PlaceOrderAPIView
)


router = DefaultRouter()

router.register(
    'orders',
    OrderViewSet,
    basename='order'
)


urlpatterns = [
    path(
        'categories/',
        CategoryListAPIView.as_view(),
        name='category-list'
    ),

    path(
        'menu-items/',
        MenuItemListCreateAPIView.as_view(),
        name='menu-item-list-create'
    ),

    path(
        'menu-items/<int:pk>/',
        MenuItemDetailAPIView.as_view(),
        name='menu-item-detail'
    ),

    path(
        'my-orders/',
        PlaceOrderAPIView.as_view(),
        name='my-orders'
    ),
]


urlpatterns += router.urls