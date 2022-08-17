from django.shortcuts import render
import json
import urllib.request
from .forms import ForecastForm

# Create your views here.
def forecast(request):
    if request.method == "POST":
        form = ForecastForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            city = cd['city']
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b68db3498a4724b624acf40f2b6cb65d&units=imperial').read()
            list_data = json.loads(source)
            data = {
                "country_code": str(list_data['sys']['country']),
                "coordinate": str(list_data['coord']['lon']) +', '+ str(list_data['coord']['lat']),
                "temp": str(list_data['main']['temp']),
                "pressure": str(list_data['main']['pressure']),
                "humidity": str(list_data['main']['humidity']),
                "main": str(list_data['weather'][0]['main']),
                "description": str(list_data['weather'][0]['description']),
            }
            return render(request,'forecast/forecast.html',{'form':form,'data':data})
    else:
        city = ForecastForm()
        return render(request,'forecast/forecast.html',{'form':form}) 