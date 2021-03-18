from django.contrib.auth.models import AbstractUser
from djongo import models


class EmbQuestion(models.Model):
    question = models.ObjectIdField() 
    entries = models.IntegerField(default=0)

    class Meta:
        abstract = True


SEX_CHOICES = (
    ('F', 'female'),
    ('M', 'male'),
)

class Child(models.Model):
    sex = models.TextField(choices=SEX_CHOICES) 
    age = models.IntegerField(default=0)

    class Meta:
        abstract = True

class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True)
    age = models.IntegerField()
    diaries = models.ArrayReferenceField(to='api.Diary', related_name="author")
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
    children = models.EmbeddedField(Child, blank=True, null=True)
  


