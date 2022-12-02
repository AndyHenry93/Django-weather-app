from django.shortcuts import render
import os
import json
import urllib.request
from dotenv import load_dotenv
load_dotenv()
from .forms import ForecastForm

# Create your views here.
def forecast(request):
    api = str(os.getenv('api'))
    if request.method == "POST":
        form = ForecastForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            zip=cd['zipcode']
            code=cd['country_code']
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?zip='+zip+','+code+'&appid='+api+'&units=imperial').read()
            list_data = json.loads(source)
            data = {
                "name": str(list_data['name']),
                "country_code": str(list_data['sys']['country']),
                "coordinate": str(list_data['coord']['lon']) +', '+ str(list_data['coord']['lat']),
                "curr_temp": str(list_data['main']['temp']),
                "temp_min": str(list_data['main']['temp_min']),
                "temp_max": str(list_data['main']['temp_max']),
                "pressure": str(list_data['main']['pressure']),
                "humidity": str(list_data['main']['humidity']),
                "main": str(list_data['weather'][0]['main']),
                "description": str(list_data['weather'][0]['description']),
            }
            return render(request,'forecast/forecast.html',{'form':form,'data':data})
    else:
        form = ForecastForm()
        return render(request,'forecast/forecast.html',{'form':form}) 