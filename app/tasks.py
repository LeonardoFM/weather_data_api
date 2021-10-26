
from .services import OpenWeatherService
from celery.decorators import task
from celery.utils.log import get_task_logger
from weather_app.celery import app

logger = get_task_logger(__name__)

app.conf.beat_schedule = {
    'free-plan-routine': {
        # Task Name (Name Specified in Decorator)
        'task': 'weather app task',  
        'schedule': 10.0
    },
} 

@task(name='weather app task')
def list_weather_by_city_id_task(*args, **kwargs):
    from .models import Weather, User

    weather_list = Weather.objects.filter(status='INACTIVE')
    if len(weather_list) > 60:
        weather_list = weather_list[0: 2]

    ows = OpenWeatherService()

    for weather in weather_list:
        response = ows.get_by_city_id(city_id=weather.city_id)

        if response.status_code == 200:
            data = response.json()
            main = data.get('main')
            weather.temperature = main.get('temp')
            weather.humidity = main.get('humidity')
            weather.status = 'DONE'
            weather.save(update_fields=['temperature', 'humidity', 'status'])

            user_id = weather.user_id
            user = User.objects.filter(user_id=user_id).first()
            user.processed_data += 1
            if user.data_length == user.processed_data:
                user.status = 'DONE'
            else:
                user.status = 'ACTIVATED'
            user.save(update_fields=['processed_data', 'data_length', 'status'])
