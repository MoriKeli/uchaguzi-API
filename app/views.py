from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import AspirantsSerializer, NominateAspirantsSerializer, VotingSerializer, PollingSerializer

class VieForElectoralPostView(APIView):
    def post(self, request):
        serializer = AspirantsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(name=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VotingView(APIView):
    def post(self, request):
        serializer = VotingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class PollingView(APIView):
    def post(self, request):
        serializer = PollingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class NominationView(APIView):
    def post(self, request):
        serializer = NominateAspirantsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


