from os import stat

from rest_framework.exceptions import NotFound
from .exceptions import NotValidForSerialize
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .controller.Diary import *
from .controller.Question import *
from .controller.Record import *
from .controller.TitleRecord import *
from .controller.Transfer import *
from .controller.Psycologist import *

import logging

# Create your views here.


class TransferView(APIView):
    # get all user transfers
    permission_classes = [IsAuthenticated]
    def get(self, request):
        transfers = GetUserTransfers(user_id=request.user._id)
        

        return Response(transfers, status=200)

    # user - create transfer
    def post(self, request):
        # pid - can be None
        pid = request.data.get('pid')
        diary_id = request.data.get('diary_id')
        try:
            transfer = CreateTransfer(diary_id, request.user._id, pid)
            return Response(data=transfer, status=201)
        except NotValidForSerialize:
            return Response({"message": "Some object not valid"}, status=403) 
        except NotEnoughtDiaries:
            return Response({"message": "You have not enougth diaties for making transfers"}, status=405) 

class HowMuchDiariesUserNeed(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        userId = request.user._id
        return Response({"message": "You have not enougth diaties for making transfers"}, status=405) 
        

class TitleRecord(APIView):
    def get(self, request):
        trecords = GetTitleRecords()
        return JsonResponse(trecords, safe=False)

class RecordsList(APIView):
    # parser_classes = [UploadFile]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        records = GetRecords()
        logging.debug(records.data)
        return JsonResponse(records.data, safe=False)

    def post(self, request, format=None):
        try:
            logging.debug(request.data)

            diary_id = request.query_params['diary_id']
            logging.debug(diary_id, type(diary_id))
            record_data = request.data
            record = AppendRecordToDiary(diary_id, record_data)
            if not record:
                return JsonResponse({"message": "Diary not found or Record not found"}, status=404)

            return JsonResponse(data=record, status=201)
        except NotValidForSerialize:
            return JsonResponse({"message": "error"}, status=403)

class RecordsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            record = GetRecord(id)
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
            user_id = request.user._id
            logging.debug(id)
            record = DeleteRecord(user_id=user_id, record_id=id)
            return Response(record, status=200)
        except NotFound:
            return JsonResponse({"message": "id={} not exsits".format(id)}, status=404)

class DiaryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        logging.debug("request.user", request.user.is_authenticated, request.user._id)
        
        diary = GetDiaries(user_data=request.user)
        return JsonResponse(diary, safe=False)

    def post(self, request):
        try:
            diary = CreateDiary(data=request.data, user_data=request.user)
            return JsonResponse(data=diary, status=201)
        except NotValidForSerialize:
            return JsonResponse({"message": "error"}, status=403)

class DiaryView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        diary = GetDiary(id, request.user)

        return JsonResponse(data=diary)
        
class QuestionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, mood):
        questions = GetQuestionsByMood(mood, request.user._id)
        return JsonResponse(questions, safe=False)













