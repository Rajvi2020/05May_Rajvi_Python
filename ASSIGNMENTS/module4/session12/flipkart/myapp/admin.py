from django.contrib import admin
from .models import *
# Register your models here.
class productdata(admin.ModelAdmin):
  ordering=['id']
  list_display=['name','price','category']
admin.site.register(product,productdata)