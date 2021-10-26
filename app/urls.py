from django import urls

from app.views import WeatherDataUserView


app_name = 'weather'

urlpatterns = [
    urls.path(f'{app_name}', WeatherDataUserView.as_view()),
]
