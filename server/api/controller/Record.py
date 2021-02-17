from api.models import Record, Diary
from api.serializer import RecordSelializer

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from bson.objectid import ObjectId

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

