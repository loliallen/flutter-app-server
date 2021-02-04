from .models import Diary, Record, TitleRecord
from django.contrib import admin

# Register your models here.

admin.site.register(Diary)
admin.site.register(Record)
admin.site.register(TitleRecord)