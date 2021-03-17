from django.conf import settings
from rest_framework import fields, serializers
from django.core import serializers as django_serializers 
from .models import Supervisor
import json


class SupervisorSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Supervisor
        fields = "__all__"
