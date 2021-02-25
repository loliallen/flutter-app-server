from .models import Diary, Record, TitleRecord, Question, Transfer, TransferGroup, Configuration 
from django.contrib import admin
from django import forms

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        ('content', 'mood')
    )

class DiaryAdmin(admin.ModelAdmin):
    list_display = (
        ('title',)
    )

class TransferAdmin(admin.ModelAdmin):
    list_display = (
        ('diary',)
    )

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        ('_id','count_of_questions', 'min_count_of_diaries_for_transfer')
    )


admin.site.register(Diary, DiaryAdmin)
admin.site.register(Record)
admin.site.register(TitleRecord)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Configuration, ConfigurationAdmin)