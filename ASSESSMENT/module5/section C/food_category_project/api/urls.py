from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    MenuItemViewSet,
    OrderViewSet
)


router = DefaultRouter()

router.register(
    'categories',
    CategoryViewSet,
    basename='category'
)

router.register(
    'menu-items',
    MenuItemViewSet,
    basename='menu-item'
)

router.register(
    'orders',
    OrderViewSet,
    basename='order'
)


urlpatterns = []

urlpatterns += router.urls