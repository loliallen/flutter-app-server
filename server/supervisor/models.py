from django.db import models
from djongo import models
import random, string
# Create your models here.

def random_string():
    return ''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for i in range(64)])

class Supervisor(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.TextField()
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()

    token = models.TextField(default=random_string)