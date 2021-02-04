from .models import User
from .serializer import CreateUserSerializer

def CreateUser(data):
    user = CreateUserSerializer(data=data)
    if user.is_valid():
        user.save()
        return user
    return None
    