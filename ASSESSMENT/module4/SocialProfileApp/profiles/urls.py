from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.profile_list,
        name='profile_list'
    ),

    path(
        'create/',
        views.profile_create,
        name='profile_create'
    ),

    path(
        'export/',
        views.export_profiles,
        name='export_profiles'
    ),
]