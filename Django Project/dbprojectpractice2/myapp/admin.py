from django.contrib import admin
from .models import *
# Register your models here.
class emp(admin.ModelAdmin):
     ordering=['id']
     list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'mobile',
        'gender',
        'dob',
        'department',
        'designation',
        'salary',
        'joining_date',
        'city',
        'address',]
admin.site.register(Employee,emp)