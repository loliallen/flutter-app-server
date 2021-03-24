from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import User, Child
from .serializer import ChildSerializer
# Create your views here.

class ChildView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        data = request.data
        children = data['children']
        children_data = []
        try:
            user = request.user
            for child in children:
                new_child = Child(**child)
                new_child.save()
                user.children.add(new_child)
                children_data.append(new_child)
            
            user.save()
            data = ChildSerializer(user.children, many=True)

            return Response(data.data)
        except:
            return Response("Not valid data", status=403)
