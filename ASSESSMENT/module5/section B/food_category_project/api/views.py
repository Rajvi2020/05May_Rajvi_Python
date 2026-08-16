from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Order
from .serializers import OrderSerializer

class CategoryListAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MenuItemListCreateAPIView(APIView):

    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MenuItemDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return None

    def get(self, request, pk):
        menu_item = self.get_object(pk)

        if menu_item is None:
            return Response(
                {"detail": "Menu item not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MenuItemSerializer(menu_item)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        menu_item = self.get_object(pk)

        if menu_item is None:
            return Response(
                {"detail": "Menu item not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MenuItemSerializer(
            menu_item,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        menu_item = self.get_object(pk)

        if menu_item is None:
            return Response(
                {"detail": "Menu item not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        menu_item.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )



from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Order.objects.all()

        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status=status)

        return queryset


class PlaceOrderAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            order = serializer.save(owner=request.user)

            return Response(
                OrderSerializer(order).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):

        orders = Order.objects.filter(
            owner=request.user
        )

        serializer = OrderSerializer(
            orders,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )