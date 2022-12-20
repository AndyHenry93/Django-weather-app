import os
import json
from django.shortcuts import render
from .forms import ForecastForm
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def forecast(request):
    api = str(os.getenv('API_KEY'))
    if request.method == "POST":
        form = ForecastForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            zip_code=cd['zipcode']
            code=cd['country_code']
            source = urlopen('https://api.openweathermap.org/data/2.5/weather?zip='+zip_code+','+code+'&appid='+api+'&units=imperial').read()
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