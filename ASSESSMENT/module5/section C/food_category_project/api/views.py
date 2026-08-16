from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Category, MenuItem, Order
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    OrderSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemViewSet(viewsets.ModelViewSet):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderPagination(PageNumberPagination):

    page_size = 5


class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = OrderPagination

    def get_queryset(self):

        queryset = Order.objects.filter(
            owner=self.request.user
        )

        status_value = self.request.query_params.get('status')

        if status_value:
            queryset = queryset.filter(
                status=status_value
            )

        return queryset

    def perform_create(self, serializer):

        serializer.save(
            owner=self.request.user
        )