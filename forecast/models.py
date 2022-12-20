from django.db import models

# === Models for weather app ===

# Create your models here.
class Forecast(models.Model):
    zipcode = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)