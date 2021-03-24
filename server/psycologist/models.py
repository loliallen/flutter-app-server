from django.conf import settings
from djongo import models
import string
import random
from django.db.models import signals
# Create your models here.


def random_string():
    return ''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for i in range(64)])

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    password = models.TextField(default="*()Shalom")
    name = models.TextField(default="")
    username = models.TextField(unique=True)
    delay_duration = models.IntegerField(null=True, blank=True, default=1)
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
    possible_transfers = models.ArrayReferenceField(
        to='api.TransferGroup', 
        related_name='to_possible',
        blank=True,
        default=[]    
    )
    done_transfers = models.ArrayReferenceField(
        to='api.TransferGroup', 
        related_name='to_done',
        blank=True,
        default=[]    
    )
    verified = models.BooleanField(default=False)

    token = models.TextField(default=random_string)

    def __str__(self):
        return "{}({})".format(self.name, self._id)


def pre_user_save(sender, instance, raw,  **kwargs):
    print(sender, instance, raw)



signals.pre_save.connect(receiver=pre_user_save, sender=User)

