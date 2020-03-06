from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from accounts.models import ProUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProUser
        fields = ('email', 'username', 'fullname', 'is_active', 'created_at', 'updated_at',)

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    password_2 = serializers.CharField(
        required=True,
        label="Confirm Password",
        style={'input_type': 'password'}
    )

    fullname = serializers.CharField(
        required=True
    )

    def validate_password_2(self, value):
        data = self.get_initial()
        password = data.get('password')
        if password != value:
            raise serializers.ValidationError("Passwords doesn't match.")
        return value

    class Meta(object):
        model = ProUser
        fields = ('username', 'email', 'password', 'fullname',)

    def validate_email(self, value):
        if ProUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value


    def validate_username(self, value):
        if ProUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value


    # def create(self, validated_data):
    #     user_data = {
    #         'username': validated_data.get('username'),
    #         'email': validated_data.get('email'),
    #         'password': validated_data.get('password'),
    #         'fullname': validated_data.get('fullname'),
    #     }

       # is_active = False

        #return validated_data