from .models import Diary, Record, TitleRecord, Question 
from django.contrib import admin

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        ('content', 'mood')
    )

class DiaryAdmin(admin.ModelAdmin):
    list_display = (
        ('title',)
    )

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Record)
admin.site.register(TitleRecord)
admin.site.register(Question, QuestionAdmin)