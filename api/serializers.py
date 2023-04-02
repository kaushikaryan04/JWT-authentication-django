from rest_framework import serializers
from .models import User , Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"