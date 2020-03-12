from rest_framework import generics
from accounts.models import ProUser
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = ProUser.objects.all()
    serializer_class = serializers.UserSerializer

# The process for verifying would be this:
# register user
# send email to user with url
# when user navigates to url, request is handled by frontend JavaScript framework (ie. React)
# JavaScript parses key (ie. React Router) from url and makes request (ie. axios, fetch, etc) to new verify-email url with key in payload
# returns response to display on frontend to user
class RegisterView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """
    #permission_classes = (permissions.AllowAny,)
    queryset = ProUser.objects.all()
    serializer_class = serializers.UserRegistrationSerializer

class LoginView(generics.APIView):
    queryset = ProUser.objects.all()
    serializer_class = serializers.UserLoginSerializer