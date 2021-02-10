from os import stat

from rest_framework.exceptions import NotFound
from .exceptions import NotValidForSerialize
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .controller import AppendRecordToDiary, CreateDiary, DeleteRecord, GetDiaries, GetRecords, CreateRecord, GetRecord, GetTitleRecords, UpdateRecord

# Create your views here.


class TitleRecord(APIView):
    def get(self, request):
        trecords = GetTitleRecords()
        return JsonResponse(trecords, safe=False)
class RecordsList(APIView):
    def get(self, request, format=None):
        print("request.user", request.user.is_authenticated, request.user._id)
        records = GetRecords()
        return JsonResponse(records.data, safe=False)

    def post(self, request, format=None):
        try:

            diary_id = request.query_params['diary_id']
            print(diary_id, type(diary_id))
            record_data = request.data
            record = AppendRecordToDiary(diary_id, record_data)
            if not record:
                return JsonResponse({"message": "Diary not found or Record not found"}, status=404)

            return JsonResponse(data=record, status=201)
        except NotValidForSerialize:
            return JsonResponse({"message": "error"}, status=403)

class RecordsView(APIView):
    def get(self, request, id):
        try:
            print("id", id)
            record = GetRecord(id)
            print(record)
            return JsonResponse(record, status=200)
        except NotFound:
            return JsonResponse({"message": "id={} not exsits".format(id)}, status=404)

    def put(self, request, id):
        try:
            record = UpdateRecord(id, request.data)
            return JsonResponse(record, status=200)
        except NotFound:
            return JsonResponse({"message": "id={} not exsits".format(id)}, status=404)

    def delete(self, request, id):
        try:
            record = DeleteRecord(id)
            return JsonResponse(record, status=200)
        except NotFound:
            return JsonResponse({"message": "id={} not exsits".format(id)}, status=404)


class DiaryListView(APIView):
    def get(self, request):
        print("request.user", request.user.is_authenticated, request.user._id)
        diary = GetDiaries(user_data=request.user)
        return JsonResponse(diary, safe=False)

    def post(self, request):
        try:
            print(request.data)
            diary = CreateDiary(data=request.data, user_data=request.user)
            return JsonResponse(data=diary, status=201)
        except NotValidForSerialize:
            return JsonResponse({"message": "error"}, status=403)