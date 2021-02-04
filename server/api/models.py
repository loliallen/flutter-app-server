
from djongo import models


# Create your models here.

file_type_choice = (
    ('s', 'sound'),
    ('i', 'image')
)
class Record(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    text = models.TextField()
    attatched_file = models.FileField(blank=True)
    file_type = models.TextField(choices=file_type_choice, blank=True)

class Diary(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.TextField()
    records = models.ArrayReferenceField(to=Record, on_delete=models.CASCADE)

class TitleRecord(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    text = models.TextField()
    attatched_file = models.FileField(blank=True)
