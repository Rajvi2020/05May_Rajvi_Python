import json
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from .models import Song, Product, Movie
from django.views.decorators.csrf import csrf_exempt

def playlist(request):
    songs = Song.objects.all()

    return render(
        request,
        "music/playlist.html",
        {"songs": songs}
    )

@csrf_exempt
def delete_song(request, song_id):

    if request.method == "DELETE":

        try:
            song = Song.objects.get(id=song_id)
            song.delete()

            return JsonResponse({
                "success": True,
                "message": "Song deleted successfully!"
            })

        except Song.DoesNotExist:

            return JsonResponse({
                "success": False,
                "message": "Song not found!"
            }, status=404)

    return JsonResponse({
        "success": False,
        "message": "Invalid request!"
    }, status=400)

def wishlist(request):

    products = Product.objects.all()

    return render(
        request,
        "music/wishlist.html",
        {"products": products}
    )

@csrf_exempt
def delete_product(request, product_id):

    if request.method == "DELETE":

        try:
            product = Product.objects.get(id=product_id)

            product.delete()

            return JsonResponse({
                "success": True,
                "message": "Product removed from wishlist!"
            })

        except Product.DoesNotExist:

            return JsonResponse({
                "success": False,
                "message": "Product not found!"
            }, status=404)

    return JsonResponse({
        "success": False,
        "message": "Invalid request!"
    }, status=400)

def watch_later(request):

    movies = Movie.objects.all()

    return render(
        request,
        "music/watch_later.html",
        {"movies": movies}
    )

@csrf_exempt
def delete_movie(request):

    if request.method == "DELETE":

        try:

            data = json.loads(request.body)

            movie_id = data.get("movie_id")

            movie = Movie.objects.get(id=movie_id)

            movie.delete()

            return JsonResponse({
                "success": True,
                "message": "Movie removed from Watch Later!"
            })

        except Movie.DoesNotExist:

            return JsonResponse({
                "success": False,
                "message": "Movie not found!"
            }, status=404)

    return JsonResponse({
        "success": False,
        "message": "Invalid request!"
    }, status=400)