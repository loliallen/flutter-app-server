from django.contrib.auth.models import AbstractUser
from djongo import models


class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True)
    token = models.TextField(max_length=16, unique=True, blank=True)
    token_refresh_date = models.DateField(auto_now_add=True, blank=True)