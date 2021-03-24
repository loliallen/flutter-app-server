from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, ListField

from .models import AbstractUser, User, Child

import random
import string
# from rest_framework import serializers
# from django.core import serializers as django_serializers


class CreateUserSerializer(ModelSerializer):
    children = ListField(required=False)
    diaries = ListField(required=False)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        token = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        user = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=make_password(validated_data.get('password')),
            is_active=False,
            token=token
        )
        return user

class ChildSerializer(ModelSerializer):
    class Meta:
        model = Child
        fields = ('sex', 'age')

class AllUserIdSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk',)