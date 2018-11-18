from django.shortcuts import render
import requests
from .models import City
from .models import Answer
from .forms import CityForm
from .forms import AnswerForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ef0a893ccbab805c129e6c2bc9e7279e'
    cities = City.objects.all() #return all the cities in the database
    answers = Answer.objects.all()
    if request.method == 'POST': # only true if form is submitted
        form = AnswerForm(request.POST)
        form.save()
        #form = CityForm(request.POST) # add actual request data to form for processing
        #form.save() # will validate and save if validate

    form = AnswerForm()
    weather_data = []
    answer_data = []
    for answer in answers:
        answer_data.append(answer)
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'answer_data' : answer_data,  'form' : form}
    return render(request, 'weather/index.html', context)
