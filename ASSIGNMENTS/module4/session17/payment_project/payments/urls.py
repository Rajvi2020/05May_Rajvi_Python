
from django.urls import path
from payments.views import home, pay, payment_callback,food_order,food_success,food_cancel

urlpatterns = [
    path("", home, name="home"),
    path("pay/", pay, name="pay"),
    path(
        "payment-callback/",
        payment_callback,
        name="payment_callback"
    ),
    path("food-order/", food_order, name="food_order"),
    path("food-success/", food_success, name="food_success"),
path("food-cancel/", food_cancel, name="food_cancel"),
]

