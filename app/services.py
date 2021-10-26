from django.conf import settings
import requests
from .models import User, Weather


def set_weather_data(user_id, data):

    for city_id in data.split(','):
        if city_id:
            weather = Weather.objects.create(
                user_id=user_id,
                city_id=city_id)
            weather.save()


def verify_user(user_id, data):

    user = User.objects.filter(user_id=user_id).first()
    if user:
        if user.status == 'REGISTERED':
            return "user registered"
        elif user.status == 'ACTIVATED':
            return "user activated"
    else:
        user = User.objects.create(
            user_id=user_id,
            data_length=len(data.split(',')),
            status='REGISTERED')
        user.save()

    return user



class OpenWeatherService:

    def __init__(self, url=settings.OPEN_WEATHER_URL):
        self.url = url
    
    def get_by_city_id(self, city_id):
        url = f"{self.url}?id={city_id}&appid={settings.OPEN_WEATHER_TOKEN}"
        response = requests.get(url)
        return response
