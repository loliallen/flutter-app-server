from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from .models import AbstractUser, User

import random
import string
# from rest_framework import serializers
# from django.core import serializers as django_serializers


class CreateUserSerializer(ModelSerializer):
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


# class UserInfoSerializer(ModelSerializer):
#     posts = serializers.SerializerMethodField()

#     def get_posts(self, obj):
#         json_string = django_serializers.serialize('json',
#                                                    Article.objects.filter(author=obj))
#         return json_string

#     class Meta:
#         model = User
#         fields = "__all__"


class AllUserIdSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk',)