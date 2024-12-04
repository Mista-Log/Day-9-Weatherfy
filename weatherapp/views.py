import urllib.request
from django.shortcuts import render
import json
import urllib

# Create your views here.
def index(request):
    if request.method == 'POST' :
        city = request.POST.get('city')
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6ad38b9f281351fd46bf1fef9f771d18').read()
        json_data = json.loads(res)

        data = {
            "city": str(json_data['name']),
            "description": (json_data['weather'][0]['description']),
            "icon": (json_data['weather'][0]['icon']),
            "temperature": str(json_data['main']['temp']),
            "humidity": str(json_data['main']['humidity']),
            "wind": str(json_data['wind']['speed']),
        }



    else:
        city = ''
        data = {}

    context = {"data": data, "city": city }

    return render(request, "index.html", context)