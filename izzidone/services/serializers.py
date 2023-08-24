from rest_framework import serializers
from .models import Service, Subservice
from .models import Service, Subservice, ChooseService

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['created_at', 'is_active']

class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        exclude = ['created_at', 'is_active']

class ChooseServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseService
        exclude = ['created_at', 'is_active']
