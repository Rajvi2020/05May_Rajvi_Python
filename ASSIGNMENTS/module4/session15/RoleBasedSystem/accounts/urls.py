from django.urls import path
from .views import admin_dashboard
from .views import (
    home,
    my_orders,
    post_product,
    user_login,
    seller_dashboard,
    buyer_dashboard,
    user_logout,
)

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'login/',
        user_login,
        name='login'
    ),

    path(
        'my-orders/',
        my_orders,
        name='my_orders'
    ),

    path(
        'post-product/',
        post_product,
        name='post_product'
    ),

    path(
        'seller-dashboard/',
        seller_dashboard,
        name='seller_dashboard'
    ),

    path(
        'buyer-dashboard/',
        buyer_dashboard,
        name='buyer_dashboard'
    ),

    path(
        'logout/',
        user_logout,
        name='logout'
    ),
path(
    'admin-dashboard/',
    admin_dashboard,
    name='admin_dashboard'
),
]