from rest_framework import serializers
from user.models import ProfileUserModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    '''serializador de usuarios '''

    class Meta:
        model = User
        fields = [
            "username", "first_name", "last_name", "email", "password"
        ]


class ProfileUserSerializer(serializers.ModelSerializer):
    '''serializador de usuarios '''

    class Meta:
        model = ProfileUserModel
        fields = '__all__'
