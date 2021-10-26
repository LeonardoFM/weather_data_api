from django.db import models
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem
import uuid


class Status(DjangoChoices):
    inactive = ChoiceItem('INACTIVE')
    activated = ChoiceItem('ACTIVATED')
    registered = ChoiceItem('REGISTERED')
    done = ChoiceItem('DONE')


class Weather(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    user_id = models.CharField('USER_ID', max_length=10)
    city_id = models.CharField('CITY_ID', max_length=20, null=True)
    temperature = models.DecimalField('TEMPERATURE', default=0.000, decimal_places=3, max_digits=10)
    humidity = models.DecimalField('HUMIDITY', default=0.000, decimal_places=3, max_digits=10)
    status = models.CharField('STATUS', max_length=10, choices=Status.choices, default=Status.inactive)


class User(TimeStampedModel):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    user_id = models.CharField('USER_ID', max_length=10, unique=True)
    data_length = models.IntegerField('DATA_LENGTH', default=0)
    processed_data = models.IntegerField('PROCESSED_DATA', default=0)
    status = models.CharField('STATUS', max_length=10, choices=Status.choices, default=Status.inactive)
