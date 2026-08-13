
from django.urls import path
from .views import music_weather, food_location, country_info,github_repos
urlpatterns = [
    path('api/music-weather/<city>/', music_weather),
    path('api/food-location/', food_location),
      path('api/country-info/<country_name>/', country_info),
         path('api/github-repos/<username>/', github_repos),
]