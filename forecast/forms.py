from django import forms
from .models import Forecast

# created a simple ModelForm named ForecastForm which is based off the Forecast model 
# and has the fields zipcode and country_code
class ForecastForm(forms.ModelForm):
    class Meta:
        model = Forecast
        fields = ('zipcode','country_code')