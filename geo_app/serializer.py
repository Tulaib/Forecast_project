from rest_framework import serializers
from .models import Geo_info
from django.core import exceptions


class Geo_serializer(serializers.ModelSerializer):
    class Meta:
        model = Geo_info
        fields = '__all__'