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

class VerifyEmailView(APIView, ConfirmEmailView):
    """
    Endpoint for user registration email verification.
    """
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)