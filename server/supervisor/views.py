from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .controller import *
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
        