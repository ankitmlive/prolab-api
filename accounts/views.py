from rest_framework import generics
from accounts.models import ProUser
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = ProUser.objects.all()
    serializer_class = serializers.UserSerializer

class RegisterView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """

    #permission_classes = (permissions.AllowAny,)
    queryset = ProUser.objects.all()
    serializer_class = serializers.UserRegistrationSerializer
    