from .models import User as Psycologist
from .serializer import PsycologistSerializer
from account.models import User
from django.core.exceptions import ValidationError

from bson.objectid import ObjectId


def compare_passwords(p1, p2):
    return p1 == p2


def PsycologistLogin(username, password):
    try:
        psy = Psycologist.objects.get(username=username)

        if not compare_passwords(password, psy.password):
            raise ValidationError
        data = PsycologistSerializer(psy)
        return data.data
    except Psycologist.DoesNotExist:
        raise ValidationError


def GetAllPsycologists():
    psys = Psycologist.objects.all()

    data = PsycologistSerializer(psys, many=True)
    print(type(data.data))
    return data.data


def GetPsycologistById(psy_id):
    psy = Psycologist.objects.get(_id=ObjectId(psy_id))

    data = PsycologistSerializer(psy)

    return data.data

def CreatePsycologist(data):
    print(data)
    psy_data = PsycologistSerializer(data=data)

    if psy_data.is_valid():
        psy_data.save()
        return psy_data.data
    
    raise ValidationError

def UpdatePsycologistInfo(new_info):
    psy = Psycologist.objects.get(_id=ObjectId(psy_id))

    #  set updatable fields


def AppendPatinetForPsycolog(psy_id, patient_id):
    try:
        patient = User.objects.get(_id=ObjectId(patient_id))
        psy = Psycologist.objects.get(_id=ObjectId(psy_id))

        psy.patients.add(patient)

        psy.save() 
        return True
    except User.DoesNotExist:
        return False
    except PsycologistLogin.DoesNotExist:
        return False

def DeletePsycologist(psy_id):
    psy = Psycologist.objects.get(_id=ObjectId(psy_id))
    psy.delete()

    return True