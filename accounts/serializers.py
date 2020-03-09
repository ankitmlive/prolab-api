from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from accounts.models import ProUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProUser
        fields = ('email', 'username', 'fullname', 'is_active', 'created_at', 'updated_at',)

class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, label="Email Address")
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(required=True, label="Password", style={'input_type': 'password'})
    password_2 = serializers.CharField(required=True, label="Confirm Password", style={'input_type': 'password'})
    fullname = serializers.CharField(required=True)

    def validate_password_2(self, value):
        data = self.get_initial()
        password = data.get('password')
        if password != value:
            raise serializers.ValidationError("Passwords doesn't match.")
        return value

    class Meta(object):
        model = ProUser
        fields = ('username', 'email', 'password', 'password_2', 'fullname',)
        write_only_fields = ('password',)

    def validate_email(self, value):
        if ProUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_username(self, value):
        if ProUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError("Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8))
        return value

    def create(self, validated_data):
        fullname = validated_data['fullname']
        username = validated_data['username']
        email    = validated_data['email']
        password = validated_data['password']
        user_obj = ProUser(
                username = username,
                email = email,
                fullname = fullname,
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data