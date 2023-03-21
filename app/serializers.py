from rest_framework import serializers
from .models import Aspirants

class AspirantsSerializer(serializers.ModelSerializer):
    """ Aspirants can use this serializer to fill in their details when vying for an electoral post. """

    class Meta:
        model = Aspirants
        fields = '__all__'

