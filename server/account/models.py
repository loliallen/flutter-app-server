from django.contrib.auth.models import AbstractUser
from djongo import models


class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True)
    age = models.IntegerField()
    diaries = models.ArrayReferenceField(to='api.Diary', related_name="author")
    token = models.TextField(max_length=16, unique=True, blank=True)
    token_refresh_date = models.DateField(auto_now_add=True, blank=True)

# class Psychologist(models.Model):
#     patients = models.ArrayField(models.ForeignKey(to=User, blank=True, on_delete=models.SET_NULL))
#     name = models.TextField()
#     login = models.TextField()
#     password = models.TextField()