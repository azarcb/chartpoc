from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from charts.models import Chartdata


class ChartSerailizer(serializers.ModelSerializer):
    class Meta:
        model =  Chartdata
        fields = ('year','value')