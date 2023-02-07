from user.models import ProfileUserModel
from django.contrib.auth.models import User
from user.serializers import UserSerializer, ProfileUserSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from django.shortcuts import redirect

class UserViewSet(viewsets.ModelViewSet):
    '''API para usuarios'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
       

class ProfileUserViewSet(viewsets.ModelViewSet):
    '''API para perfiles de usuario'''
    queryset = ProfileUserModel.objects.all()
    serializer_class = ProfileUserSerializer


class LoginView(APIView):
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"login":"conectado"})
        else:
            return Response({"error": "Wrong Credentials"}, status=400)

def my_logout(request):
    logout(request)
    return redirect('company:login')