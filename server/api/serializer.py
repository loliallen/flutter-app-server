from django.conf import settings
from .ulits import image_to_str, mp3_to_str
from rest_framework import fields, serializers
from .models import *

BASE_DIR = settings.MEDIA_ROOT

class RecordSelializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"

    def create(self, validated_data):
        record = Record(**validated_data)
        file = "attatched_file" in validated_data
        record.save()

        if file:
            print(record.attatched_file)
            text = ""
            if validated_data["file_type"] == 's':
                text = mp3_to_str(record.attatched_file)
            elif validated_data["file_type"] == 'i':
                text = image_to_str(record.attatched_file)
            record.text = text
            record.save()
        
        return record

class TitleRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleRecord
        fields = "__all__"


# class DiarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Diary
#         fields = "__all__"

#     def create(self, validated_data):
#         return Diary(**validated_data)

    