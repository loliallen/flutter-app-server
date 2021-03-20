from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from account.serializer import CreateUserSerializer, User
from psycologist.serializer import PsycologistSerializer, User as Psycologist

class AccountListView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass


# Create your views here.
