from django.core.exceptions import ObjectDoesNotExist, ValidationError
from api.models import Diary, Record
from api.serializer import DiarySerializer, RecordSelializer

from account.models import User
from bson.objectid import ObjectId

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
            
    return user_diary   
    

def UpdateDiary(_id, data):

    diary = Diary.objects.filter(_id=ObjectId(_id))
    serializer = DiarySerializer(diary.first(), many=False)
    record = RecordSelializer(data=data)

    serializer.data.records.add(record.data)
    serializer.save()
    
    return serializer

