from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test-email/', views.test_email, name='test_email'),
    path('order-email/', views.order_email, name='order_email'),
    path('reset-email/', views.send_password_reset_email, name='reset_email'),
    path('welcome-email/', views.welcome_email, name='welcome_email'),
]