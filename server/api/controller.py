# from server.main.models import User
from account.models import User 
from django.core import serializers
from rest_framework.exceptions import NotFound
from .exceptions import NotValidForSerialize
from .models import Diary, Record, TitleRecord
from .serializer import RecordSelializer, TitleRecordSerializer, DiarySerializer
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from bson.objectid import ObjectId 

import json

# def createRecord(_record, file=None):
    # try:
    #     record = Record(_record)
    #     if file:
    #         if _record.file_type == 'sound':
    #             text = mp3_to_str(file)
    #         else:
    #             text = image_to_str(file)
        
    #         record.text = text
        
    #     record.save()
    #     return record
    # except ValidationError:
    #     raise ValidationError

def CreateDiary(data, user_data):
    try:
        _diary = DiarySerializer(data=data)
        if not _diary.is_valid():
            raise ValidationError(message=_diary.errors)
        
        _diary.save()
        
        diary = Diary.objects.get(_id=ObjectId(_diary.data.get('_id')))
        user = User.objects.get(_id=ObjectId(user_data._id))

        user.diaries.add(diary)
        user.save()
        print(user)
        diary = DiarySerializer(diary)

        print(diary.data)
        return diary.data
    except ValidationError as e:
        print(e)
        # raise ValidationError(message=e)

def GetDiaries(user_data):
    user = User.objects.get(_id=ObjectId(user_data._id))
    print(user.diaries.all())
    
    data = DiarySerializer(user.diaries.all(), many=True)
    print(data.data)
    return data.data

def UpdateDiary(_id, data):

    diary = Diary.objects.filter(_id=ObjectId(_id))
    serializer = DiarySerializer(diary.first(), many=False)
    record = RecordSelializer(data=data)

    serializer.data.records.add(record.data)
    serializer.save()
    
    return serializer

def AppendRecordToDiary(diary_id, record_data):
    try:
        diary = Diary.objects.get(_id=ObjectId(diary_id))

        s_record = CreateRecord(record_data)

        record = Record.objects.get(_id=ObjectId(s_record.get('_id')))

        diary.records.add(record)
        diary.save()
        return s_record
    except Diary.DoesNotExist:
        return False
    except Record.DoesNotExist:
        return False
    except NotValidForSerialize:
        raise NotValidForSerialize


def GetRecords() -> RecordSelializer:
    records = Record.objects.all()
    serializer = RecordSelializer(records, many=True)
    return serializer

def CreateRecord(data):
    serializer = RecordSelializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data

    raise NotValidForSerialize(serializer.errors)

def UpdateRecord(id, data):
    try:
        record = Record.objects.filter(_id=ObjectId(id))
        record.update(**data)
        
        serializer = RecordSelializer(record.first(), many=False)
        # record = Record.objects.filter(pk=id).first()
        return serializer.data
    except ObjectDoesNotExist:
        raise NotFound

    
def GetRecord(id) -> RecordSelializer:
    try:
        record = Record.objects.get(_id=ObjectId(id))
        
        serializer = RecordSelializer(record, many=False)
        # record = Record.objects.filter(pk=id).first()
        return serializer.data
    except ObjectDoesNotExist:
        raise NotFound



def DeleteRecord(id):
    try:
        record = Record.objects.filter(_id=ObjectId(id))
        print(record)
        record.delete()
        
        serializer = RecordSelializer(record.first(), many=False)
        # record = Record.objects.filter(pk=id).first()
        return serializer.data
    except ObjectDoesNotExist:
        raise NotFound

def GetTitleRecords():
    records = TitleRecord.objects.all()
    serializer = TitleRecordSerializer(records, many=True)
    return serializer.data


def get_user_with_given_token(token):
    """
    Получить пользователя из бд по его токену
    """
    users = User.objects.filter(token=token)
    if not users.exists():
        return None
    return users[0]