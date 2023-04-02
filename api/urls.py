from django.urls import path
from . import views
from .views import ListAllPost
urlpatterns = [
    # path("" , views.home , name = "home"),
    path("home" , ListAllPost.as_view())
]