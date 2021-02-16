from django.conf import settings
from rest_framework import fields, serializers
from django.core import serializers as django_serializers 
from .models import *

from api.serializer import TransferGroupSerializer


import json

class PsycologistSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)

    shared_transfers = TransferGroupSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = "__all__"
