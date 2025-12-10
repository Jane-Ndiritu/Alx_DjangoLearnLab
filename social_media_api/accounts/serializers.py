from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        return user
    
    class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)

        def validate(self, data):
            user = authenticate(username=data['username'], password=data['password'])
            if user and user.is_active:
                return user
            raise serializers.ValidationError("Invalid username or password.")
        
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = CustomUser
                fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']