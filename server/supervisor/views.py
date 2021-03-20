from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .controller import *
from psycologist.controller import AppendPatinetForPsycolog, CreatePsycologist, GetAllPsycologists, GetPsycologistById, DeletePsycologist, UpdatePsycologistInfo 
import json

# create and get list for admins
class SupervisorList(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        sups = getAll()
        return Response(sups)

    def post(self, request):
        rData = request.data

        try:
            sup = createSupervisor(rData)
            return Response(sup)
        except:
            return Response("Error", status=400)


# supervisor auth
class SupervisorAuth(APIView):
    def post(self, request, method_format):
        rData = request.data
        try:
            if method_format == "signin":
                sup = loginSupervisor(email=rData.email, password=rData.password)
                return Response(sup)
            elif method_format == "signup":
                sup = createSupervisor(rData)
                return Response("Successfuly registered")
        except:
            return Response("Error", status=400)

    # def get():
    #     sups = getAll()
    #     return Response(sups)


#  supervisor transfers
class TransferList(APIView):
    def get(self, request):
        trgs = GetTransfers()
        return Response(trgs)

class TransferView(APIView):
    def get(self, request, tid):
        try:
            group = getTransferGroupById(tid)
            return Response(group)
        except:
            return Response({'message': "Transfer not found"}, status=400)
    def put(self, request, tid):
        data = request.data.get('updates')

        return Response("p")
        


        
class PsycologistManageList(APIView):
    def get(self, request):
        psys = GetAllPsycologists()
        return Response(psys)
    def post(self, request):
        data = request.data

        try:
            psy = CreatePsycologist(data)
            return Response(psy, status=201)
        except:
            return Response({'message': "error"}, status=400)


class PsycologistManage(APIView):
    def get(self, request, id):
        try:
            psy = GetPsycologistById(id)
            return Response(psy, status=200)
        except:
            return Response({'message': "error"}, status=400)

    def put(self, request, id):
        data = request.data
        
        try:
            psy = UpdatePsycologistInfo(id, data)
            return Response(psy, status=200)
        except:
            return Response({'message': "error"}, status=400)

    def delete(self, request, id):
        try:
            psy = DeletePsycologist(id)
            return Response(psy)
        except:
            return Response({'message': "error"}, status=400)