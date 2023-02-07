from rest_framework import serializers
from user.models import ProfileUserModel
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    '''serializador de usuarios '''

    def create(self, validated_data) -> None:
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = "__all__"


class ProfileUserSerializer(serializers.ModelSerializer):
    '''serializador de usuarios '''

    class Meta:
        model = ProfileUserModel
        fields = '__all__'
