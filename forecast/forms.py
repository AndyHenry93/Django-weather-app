from pyexpat import model
from django import forms
from .models import Forecast

class ForecastForm(forms.ModelForm):
    class Meta:
        model = Forecast
        fields = ('city',)