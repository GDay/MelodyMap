from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from users.serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from users.models import User


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    @method_decorator(csrf_protect)
    def post(self, request):
        username = request.data.get('username', '').strip().lower()
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response()
            else:
                return Response({'error': 'Your account is deactivated.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Username and password don\'t match.'}, status=status.HTTP_400_BAD_REQUEST)


class SignupView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = User
    serializer_class = UserSerializer


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response()


class CSRFTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
       return HttpResponse()


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)    
        return Response(serializer.data)