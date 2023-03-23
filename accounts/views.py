from django.contrib import auth
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import SignupSerializer, VoterRegistrationSerializer
from datetime import datetime, timedelta
import jwt


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = auth.authenticate(email=email, password=password)
        
        if user is None:
            raise AuthenticationFailed('INVALID CREDENTIALS!!!')

        payload = {
            "id": user.id,
            "exp": datetime.utcnow() + timedelta(minutes=60),    # token expires after 1 hour.
            "iat": datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.data = {"User logged in ..."}

        # store token as a cookies
        response.set_cookie(key='jwt', value=token, httponly=True)

        return response


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VoterRegistrationView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = VoterRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.is_staff is True and request.user.is_official is True:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        elif request.user.is_staff is True and request.user.is_superuser is True:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer.save(voter=request.user, is_registered=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LogoutUser(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {"message": "User logged out ..."}
        
        return response

