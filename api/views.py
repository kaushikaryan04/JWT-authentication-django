from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView
from .serializers import PostsSerializer
from .models import Post
def home(request):
    return HttpResponse("Home")

class ListAllPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

