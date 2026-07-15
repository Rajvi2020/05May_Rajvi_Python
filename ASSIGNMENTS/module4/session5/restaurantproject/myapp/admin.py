from django.contrib import admin
from .models import *
# Register your models here.
class restaturantdisplay(admin.ModelAdmin):
  list_display=['name', 'cuisine', 'rating']
  search_fields = ['name', 'cuisine']
  list_filter = ['cuisine']

admin.site.register(Restaturant,restaturantdisplay)

