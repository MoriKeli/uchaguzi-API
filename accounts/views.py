from django.contrib import auth
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
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
    def post(self, request):
        serializer = VoterRegistrationSerializer(data=request.data, instance=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_voter=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

