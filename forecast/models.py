from django.db import models

# Create your models here.
class Forecast(models.Model):
    city = models.CharField(max_length=100)
    