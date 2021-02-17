from django.conf import settings
from djongo import models

from django.db.models import signals
# Create your models here.

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    password = models.TextField()
    name = models.TextField()
    username = models.TextField(unique=True)
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
    def __str__(self):
        return "{}({})".format(self.name, self._id)


def pre_user_save(sender, instance, raw,  **kwargs):
    print(sender, instance, raw)


signals.pre_save.connect(receiver=pre_user_save, sender=User)
