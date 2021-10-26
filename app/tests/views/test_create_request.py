from rest_framework.test import APIClient
from unittest.mock import patch
import pytest


class TestCreateUserRequest:
    def setup(self):
        self.url = '/api/v1/weather'
        self.client = APIClient()

    @pytest.mark.django_db
    @patch('app.services.set_weather_data')
    @patch('app.services.verify_user')
    def test_should_create_user_request(self, mock_verify_user, mock_set_weather_data, user_activated):
        mock_verify_user.return_value = user_activated
        user_request_input = {'user_id': '1234'}
        response = self.client.post(self.url, data=user_request_input)
        assert response.status_code == 201
