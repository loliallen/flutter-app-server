
from django.conf import settings
from djongo import models
from django.db.models import signals


# Create your models here.

file_type_choice = (
    ('s', 'sound'),
    ('i', 'image')
)

mood_type_choice = (
    ('1', 'Sad'),
    ('2', 'Bad'),
    ('3', 'It\'s ok'),
    ('4', 'Good'),
    ('5', 'Happy'),
)
class Record(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    text = models.TextField()
    attatched_file = models.FileField(blank=True, upload_to="records/")
    file_type = models.TextField(choices=file_type_choice, blank=True)

    def __str__(self):
        return self.text

class Diary(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.TextField()
    records = models.ArrayReferenceField(to=Record, related_name="diary")

    def __str__(self):
        return self.title

class Question(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    content = models.TextField()
    mood = models.TextField(choices=mood_type_choice)

class TitleRecord(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    text = models.TextField()
    attatched_file = models.FileField(blank=True, upload_to="title_records/")
    duration = models.IntegerField(blank=True)

def post_title(sender, instance, created, **kwargs):
    print(sender, instance, created)
    if created:
        p_mp3 = settings.MEDIA_ROOT / str(instance.attatched_file.name)
        length = mutagen_length(p_mp3)
        if length != None:
            instance.duration = int(length)
            instance.save()


signals.post_save.connect(receiver=post_title, sender=TitleRecord)


    

from mutagen.mp3 import MP3 

def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None