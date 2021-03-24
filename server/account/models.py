from django.contrib.auth.models import AbstractUser
from djongo import models
from django import forms


class EmbQuestion(models.Model):
    question = models.ObjectIdField() 
    entries = models.IntegerField(default=0)

    class Meta:
        abstract = True


SEX_CHOICES = (
    ('N', 'none'),
    ('F', 'female'),
    ('M', 'male'),
)

class Child(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    sex = models.TextField(choices=SEX_CHOICES, default="N")    
    age = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.sex, self.age)

class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True)
    username = models.TextField(unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(blank=True)
    diaries = models.ArrayReferenceField(to='api.Diary', related_name="author", blank=True)
    transfer_groups = models.ArrayReferenceField(
        to='api.TransferGroup', 
        related_name="from_user",
        blank=True,
        default=[]
    )
    done_transfer_groups = models.ArrayReferenceField(
        to='api.TransferGroup', 
        related_name="from_done",
        blank=True,
        default=[]
    )
    children = models.ArrayReferenceField(
        to=Child, 
        related_name="parent",
        blank=True,
        default=[]
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
  


