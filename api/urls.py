from django.urls import path
from . import views
from .views import ListAllPost , UpdatePost , DeletePost , CreatePost
urlpatterns = [
    # path("" , views.home , name = "home"),
    path("home" , ListAllPost.as_view()),
    path("create" , CreatePost.as_view() ),
    path("edit" , UpdatePost.as_view() ),
    path("delete" , DeletePost.as_view())
]