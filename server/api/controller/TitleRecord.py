from api.models import TitleRecord
from api.serializer import TitleRecordSerializer

def GetTitleRecords():
    records = TitleRecord.objects.all()
    serializer = TitleRecordSerializer(records, many=True)

    print(type(serializer.data))
    print(serializer.data)

    return serializer.data
