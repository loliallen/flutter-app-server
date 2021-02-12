# from server.main.models import User
from account.models import User 
from rest_framework.exceptions import NotFound
from .exceptions import NotValidForSerialize
from .models import Diary, Psycologist, Record, TitleRecord, Transfer
from .serializer import RecordSelializer, TitleRecordSerializer, DiarySerializer, TransferSerializer
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from bson.objectid import ObjectId 

import json

def GetUserTransfers(user_id):
    user = User.objects.get(_id=ObjectId(user_id))
    transfers = user.transfers.all()

    data = TransferSerializer(data=transfers, many=True)

    return data.data

def GetPsyTransfers(psy_id):
    psy = Psycologist.objects.get(_id=ObjectId(psy_id))
    transfers = psy.shared_transfers.all()

    data = TransferSerializer(data=transfers, many=True)

    return data.data


def CreateTransfer(diary_id, user_id, pid = None):
    """
        recive:
            diary_id
            user_id
            psy_id
    """
    try:
        user = User.objects.get(_id=ObjectId(user_id))
        diary = Diary.objects.get(_id=ObjectId(diary_id))
        
        transfer = Transfer()
        transfer.diary_id = diary
        
        transfer.save()
        
        
        if pid:
            psy = Psycologist.objects.get(_id=ObjectId(pid))
            psy.shared_transfers.add(transfer)
        
        user.transfers.add(transfer)
        user.save()
        return True
    except Diary.DoesNotExist:
        return False
    except Psycologist.DoesNotExist:
        return False
    

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
    print('data', data.data)
    return data.data

def GetDiary(id, user_data):
    user_diaries = GetDiaries(user_data)
    
    user_diary = {}

    for d in user_diaries:
        if d.get('_id') == id:
            user_diary = d
    # print("diary", model_to_dict(diary))
    
    # data 
    # if data.is_valid():
    return user_diary   
    # print(data.errors)
    # raise NotValidForSerialize

def UpdateDiary(_id, data):

    diary = Diary.objects.filter(_id=ObjectId(_id))
    serializer = DiarySerializer(diary.first(), many=False)
    record = RecordSelializer(data=data)

    serializer.data.records.add(record.data)
    serializer.save()
    
    return serializer

def AppendRecordToDiary(diary_id, record_data, file=None):
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
    print(data)
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