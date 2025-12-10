from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from social_media_api.posts.models import Post
CustomUser = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )

        # Create authentication token automatically
        Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid username or password.")

#comment Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']

        class PostSerializer(serializers.ModelSerializer):
            author = serializers.ReadOnlyField(source='author.username')    
            comments = serializers.PrimaryKeyRelatedField(
                many=True, 
                read_only=True
        )
            class Meta:
                model = Post
                fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']

                def validate_title(self, value):
                    if len(value) < 5:
                        raise serializers.ValidationError("Title must be at least 5 characters long.")
                    return value
                
                def validate_content(self, value):
                    if len(value) < 20:
                        raise serializers.ValidationError("Content must be at least 20 characters long.")
                    return value
                
#comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Post
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

        def validate_content(self, value):
            if not value.strip():
                raise serializers.ValidationError("Comment content cannot be empty.")   
            return value
