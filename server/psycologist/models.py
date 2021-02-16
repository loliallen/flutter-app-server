from django.conf import settings
from djongo import models

# Create your models here.

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    username = models.TextField(unique=True)
    password = models.TextField()
    patients = models.ArrayReferenceField(
        to='account.User', 
        related_name="psycologist",
        blank=True,
        default=[]
    )
    shared_transfers = models.ArrayReferenceField(
        to='api.TransferGroup', 
        related_name='to',
        blank=True,
        default=[]    
    )
    