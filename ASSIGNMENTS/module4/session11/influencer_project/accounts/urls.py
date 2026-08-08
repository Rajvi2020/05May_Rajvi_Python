from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("login/", views.user_login, name="login"),
    path("profile/", views.profile, name="profile"),
]