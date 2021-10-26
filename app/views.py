from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import IN_QUERY, Parameter
from rest_framework import views
from rest_framework.response import Response
from rest_framework import serializers

from .data import Data
from .services import verify_user, set_weather_data
from .models import User


class WeatherDataUserView(views.APIView):

    class UserSerializer(serializers.Serializer):
        user_id = serializers.CharField(required=True)


    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: "CREATED", 400: "BAD REQUESTION"}
    )
    def post(self, request):
        data = Data().city_ids()
        serializer = self.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.data.get('user_id')
        user = verify_user(user_id, data)
        if isinstance(user, str):
            return Response(data={"message": user}, status=400)

        set_weather_data(user_id, data)
        return Response(data={"message": "CREATED"}, status=201)

    @swagger_auto_schema(
        manual_parameters=[Parameter(in_=IN_QUERY, name='user_id', required=True, type='string')],
        responses={200: "OK", 400: "BAD REQUESTION"}
    )
    def get(self, request):
        params = dict(request.query_params)
        user = get_object_or_404(User, user_id=params['user_id'][0])
        progress = (user.processed_data/float(user.data_length))
        return Response(data={"progress": f"{progress}", "relation": f"{user.processed_data}:{user.data_length}"}, status=200)
