from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework import generics
from .serializers import PostsSerializer
from .models import Post , Like , User
from django.shortcuts import get_object_or_404

def home(request):
    return HttpResponse("Home")

def likePost(request , postId):
    user = request.user
    post = get_object_or_404(Post , postId)
    error = {"Already Liked Picture" : "You have already liked this picture"}
    if Like.objects.filter(user = user ,post = post).exists():
        return JsonResponse(error)
    like = Like.objects.create(user = user , post = post)
    like.save()
    success = {"Liked Post" : "Post liked successfully"}
    return JsonResponse(success)


class ListAllPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class CreatPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class DeletePost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    lookup_field = "id"

class UpdatePost(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    lookup_field = "id"
