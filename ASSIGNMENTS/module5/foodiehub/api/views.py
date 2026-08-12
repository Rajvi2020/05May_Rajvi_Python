from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hello_spotify(request):
    return Response({
        "message": "Hello, Spotify Fans!"
    })

# JSON Example:
# {
#     "name": "Samsung Galaxy S24",
#     "price": 79999
# }

# XML Example:
# <product>
#     <name>Samsung Galaxy S24</name>
#     <price>79999</price>
# </product>