from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests
from .forms import CityForm
from .models import City

load_dotenv()


def index(request):
    appid = os.getenv('API_KEY')
    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}"

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.is_valid()
        form.save()

    form = CityForm()

    cities = City.objects.all()
    
    all_cities = []

    for city in cities:
        response = requests.get(url.format(city=city.name, appid=appid)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    
    context = {
        'all_info': all_cities,
        'form': form
    }
    return render(request, 'weather/index.html', context)