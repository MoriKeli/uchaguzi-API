from rest_framework import serializers
from .models import Aspirants, Nominations, VotingResults, PollsResults

class AspirantsSerializer(serializers.ModelSerializer):
    """ Aspirants can use this serializer to fill in their details when vying for an electoral post. """

    class Meta:
        model = Aspirants
        fields = '__all__'

class NominateAspirantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominations
        fields = '__all__'


class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingResults
        fields = '__all__'

class PollingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollsResults
        fields = '__all__'

