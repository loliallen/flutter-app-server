from .models import Diary, Record, TitleRecord
from django.contrib import admin

# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
    list_display = (
        ('title',)
    )

admin.site.register(Diary)
admin.site.register(Record)
admin.site.register(TitleRecord)