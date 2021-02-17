from .models import Diary, Record, TitleRecord, Question, Transfer, TransferGroup 
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


admin.site.register(Diary, DiaryAdmin)
admin.site.register(Record)
admin.site.register(TitleRecord)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Transfer, TransferAdmin)