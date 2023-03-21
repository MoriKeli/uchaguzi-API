from rest_framework import serializers
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'phone_no', 'national_id', 'password']
        extra_kwargs = {'password': {'write_only': True}}    # this attr. prevents a user password from being displayed after creating a user account.
    
    def create(self, validated_data):
        """ Unlike django, django REST framework does not hash a user's password therefore we need to override create() method and hash a
            user's password when he/she creates a new account. 
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
            instance.save()
        
        return instance

