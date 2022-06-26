import imp
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class PlanInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanInfo
        fields = '__all__'
