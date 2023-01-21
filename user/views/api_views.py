from user.models import ProfileUserModel
from django.contrib.auth.models import User
from user.serializers import UserSerializer, ProfileUserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    '''API para usuarios'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
       

class ProfileUserViewSet(viewsets.ModelViewSet):
    '''API para perfiles de usuario'''
    queryset = ProfileUserModel.objects.all()
    serializer_class = ProfileUserSerializer