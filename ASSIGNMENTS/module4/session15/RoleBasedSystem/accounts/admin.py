# from django.contrib import admin
# from .models import Order, Product, Review, Playlist


# admin.site.register(Order)
# admin.site.register(Product)
# admin.site.register(Review)
# admin.site.register(Playlist)

from django.contrib import admin
from django.core.exceptions import PermissionDenied

from .models import Order, Product, Review, Playlist


admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Review)
from django.contrib import admin
from .models import Playlist




@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):

        if request.user.groups.filter(name="Admin").exists():
            return True

        if request.user.is_superuser:
            return True

        return False


    def has_view_permission(self, request, obj=None):

        if request.user.groups.filter(name="Admin").exists():
            return True

        if request.user.is_superuser:
            return True

        raise PermissionDenied


    def has_change_permission(self, request, obj=None):

        if request.user.groups.filter(name="Admin").exists():
            return True

        if request.user.is_superuser:
            return True

        raise PermissionDenied