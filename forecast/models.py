from django.db import models

# simple Forecast model which has two fields zipcode and country_code both charfields 
# Create your models here.
class Forecast(models.Model):
    zipcode = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)