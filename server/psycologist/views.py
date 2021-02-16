from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from psycologist.controller import *
import api.controller.Transfer as TransferController
import json

# Create your views here.

class AuthView(APIView):
    def post(self, request, format=None):
        request_data = request.data

        try:
            if format == "signup":
                # register
                user = CreatePsycologist(request_data)
                return Response(data=user, status=201)
            elif format == "signin":
                user = PsycologistLogin(request_data.get('username'), request_data.get('password'))
                return Response(user, status=200)

            return JsonResponse({ 'message': 'Undefined format /{}'.format(format)}, status=404 )
        except ValidationError:
            return Response({'message': 'Not valid data'}, 403)

class UserListView(APIView):
    def get(self, request):
        psys = GetAllPsycologists()
        return Response(psys)

    def post(self, request):
        raw_data = request.data

        psy = CreatePsycologist(raw_data)

        return Response(data=psy, status=201)
    def put(self, request):
        psy_id = request.data.get('psy_id')
        patient_id = request.data.get('patient_id')

        appended = AppendPatinetForPsycolog(psy_id, patient_id)
        if not appended:
            return Response({'message': 'Error while appending'}, status=400)
        return Response({'message': 'appended'})
    
class UserView(APIView):
    def get(self, request, id):
        transfers = TransferController.GetTranferGroup(id)
        return Response(transfers)

    def post(self, request, id):
        pass
    def put(self, request, id):
        updates = request.data

        tf = TransferController.UpdateTransferGroup(id, updates)
        
        if not tf:
            return Response({'message', 'Bad request'}, status=403)

        return Response(tf)

        pass
    def delete(self, request, id):
        pass

class UserTransfersView(APIView):
    def get(seld, request, id):
        print("id", id)
        transfers = TransferController.GetPsyTransfers(id)

        return Response(transfers)


