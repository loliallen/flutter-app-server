from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from psycologist.controller import *
import api.controller.Transfer as TransferController
from .models import User
import json
# Create your views here.

class AuthView(APIView):
    def post(self, request, method_format):
        print(method_format)
        request_data = request.data
        print(request_data)

        try:
            if method_format == "signup":
                # register
                user = CreatePsycologist(request_data)
                return Response(data=user, status=201)
            elif method_format == "signin":
                user = PsycologistLogin(request_data.get('username'), request_data.get('password'))
                return Response(user, status=200)

            return JsonResponse({ 'message': 'Undefined format /{}'.format(method_format)}, status=404 )
        except ValidationError:
            return Response({'message': 'Not valid data'}, 403)
        return Response({'message': 'Not valid data'}, 403)
        
class UserListView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        psys = GetAllPsycologists()
        return Response(psys)

    def post(self, request):
        raw_data = request.data

        psy = CreatePsycologist(raw_data)

        return Response(data=psy, status=201)
    
class UserView(APIView):
    permission_classes = [IsAdminUser]
    def put(self, request, id):
        updates = request.data

        psy = UpdatePsycologistInfo(id, updates)

        return Response(psy)
    def delete(self, request, id):
        DeletePsycologist(id)
        return Response({'message', 'Psycologist deleted'})

class UserTransfersView(APIView):
    def get(self, request):
        
        psy = request.psy
        if psy == None:
            return Response({'message': 'Not authed'}), 401

        transfers = TransferController.GetPsyTransfers(psy._id)

        return Response(transfers)

    def post(self, request, id):
        if request.user == None:
            return Response({'message': 'Not authed'}), 401
        
        tgid = request.data.get('tgid')
        appended = TransferController.AppendTGToPsycologist(tgid, id)

        if not appended:
            return Response({'message': 'Not appended'}, 403)
        return Response({'message': 'Appended'}, 200)

    def put(self, request, id):
        updates = request.data
        psy = request.psy
        tf = TransferController.UpdateTransferGroup(id, updates, psy)
        
        if not tf:
            return Response({'message', 'Bad request'}, status=403)

        return Response(tf)

class UserPatientsView(APIView):
    # get all patients
    # supervisor
    permission_classes = [IsAdminUser]
    def get(self, request, id):
        psy = GetPsycologistById(id)

        return Response(psy)

    def post(self, request, id):
        psy_id = id
        patient_id = request.data.get('patient_id')

        appended = AppendPatinetForPsycolog(psy_id, patient_id)
        if not appended:
            return Response({'message': 'Error while appending'}, status=400)
        return Response({'message': 'Appended'})

    # moderate transaction
    def put(self, request, id):
        psy_id = id
        patient_id = request.data.get('patient_id')
        tgid = request.data.get('tgid')
        updates = request.data.get('updates')

        transfer = TransferController.UpdateTransferGroupStatus(tgid, updates, psy_id)
        
        return Response({'message': 'Appended'})

    def delete(self, request, id):
        psy_id = id
        patient_id = request.data.get('patient_id')
        RemovePatientFromPsycologist(psy_id, patient_id)
        return Response({'message': 'Transfers removed'})


