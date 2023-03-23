from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.decorators import user_passes_test
from .serializers import AspirantsSerializer, NominateAspirantsSerializer, VotingSerializer, PollingSerializer
from .models import Aspirants, VotingResults, PollsResults


class VieForElectoralPostView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    @user_passes_test(lambda user: user.is_voter is True)
    def post(self, request):
        serializer = AspirantsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(name=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VotingView(APIView):
    def object_ID(self, aspirantID):
        try:
            return Aspirants.objects.get(id=aspirantID, nominated=True)
        except Aspirants.DoesNotExist:
            return Response({"Aspirant not found or was never nominated ..."}, status=status.HTTP_404_NOT_FOUND)
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    @user_passes_test(lambda user: user.is_voter is True)
    def post(self, request, aspirantID):
        serializer = VotingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # come up with an algo. to add votes to each aspirant and voter turnout.
        # try calculating voter_turnout using pre_save()
        serializer.save(aspirant=aspirantID)

        return Response(serializer.data, status=status.HTTP_200_OK)

class PollingView(APIView):
    def poll_objectID(self, aspirantID):
        try:
            return Aspirants.objects.get(id=aspirantID)
        except Aspirants.DoesNotExist:
            return Response({"Aspirant not found or was never nominated."}, status=status.HTTP_404_NOT_FOUND)

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    @user_passes_test(lambda user: user.is_voter is True)
    def post(self, request, aspirantID):
        serializer = PollingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(aspirant=aspirantID)

        return Response(serializer.data, status=status.HTTP_200_OK)

class NominationView(APIView):
    def aspirant_objectID(self, aspirantID):
        try:
            return Aspirants.objects.get(id=aspirantID)
        except Aspirants.DoesNotExist:
            return Response({"Aspirant not found or was never nominated."}, status=status.HTTP_404_NOT_FOUND)

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    @user_passes_test(lambda user: user.is_official is True)
    def post(self, request, aspirantID):
        serializer = NominateAspirantsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(aspirant=aspirantID, officer_name=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


