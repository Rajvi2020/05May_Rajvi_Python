from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.playlist,
        name="playlist"
    ),

    path(
        "delete-song/<int:song_id>/",
        views.delete_song,
        name="delete_song"
    ),
 path(
        "wishlist/",
        views.wishlist,
        name="wishlist"
    ),

    path(
        "delete-product/<int:product_id>/",
        views.delete_product,
        name="delete_product"
    ),
    path(
    "watch-later/",
    views.watch_later,
    name="watch_later"
),

path(
    "delete-movie/",
    views.delete_movie,
    name="delete_movie"
),

]