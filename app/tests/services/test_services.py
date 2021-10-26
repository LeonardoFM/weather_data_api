from app.models import Weather
from rest_framework.test import APIClient
from rest_framework import status
import responses
from django.conf import settings
from unittest.mock import patch
import pytest

from app.services import set_weather_data, verify_user, OpenWeatherService


class TestAppServices:
    def setup(self):
        self.url = '/api/v1/weather'
        self.client = APIClient()
        self.user_id = '234'
        self.data = '123456,'
        self.city_id = '3439525'

    def test_should_set_weather_data(self, weather):
        set_weather_data(self.user_id, self.data)
        wtr = Weather.objects.filter(user_id=self.user_id).first()
        assert wtr

    def test_should_verify_activated_user(self, user_activated, weather):
        usr = verify_user(self.user_id, self.data)
        assert type(usr) == str

    def test_should_verify_registered_user(self, user_registered, weather):
        usr = verify_user(self.user_id, self.data)
        assert type(usr) == str

    @pytest.mark.django_db
    def test_should_verify_new_user(self):
        usr = verify_user(self.user_id, self.data)
        assert usr


    @responses.activate
    def test_shoud_get_weather_data_by_city_id(self, weather_response):
        ows = OpenWeatherService() 

        url = f"{ows.url}?id={self.city_id}&appid={settings.OPEN_WEATHER_TOKEN}"

        responses.add(responses.GET,
            url,
            json=weather_response,
            status=status.HTTP_200_OK)

        response = ows.get_by_city_id(self.city_id)
        assert response.status_code == 200
