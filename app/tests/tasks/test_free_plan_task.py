from app.models import Weather
from rest_framework.test import APIClient
from rest_framework import status
import responses
from django.conf import settings
from unittest.mock import patch
import pytest

from app.tasks import list_weather_by_city_id_task


class TestAppTasks:

    def test_should_verify_task(self):
        result = list_weather_by_city_id_task.delay()
        assert result
    
    @pytest.mark.django_db
    def test_should_verify_task_function(self):
        list_weather_by_city_id_task()

    def test_weather_inactive_status(self, weather_inactive_status):
        list_weather_by_city_id_task()
        