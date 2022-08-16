from django.urls import path
from . import views

app_name = "forecast"

urlpatterns = [
    path('forecast/',views.forecast,name='weather'),
]
