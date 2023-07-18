from django.contrib.auth import login
from rest_framework import generics, permissions, status
from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.constant import LOGIN_SUCCESS_MSG
from users.models import User
from users.serializer import LoginSerializer
from users.serializer import UserSerializer, RegisterSerializer


# Class based view to Get User Details using Token Authentication
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(LOGIN_SUCCESS_MSG, status=status.HTTP_202_ACCEPTED)