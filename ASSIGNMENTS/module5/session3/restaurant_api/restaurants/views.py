from django.shortcuts import render


from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Restaurant
from .serializers import RestaurantSerializer

from django_filters.rest_framework import DjangoFilterBackend
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [OrderingFilter,DjangoFilterBackend]
    ordering_fields = ['name', 'cuisine']
    filterset_fields = ['cuisine']
    

    

    
