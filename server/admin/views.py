from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from account.serializer import CreateUserSerializer, User
from psycologist.serializer import PsycologistSerializer, User as Psycologist


import psycologist.controller as PsycologistController
import supervisor.controller as SupervisorController
from api.controller import Diary, Transfer
from api.serializer import ConfigurationSerializer, Configuration

# Psycologists [x][]
# Diaries (Transfer Groups) (not Readable) [x][]
# Add Psy to TG [][]
# Supervisors [x][]
# Configuration [x][]

class SupervisorListView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        # get list
        sups = SupervisorController.getAll()
        return Response(sups)
    def post(self, request):
        # create supervisor
        data = request.data
        sup = SupervisorController.createSupervisor(data)
        
        return Response(sup)

class SupervisorView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, id):
        try:
            sup = SupervisorController.getById(id)
            return Response(sup)
        except:
            return Response({'message': 'Supervisor not found'})

    def put(self, request, id):
        updates = request.data

        try:
            sup = SupervisorController.updateSupervisor(id, updates)
            return Response(sup)
        except:
            return Response({'message': 'error'}, status=400)

    def delete(self, request, id):
        try:
            sup = SupervisorController.deleteSupervisor(id)

            return Response({'message': 'Supervisor deleted'}, status=200)
        except:
            return Response({'message': 'error'}, status=400)


# END - Supervisor

class PsycologistListView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        try:
            psys = PsycologistController.GetAllPsycologists()

            return Response(psys)
        except:
            return Response({"message": "error"}, status=400)


    def post(self, request):
        data = request.data
        try:
            psy = PsycologistController.CreatePsycologist(data)

            return psy
        except:
            return Response({"message": "error"}, status=400)


class PsycologistView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, id):
        try:
            psy = PsycologistController.GetPsycologistById(id)

            return Response(psy)
        except:
            return Response({"message": "error"}, status=400)



    def put(self, request, id):

        updates = request.data
        try:
            psy = PsycologistController.UpdatePsycologistInfo(id, updates)
            return psy
        except:
            return Response({"message": "error"}, status=400)


    def delete(self, request, id):
        try:
            psy = PsycologistController.DeletePsycologist(id)

            return Response(psy)
        except:
            return Response({"message": "error"}, status=400)




class TransferGroupListView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        transfers = Transfer.GetTransfers()
        
        return Response(transfers)

class TransferGroupView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, id):
        tg = Transfer.GetTranferGroup(id)
        return Response(tg)
    def put(self, request, id):
        updates = request.data
        tg = Transfer.UpdateTransferGroup(updates)
        return Response(tg)


class ConfigurationView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        conf = Configuration.objects.all().last()
        data = ConfigurationSerializer(conf)

        return Response(data.data)
    def post(self, request):
        data = request.data
        conf = Configuration.objects.all().last()

        conf.count_of_questions = data.get('count_of_questions')
        conf.min_count_of_diaries_for_transfer = data.get('min_count_of_diaries_for_transfer')
        conf.count_of_diaries_each_day_for_psycologist = data.get('count_of_diaries_each_day_for_psycologist')
        
        conf.save()
        res = ConfigurationSerializer(conf) 

        return Response(res.data)
        