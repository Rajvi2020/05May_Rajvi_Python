# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Restaurant
# from .serializers import RestaurantSerializer


# class RestaurantListCreateAPIView(APIView):

#     def get(self, request):
#         restaurants = Restaurant.objects.all()
#         serializer = RestaurantSerializer(restaurants, many=True)

#         return Response(serializer.data)

#     def post(self, request):
#         serializer = RestaurantSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )


# class RestaurantDetailAPIView(APIView):

#     def get_object(self, id):
#         try:
#             return Restaurant.objects.get(id=id)
#         except Restaurant.DoesNotExist:
#             return None

#     def put(self, request, id):
#         restaurant = self.get_object(id)

#         if restaurant is None:
#             return Response(
#                 {"message": "Restaurant not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = RestaurantSerializer(
#             restaurant,
#             data=request.data
#         )

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     def patch(self, request, id):
#         restaurant = self.get_object(id)

#         if restaurant is None:
#             return Response(
#                 {"message": "Restaurant not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = RestaurantSerializer(
#             restaurant,
#             data=request.data,
#             partial=True
#         )

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     def delete(self, request, id):
#         restaurant = self.get_object(id)

#         if restaurant is None:
#             return Response(
#                 {"message": "Restaurant not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         restaurant.delete()

#         return Response(
#             {"message": "Restaurant deleted successfully"},
#             status=status.HTTP_200_OK
#         )

from rest_framework import generics, mixins

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListCreateAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RestaurantDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)