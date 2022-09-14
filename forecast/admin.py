from django.contrib import admin
from .models import Forecast
# Register your models here.

@admin.register(Forecast)
class ForcastAdmin(admin.ModelAdmin):
    list_display = ('zipcode','country_code')
