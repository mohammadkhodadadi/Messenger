from .serializers import MyTokenObtainPairSerializer, \
    RegisterSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.contrib.auth import get_user_model

User = get_user_model()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

        # refresh = RefreshToken.for_user(user)
        reset_url = f'{request.scheme}://{request.get_host()}/{request.resolver_match.route}{uidb64}/{token}/'

        # Send the password reset email here...
        self._send_email(message=reset_url)
        return Response({'detail': 'Password reset email sent.'}, status=status.HTTP_200_OK)

    @staticmethod
    def _send_email(message, subject=None, body=None):
        print("--------------------------------")
        print(message)
        print("--------------------------------")


class PasswordResetConfirmAPIView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def get_serializer_context(self):
        return {'token': self.kwargs.get('token'), 'uidb64': self.kwargs.get('uidb64')}

    def post(self, request, **kwargs):
        serializer = self.get_serializer(
            data={'new_password': request.data['new_password']})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            new_password = serializer.validated_data['new_password']
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password has been reset.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
