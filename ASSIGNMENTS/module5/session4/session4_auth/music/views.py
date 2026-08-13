from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication,
    SessionAuthentication
)
from .models import Playlist, Order
from .serializers import PlaylistSerializer, OrderSerializer,CartSerializer
from rest_framework.authentication import SessionAuthentication
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import IsPremiumUser

class PlaylistListView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        playlists = Playlist.objects.all()

        serializer = PlaylistSerializer(playlists, many=True)

        return Response(serializer.data)

class OrderListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)


class CartView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

class TicketView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsPremiumUser]

    def get(self, request):

        tickets = Ticket.objects.all()

        serializer = TicketSerializer(tickets, many=True)

        return Response(serializer.data)