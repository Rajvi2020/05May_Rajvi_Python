from django.urls import path
from .views import PlaylistListView, OrderListView,CartView,TicketView

urlpatterns = [
    path("playlists/", PlaylistListView.as_view()),
    path("orders/", OrderListView.as_view()),
     path('cart/', CartView.as_view()),
     path('tickets/', TicketView.as_view()),
]
