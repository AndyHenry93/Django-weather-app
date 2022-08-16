from django.shortcuts import render



# Create your views here.
def forecast(request):
    return render(request,'forecast.html')