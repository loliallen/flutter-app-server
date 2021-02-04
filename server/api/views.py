from os import stat

from rest_framework.exceptions import NotFound
from .exceptions import NotValidForSerialize
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .controller import DeleteRecord, GetRecords, CreateRecord, GetRecord, UpdateRecord

# Create your views here.


class RecordsList(APIView):
    def get(self, request, format=None):
        print("request.user", request.user.is_authenticated, request.user._id)
        records = GetRecords()
        return JsonResponse(records.data, safe=False)

    def post(self, request, format=None):
        try:
            print(request.data)
            record = CreateRecord(data=request.data)
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