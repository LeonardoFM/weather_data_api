import pytest
import uuid
from factory import LazyAttribute
from factory.django import DjangoModelFactory

from app.models import User, Weather


class WeatherFactory(DjangoModelFactory):
    id = LazyAttribute(lambda x: uuid.uuid4())
    user_id = '234'
    city_id = '123456'
    temperature = 2.0
    humidity = 1.0
    status = 'DONE'
    class Meta:
        model = Weather


class WeatherInactiveStatusFactory(DjangoModelFactory):
    id = LazyAttribute(lambda x: uuid.uuid4())
    user_id = '234'
    city_id = '123456'
    temperature = 2.0
    humidity = 1.0
    status = 'INACTIVE'
    class Meta:
        model = Weather


class UserActivatedFactory(DjangoModelFactory):
    id = LazyAttribute(lambda x: uuid.uuid4())
    user_id = '234'
    data_length = 1230
    status = 'ACTIVATED'
    class Meta:
        model = User


class UserRegisteredFactory(DjangoModelFactory):
    id = LazyAttribute(lambda x: uuid.uuid4())
    user_id = '234'
    data_length = 1230
    status = 'REGISTERED'
    class Meta:
        model = User


@pytest.fixture
def user_activated(db):
    return UserActivatedFactory()


@pytest.fixture
def user_registered(db):
    return UserRegisteredFactory()


@pytest.fixture
def weather(db):
    return WeatherFactory()


@pytest.fixture
def weather_inactive_status(db):
    return WeatherInactiveStatusFactory()


@pytest.fixture
def weather_response():
    return {
        "coord": {
            "lon": -57.6333,
            "lat": -32.6833
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 308.28,
            "feels_like": 311.24,
            "temp_min": 308.28,
            "temp_max": 308.28,
            "pressure": 1014,
            "humidity": 42,
            "sea_level": 1014,
            "grnd_level": 1004
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.13,
            "deg": 357,
            "gust": 6.1
        },
        "clouds": {
            "all": 0
        },
        "dt": 1635279351,
        "sys": {
            "type": 2,
            "id": 2019376,
            "country": "UY",
            "sunrise": 1635238643,
            "sunset": 1635286279
        },
        "timezone": -10800,
        "id": 3439525,
        "name": "Young",
        "cod": 200
    }