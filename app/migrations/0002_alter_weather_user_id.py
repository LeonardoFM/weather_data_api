# Generated by Django 3.2.8 on 2021-10-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='user_id',
            field=models.CharField(max_length=10, verbose_name='USER_ID'),
        ),
    ]