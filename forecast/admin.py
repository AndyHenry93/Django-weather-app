from django.contrib import admin
from .models import Forecast


# Register your models here.
# created a new modelAdmin with the Forecast model object, which displays only the zipcode 
# code country code  
@admin.register(Forecast)
class ForcastAdmin(admin.ModelAdmin):
    list_display = ('zipcode','country_code')
