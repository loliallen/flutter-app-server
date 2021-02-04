# from server.main.models import User
from rest_framework.exceptions import NotFound
from .exceptions import NotValidForSerialize
from .models import Diary, Record, TitleRecord
from .serializer import RecordSelializer, TitleRecordSerializer
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from bson.objectid import ObjectId 


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

def createDiary(_diary, user):
    try:
        diary = Diary(_diary)
        user.diaries.append(diary._id)
        user.save()
        diary.save()
        return diary
    except ValidationError:
        raise ValidationError


def GetRecords() -> RecordSelializer:
    records = Record.objects.all()
    serializer = RecordSelializer(records, many=True)
    return serializer

def CreateRecord(data):
    serializer = RecordSelializer(data=data)
    if serializer.is_valid():
        serializer.save()
        print("data", serializer.data)
        return serializer.data
    print("Errors: ",serializer.errors)
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
