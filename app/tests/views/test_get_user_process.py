from rest_framework.test import APIClient
from unittest.mock import patch
import pytest


class TestListUserRequest:
    def setup(self):
        self.url = '/api/v1/weather'
        self.client = APIClient()

    def test_should_list_user_request(self, user_activated):
        response = self.client.get(f"{self.url}?user_id=234")
        assert response.status_code == 200
