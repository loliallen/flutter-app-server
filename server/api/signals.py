# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from .models import TitleRecord
# from mutagen.mp3 import MP3 

# def mutagen_length(path):
#     try:
#         audio = MP3(path)
#         length = audio.info.length
#         return length
#     except:
#         return None

# @receiver(post_save, sender=TitleRecord)
